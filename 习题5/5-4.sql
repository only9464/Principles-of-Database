SELECT
	P.PNAME,
	SPJ.QTY 
FROM
	P,
	SPJ 
WHERE
	P.PNO = SPJ.PNO 
	AND SPJ.JNO = 'J2';