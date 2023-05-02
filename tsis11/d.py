import psycopg2

def query_data_with_pagination(table_name, limit, offset):
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="martini"
    )
    cur = conn.cursor()

    # Query data with pagination
    query = f"SELECT * FROM {table_name} LIMIT %s OFFSET %s"
    cur.execute(query, (limit, offset))
    rows = cur.fetchall()

    # Process the retrieved data
    for row in rows:
        # Process each row
        print(row)

    cur.close()
    conn.close()

# Usage example
table_name = "Phonebook"
limit = 7
offset = 0
query_data_with_pagination(table_name, limit, offset)
