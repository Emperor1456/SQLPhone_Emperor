# 📘 SQLPhone Emperor · SQL Module 09
# 📖 L‑73 – Parameterized Insert (Anti‑Injection)

## 🎯 OBJECTIVE
Insert data safely using parameterized queries to
prevent SQL injection.

## 🧱 BRICK 1 – Parameterized Queries
Use placeholders (`?`) and a tuple of values.
```python
name = input('Name: ')
salary = float(input('Salary: '))
cur.execute('INSERT INTO employees (name, salary) VALUES (?, ?)', (name, salary))
```
SQLite automatically escapes and quotes the values.

**Never** use string formatting (`f'...'` or `%`) to build
SQL with user input – it’s a major security risk.

## 🧱 BRICK 2 – Inserting Multiple Rows
`executemany()` efficiently inserts many records.
```python
employees = [('Alice', 60000), ('Bob', 75000), ('Carol', 80000)]
cur.executemany('INSERT INTO employees (name, salary) VALUES (?, ?)', employees)
```
This is faster than a loop with `execute()`.

## 💡 Real‑world Usage
- User registration.
- Importing CSV data.
- Anywhere external data enters the database.

## 📌 Key Takeaway
Always use parameterized queries with `?` placeholders.
`executemany()` for batch inserts.
Protect your database from malicious input.

*Trust no input – parameters are your shield.*