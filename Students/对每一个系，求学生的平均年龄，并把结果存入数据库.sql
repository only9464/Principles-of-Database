INSERT
        INTO  Deptage(Sdept,Avgage)
              SELECT  Sdept,AVG(Sage)
              FROM  Student
              GROUP BY Sdept;