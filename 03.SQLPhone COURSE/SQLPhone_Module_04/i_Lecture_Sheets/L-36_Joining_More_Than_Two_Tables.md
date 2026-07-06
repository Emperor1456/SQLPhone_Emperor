# 📘 SQLPhone Emperor · SQL Module 04
# 📖 L‑36 – Joining More Than Two Tables

## 🎯 OBJECTIVE
Chain multiple joins together to retrieve data spread
across three or more tables.

## 🧱 BRICK 1 – Multi‑Join Syntax
You can join additional tables by adding more `JOIN` clauses:
```sql
SELECT c.name, o.order_date, p.product_name
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id;
```
Each join adds a new table and a condition.

## 🧱 BRICK 2 – Execution Order and Readability
The database determines the join order internally.
For readability, join in logical sequence: start with the
main entity, then follow relationships.

Use indentation and consistent formatting to keep it readable.
Aliases are even more important here.

## 💡 Real‑world Usage
- Order history with customer, product, and shipment details.
- Employee project assignments with department and manager info.
- Many‑to‑many relationship traversal.

## 📌 Key Takeaway
Joining multiple tables is just chaining `JOIN`s.
Follow the relationships from one table to the next.
Keep it readable with aliases and clean formatting.

*The data web is navigated one join at a time.*