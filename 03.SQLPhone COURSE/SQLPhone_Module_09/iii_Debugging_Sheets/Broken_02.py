# 🐛 BROKEN – Module 09, Lesson 72 (Create Table)
# Missing conn.commit() after DDL; table not saved.

cur.execute('CREATE TABLE test (id INT)')
# ❌ need conn.commit()
