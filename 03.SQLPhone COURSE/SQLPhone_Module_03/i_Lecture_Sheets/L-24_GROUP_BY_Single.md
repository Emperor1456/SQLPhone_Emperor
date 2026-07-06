# 📘 SQLPhone Emperor · SQL Module 03
# 📖 L‑24 – GROUP BY – Single Column

## 🎯 OBJECTIVE
Group rows by a single column and apply aggregate
functions per group.

## 🧱 BRICK 1 – GROUP BY Syntax
`GROUP BY` collapses rows that share the same value
in a column into a single summary row.
```sql
SELECT department, COUNT(*) AS total
FROM employees
GROUP BY department;
```
Each department appears once, with the count of employees.

## 🧱 BRICK 2 – Rules of GROUP BY
- All non‑aggregated columns in `SELECT` must appear
  in the `GROUP BY` clause.
- Aggregates like `COUNT`, `SUM`, `AVG` compute per group.
- `GROUP BY` comes after `WHERE` and before `ORDER BY`.

Example with `ORDER BY`:
```sql
SELECT city, AVG(age) AS avg_age
FROM residents
GROUP BY city
ORDER BY avg_age DESC;
```

## 💡 Real‑world Usage
- Number of orders per customer.
- Average test score per class.
- Total sales per region.

## 📌 Key Takeaway
`GROUP BY` segments your data.
Apply aggregate functions to each segment.
Non‑aggregated columns must be in the GROUP BY.

*Grouping organises chaos into categories.*