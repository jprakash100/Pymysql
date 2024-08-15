try :
    import pymysql as sql

    conn=sql.connect(host="localhost",user="root",password='1234',port=3306,)
    smt=conn.cursor()
    smt.execute("Create Schema LIC")
    print("Database Create...")
    conn.close()
except sql.err.OperationalError as err:
    print(err)
except sql.err.ProgrammingError as err:
    print(err)
except sql.err.DatabaseError as err:
    print(err)

