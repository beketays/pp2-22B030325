import psycopg2

def delete_data_by_username_or_phone(username, phone):
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="martini"
    )
    cur = conn.cursor()

    if username is not None:
        cur.execute("DELETE FROM Phonebook WHERE first_name = %s OR last_name = %s", (username, username))
    
    if phone is not None:
        cur.execute("DELETE FROM Phonebook WHERE phone_number = %s", (phone,))

    conn.commit()
    cur.close()
    conn.close()

# Usage example
username = 'pp2'
phone = '1234567890'
delete_data_by_username_or_phone(username, phone)
