import psycopg2



conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="martini")



cur = conn.cursor()




cur.execute("SELECT d.doctor_name, h.name FROM Doctor d JOIN hospital h ON d.hospital_id = h.Id WHERE h.bet_count > 800 AND d.salary >= 32000;")

rows = cur.fetchall()


for row in rows:
    print(row)



conn.commit()


cur.close()
conn.close()
