import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="martini")

cur = conn.cursor()

# Execute an INSERT statement to add a new employee to the employees table



#hospital = "SELECT * FROM hospital "


cur.execute("SELECT * FROM hospital")

rows = cur.fetchall()

for row in rows:
    # Process each row
    print(row)
# Commit the transaction
conn.commit()

# Close the cursor and database connection
cur.close()
conn.close()
