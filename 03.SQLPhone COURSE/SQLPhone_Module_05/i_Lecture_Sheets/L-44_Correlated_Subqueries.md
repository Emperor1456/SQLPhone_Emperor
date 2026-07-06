# 📘 SQLPhone Emperor · SQL Module 05
# 📖 L‑44 – Correlated Subqueries

## 🎯 OBJECTIVE
Write subqueries that reference columns from the outer
query, executing once per outer row.

## 🧱 BRICK 1 – How Correlation Works
A correlated subquery contains a reference to the
outer query. It cannot run independently; it is
evaluated for each row of the outer query.

```sql
SELECT e.name, e.salary
FROM employees e
WHERE e.salary > (
    SELECT AVG(salary)
    FROM employees
    WHERE department = e.department
);
```
For each employee, the subquery computes the average
salary of their own department.

## 🧱 BRICK 2 – Performance Considerations
Correlated subqueries can be slow on large datasets
because the inner query runs many times.
Often a `JOIN` with `GROUP BY` can achieve the same
result more efficiently. Use `EXPLAIN QUERY PLAN`
to compare.

But for clarity and small data, correlated subqueries
are readable and expressive.

## 💡 Real‑world Usage
- "Above‑average‑in‑their‑category" queries.
- Row‑by‑row cumulative calculations (advanced).
- Where performance is not critical.

## 📌 Key Takeaway
Correlated subqueries bring per‑row context.
They are powerful but can be performance‑heavy.
Always consider a join‑based alternative for large tables.

*Let the outer row whisper to the inner query.*