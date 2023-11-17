import mysql.connector as conn


my_db = conn.connect(
    # host = os.getenv("DB_HOST"),
    host = 'localhost',
    user = 'AJAYI MOJOLAOLUWA',
    password = 'mynameisajayicoder'
)

# print(my_db)

my_cursor = my_db.cursor()

# Create a database
# my_cursor.execute('CREATE DATABASE ww')
my_cursor.execute('USE ww')
# Create table
# my_cursor.execute("CREATE TABLE students (name VARCHAR(255), matno VARCHAR(255), hall VARCHAR(255), room VARCHAR(255))")

# Add data
# sql = "INSERT INTO students (name, matno, hall, room) VALUES (%s, %s, %s, %s)"
# val = ("Ajayi Mojolaoluwa", "20CJ027416", "Daniel hall", "F203")
# my_cursor.execute(sql, val)

# my_db.commit()

# print(my_cursor.rowcount, "record inserted.")

# Read data
my_cursor.execute("SELECT name, matno, hall, room FROM students")

myresult = my_cursor.fetchall()

for x in myresult:
  print(x)

# Update data
# sql = "UPDATE students SET matno = '20CJ027450' WHERE matno = '20CJ027415'"

# my_cursor.execute(sql)

# my_db.commit()

print(my_cursor.rowcount, "record(s) affected")

# Delete data
#sql = "DELETE FROM students WHERE matno = '20CJ027416'"

#my_cursor.execute(sql)

#my_db.commit()

#print(my_cursor.rowcount, "record(s) deleted")

# Delete table
#sql = "DROP TABLE students"

#my_cursor.execute(sql)

# Delete database
#sql = "DROP DATABASE cen434_live"

#my_cursor.execute(sql)


# close connection
my_db.close()