# 📘 SQLPhone Emperor · SQL Module 03
# 📖 L‑27 – Combining WHERE, GROUP BY, and HAVING

## 🎯 OBJECTIVE
Master the full aggregation pipeline by combining
all three clauses in one query.

## 🧱 BRICK 1 – Query Pipeline Order
A complete aggregation query follows this logical order:
1. `FROM` – source tables
2. `WHERE` – row filter
3. `GROUP BY` – form groups
4. `HAVING` – group filter
5. `SELECT` – choose output columns
6. `ORDER BY` – sort

Example:
```sql
SELECT store_id, COUNT(*) as num_orders, SUM(total) as revenue
FROM orders
WHERE order_date >= '2026-01-01'
GROUP BY store_id
HAVING revenue > 10000
ORDER BY revenue DESC;
```

## 🧱 BRICK 2 – Common Pitfalls
- Using a column in `SELECT` that is neither an aggregate
  nor in `GROUP BY`.
- Forgetting that `WHERE` cannot filter on aggregates.
- Putting a column in `HAVING` without it being an aggregate
  or a group column (though SQLite allows it, the result
  may be ambiguous).

**Best practice:** Always include only aggregates and
group columns in `SELECT` when using `GROUP BY`.

## 💡 Real‑world Usage
- Monthly reports: sales by month, filtered for months
  exceeding a target.
- Top‑performing stores with high average order values.

## 📌 Key Takeaway
Combine `WHERE`, `GROUP BY`, and `HAVING` to answer
sophisticated business questions.
Follow the logical pipeline to avoid errors.

*Precision filtering on both raw data and aggregates
is the hallmark of a skilled SQL engineer.*