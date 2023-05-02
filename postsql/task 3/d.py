import psycopg2
import csv



conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="martini")


cur = conn.cursor()


def export_data_to_csv(file_path):
    cur.execute("SELECT d.doctor_name, h.name, d.joining_date, d.speciality, d.salary, d.experience FROM Doctor d JOIN Hospital h ON d.hospital_id = h.Id")
    rows = cur.fetchall()


    with open('/Users/symbat/Documents/pp2-22B030325/postsql/task 3/Sheet2.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['doctor-name', 'name', 'joining_date', 'speciality', 'salary', 'experience'])
        writer.writerows(rows)

    print("Data exported to CSV file successfully.")


export_data_to_csv("output.csv")

cur.close()
conn.close()