# 📘 SQLPhone Emperor · SQL Module 08
# 📖 L‑68 – Updatable Views

## 🎯 OBJECTIVE
Understand when a view allows `INSERT`, `UPDATE`, or `DELETE`.

## 🧱 BRICK 1 – Conditions for Updatability
In SQLite, a view is updatable only if:
- It references exactly one table (no joins).
- It does not use `DISTINCT`, `GROUP BY`, `HAVING`, `UNION`.
- All columns map directly to the underlying table columns.
- The view includes all `NOT NULL` columns without defaults.

## 🧱 BRICK 2 – Practical Implications
Example of an updatable view:
```sql
CREATE VIEW active_users AS
SELECT id, name, status
FROM users
WHERE status = 'active';
```
You can `UPDATE active_users SET status = 'inactive' WHERE id = 1;` and the base table is updated.

**Non‑updatable views** are very common; they are just read‑only.
For complex data modifications, write directly to the base tables.

## 💡 Real‑world Usage
- Provide a safe subset of columns for API endpoints.
- Simplify updates on filtered rows.

## 📌 Key Takeaway
Not all views are updatable.
Keep them simple if you need write operations.
Otherwise, treat them as read‑only abstractions.

*A view you can write to is rare – use it wisely.*