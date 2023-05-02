import psycopg2

def insert_or_update_user(name, phone):
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="martini"
    )
    cur = conn.cursor()

    # Check if the user already exists
    cur.execute("SELECT COUNT(*) FROM Phonebook WHERE first_name = %s", (name,))
    
    count = cur.fetchone()[0]

    if count > 0:
        # Update the phone number for the existing user
       
        cur.execute("UPDATE Phonebook SET phone_number = %s WHERE first_name = %s", (phone, name))
        print("the name exist")
    else:
        # Insert a new user
        cur.execute("INSERT INTO Phonebook (first_name, phone_number) VALUES (%s, %s)", (name, phone))

    conn.commit()
    cur.close()
    conn.close()

# Usage example
a= input("enter the name:   ")
b= int(input("enter the phone number:   "))
insert_or_update_user(a, b)
