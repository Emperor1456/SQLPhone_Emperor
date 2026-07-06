# 📘 SQLPhone Emperor · SQL Module 08
# 📖 L‑67 – Views – Create, Query, Drop

## 🎯 OBJECTIVE
Save a query as a virtual table (view) and use it like
a real table.

## 🧱 BRICK 1 – Creating and Querying Views
A view stores a query definition, not data.
```sql
CREATE VIEW high_earners AS
SELECT name, salary
FROM employees
WHERE salary > 100000;
```
Now you can use it like a table:
```sql
SELECT * FROM high_earners;
```
The underlying query runs each time you access the view.

## 🧱 BRICK 2 – Managing Views
- **Drop a view:** `DROP VIEW IF EXISTS high_earners;`
- **List views:** `.tables` also lists views, or query `sqlite_master`.
- Views can be used in joins, subqueries, and even other views.

Views are read‑only unless certain conditions are met (L‑68).

## 💡 Real‑world Usage
- Simplify complex joins for end‑users.
- Restrict access to sensitive columns.
- Reusable report templates.

## 📌 Key Takeaway
A view is a saved `SELECT`.
It abstracts complexity and enhances security.
Use it to freeze business logic into a simple name.

*A view is a window into your data – shape it carefully.*