import psycopg2


# Establish a connection to the database
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="martini")



cur = conn.cursor()

# Execute an INSERT statement to add a new employee to the employees table


cur.execute("UPDATE Doctor SET Speciality = %s, Salary = %s WHERE Doctor_Name = %s;",('general', 8000, 'Susan'))



# Commit the transaction
conn.commit()

# Close the cursor and database connection
cur.close()
conn.close()
