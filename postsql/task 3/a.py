import psycopg2


conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="martini")



cur = conn.cursor()


cur.execute("SELECT d.doctor_name, h.name, d.joining_date, d.salary FROM Doctor d JOIN hospital h ON d.hospital_Id = h.Id;")

rows = cur.fetchall()


for row in rows:
        print(row)



conn.commit()


cur.close()
conn.close()
