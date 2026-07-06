# 04.SQLPhone NOTES/Module_09_Python_SQLite.md
# SQLPhone Emperor — The Best Phone‑First SQL Curriculum

# 📝 Module 09 – Python + SQLite Integration

## Connecting
```python
import sqlite3
conn = sqlite3.connect('mydb.db')   # file or ':memory:'
cur = conn.cursor()
```

## Executing Queries
- `cur.execute(sql, params)` – parameterized (`?` placeholders).
- `cur.executescript(sql_script)` – multiple statements.
- `conn.commit()` to save changes.

## Fetching Results
- `fetchone()`, `fetchall()`, `fetchmany(size)`

## Error Handling
- Catch `sqlite3.Error`, `IntegrityError`, etc.
- Use `try/except` and `conn.rollback()`.

## Reusable Helper Class
```python
class DB:
    def __init__(self, db): self.conn = sqlite3.connect(db)
    def query(self, sql, params=()): return self.conn.execute(sql, params).fetchall()
    def execute(self, sql, params=()): self.conn.execute(sql, params); self.conn.commit()
    def close(self): self.conn.close()
```

## Mini Project: Contact Book
- Menu loop, CRUD operations, parameterized queries.
- Export to CSV option.
