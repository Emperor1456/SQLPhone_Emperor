# 📘 SQLPhone Emperor · SQL Module 04
# 📖 L‑30 – INNER JOIN

## 🎯 OBJECTIVE
Combine rows from two tables when a match exists
in both, using `INNER JOIN`.

## 🧱 BRICK 1 – INNER JOIN Syntax
`INNER JOIN` returns only rows that have matching values
in both tables based on the join condition.

```sql
SELECT orders.order_id, customers.name
FROM orders
INNER JOIN customers ON orders.customer_id = customers.customer_id;
```

Table aliases keep it short:
```sql
SELECT o.order_id, c.name
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id;
```

## 🧱 BRICK 2 – Join Condition
The `ON` clause specifies how rows are matched.
Usually it’s a foreign key = primary key.
If no match, the row is excluded.

Inner joins can also use non‑key columns, but that’s less common.

**Result set:** only rows where both tables have the key.

## 💡 Real‑world Usage
- List orders with customer details.
- Find products with their supplier information.
- Combine user profiles with login logs.

## 📌 Key Takeaway
`INNER JOIN` is the most common join.
It returns only matched rows.
Always use meaningful aliases for readability.

*Inner joins bring related data together.*