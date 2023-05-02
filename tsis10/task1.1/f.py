# Implement updating data in the table (change user first name or phone)


import psycopg2

# Establish a connection to the database
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="postgres",
    user="postgres",
    password="martini"
)

cur = conn.cursor()

# Execute an INSERT statement to add a new employee to the employees table


cur.execute("SELECT * FROM Phonebook WHERE address = 'Almaty';")
rows = cur.fetchall()

# Process the retrieved data
for row in rows:
    # Process each row
    print(row)




# Commit the transaction
conn.commit()

# Close the cursor and database connection
cur.close()
conn.close()