import psycopg2

# Establish a connection to the database
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="postgres",
    user="postgres",
    password="martini"
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute an INSERT statement to add a new employee to the employees table
people = "INSERT INTO Phonebook (first_name, last_name, address, phone_number ) VALUES (%s, %s, %s, %s) RETURNING id;"

many = "INSERT INTO Phonebook (first_name, last_name, address, phone_number )  VALUES (%s, %s, %s, %s);"

cur.execute(people, ("her", "pro", "Almaty", 23232))


p = [
    ('fgd2','python', 'KZ', 7700245350),
    ('gfd1', 'java', 'Kz', 2987656789)
]
cur.executemany(many, p)



# Commit the transaction
conn.commit()

# Close the cursor and database connection
cur.close()
conn.close()
