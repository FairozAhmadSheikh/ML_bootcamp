import pymysql

mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="Database@786",
    database="newdatabase"
)
print("Database Connected Sucessfull ! ")

mycursor=mydb.cursor()

# Selecting  specific things

# mycursor.execute("select class from details_db where name='FEROZ'")
# mycursor.execute("select name,class from DETAILS_DB")
mycursor.execute("SELECT * FROM DETAILS_DB WHERE roll_no>3")
# fetch all

# res=mycursor.fetchall()

for row in mycursor :
    print(row)