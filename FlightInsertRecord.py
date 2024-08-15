import pymysql as sql
try:
    conn=sql.connect(host="localhost",user="root",port=3306,password="1234",database="IndianFlights")
    smt=conn.cursor()
    while True:
        id=input("Enter Flights id:")
        CN=input("Enter Company Name:")
        FT=input("Enter FlightS Type:")
        FA=input("Enter Fare Amount:")
        F=input("Enter From:")
        T=input("Enter To:")
        S=input("Enter Seats:")
        NOS=input("Enter Noofseats:")
      

        q = "INSERT INTO flight VALUES ({0}, '{1}', '{2}', '{3}', '{4}', {5}, {6},{7})".format(id, CN, FT,F, T, FA, S,NOS)
        print(q)



        smt.execute(q)
        conn.commit()
        print('Data Submitted Successfully')
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
    
    
    
    
    
    
    
