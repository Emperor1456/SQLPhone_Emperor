# 04.SQLPhone NOTES/Module_05_Subqueries_CTEs.md
# SQLPhone Emperor — The Best Phone‑First SQL Curriculum

# 📝 Module 05 – Subqueries & CTEs

## Subquery Types
- **Scalar**: returns one value (used with `=`, `>`, etc.)
- **Multi‑row**: returns a column (used with `IN`, `ANY`, `ALL`)
- **Correlated**: references outer query columns

## Common Patterns
```sql
-- Subquery in WHERE
SELECT name FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Subquery in SELECT
SELECT name, (SELECT AVG(salary) FROM employees) AS avg_salary
FROM employees;

-- EXISTS / NOT EXISTS (NULL‑safe)
SELECT c.name FROM customers c
WHERE EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id);

-- ANY / ALL
SELECT name FROM products
WHERE price > ALL (SELECT price FROM products WHERE category='Electronics');
```

## CTEs (WITH clause)
- Named temporary result set for readability.
```sql
WITH dept_avg AS (
  SELECT department, AVG(salary) AS avg_sal
  FROM employees GROUP BY department
)
SELECT e.name, e.salary, d.avg_sal
FROM employees e JOIN dept_avg d ON e.department = d.department
WHERE e.salary > d.avg_sal;
```
