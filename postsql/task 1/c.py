import psycopg2



conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="martini")



cur = conn.cursor()




cur.execute("SELECT AVG(bet_count) AS average_beds FROM hospital;")

rows = cur.fetchall()


for row in rows:
    print(row)



conn.commit()


cur.close()
conn.close()