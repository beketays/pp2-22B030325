import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="martini")

cur = conn.cursor()

# Execute an INSERT statement to add a new employee to the employees table



hospital = "INSERT INTO hospital (name) VALUES (%s)"


cur.execute(hospital, ('symbaT',))

# Commit the transaction
conn.commit()

# Close the cursor and database connection
cur.close()
conn.close()
