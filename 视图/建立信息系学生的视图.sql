CREATE VIEW IS_Student AS 
SELECT Sno, Sname, Sage 
FROM Student 
WHERE Sdept = 'IS';