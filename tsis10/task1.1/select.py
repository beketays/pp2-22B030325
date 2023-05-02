import psycopg2
import csv

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="postgres",
    user="postgres",
    password="martini"
)

cur = conn.cursor()

# execute a SELECT statement to retrieve all data from a table
cur.execute("SELECT * FROM Phonebook")

# fetch all rows of the result set
rows = cur.fetchall()

# print the rows
for row in rows:
    print(row)

# close the cursor and connection
cur.close()
conn.close()
