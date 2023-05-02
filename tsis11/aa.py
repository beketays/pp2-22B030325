import psycopg2

# Establish a connection to the database
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="martini"
)

cur = conn.cursor()

# Prompt the user for input
name_pattern = input("Enter the name pattern: ")
surname_pattern = input("Enter the last name pattern: ")
phone_pattern = int(input("Enter the first digit of the phone number: "))

# Execute the query
cur.execute("SELECT * FROM Phonebook WHERE first_name ILIKE %s OR last_name ILIKE %s OR phone_number::text LIKE %s", (name_pattern+'%', surname_pattern+'%', str(phone_pattern)+'%'))

rows = cur.fetchall()

# Process the retrieved data
for row in rows:
    # Process each row
    print(row)

# Close the cursor and database connection
cur.close()
conn.close()
