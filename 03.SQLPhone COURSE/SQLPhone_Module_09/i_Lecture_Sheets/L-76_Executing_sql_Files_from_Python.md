# 📘 SQLPhone Emperor · SQL Module 09
# 📖 L‑76 – Executing .sql Files from Python

## 🎯 OBJECTIVE
Run external SQL scripts stored in `.sql` files from
a Python program.

## 🧱 BRICK 1 – Reading and Executing SQL File
You can read the file and pass it to `executescript()`:
```python
with open('schema.sql', 'r') as f:
    sql = f.read()
conn.executescript(sql)
conn.commit()
```
This is ideal for database initialisation scripts.

## 🧱 BRICK 2 – Executing Statements Individually
If you need feedback per statement, split by `;` and execute
one by one (ignoring empty lines). `executescript()` is
easier for most cases.

```python
for statement in sql.split(';'):
    statement = statement.strip()
    if statement:
        cur.execute(statement)
conn.commit()
```

## 💡 Real‑world Usage
- Automated database migrations.
- Seeding data from SQL dumps.
- CI/CD pipeline database setup.

## 📌 Key Takeaway
Store complex DDL/DML in `.sql` files.
Use `executescript()` for simple execution.
Separate SQL logic from Python for maintainability.

*Script the database; Python orchestrates.*