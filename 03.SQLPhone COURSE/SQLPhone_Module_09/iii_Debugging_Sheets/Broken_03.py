# 🐛 BROKEN – Module 09, Lesson 74 (fetch methods)
# fetchone() called after fetchall() returns empty.

cur.execute('SELECT * FROM users')
all_rows = cur.fetchall()
first = cur.fetchone()  # ❌ returns None
