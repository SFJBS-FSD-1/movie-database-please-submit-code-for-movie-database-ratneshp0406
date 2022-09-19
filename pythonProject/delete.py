import pymysql

conn = pymysql.connect(user='root',password='welcome$1234',host='127.0.0.1',database="TEST_PYTHON_SQL")
cursor = conn.cursor()

sql_query = "delete from players where name = 'Rahul'"
cursor.execute(sql_query)
conn.commit()

cursor.close()
conn.close()