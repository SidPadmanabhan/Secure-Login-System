import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Create a table
# Create a table with columns: id, email, and password
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   email TEXT NOT NULL UNIQUE,
                   password TEXT NOT NULL)''')

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

cursor.execute("SELECT email, password FROM users")
rows = cursor.fetchall()

print("Stored User Credentials:")
for row in rows: 
  print(f"Email: {row[0]}, Password: {row[1]}")

conn.close()


