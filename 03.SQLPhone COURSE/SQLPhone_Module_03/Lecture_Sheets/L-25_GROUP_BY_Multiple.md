# 📘 SQLPhone Emperor · SQL Module 03
# 📖 L‑25 – GROUP BY – Multiple Columns

## 🎯 OBJECTIVE
Create nested groups using multiple columns in
the `GROUP BY` clause.

## 🧱 BRICK 1 – Multi‑Column Grouping
When you list more than one column, groups are formed
by unique combinations of the column values.
```sql
SELECT department, job_title, COUNT(*)
FROM employees
GROUP BY department, job_title;
```
Each department‑job combination gets a count.

## 🧱 BRICK 2 – Ordering and Filtering Multi‑Group Results
You can still use `ORDER BY` on any column,
and later `HAVING` (L‑26) to filter groups.

```sql
SELECT region, city, SUM(sales) AS total_sales
FROM stores
GROUP BY region, city
ORDER BY region, total_sales DESC;
```

**Remember:** Every non‑aggregate column in `SELECT`
must be in `GROUP BY`. If you forget one, SQLite
may not always complain (due to its flexibility),
but the result may be unpredictable. Stay disciplined.

## 💡 Real‑world Usage
- Sales by year and product category.
- Count of students by major and graduation year.
- Average response time by server and endpoint.

## 📌 Key Takeaway
Multiple GROUP BY columns create a finer granularity.
All non‑aggregate SELECT columns must appear in GROUP BY.
Sort afterwards with ORDER BY.

*Deeper grouping reveals hidden patterns.*