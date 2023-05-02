import psycopg2

def insert_users(user_list):
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="martini"
    )
    cur = conn.cursor()
    invalid_data = []

    for entry in user_list:
        first_name, last_name, phone = entry.split('|')
        
        # Check the correctness of the phone number
        if not phone.isdigit() or len(phone) < 10:
            invalid_data.append(entry)
        else:
            # Check if the user already exists
            cur.execute("SELECT COUNT(*) FROM Phonebook WHERE first_name = %s AND last_name = %s", (first_name, last_name))
            count = cur.fetchone()[0]

            if count > 0:
                # Update the phone number for the existing user
                cur.execute("UPDATE Phonebook SET phone_number = %s WHERE first_name = %s AND last_name = %s", (phone, first_name, last_name))
            else:
                # Insert a new user
                cur.execute("INSERT INTO Phonebook (first_name, last_name, phone_number) VALUES (%s, %s, %s)", (first_name, last_name, phone))

    conn.commit()
    cur.close()
    conn.close()

    return invalid_data

# Usage example
user_list = ['Jfgfgfhn|Doe|1234567890', 'Jane|Smith|987654321', 'Invalid|User|123']
invalid_data = insert_users(user_list)
print('Invalid Data:', invalid_data)
