import pymysql

# Establish the database connection
conc = pymysql.connect(host="localhost", user="root", password="Database@786")
print("Database Connected Successfully!")

cur = conc.cursor()

cur.execute("USE iust_employees")

# Select all
# cur.execute("SELECT * FROM emp_details")

# Select Specific
cur.execute("select name,emp_id from emp_details")

# Fetch all the results and print them
result = cur.fetchall()
for row in result:
    print(row)


cur.close()
conc.close()
