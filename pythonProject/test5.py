import pymysql
conn = pymysql.connect(user='root',password='welcome$1234',host='127.0.0.1',database="pythondb")
mycursor=conn.cursor()
sql_query = f"insert into employe(id,name,age,address, salary) values (4,'Chaitali', 25,'mumbai',6500)"

mycursor.execute(sql_query)
# conn.commit()



mycursor.execute("Select * from employe")
while True:

    table= mycursor.fetchone()
    if table is not None:
        print(table)
    else:
        break
# for table in mycursor:
#     print(table[0])
# conn.close()

mycursor.close()
conn.close()
