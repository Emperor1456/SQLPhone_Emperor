# 📘 SQLPhone Emperor · SQL Module 07
# 📖 L‑59 – Mathematical Functions

## 🎯 OBJECTIVE
Perform calculations inside SQL using built‑in math
functions.

## 🧱 BRICK 1 – Core Math Functions
- `ABS(x)` – absolute value
- `ROUND(x, d)` – round to d decimal places
- `RANDOM()` – random 64‑bit integer
- `RANDOMBLOB(n)` – n‑byte random blob
- `MAX()`, `MIN()` – aggregate functions (already covered)

```sql
SELECT ABS(-5), ROUND(3.14159, 2), RANDOM();
```

## 🧱 BRICK 2 – Arithmetic Expressions
SQLite supports standard arithmetic: `+`, `-`, `*`, `/`, `%`.
```sql
SELECT price * quantity AS total FROM orders;
```
Modulo: `10 % 3` returns 1.

There’s no native power or square root, but you can use
`pow()` via extension or compute manually if needed.
For advanced math, process data in Python.

## 💡 Real‑world Usage
- Calculate tax, discounts, totals.
- Generate random sample data.
- Round currency to two decimals.

## 📌 Key Takeaway
SQL math is basic but essential.
Do heavy calculations in the application layer.
For simple arithmetic, SQL is fast and expressive.

*Numbers don’t lie – compute them close to the data.*