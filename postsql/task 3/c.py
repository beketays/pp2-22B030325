import psycopg2


    # Establish a connection to the database
conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="martini")



cur = conn.cursor()

    # Execute an INSERT statement to add a new employee to the employees table


cur.execute("SELECT h.name, SUM(d.salary) AS Total_Payment FROM Doctor d JOIN Hospital h ON d.hospital_id = h.Id GROUP BY h.name HAVING SUM(d.salary) < 60000 ORDER BY h.name;")

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
