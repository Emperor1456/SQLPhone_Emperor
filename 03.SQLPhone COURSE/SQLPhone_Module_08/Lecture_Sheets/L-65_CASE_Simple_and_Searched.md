# 📘 SQLPhone Emperor · SQL Module 08
# 📖 L‑65 – CASE – Simple and Searched

## 🎯 OBJECTIVE
Add conditional logic to queries using `CASE` expressions.

## 🧱 BRICK 1 – Simple CASE
Compares an expression against a list of values.
```sql
SELECT name,
  CASE department
    WHEN 'Sales' THEN 'Revenue'
    WHEN 'Engineering' THEN 'Product'
    ELSE 'Support'
  END AS division
FROM employees;
```
The first matching `WHEN` is used; `ELSE` is optional (defaults to NULL).

## 🧱 BRICK 2 – Searched CASE
Evaluates boolean conditions in sequence.
```sql
SELECT name, salary,
  CASE
    WHEN salary > 100000 THEN 'High'
    WHEN salary > 50000  THEN 'Medium'
    ELSE 'Low'
  END AS band
FROM employees;
```
Much more flexible; can use any boolean expression.

## 💡 Real‑world Usage
- Translate codes to labels (e.g., status codes).
- Create custom groupings for reports.
- Apply business rules inside queries.

## 📌 Key Takeaway
`CASE` is SQL’s `if‑else`.
Use simple `CASE` for equality checks, searched `CASE` for complex conditions.
It works in `SELECT`, `WHERE`, `ORDER BY`, and more.

*Conditional logic turns data into decisions.*