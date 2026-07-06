# 📘 SQLPhone Emperor · SQL Module 06
# 📖 L‑48 – DELETE – Removing Rows

## 🎯 OBJECTIVE
Remove rows from a table using `DELETE`, with a
strong emphasis on safe filtering.

## 🧱 BRICK 1 – DELETE Syntax
`DELETE` removes rows matching a condition.
```sql
DELETE FROM table_name
WHERE condition;
```

Without `WHERE`, it deletes **every row**.
The table structure remains, but all data is gone.

Example:
```sql
DELETE FROM customers
WHERE last_order_date < '2020-01-01';
```

## 🧱 BRICK 2 – DELETE with JOINs and Subqueries
SQLite does not support `DELETE ... JOIN` directly,
but you can use a subquery:
```sql
DELETE FROM orders
WHERE customer_id IN (
    SELECT id FROM customers WHERE status = 'inactive'
);
```

**Performance:** For large tables, consider `TRUNCATE`
(not available in SQLite) or drop and recreate if you
need to clear all rows quickly. `DELETE` is slower
because it logs each row.

## 💡 Real‑world Usage
- Purge old logs.
- Remove duplicate test data.
- Clean up before a migration.

## 📌 Key Takeaway
`DELETE` is permanent and row‑by‑row.
Always use `WHERE` to target specific rows.
Test with a corresponding `SELECT` first.

*Deletion without a filter is destruction.*