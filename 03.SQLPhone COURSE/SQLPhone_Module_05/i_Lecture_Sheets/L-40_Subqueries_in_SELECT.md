# 📘 SQLPhone Emperor · SQL Module 05
# 📖 L‑40 – Subqueries in SELECT

## 🎯 OBJECTIVE
Embed a scalar subquery in the `SELECT` list to
attach computed values to each row.

## 🧱 BRICK 1 – Scalar Subquery in SELECT
A subquery in `SELECT` must return exactly one value.
It runs once per output row (unless optimised).

```sql
SELECT name, salary,
       (SELECT AVG(salary) FROM employees) AS avg_salary
FROM employees;
```
Every row gets the same average salary attached.

## 🧱 BRICK 2 – Correlated vs Uncorrelated
- **Uncorrelated** subquery does not reference the outer
  query’s columns. It runs once and the result is reused.
- **Correlated** subquery (later lesson) references outer
  columns, re‑executed for each row.

A subquery in `SELECT` is most useful for quick
comparisons without a join.

## 💡 Real‑world Usage
- Show each product’s price alongside the category average.
- Display an employee’s salary as a percentage of the
  department maximum.

## 📌 Key Takeaway
`SELECT` subqueries attach aggregated metadata.
They must be scalar (one value).
Use them for inline calculations.

*Carry the context with every row.*