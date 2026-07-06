# 📘 SQLPhone Emperor · SQL Module 04
# 📖 L‑38 – Foreign Key Enforcement in SQLite

## 🎯 OBJECTIVE
Learn how to enable and use foreign key constraints
in SQLite to protect data integrity.

## 🧱 BRICK 1 – Enabling Foreign Keys
By default, SQLite does **not** enforce foreign keys.
You must enable it per connection:
```sql
PRAGMA foreign_keys = ON;
```
This must be run every time you open a connection.

In scripts, put it at the top:
```sql
PRAGMA foreign_keys = ON;
CREATE TABLE ... ;
```

## 🧱 BRICK 2 – Referential Actions
Define what happens when a referenced row is deleted or updated:
- `ON DELETE CASCADE` – delete child rows automatically.
- `ON DELETE SET NULL` – set foreign key to NULL.
- `ON DELETE RESTRICT` – prevent deletion if children exist.

```sql
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        ON DELETE CASCADE
);
```

Test it by trying to delete a customer with orders, then
enable cascading and see the difference.

## 💡 Real‑world Usage
- Prevent orphan records in order systems.
- Cascade delete when a user account is closed.
- Set foreign key to NULL for soft deletes.

## 📌 Key Takeaway
Foreign keys are toothless without `PRAGMA foreign_keys = ON`.
Always enable it and choose appropriate referential actions.
Your database will thank you.

*Trust, but verify – and enforce.*