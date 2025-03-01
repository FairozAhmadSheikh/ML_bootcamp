import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="Database@786"
)
print("Database Connected Successfully ! ")

# cursor creation 
mycursor=mydb.cursor()

# database creation
mycursor.execute("CREATE DATABASE IF NOT EXISTS NewDatabase")
print("Database Creation Success")

# select Database 
mycursor.execute("USE NewDatabase")
print("Selected the created Databases")

#CRUD STARTS FROM HERE

# Create Table now    # CREATE
mycursor.execute("""
CREATE TABLE IF NOT EXISTS DETAILS_DB(
                 name varchar(40),
                 roll_no int,
                 age int,
                 class varchar(40)
                 )
""")
print("Table Created Successfull ! ")

# Insert Values now 
# mycursor.execute("""INSERT INTO DETAILS_DB VALUES 
#                  ("SAMEER",6,21,"BSC")
#                  """)
# print("Insertion Sucessfull ! ")

# Commit Now
mydb.commit()


# UPDATE VALUE 

mycursor.execute("UPDATE DETAILS_DB SET class='AI/ML' WHERE NAME='SAMEER' ")
print("UPDATE DONE ! ")

# Commit Now
mydb.commit()

# DELETE
mycursor.execute("DELETE FROM DETAILS_DB WHERE name='ASIF ASSAD'")
print("Delete Sucess")

# Commit Now
mydb.commit()

# READ NOW 
mycursor.execute("select * from DETAILS_DB ")
result=mycursor.fetchall()
for val in result:
    print(val)