SELECT  Sno,Sname,Sdept
FROM    Student  S1
WHERE   S1.Sdept  IN
(SELECT Sdept
FROM    Student  S2
WHERE   S2.Sname= '刘晨 ');