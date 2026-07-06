# 📘 SQLPhone Emperor · SQL Module 03
# 📖 L‑26 – HAVING

## 🎯 OBJECTIVE
Filter groups after aggregation using `HAVING`.

## 🧱 BRICK 1 – HAVING vs WHERE
`WHERE` filters individual rows **before** grouping.
`HAVING` filters groups **after** aggregation.

```sql
SELECT department, COUNT(*) as cnt
FROM employees
WHERE salary > 40000
GROUP BY department
HAVING cnt > 5;
```
This finds departments with more than 5 employees
who earn over 40k.

## 🧱 BRICK 2 – HAVING with Aggregate Conditions
You can use any aggregate expression in `HAVING`:
```sql
SELECT product_id, SUM(quantity) as total_sold
FROM order_items
GROUP BY product_id
HAVING total_sold > 100;
```

`HAVING` can reference the alias defined in `SELECT`
(in SQLite and most DBMS).

**Order of execution:**  
`FROM` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT` → `ORDER BY`

## 💡 Real‑world Usage
- Categories with more than 10 sales.
- Departments whose average salary exceeds 70k.
- Customer segments spending above a threshold.

## 📌 Key Takeaway
Use `WHERE` for row‑level filters.
Use `HAVING` for group‑level filters.
Both can appear in the same query.

*Filter rows before grouping, filter groups after.*