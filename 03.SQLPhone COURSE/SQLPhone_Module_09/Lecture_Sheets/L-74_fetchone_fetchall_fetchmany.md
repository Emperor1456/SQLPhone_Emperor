# 📘 SQLPhone Emperor · SQL Module 09
# 📖 L‑74 – fetchone(), fetchall(), fetchmany()

## 🎯 OBJECTIVE
Retrieve query results in Python using fetch methods.

## 🧱 BRICK 1 – fetchone() and fetchall()
- `fetchone()` returns the next row as a tuple, or `None`.
- `fetchall()` returns a list of all remaining rows.

```python
cur.execute('SELECT id, name FROM employees')
first = cur.fetchone()
print(first)          # (1, 'Alice')
all_rows = cur.fetchall()
print(all_rows)       # [(2, 'Bob'), (3, 'Carol')]
```
Note: after `fetchone()`, `fetchall()` returns the rest.

## 🧱 BRICK 2 – fetchmany(size)
Fetches a specific number of rows.
```python
cur.execute('SELECT * FROM large_table')
batch = cur.fetchmany(100)
```
Useful for processing large datasets without loading
everything into memory at once.

After fetching all rows, `fetch*` returns empty list/None.

## 💡 Real‑world Usage
- Display query results in a terminal.
- Export data chunk by chunk.
- Loop over result sets.

## 📌 Key Takeaway
`fetchone()` for one row, `fetchall()` for all remaining,
`fetchmany(n)` for pagination.
Choose the right method for memory efficiency.

*Fetch only what you need, when you need it.*