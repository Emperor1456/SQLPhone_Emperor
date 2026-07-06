# 📘 SQLPhone Emperor · SQL Module 06
# 📖 L‑52 – DEFAULT Values

## 🎯 OBJECTIVE
Automatically populate columns with default values
when no explicit value is given during `INSERT`.

## 🧱 BRICK 1 – Specifying DEFAULT
You can define a default at column creation:
```sql
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    created_at TEXT DEFAULT (datetime('now')),
    status TEXT DEFAULT 'pending',
    is_active INTEGER DEFAULT 1
);
```

When inserting, omit the column to trigger the default:
```sql
INSERT INTO orders DEFAULT VALUES;
```
Inserts a row with all defaults.

## 🧱 BRICK 2 – Overriding and Removing Defaults
You can still override the default by providing a value:
```sql
INSERT INTO orders (status) VALUES ('shipped');
```

`DEFAULT` can be an expression (in parentheses) or a
constant. To drop a default, use `ALTER TABLE ... ALTER COLUMN`
(in other DBMS) but SQLite doesn’t support altering column
defaults after creation (must recreate table).

## 💡 Real‑world Usage
- Auto‑timestamp rows.
- Set initial user role or status.
- Provide fallback prices.

## 📌 Key Takeaway
`DEFAULT` values reduce boilerplate and prevent NULLs.
Use expressions for dynamic defaults like timestamps.
Design defaults that make sense for the business.

*If a value is usually the same, make it the default.*