import pymysql as sql
try:
    conn=sql.connect(host="localhost",user="root",port=3306,password="1234",database="LIC")
    smt=conn.cursor()
    while True:
        id=input("Enter Employee id:")
        N=input("Enter Employee Name:")
        DOB=input("Enter DOB:")
        G=input("Enter Gender:")
        C=input("Enter City:")
        S=input("Enter Salary:")
        
      

        q = "INSERT INTO Employee VALUES ({0}, '{1}', '{2}', '{3}', '{4}', {5})".format(id, N, DOB,G, C, S)
        print(q)



        smt.execute(q)
        conn.commit()
        print('Employee Submitted Successfully')
        ch = input("Add More Record (y/n)? ")
        if ch.lower() == 'n':
            break

        
    conn.close()
        
        
        
except sql .err.ProgrammingError as err:
    print(err)
except sql.err.OperationalError as err:
    print(err)
except sql.err.DataError as err:
    print(err)
except sql.err.InterfaceError as err:
    print(err)
    
    
    
    
    
    
    
