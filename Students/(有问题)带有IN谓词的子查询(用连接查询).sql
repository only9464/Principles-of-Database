SELECT Student.Sno, Student.Sname
FROM Student
INNER JOIN SC ON Student.Sno = SC.Sno
INNER JOIN Course ON SC.Cno = Course.Cno
WHERE Course.Cname = '信息系统';
-- 以下查询语句会出现报错：1052-Column 'Sno' in field list is ambiguous
-- SELECT  Sno,Sname
-- FROM    Student,SC,Course
-- WHERE   Student.Sno = SC.Sno  AND SC.Cno = Course.Cno AND Course.Cname='信息系统';