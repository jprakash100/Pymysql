import pymysql as sql
try:
    conn=sql.connect(host="localhost",user="root",port=3306,password="1234",database="LIC")
    smt=conn.cursor()
    smt.execute("CREATE TABLE Employee (Employeeid INT PRIMARY KEY,EmployeeName VARCHAR(30),DOB DATE,Gender VARCHAR(30),City VARCHAR(30), Salary Decimal(10,2))")
    print("Table Create...")
    conn.close()
except sql.err.OperationalError as err:
    print(err)
except sql.err.ProgrammingError as err:
    print(err)


