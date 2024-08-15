import pymysql as sql
try:
    conn=sql.connect(host="localhost",user="root",password="1234",port=3306,database="IndianFlights",cursorclass=sql.cursors.DictCursor)
    smt=conn.cursor()
    id=input("Enter Flights Id U want to Display?")
    smt.execute("select * from flight  where flightid={}".format(id))
    row=smt.fetchone()
    if(row):
      print("Id\tCompanyName\tFare")

      print(row['Flightid'],row['CompanyName'],row['Fare'],sep="\t")
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
   
  
