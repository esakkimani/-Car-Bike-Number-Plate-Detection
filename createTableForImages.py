import time
import sqlite3

while True:
    try:
        conn = sqlite3.connect('database.db')

        with open('sss.jpg', 'rb') as f:
            image_data = f.read()

        # Insert the binary data into the database
        conn.execute('INSERT INTO images (image_data) VALUES (?)', ( sqlite3.Binary(image_data),))
        conn.close()
        print("created")
        break
    except sqlite3.OperationalError:
        print('Database is locked. Waiting...')
        time.sleep(1)
