"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv
from config import CASTOMERS_DATA, EMPLOYEES_DATA, ORDERS_DATA


def main():
    with psycopg2.connect(
            host="localhost",
            database="north",
            user="postgres",
            password="zb4uosnn"
    ) as conn:
        with conn.cursor() as cur:
            with open(CASTOMERS_DATA, newline="", encoding="cp1251") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    customer_id = row["customer_id"]
                    company_name = row["company_name"]
                    contact_name = row["contact_name"]
                    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)",
                                (customer_id, company_name, contact_name))

            with open(EMPLOYEES_DATA, newline="", encoding="cp1251") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    employee_id = int(row['employee_id'])
                    first_name = row['first_name']
                    last_name = row['last_name']
                    title = row['title']
                    birth_date = row['birth_date']
                    notes = row['notes']
                    cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)',
                                (employee_id, first_name, last_name, title, birth_date, notes))

                with open(ORDERS_DATA, newline="", encoding="windows-1251") as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        order_id = int(row['order_id'])
                        customer_id = row['customer_id']
                        employee_id = int(row['employee_id'])
                        order_date = row['order_date']
                        ship_city = row['ship_city']
                        cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)',
                                    (order_id, customer_id, employee_id, order_date, ship_city))
    conn.close()


if __name__ == '__main__':
    main()
