SELECT  Student.Sno,Sname,Ssex,Sage,Sdept,Cno,Grade
FROM    Student,SC
WHERE  Student.Sno = SC.Sno;