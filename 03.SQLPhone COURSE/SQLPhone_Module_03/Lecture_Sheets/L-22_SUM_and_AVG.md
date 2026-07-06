# 📘 SQLPhone Emperor · SQL Module 03
# 📖 L‑22 – SUM and AVG

## 🎯 OBJECTIVE
Calculate totals and averages over a set of rows
using `SUM` and `AVG`.

## 🧱 BRICK 1 – SUM
`SUM(column)` returns the sum of values in a numeric column.
NULLs are ignored.
```sql
SELECT SUM(salary) FROM employees;
```
Only works on numeric data.

## 🧱 BRICK 2 – AVG
`AVG(column)` returns the arithmetic mean.
It ignores NULLs and only works on numerics.
```sql
SELECT AVG(age) FROM users;
```

`AVG` can also be simulated with `SUM(column)/COUNT(column)`,
but using `AVG` is clearer and safer.

Both functions can be combined with `WHERE`:
```sql
SELECT SUM(amount) FROM orders WHERE status = 'paid';
```

## 💡 Real‑world Usage
- Total revenue of a quarter.
- Average order value.
- Sum of hours worked per project.

## 📌 Key Takeaway
`SUM` adds up values; `AVG` finds the mean.
Both ignore NULLs.
Filter with `WHERE` to aggregate subsets.

*Aggregation turns raw data into actionable insights.*