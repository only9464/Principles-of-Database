SELECT
  IS_Student.Sno,
	Sname 
FROM
	IS_Student,
	SC 
WHERE
	IS_Student.Sno = SC.Sno 
	AND SC.Cno = '1';