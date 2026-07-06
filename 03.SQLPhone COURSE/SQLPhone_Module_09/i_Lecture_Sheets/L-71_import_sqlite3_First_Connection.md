# 📘 SQLPhone Emperor · SQL Module 09
# 📖 L‑71 – import sqlite3 – First Connection

## 🎯 OBJECTIVE
Connect Python to SQLite using the built‑in `sqlite3` module.

## 🧱 BRICK 1 – Establishing a Connection
The `sqlite3` module is part of Python's standard library.
```python
import sqlite3
conn = sqlite3.connect('mydb.db')
```
If the file doesn’t exist, SQLite creates it.
To work in memory:
```python
conn = sqlite3.connect(':memory:')
```
Always close the connection when done:
```python
conn.close()
```
Use a cursor to execute SQL:
```python
cur = conn.cursor()
cur.execute('CREATE TABLE test (id INT)')
conn.commit()
```

## 🧱 BRICK 2 – Connection Settings
You can set several pragmas at connection time:
```python
conn = sqlite3.connect('mydb.db')
conn.execute('PRAGMA foreign_keys = ON')
```
Or as part of the connection string using `uri=True` (not needed for basics).
Use `with` statement for auto‑commit/rollback:
```python
with sqlite3.connect('mydb.db') as conn:
    conn.execute('INSERT INTO test VALUES (1)')
```
This commits on success, rolls back on exception.

## 💡 Real‑world Usage
- Every Python script that touches a database.
- Data pipelines, web apps, CLI tools.

## 📌 Key Takeaway
`sqlite3.connect()` opens a database file.
Use a cursor to execute SQL.
Always commit, and close or use `with`.

*Python meets SQL – the integration begins.*