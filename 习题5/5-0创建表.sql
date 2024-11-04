-- 创建供应商表 (S)
CREATE TABLE S (
    SNO VARCHAR(10) PRIMARY KEY,    -- 供应商编号，作为主键
    SNAME VARCHAR(50),              -- 供应商名称
    CITY VARCHAR(50),               -- 供应商所在城市
    PNO VARCHAR(10)                 -- 添加零件编号字段（虽然不常见，但为了满足查询需求）
);

-- 创建零件表 (P)
CREATE TABLE P (
    PNO VARCHAR(10) PRIMARY KEY,    -- 零件编号，作为主键
    PNAME VARCHAR(50),              -- 零件名称
    COLOR VARCHAR(20),              -- 零件颜色
    WEIGHT DECIMAL(10, 2)           -- 零件重量
);

-- 创建项目表 (J)
CREATE TABLE J (
    JNO VARCHAR(10) PRIMARY KEY,    -- 项目编号，作为主键
    JNAME VARCHAR(50),              -- 项目名称
    CITY VARCHAR(50)                -- 项目所在城市
);

-- 创建供应商-零件-项目关联表 (SPJ)
CREATE TABLE SPJ (
    SNO VARCHAR(10),                -- 供应商编号，外键引用 S 表的 SNO
    PNO VARCHAR(10),                -- 零件编号，外键引用 P 表的 PNO
    JNO VARCHAR(10),                -- 项目编号，外键引用 J 表的 JNO
    QTY INT,                        -- 供应数量
    PRIMARY KEY (SNO, PNO, JNO)    -- 组合主键，确保每条记录唯一
);