SELECT Sno,Sname
FROM    Student
WHERE Sno  IN
	(SELECT Sno
	FROM    SC
	WHERE  Cno IN
		(SELECT Cno
		FROM Course
		WHERE Cname= '信息系统'
		)
	);