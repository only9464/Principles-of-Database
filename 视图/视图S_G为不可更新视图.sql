CREATE VIEW S_G ( Sno, Gavg ) AS SELECT
Sno,
AVG( Grade ) 
FROM
	SC 
GROUP BY
	Sno;