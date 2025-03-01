import pymysql

# Connect to MySQL
conc = pymysql.connect(
    host="localhost",
    user="root",
    password="Database@786"
)
print("Database Connected Successfully!")

# Create a cursor object
cur = conc.cursor()

# Create a database
cur.execute("CREATE DATABASE IF NOT EXISTS IUST")

# Switch to the IUST database
cur.execute("USE IUST")

# Create a table
cur.execute("""
    CREATE TABLE IF NOT EXISTS students_details (
        name VARCHAR(40),
        roll_no INT,
        batch VARCHAR(5)
    )
""")

# Commit the changes (it's good practice)
conc.commit()

# Close the connection
cur.close()
conc.close()

print("Database and table created successfully!")
