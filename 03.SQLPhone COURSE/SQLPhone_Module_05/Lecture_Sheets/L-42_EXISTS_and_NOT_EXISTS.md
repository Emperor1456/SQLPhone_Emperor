# 📘 SQLPhone Emperor · SQL Module 05
# 📖 L‑42 – EXISTS and NOT EXISTS

## 🎯 OBJECTIVE
Test for the existence (or absence) of related rows
using `EXISTS` and `NOT EXISTS`.

## 🧱 BRICK 1 – EXISTS
`EXISTS` returns true if the subquery returns at least
one row. The subquery is usually correlated.

```sql
SELECT c.name
FROM customers c
WHERE EXISTS (
    SELECT 1 FROM orders o
    WHERE o.customer_id = c.customer_id
);
```
For each customer, check if an order exists.
The subquery column (`1`) is arbitrary – we only
care about existence.

## 🧱 BRICK 2 – NOT EXISTS
`NOT EXISTS` finds rows where the subquery returns
nothing. It is safer than `NOT IN` because it handles
NULLs correctly.

```sql
SELECT c.name
FROM customers c
WHERE NOT EXISTS (
    SELECT 1 FROM orders o
    WHERE o.customer_id = c.customer_id
);
```
Customers without orders.

## 💡 Real‑world Usage
- Anti‑join patterns (find records without a match).
- Conditional logic in `WHERE` clauses.
- Data integrity checks (e.g., orphan detection).

## 📌 Key Takeaway
`EXISTS` checks for presence, `NOT EXISTS` for absence.
They are often more efficient and NULL‑safe
than `IN` / `NOT IN` for large datasets.

*Existence is the ultimate binary.*