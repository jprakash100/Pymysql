import pymysql as sql
try: 
    conn=sql.connect(host="localhost",user="root",password="1234",port=3306,database="LIC")
    smt=conn.cursor()
    smt.execute ("Select * from  employee")
    rows=smt.fetchall()
    print("Id\t\tEmployeeName\tDOB\t\t\tCity\t\tGender\t\tSalary")
    for row in rows:
        for col in row:
            print(col,end="\t\t")
        print()
    conn.close()
except sql.err.OperationalError as err:
    print(err)