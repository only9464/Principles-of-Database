-- 创建视图 R_S_T
CREATE VIEW R_S_T AS
SELECT
    R.A,
    B,
    C,
    S_.D,
    E,
    F 
FROM
    R,
    S_,
    T 
WHERE
    R.A = S_.A 
    AND S_.D = T.D;