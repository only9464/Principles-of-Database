-- 创建学生表 Student
CREATE TABLE Student (
   Sno CHAR(10) NOT NULL,      -- 学生编号
   Sname VARCHAR(50) NOT NULL, -- 学生姓名
   Ssex CHAR(2),              -- 学生性别
   Sage INT,                  -- 学生年龄
   Sdept VARCHAR(50),         -- 学生所在院系
   PRIMARY KEY (Sno)          -- 主键为学号
);

-- 创建课程表 Course
CREATE TABLE Course (
   Cno CHAR(10) NOT NULL,     -- 课程编号
   Cname VARCHAR(100) NOT NULL,-- 课程名称
   Cpno CHAR(10),             -- 先修课程编号
   Ccredit INT,               -- 课程学分
   PRIMARY KEY (Cno)          -- 主键为课程编号
);

-- 创建学生选课表 SC
CREATE TABLE SC (
   Sno CHAR(10) NOT NULL,     -- 学号
   Cno CHAR(10) NOT NULL,     -- 课程编号
   Grade DECIMAL(4,1),        -- 成绩
   PRIMARY KEY (Sno, Cno),    -- 复合主键，确保一个学生对于一门课程只有一个成绩
   FOREIGN KEY (Sno) REFERENCES Student(Sno), -- 外键约束，引用学生表
   FOREIGN KEY (Cno) REFERENCES Course(Cno)  -- 外键约束，引用课程表
);