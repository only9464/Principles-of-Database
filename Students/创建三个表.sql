-- 创建学生表 Student
CREATE TABLE Student (
   Sno CHAR(10) NOT NULL COMMENT '学号',
   Sname VARCHAR(50) NOT NULL COMMENT '学生姓名',
   Ssex CHAR(2) COMMENT '学生性别',
   Sage INT COMMENT '学生年龄',
   Sdept VARCHAR(50) COMMENT '学生所在院系',
   PRIMARY KEY (Sno)
) COMMENT='学生表';

-- 创建课程表 Course
CREATE TABLE Course (
   Cno CHAR(10) NOT NULL COMMENT '课程编号',
   Cname VARCHAR(100) NOT NULL COMMENT '课程名称',
   Cpno CHAR(10) COMMENT '先修课程编号',
   Ccredit INT COMMENT '课程学分',
   PRIMARY KEY (Cno)
) COMMENT='课程表';

-- 创建学生选课表 SC
CREATE TABLE SC (
   Sno CHAR(10) NOT NULL COMMENT '学号',
   Cno CHAR(10) NOT NULL COMMENT '课程编号',
   Grade DECIMAL(4,1) COMMENT '成绩',
   PRIMARY KEY (Sno, Cno),
   FOREIGN KEY (Sno) REFERENCES Student(Sno),
   FOREIGN KEY (Cno) REFERENCES Course(Cno)
) COMMENT='学生选课表';