# 📘 SQLPhone Emperor · SQL Module 12
# 📖 L‑97 – Connecting Python to PostgreSQL

## 🎯 OBJECTIVE
Use the `psycopg2` library to connect Python to
PostgreSQL and perform basic operations.

## 🧱 BRICK 1 – Installing psycopg2
Inside your Debian proot environment (or any system
with PostgreSQL), install the adapter:
```bash
pip install psycopg2-binary
```

## 🧱 BRICK 2 – Basic Connection and Query
```python
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="testdb",
    user="emperor",
    password="your_password"
)
cur = conn.cursor()
cur.execute("SELECT version();")
print(cur.fetchone())
conn.close()
```

The pattern is nearly identical to `sqlite3`:
- `cursor()`, `execute()`, `fetchone()`, `fetchall()`
- Use `%s` as a placeholder instead of `?`
- Commit is required for DML.

## 💡 Real‑world Usage
- Building production backend services with Python.
- Migrating from SQLite to PostgreSQL when your app scales.

## 📌 Key Takeaway
`psycopg2` is the bridge from Python to PostgreSQL.
The syntax is familiar; the placeholder differs (`%s` vs `?`).
Your knowledge transfers seamlessly.

*What you learned on a phone, you can deploy to the cloud.*