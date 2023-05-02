import psycopg2



conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="martini")



cur = conn.cursor()




cur.execute("select * from hospital ORDER BY name ASC;")

rows = cur.fetchall()


for row in rows:
    print(row)



conn.commit()


cur.close()
conn.close()
