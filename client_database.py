import sqlite3


conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   email TEXT NOT NULL UNIQUE,
                   password TEXT NOT NULL)''')

cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", ("john@gmail.com", "johnny"))
cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", ("jane@gmail.com", "jane123" ))
cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", ("goat@gmail.com", "iamlebron"))
cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", ("franksinatra@gmail.com", "music55" ))
cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", ("drake@gmail.com", "drizzy"))
cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", ("abeltesfaye@gmail.com", "theweeknd23" ))
cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", ("aaronrodgers@gmail.com", "ifelloff"))


conn.commit()

cursor.execute("SELECT email, password FROM users")
rows = cursor.fetchall()

print("Stored User Credentials:")
for row in rows: 
  print(f"Email: {row[0]}, Password: {row[1]}")

conn.close()


