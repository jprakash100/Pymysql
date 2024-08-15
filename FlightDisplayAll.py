import pymysql as sql
try: 
    conn=sql.connect(host="localhost",user="root",password="1234",port=3306,database="indianflights")
    smt=conn.cursor()
    smt.execute ("Select * from  flight")
    rows=smt.fetchall()
    #print(rows)
    print("Id\t\tCompanyName\t\tFlightType\t\tFrom\t\tTo\t\tFareAmount\t\tSeats")
    for row in rows:
        for col in row:
            print(col,end="\t\t")

    
    conn.close()
except sql.err.OperationalError as err:
    print(err)
    
    