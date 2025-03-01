import pymysql

conc=pymysql.connect(
    host="localhost",
    user="root",
    password="Database@786"
)
print("Database Connected Sucessfully ! ")


# Create a cursor
cur=conc.cursor()

# Create a Database
cur.execute("create database if not exists iust_employees")

# switch to db
cur.execute("use iust_employees")

print("Database  Created Successfully ")

# create table 

cur.execute("""
            create table if not exists emp_details(
            name varchar(40),
            emp_id   int,
            salaray int)
            """)

print(" Table Created Successfully ")

# inserting real values now 
cur.execute('insert into emp_details values("ali",121,1200)')

print(" values inserted  Successfully ")

# commit changes
conc.commit()

# close connection
cur.close()
conc.close()
