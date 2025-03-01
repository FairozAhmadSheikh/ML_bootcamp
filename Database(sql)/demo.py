import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="Database@786",
)
cur=conn.cursor()
a=cur.execute('SHOW DATABASES;')
print("Number of Databases",a)
for i in cur:
    print(i)
print("Connected to MySQL successfully!")