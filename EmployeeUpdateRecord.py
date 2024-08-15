import pymysql as sql

try: 
    
    


    conn=sql.connect(host="localhost",user="root",password="1234",port=3306,database="LIC",cursorclass=sql.cursors.DictCursor)
    smt=conn.cursor()

    id=input("Enter Employee Id u want to Update:")
    q=f"Select * from Employee where Employeeid={id}"
    print(q)
    smt.execute (q)
   
    
    row=smt.fetchone()
    if(row):
                
        print("1 Employee Name;",row["EmployeeName"])
        print("2 DOB:",row["DOB"])
        print("3 Gender:",row["Gender"])
        print("4 City:",row["City"])
        print("5 Salary :",row["Salary"])
        print("6 Exit")
        Ch=int(input("Enter Ur choice:"))
        if(Ch==1):
            Date=input("Enter New Employee Name:")
            Pat=f"EmployeeName='{Date}'"
        elif(Ch==2):
            Date=input("Enter New Employee DOB:")
            Pat=f"DOB='{Date}'"
        elif(Ch==3):
            Date=input("Enter New Employee Gender:")
            Pat=f"Gender='{Date}'"
        elif(Ch==4):
            Date=input("Enter New Employee City:")
            Pat=f"City='{Date}'"
        elif(Ch==5):
            Date=input("Enter New Employee Salary:")
            Pat=f"Salary='{Date}'"
        elif(Ch==6):
            print("Good Bye...")
            
        if(Ch>=1 and Ch<=5):
            q=f"update Employee set {Pat} Where Employeeid={id}"
            smt.execute(q)
            conn.commit()
            
            print("Record Updated Successfully...")
        
        elif(Ch!=6):
            print("Invalid Choice")   
            
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



