import random
from faker import Faker
import os
from typing import List, Tuple, Dict, Set

# 初始化 Faker
fake = Faker(['zh_CN'])

class DataGenerator:
    def __init__(self):
        # 所有必需的示例值和字段定义都集中在这里
        self.field_examples = {
            'Student': {
                'Sno': ['95001','95019'],  # 学号示例
                'Sname': ['刘晨','蔡徐坤'],  # 学生姓名示例（包含所有必需的名字）
                'Ssex': ['男', '女'],  # 性别示例
                'Sage': [19,20,22,23],  # 年龄示例
                'Sdept': ['IS','MA','CS']  # 院系示例
            },
            'Course': {
                'Cno': ['1','2','3'],  # 课程号示例
                'Cname': ['信息系统'],  # 课程名示例
                'Cpno': ['1','2'],  # 先修课程号示例（与Cno格式相同）
                'Ccredit': [2,3,4]  # 学分示例
            },
            'SC': {
                'Sno': ['95001','95019'],  # 学号示例（与Student.Sno格式相同）
                'Cno': ['1','2','3'],  # 课程号示例（与Course.Cno格式相同）
                'Grade': [85.5,90.0,76.5,92.0]  # 成绩示例
            }
        }

        # 额外的可选课程名称池（不包含示例课程）
        self.course_names = [
            '线性代数', '概率论', '离散数学', 'Python程序设计',
            'Java程序设计', '数据结构', '算法分析', '软件工程', '人工智能导论',
            '机器学习', '计算机组成原理', '编译原理', '网络安全', '分布式系统',
            '云计算技术', '大数据处理'
        ]

        # 额外的可选院系（不包含示例院系）
        self.departments = ['NE', 'IS', 'IoT', 'MA']

    def generate_student_data(self, num_records: int = 10) -> Tuple[List[Dict], List[str]]:
        """生成学生数据并返回学生数据列表和学号列表"""
        if num_records < len(self.field_examples['Student']['Sname']):
            raise ValueError(f"生成的记录数量不能少于必需的名字数量({len(self.field_examples['Student']['Sname'])})")
            
        students = []
        student_nos = set()
        
        # 先生成示例学生数据
        for sno, name in zip(self.field_examples['Student']['Sno'], self.field_examples['Student']['Sname'][:2]):
            if sno not in student_nos:
                student_nos.add(sno)
                student = {
                    'Sno': sno,
                    'Sname': name,
                    'Ssex': random.choice(self.field_examples['Student']['Ssex']),
                    'Sage': random.choice(self.field_examples['Student']['Sage']),
                    'Sdept': random.choice(self.field_examples['Student']['Sdept'])
                }
                students.append(student)
        
        # 生成其他必需名字的记录
        for name in self.field_examples['Student']['Sname'][2:]:
            if name not in [s['Sname'] for s in students]:
                sno = f'{random.randint(94000, 99999)}'
                while sno in student_nos:
                    sno = f'{random.randint(94000, 99999)}'
                student_nos.add(sno)
                
                student = {
                    'Sno': sno,
                    'Sname': name,
                    'Ssex': random.choice(self.field_examples['Student']['Ssex']),
                    'Sage': random.choice(self.field_examples['Student']['Sage']),
                    'Sdept': random.choice(self.field_examples['Student']['Sdept'])
                }
                students.append(student)
        
        # 生成剩余的随机记录
        remaining_records = num_records - len(students)
        for _ in range(remaining_records):
            sno = f'{random.randint(94000, 99999)}'
            while sno in student_nos:
                sno = f'{random.randint(94000, 99999)}'
            student_nos.add(sno)
            
            student = {
                'Sno': sno,
                'Sname': fake.name(),
                'Ssex': random.choice(self.field_examples['Student']['Ssex']),
                'Sage': random.choice(self.field_examples['Student']['Sage']),
                'Sdept': random.choice(self.field_examples['Student']['Sdept'] + self.departments)
            }
            students.append(student)
            
        # 随机打乱学生列表顺序
        random.shuffle(students)
        return students, list(student_nos)

    def generate_course_data(self, num_records: int = 10) -> Tuple[List[Dict], List[str]]:
        """生成课程数据并返回课程数据列表和课程编号列表"""
        courses = []
        course_nos = set()
        
        # 先生成示例课程数据
        for cno, cname in zip(self.field_examples['Course']['Cno'], self.field_examples['Course']['Cname']):
            if cno not in course_nos:
                course_nos.add(cno)
                course = {
                    'Cno': cno,
                    'Cname': cname,
                    'Cpno': None,  # 示例课程默认无先修课
                    'Ccredit': random.choice(self.field_examples['Course']['Ccredit'])
                }
                courses.append(course)
        
        # 生成剩余的课程
        remaining_records = num_records - len(courses)
        for i in range(remaining_records):
            cno = f'{random.randint(1, 999)}'
            while cno in course_nos:
                cno = f'{random.randint(1, 999)}'
            course_nos.add(cno)
            
            course = {
                'Cno': cno,
                'Cname': self.course_names[i % len(self.course_names)],
                'Cpno': random.choice([None] + list(course_nos - {cno})),
                'Ccredit': random.choice(self.field_examples['Course']['Ccredit'])
            }
            courses.append(course)
        
        return courses, list(course_nos)

    def generate_sc_data(self, student_nos: List[str], course_nos: List[str], num_records: int = 20) -> List[Dict]:
        """生成选课数据"""
        sc_records = []
        existing_pairs: Set[Tuple[str, str]] = set()
        
        # 先生成示例选课数据
        for sno, cno, grade in zip(
            self.field_examples['SC']['Sno'],
            self.field_examples['SC']['Cno'],
            self.field_examples['SC']['Grade']
        ):
            if sno in student_nos and cno in course_nos and (sno, cno) not in existing_pairs:
                existing_pairs.add((sno, cno))
                sc_record = {
                    'Sno': sno,
                    'Cno': cno,
                    'Grade': grade
                }
                sc_records.append(sc_record)
        
        # 确保至少有5个学生选修了3号课程
        course_3_students = random.sample(student_nos, 5)  # 随机选择5个学生
        for sno in course_3_students:
            if ('3' in course_nos) and (sno, '3') not in existing_pairs:
                existing_pairs.add((sno, '3'))
                sc_record = {
                    'Sno': sno,
                    'Cno': '3',
                    'Grade': round(random.uniform(60, 100), 1)  # 生成60-100之间的随机成绩
                }
                sc_records.append(sc_record)
        
        # 生成剩余的随机选课记录
        attempts = 0
        max_attempts = num_records * 2
        
        while len(sc_records) < num_records and attempts < max_attempts:
            sno = random.choice(student_nos)
            cno = random.choice(course_nos)
            
            if (sno, cno) not in existing_pairs:
                existing_pairs.add((sno, cno))
                
                # 20%的概率生成没有成绩的记录
                if random.random() < 0.2:
                    grade = None
                else:
                    grade = round(random.uniform(60, 100), 1)
                
                sc_record = {
                    'Sno': sno,
                    'Cno': cno,
                    'Grade': grade
                }
                sc_records.append(sc_record)
            
            attempts += 1
        
        return sc_records
    def generate_insert_sql(self, students: List[Dict], courses: List[Dict], sc_records: List[Dict]) -> str:
        """生成所有表的SQL插入语句"""
        sql_statements = []
        
        # 添加注释和使用声明
        sql_statements.extend([
            "-- 生成的数据插入语句",
            "\n-- 插入学生数据"
        ])
        
        # 生成学生表INSERT语句
        for student in students:
            values = [
                f"'{student['Sno']}'",
                f"'{student['Sname']}'",
                f"'{student['Ssex']}'",
                str(student['Sage']),
                f"'{student['Sdept']}'"
            ]
            sql = f"INSERT INTO Student (Sno, Sname, Ssex, Sage, Sdept) VALUES ({', '.join(values)});"
            sql_statements.append(sql)
        
        # 生成课程表INSERT语句
        sql_statements.append("\n-- 插入课程数据")
        for course in courses:
            values = [
                f"'{course['Cno']}'",
                f"'{course['Cname']}'",
                'NULL' if course['Cpno'] is None else f"'{course['Cpno']}'",
                str(course['Ccredit'])
            ]
            sql = f"INSERT INTO Course (Cno, Cname, Cpno, Ccredit) VALUES ({', '.join(values)});"
            sql_statements.append(sql)
        
        # 生成选课表INSERT语句
        sql_statements.append("\n-- 插入选课数据")
        for sc in sc_records:
            values = [
                f"'{sc['Sno']}'",
                f"'{sc['Cno']}'",
                'NULL' if sc['Grade'] is None else str(sc['Grade'])
            ]
            sql = f"INSERT INTO SC (Sno, Cno, Grade) VALUES ({', '.join(values)});"
            sql_statements.append(sql)
        
        return '\n'.join(sql_statements)

    def save_to_sql_file(self, sql_content: str, filename: str = 'data.sql') -> None:
        """保存SQL语句到文件"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(sql_content)

def main():
    generator = DataGenerator()
    
    # 生成数据
    students, student_nos = generator.generate_student_data(50)  # 生成20个学生
    courses, course_nos = generator.generate_course_data(50)     # 生成15门课程
    sc_records = generator.generate_sc_data(student_nos, course_nos, 200)  # 生成40条选课记录
    
    # 生成SQL语句
    sql_content = generator.generate_insert_sql(students, courses, sc_records)
    
    # 保存到文件
    generator.save_to_sql_file(sql_content)
    print(f"SQL语句已生成并保存到 data.sql 文件中")

if __name__ == "__main__":
    main()