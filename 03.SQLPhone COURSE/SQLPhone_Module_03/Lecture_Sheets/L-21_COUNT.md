# 📘 SQLPhone Emperor · SQL Module 03
# 📖 L‑21 – COUNT

## 🎯 OBJECTIVE
Count rows in a table using `COUNT`, understand its
behaviour with NULLs and `DISTINCT`.

## 🧱 BRICK 1 – COUNT(*)
`COUNT(*)` returns the total number of rows in a table
or group, regardless of NULL values.
```sql
SELECT COUNT(*) FROM employees;
```

`COUNT(column)` counts only non‑NULL values in that column.
```sql
SELECT COUNT(phone) FROM contacts;
```
If some phone numbers are NULL, they are ignored.

## 🧱 BRICK 2 – COUNT with DISTINCT
`COUNT(DISTINCT column)` counts unique non‑NULL values.
```sql
SELECT COUNT(DISTINCT department) FROM employees;
```
Returns the number of different departments.

**Performance note:** `COUNT(*)` is optimised in SQLite
because it can read from internal table metadata
when there is no `WHERE` clause.

## 💡 Real‑world Usage
- Number of registered users.
- Count of distinct products sold.
- Total orders placed in a month.

## 📌 Key Takeaway
`COUNT(*)` counts rows.
`COUNT(column)` ignores NULLs.
Add `DISTINCT` to count unique values.

*Counting is the first step of data analysis.*