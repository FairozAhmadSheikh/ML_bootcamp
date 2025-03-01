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

mycursor.execute("select class from details_db where name='FEROZ'")
mycursor.execute("select name,class from DETAILS_DB")
mycursor.execute("SELECT * FROM DETAILS_DB WHERE roll_no>3")
mycursor.execute("select min(roll_no) from DETAILS_DB")
mycursor.execute("select max(roll_no) from DETAILS_DB")
mycursor.execute("select name from DETAILS_DB where roll_no between 3 and 5 ")
mycursor.execute("select count(*),class from DETAILS_DB group by class")

# fetch all
# res=mycursor.fetchall()

for row in mycursor :
    print(row) 