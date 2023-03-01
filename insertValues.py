import sqlite3

# Open a connection to the database
conn = sqlite3.connect('image.db')

# Open the image file and convert it to binary format
with open('sss.jpg', 'rb') as f:
    image_data = f.read()

# Insert the binary data into the database
conn.execute('INSERT INTO images (image_data) VALUES (?)', (sqlite3.Binary(image_data),))

# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()
