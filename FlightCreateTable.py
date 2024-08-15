import pymysql as sql
try:
    conn=sql.connect(host="localhost",user="root",port=3306,password="1234",database="IndianFlights")
    smt=conn.cursor()
    smt.execute("CREATE TABLE Flight (Flightid INT PRIMARY KEY, CompanyName VARCHAR(60),FlightType int, `From` VARCHAR(60), `To` VARCHAR(60), Fare Decimal(10,2),Seats INT, NoOfSeats INT)")
    print("Table Create...")
    conn.close()
except sql.err.OperationalError as err:
    print(err)
except sql.err.ProgrammingError as err:
    print(err)
