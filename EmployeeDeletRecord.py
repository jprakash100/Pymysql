import pymysql as sql
try: 
    conn=sql.connect(host="localhost",user="root",password="1234",port=3306,database="LIC",cursorclass=sql.cursors.DictCursor)
    smt=conn.cursor()

    id=input("Enter Employee Id u want to Delete:")
    q=f"Select * from Employee where Employeeid={id}"
    print(q)
    smt.execute (q)
   
    
    row=smt.fetchone()
    if(row):
        
        print("Id\t\tEmployeeName\tDOB\t\t\tCity\t\tGender\t\tSalary")
        
        print(row["Employeeid"],row["EmployeeName"],row["DOB"],row["City"],row["Gender"],row["Salary"],sep="\t\t")
        Ch=input('Are u sure to remove the above record yesh/no?')
        if(Ch.lower()=="yes"):
            q=f"delete from Employee where Employeeid={id}"
            smt.execute(q)
            conn.commit() 
            print("Employee",id,"deleted successfully...")      
    
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