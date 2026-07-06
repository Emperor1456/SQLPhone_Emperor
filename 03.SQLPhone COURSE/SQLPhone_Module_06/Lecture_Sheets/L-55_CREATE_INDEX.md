# 📘 SQLPhone Emperor · SQL Module 06
# 📖 L‑55 – CREATE INDEX

## 🎯 OBJECTIVE
Speed up queries by creating indexes on frequently
searched or sorted columns.

## 🧱 BRICK 1 – Index Basics
An index is like a book’s index: it helps the database
find rows without scanning the entire table.

```sql
CREATE INDEX idx_customer_name ON customers(name);
```
This accelerates `WHERE name = '...'` and `ORDER BY name`.

Indexes are automatically created for `PRIMARY KEY` and
`UNIQUE` columns.

## 🧱 BRICK 2 – When and When Not to Index
- **Index columns used in `WHERE`, `JOIN`, `ORDER BY`, `GROUP BY`.**
- **Don’t index every column** – indexes slow down `INSERT`, `UPDATE`, `DELETE` because they must be maintained.
- **Composite indexes** are useful for multi‑column searches:
  ```sql
  CREATE INDEX idx_emp_dept_sal ON employees(department, salary);
  ```
- Use `EXPLAIN QUERY PLAN` to see if your index is being used.

## 💡 Real‑world Usage
- Customer lookup by email.
- Recent orders sorted by date.
- Filtering by status and date range.

## 📌 Key Takeaway
Indexes trade write speed for read speed.
Index strategically, not blindly.
The query planner decides whether to use an index.

*An index is a shortcut – but shortcuts have costs.*