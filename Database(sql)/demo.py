import sql.connector
mydb=sql.connector.connect(
    host="localhost",
    user="root",
    password="Database@786"

)

print(mydb.is_connected())