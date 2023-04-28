

import psycopg2
import csv

# Establish a connection to the database
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="martini")

cur = conn.cursor()

with open('/home/asifjahish/vscode/.vscode/practice/task2/Sheet1.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        cur.execute("INSERT INTO Doctor(doctor_id, doctor_name, hospital_id,joining_date, speciality, salary, experience) VALUES (%s, %s, %s, %s, %s, %s,%s);",
            (row[0], row[1], row[2], row[3],row[4], row[5], row[6]))

conn.commit()

cur.close()
conn.close()