-- 创建教师表 Teacher
CREATE TABLE Teacher (
   Tno CHAR(10) NOT NULL COMMENT '教工号',
   Tname VARCHAR(50) NOT NULL COMMENT '教师姓名',
   PRIMARY KEY (Tno)
) COMMENT='教师表';