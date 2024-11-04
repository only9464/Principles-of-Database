SELECT
    Sno 
FROM
    SC 
WHERE
    Cno = '2' 
    AND Grade >= ALL ( SELECT Grade FROM SC WHERE Cno = '2' );