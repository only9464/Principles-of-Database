UPDATE SC
        SET  Grade=0
        WHERE  'CS'=
              (SELECT Sdept
               FROM  Student
               WHERE  Student.Sno = SC.Sno);