# 📘 SQLPhone Emperor · SQL Module 06
# 📖 L‑50 – ALTER TABLE

## 🎯 OBJECTIVE
Modify a table’s structure after creation using
`ALTER TABLE`.

## 🧱 BRICK 1 – Adding and Dropping Columns
SQLite’s `ALTER TABLE` is limited compared to other DBMS.
- **Add a column:** 
  ```sql
  ALTER TABLE employees ADD COLUMN phone TEXT;
  ```
- **Drop a column:** (SQLite 3.35.0+)
  ```sql
  ALTER TABLE employees DROP COLUMN phone;
  ```
- **Rename a column:** (SQLite 3.25.0+)
  ```sql
  ALTER TABLE employees RENAME COLUMN phone TO contact;
  ```

## 🧱 BRICK 2 – Renaming Tables and Other Operations
- **Rename a table:**
  ```sql
  ALTER TABLE employees RENAME TO staff;
  ```

**Not directly supported:** changing a column’s data type,
removing constraints, or reordering columns. The workaround
is to create a new table, copy data, drop the old one, and
rename.

**Best practice:** Plan your schema upfront. `ALTER TABLE`
is for emergency changes, not routine design.

## 💡 Real‑world Usage
- Add an `updated_at` timestamp column.
- Rename a column for clarity.
- Drop a deprecated column safely.

## 📌 Key Takeaway
`ALTER TABLE` changes structure, not data.
SQLite’s version is lightweight but sufficient.
Know its limitations to avoid frustration.

*The schema can evolve, but with constraints.*