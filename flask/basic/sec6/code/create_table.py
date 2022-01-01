import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_user_query = "CREATE table users (id INTEGER PRIMARY KEY, username text, password text)"

cursor.execute(create_user_query)

create_item_query = "CREATE table items (name text, price real)"

cursor.execute(create_item_query)

connection.commit()

connection.close()