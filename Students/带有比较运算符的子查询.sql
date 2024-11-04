SELECT Sno, Sname, Sdept
FROM Student
WHERE Sdept = (
    SELECT Sdept
    FROM Student
    WHERE Sname = '刘晨'
);
-- 使用IN的时候：
-- SELECT Sno, Sname, Sdept
-- FROM Student
-- WHERE Sdept IN (
--     SELECT Sdept
--     FROM Student
--     WHERE Sname = '刘晨'
-- );