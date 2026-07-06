# 🐛 BROKEN – Module 09, Lesson 73 (Parameterized Insert)
# Uses string formatting instead of parameters. Fix with ?.

name = input('Name: ')
cur.execute(f"INSERT INTO users (name) VALUES ('{name}')")
conn.commit()
