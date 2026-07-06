# 📘 SQLPhone Emperor · SQL Module 08
# 📖 L‑69 – Materialized Views (Alternatives)

## 🎯 OBJECTIVE
Learn what materialized views are and how to simulate
them in SQLite.

## 🧱 BRICK 1 – Materialized View Concept
A materialized view stores the result set of a query
on disk, like a cached table. It’s refreshed manually
or on a schedule. SQLite does not support them natively.

## 🧱 BRICK 2 – Simulation in SQLite
Create a physical table and populate it with the query
result. Refresh by dropping and recreating.

```sql
-- Initial creation
CREATE TABLE sales_summary AS
SELECT product_id, SUM(amount) AS total
FROM orders
GROUP BY product_id;

-- Refresh
DELETE FROM sales_summary;
INSERT INTO sales_summary
SELECT product_id, SUM(amount) AS total
FROM orders
GROUP BY product_id;
```
Alternatively, use a trigger to keep it updated (advanced).

## 💡 Real‑world Usage
- Pre‑compute reports for dashboards.
- Cache expensive aggregations.
- Improve read performance on static data.

## 📌 Key Takeaway
SQLite lacks materialized views, but you can mimic them.
Manually refresh a summary table when needed.
This is a performance optimisation pattern.

*Cache your complex queries in a table, not in memory.*