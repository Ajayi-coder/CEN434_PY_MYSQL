#To connect to mySQL
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="KING-JYNX5",
    password="",
    database="CEN434"
)

cursor = connection.cursor()

#To create a database
database_name = "CEN434"
cursor.execute("CREATE DATABASE {database_name}")

#To create a table
table_creation_query = """
CREATE TABLE Students (
    Name VARCHAR(255),
    Matno VARCHAR(255),
    PRIMARY KEY(Name)
)
"""
cursor.execute(table_creation_query)

#To add info
insert_query = """
INSERT INTO Students (Name, Matno)
VALUES (%s, %s)
"""
data = ('Ajayi', '20CJ027415')

cursor.execute(insert_query, data)

#To read data
select_query = "SELECT Name, Matno FROM Students"

cursor.execute(select_query)

rows = cursor.fetchall()

for row in rows:
    print(row)

#To modify/update data in the table
update_query = "UPDATE Students SET Name = 'Mojolaoluwa' WHERE Matno = '20CJ027415'"
cursor.execute(update_query)

#To delete data from the table
delete_query = "DELETE FROM Students WHERE Name = 'Ajayi'"
cursor.execute(delete_query)

#To delete database
delete_query = "DELETE FROM Students WHERE Name = 'Ajayi'"
cursor.execute(delete_query)

#To commit changes and close connections
connection.commit()
connection.close()


