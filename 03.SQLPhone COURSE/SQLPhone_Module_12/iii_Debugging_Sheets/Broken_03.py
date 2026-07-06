# 🐛 BROKEN – Module 12, Lesson 97 (psycopg2)
# Using SQLite placeholder '?' instead of '%s'.

cur.execute('SELECT * FROM users WHERE id = ?', (1,))  # ❌ should be %s
