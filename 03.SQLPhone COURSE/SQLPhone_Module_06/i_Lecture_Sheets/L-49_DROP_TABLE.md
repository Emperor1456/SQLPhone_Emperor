# 📘 SQLPhone Emperor · SQL Module 06
# 📖 L‑49 – DROP TABLE

## 🎯 OBJECTIVE
Completely remove a table and all its data from
the database using `DROP TABLE`.

## 🧱 BRICK 1 – DROP TABLE Syntax
```sql
DROP TABLE [IF EXISTS] table_name;
```

`IF EXISTS` prevents an error if the table doesn’t
exist – essential for repeatable scripts.

Example:
```sql
DROP TABLE IF EXISTS temp_logs;
```
This removes the table definition and every row.
All associated indexes and triggers are also dropped.

## 🧱 BRICK 2 – Safe Dropping with Foreign Keys
If foreign key constraints are enabled, you cannot
drop a table that is referenced by another table’s
foreign key unless you use `CASCADE` or drop the
dependent table first.

Order matters: drop child tables before parent tables.

```sql
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;
```

**Warning:** `DROP` is irreversible – there is no
“undo” unless you have a backup.

## 💡 Real‑world Usage
- Reset a test database.
- Remove deprecated tables during schema refactoring.
- Clean up failed migrations.

## 📌 Key Takeaway
`DROP TABLE` obliterates everything.
Use `IF EXISTS` for safe scripting.
Respect foreign key dependencies when dropping.

*Sometimes you must erase to rebuild.*