import psycopg2



conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="martini")



cur = conn.cursor()



cur.execute("UPDATE Doctor SET Speciality = %s, Salary = %s WHERE Doctor_Name = %s;",('general', 10000, 'David'))




conn.commit()


cur.close()
conn.close()
