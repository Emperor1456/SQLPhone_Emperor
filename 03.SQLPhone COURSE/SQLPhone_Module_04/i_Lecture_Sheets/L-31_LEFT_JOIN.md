# 📘 SQLPhone Emperor · SQL Module 04
# 📖 L‑31 – LEFT JOIN

## 🎯 OBJECTIVE
Return all rows from the left table, plus matching
rows from the right table; if no match, NULLs appear.

## 🧱 BRICK 1 – LEFT JOIN Behaviour
`LEFT JOIN` keeps every row from the **left** table (the one before `LEFT JOIN`),
regardless of whether a match exists in the right table.

```sql
SELECT c.name, o.order_id
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;
```
If a customer has no orders, `order_id` will be NULL.

## 🧱 BRICK 2 – Handling NULLs from Missing Matches
You can filter for customers **without** orders:
```sql
SELECT c.name
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;
```

This pattern is useful for finding unmatched records.

## 💡 Real‑world Usage
- Show all products, even those never sold.
- List all users, including those without a profile picture.
- Audit orphan records.

## 📌 Key Takeaway
`LEFT JOIN` preserves the left table’s rows.
Missing matches become NULLs.
Use `IS NULL` to find unmatched rows.

*The left table always survives.*