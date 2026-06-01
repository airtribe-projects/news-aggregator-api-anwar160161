import sqlite3

conn = sqlite3.connect("news.db")

cursor = conn.cursor()

print("USERS")
for row in cursor.execute("SELECT * FROM users"):
    print(row)

print("\nPREFERENCES")
for row in cursor.execute("SELECT * FROM preferences"):
    print(row)

conn.close()