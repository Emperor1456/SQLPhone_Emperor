# 📘 SQLPhone Emperor · SQL Module 09
# 📖 L‑78 – Reusable Helper Module

## 🎯 OBJECTIVE
Build a reusable Python module that simplifies common
database operations.

## 🧱 BRICK 1 – Creating a Database Class
Encapsulate connection, cursor, and common methods.
```python
class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.conn.execute('PRAGMA foreign_keys = ON')
    
    def query(self, sql, params=()):
        cur = self.conn.cursor()
        cur.execute(sql, params)
        return cur.fetchall()
    
    def execute(self, sql, params=()):
        cur = self.conn.cursor()
        cur.execute(sql, params)
        self.conn.commit()
    
    def close(self):
        self.conn.close()
```
This reduces boilerplate in the main application.

## 🧱 BRICK 2 – Adding Convenience Methods
Add methods like `insert(table, data_dict)`, `update(...)`, etc.
Make the module importable from other scripts.
Store it as `db_helper.py` or `database.py`.

## 💡 Real‑world Usage
- Centralise connection management.
- Enforce consistent error handling.
- Speed up development of database‑driven apps.

## 📌 Key Takeaway
Wrap raw `sqlite3` calls in a class to reduce repetition.
Make it your personal library for every project.
Keep it simple, but robust.

*Build once, use everywhere – your database toolkit.*