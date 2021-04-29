import psycopg2 as db
from faker import Faker

fake = Faker()
data = []
id = 1

for i in range(1000):
    data.append((id, fake.name(), fake.street_address(), fake.city(), fake.zipcode()))

    id += 1


data_for_db = tuple(data)

conn_string = "dbname='postgres' host='localhost' user='postgres' password='hello'"

conn = db.connect(conn_string)

cur = conn.cursor()

query = "insert into users(id,name,street,city,zip) values(%s,%s,%s,%s,%s)"

cur.executemany(query,data_for_db)
conn.commit()