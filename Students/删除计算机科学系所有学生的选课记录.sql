DELETE FROM SC
WHERE Sno IN (
    SELECT Sno
    FROM Student
    WHERE Sdept = 'CS'
);