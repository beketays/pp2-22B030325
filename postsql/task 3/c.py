import psycopg2



conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="martini")



cur = conn.cursor()




cur.execute("SELECT h.name, SUM(d.salary) AS Total_Payment FROM Doctor d JOIN Hospital h ON d.hospital_id = h.Id GROUP BY h.name HAVING SUM(d.salary) < 60000 ORDER BY h.name;")

rows = cur.fetchall()


for row in rows:
    print(row)



conn.commit()


cur.close()
conn.close()
