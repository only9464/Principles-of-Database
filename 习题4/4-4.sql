SELECT
	JNO 
FROM
	J 
WHERE
	NOT EXISTS (
	SELECT
		* 
	FROM
		SPJ,
		S,
		P 
	WHERE
		SPJ.JNO = J.JNO 
		AND SPJ.SNO = S.SNO 
		AND SPJ.PNO = P.PNO 
	AND S.CITY ='天津'
	AND P.COLOR ='红');