import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   email TEXT)''')
# Insert data into the table
cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", ("john@gmail.com", "johnny"))
cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", ("jane@gmail.com", "jane123" ))
cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", ("goat@gmail.com", "iamlebron"))
cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", ("franksinatra@gmail.com", "music55" ))
cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", ("drake@gmail.com", "drizzy"))
cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", ("abeltesfaye@gmail.com", "theweeknd23" ))
cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", ("aaronrodgers", "ifellof"))




# Commit the changes and close the connection
conn.commit()
conn.close()

# Retrieve data from the table
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Display the retrieved data
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")

# Close the connection
conn.close()


