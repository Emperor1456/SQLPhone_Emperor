# 🐛 BROKEN SCRIPT – Module 09
# This Python script should insert a user safely, but it's vulnerable to SQL injection.
# Fix it by using parameterized queries.

import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE users (name TEXT, password TEXT)")

user = input("Enter username: ")
pwd = input("Enter password: ")

# Broken: string formatting
conn.execute(f"INSERT INTO users VALUES ('{user}', '{pwd}')")
conn.commit()

print("User added.")

# After fixing, remove the f-string and use ? placeholders.
