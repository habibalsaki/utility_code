import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_query = "CREATE table users (id int, username text, password text)"

cursor.execute(create_query)

insert_query = "INSERT into users VALUES (?, ?, ?)"

users = [
    (1,"habib","hello"),
    (2,"zobayer","asdf")
]

cursor.executemany(insert_query,users)

connection.commit()

connection.close()