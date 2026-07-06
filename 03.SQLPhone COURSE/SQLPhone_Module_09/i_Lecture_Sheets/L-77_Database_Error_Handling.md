# 📘 SQLPhone Emperor · SQL Module 09
# 📖 L‑77 – Database Error Handling

## 🎯 OBJECTIVE
Handle database errors gracefully using `try/except`.

## 🧱 BRICK 1 – Catching sqlite3 Errors
All database errors inherit from `sqlite3.Error`.
```python
try:
    cur.execute('INSERT INTO employees VALUES (1, "Alice")')
except sqlite3.IntegrityError:
    print('Duplicate ID!')
except sqlite3.Error as e:
    print(f'Database error: {e}')
```
`IntegrityError` is raised for constraint violations,
`OperationalError` for syntax mistakes, etc.

## 🧱 BRICK 2 – Transaction Rollback on Error
Wrap multiple operations in a transaction.
If any fails, roll back all changes.
```python
try:
    cur.execute('INSERT ...')
    cur.execute('UPDATE ...')
    conn.commit()
except sqlite3.Error:
    conn.rollback()
    print('Transaction failed, rolled back.')
```
Using `with conn:` also handles this automatically.

## 💡 Real‑world Usage
- User‑friendly error messages.
- Atomic operations (all or nothing).
- Logging and debugging.

## 📌 Key Takeaway
Always catch `sqlite3.Error` around database operations.
Use `rollback()` to revert partial changes.
Don’t let a query crash your whole program.

*Errors happen; handle them with grace.*