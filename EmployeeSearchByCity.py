import pymysql as sql
try: 
    conn=sql.connect(host="localhost",user="root",password="1234",port=3306,database="LIC",cursorclass=sql.cursors.DictCursor)
    smt=conn.cursor()

    Pat=input("Enter Cities:")
    Pat="'"+Pat.replace(",","','")+"'"
    q=f"Select * from Employee where City in. ({Pat})"
    print(q)
    smt.execute (q)
   
    
    rows=smt.fetchall()
    if(len(rows)>0):
        print("Id\t\tEmployeeName\tDOB\t\t\tCity\t\tGender\t\tSalary")
        for row in rows:
            print(row["Employeeid"],row["EmployeeName"],row["DOB"],row["City"],row["Gender"],row["Salary"],sep="\t\t")
    else:
        print("Record Not Found....")
    
    
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