# 📘 SQLPhone Emperor · SQL Module 05
# 📖 L‑45 – WITH Clause (CTEs)

## 🎯 OBJECTIVE
Simplify complex queries by defining temporary
named result sets using Common Table Expressions (CTEs).

## 🧱 BRICK 1 – CTE Syntax
`WITH` defines one or more named queries that can be
referenced later in the main `SELECT`.

```sql
WITH department_avg AS (
    SELECT department, AVG(salary) AS avg_sal
    FROM employees
    GROUP BY department
)
SELECT e.name, e.salary, d.avg_sal
FROM employees e
JOIN department_avg d ON e.department = d.department
WHERE e.salary > d.avg_sal;
```
`department_avg` is used like a temporary table.

## 🧱 BRICK 2 – Multiple CTEs and Recursion
Multiple CTEs can be chained:
```sql
WITH
cte1 AS (...),
cte2 AS (...)
SELECT ... FROM cte1 JOIN cte2 ...
```

SQLite also supports recursive CTEs for hierarchical
data (advanced). That’s beyond this scope, but know
that `WITH` is the foundation.

## 💡 Real‑world Usage
- Break complex reports into logical steps.
- Reuse intermediate calculations.
- Make queries self‑documenting.

## 📌 Key Takeaway
CTEs (WITH) improve readability and maintainability.
They let you compose queries step by step.
Think of them as views that exist only for the query.

*Name your intermediate steps – clarity over cleverness.*