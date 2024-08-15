import pymysql as sql
try:
    conn=sql.connect(host="localhost",user="root",password="1234",port=3306,database="indianflights",cursorclass=sql.cursors.DictCursor)
    smt=conn.cursor()

    smt.execute("select * from flight")
    rows=smt.fetchall()
    
    print("Id\t\tCompanyname\t\tFare\t\tSeats\t\t")
    
    for row in rows:
      print(row['Flightid'],row['CompanyName'],row['Fare'],row['Seats'],sep="\t\t")
    print(end="\t\t")
  
  
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
   
  
