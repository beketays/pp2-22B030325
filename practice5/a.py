import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="your_host",
    database="your_database",
    user="your_user",
    password="your_password"
)

# Create a new table called "myqueue"
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE myqueue (
    id SERIAL PRIMARY KEY,
    data TEXT,
    insert_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
''')
conn.commit()

# Insert data into the queue
cursor.execute("INSERT INTO myqueue (data) VALUES ('first')")
cursor.execute("INSERT INTO myqueue (data) VALUES ('second')")
cursor.execute("INSERT INTO myqueue (data) VALUES ('third')")
conn.commit()

# Retrieve data from the queue
cursor.execute("SELECT * FROM myqueue ORDER BY insert_time ASC")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Remove data from the queue
cursor.execute("DELETE FROM myqueue WHERE id = (SELECT MIN(id) FROM myqueue)")
conn.commit()