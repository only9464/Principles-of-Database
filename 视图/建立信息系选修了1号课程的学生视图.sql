CREATE VIEW IS_S1(Sno,Sname,Grade)
               AS 
               SELECT Student.Sno,Sname,Grade
               FROM  Student,SC
               WHERE  Sdept= 'IS' AND
                      Student.Sno=SC.Sno AND
                      SC.Cno= '1';