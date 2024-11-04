CREATE TABLE BookRecord (
   BookNo  CHAR(30) NOT NULL UNIQUE,
   BookName CHAR(200),
   Publisher CHAR(100),
   Author CHAR(30),
   SalesPrice DECIMAL(10, 2),  -- 使用 DECIMAL 类型来代替 Money
   Quantity INT,
   Discount DECIMAL(2, 2),
   PRIMARY KEY(BookNo)
);