import pymysql as sql
try:
    conn=sql.connect(host="localhost",user="root",password="1234",database="LIC",cursorclass=sql.cursors.DictCursor)
    smt=conn.cursor()
    id=input("Enter Employee Id U want to Display?")
    smt.execute("select * from Employee  where Employeeid={}".format(id))
    row=smt.fetchone()
    if(row):
        print("Id\t\tEmployeeName\tDOB\t\t\tCity\t\tGender\t\tSalary")

        
        print(row["Employeeid"],row["EmployeeName"],row["DOB"],row["City"],row["Gender"],row["Salary"],sep="\t\t")

    else:
        print("Record Not found")
  
    conn.close()

except sql.err.ProgrammingError as err:
    print(err)

except sql.err.IntegrityError as err:
    print(err)

except sql.err.InterfaceError as err:
    print(err)

except sql.err.OperationalError as err:
    print(err)

except sql.err.DataError as err:
    print(err)
   
  
