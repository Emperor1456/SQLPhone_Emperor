# 📘 SQLPhone Emperor · SQL Module 09
# 📖 L‑72 – Creating Tables via Python

## 🎯 OBJECTIVE
Execute `CREATE TABLE` statements from Python scripts.

## 🧱 BRICK 1 – Executing DDL
Use `cursor.execute()` for a single statement.
```python
cur.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        salary REAL
    )
''')
conn.commit()
```

`IF NOT EXISTS` prevents errors if the table already exists.

## 🧱 BRICK 2 – Executing Multiple Statements
`executescript()` runs multiple SQL statements separated
by semicolons. It’s useful for initialising a database.
```python
conn.executescript('''
    DROP TABLE IF EXISTS temp;
    CREATE TABLE temp (data TEXT);
    INSERT INTO temp VALUES ('seed');
''')
```
`executescript()` does not return results, only executes.

## 💡 Real‑world Usage
- Schema migrations.
- Test database setup.
- Application first‑run.

## 📌 Key Takeaway
Use `execute()` for single DDL statements.
Use `executescript()` for multi‑statement scripts.
Always commit after structural changes.

*Build your schema with Python as the architect.*