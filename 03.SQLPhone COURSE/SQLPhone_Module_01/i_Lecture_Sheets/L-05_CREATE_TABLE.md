# 📘 SQLPhone Emperor · SQL Module 01
# 📖 L‑05 – CREATE TABLE

## 🎯 OBJECTIVE
Write robust `CREATE TABLE` statements that define schema,
constraints, and default values to enforce data integrity
at the database level.

## 🧱 BRICK 1 – Table Structure & Column Definitions
`CREATE TABLE` defines the blueprint for a relation.
Each column has a name, a type (affinity), and optional constraints.

```sql
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    signup_date TEXT DEFAULT (datetime('now'))
);
```

**Core column constraints:**
- `NOT NULL` – reject NULL inserts
- `UNIQUE` – prevent duplicate values in the column
- `DEFAULT` – provide a default value if none supplied
- `CHECK` – enforce a logical condition (`CHECK(salary > 0)`)

## 🧱 BRICK 2 – Primary Keys & Row Identity
Every table should have a primary key – a column (or combination)
that uniquely identifies each row.

In SQLite, `INTEGER PRIMARY KEY` is special: it becomes an
alias for the internal `rowid`. If you insert NULL into an
`INTEGER PRIMARY KEY`, SQLite automatically assigns a unique
integer value (auto‑increment behavior without `AUTOINCREMENT`).

Explicit composite keys:
```sql
CREATE TABLE order_items (
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER NOT NULL,
    PRIMARY KEY (order_id, product_id)
);
```

Without a primary key, SQLite creates a hidden `rowid` for internal use,
but you lose explicit row identity and performance benefits.

## 💡 Enterprise Schema Design
- Always define a primary key.
- Use `NOT NULL` on business‑critical fields.
- Use `UNIQUE` constraints for natural keys (email, username).
- Use `CHECK` constraints to enforce business rules (age >= 0).
- Use `DEFAULT` for audit columns: `created_at TEXT DEFAULT (datetime('now'))`.

## 📌 Key Takeaway
The `CREATE TABLE` statement is a contract.
Constraints enforce that contract at the database level,
preventing bad data before it enters your application.

*Your schema is your first line of defense.*