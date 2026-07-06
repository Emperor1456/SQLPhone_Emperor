# 📘 SQLPhone Emperor · SQL Module 06
# 📖 L‑54 – FOREIGN KEY – Referential Integrity

## 🎯 OBJECTIVE
Enforce relationships between tables using foreign keys
and understand referential actions.

## 🧱 BRICK 1 – Defining Foreign Keys
A foreign key links a child table column to a parent
table’s primary key.

```sql
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);
```
With `PRAGMA foreign_keys = ON`, inserting a non‑existent
customer ID will fail.

## 🧱 BRICK 2 – Referential Actions
Define what happens when the parent row is updated/deleted:
- `ON DELETE CASCADE` – delete child rows.
- `ON DELETE SET NULL` – set foreign key to NULL.
- `ON DELETE RESTRICT` – block deletion if children exist.
- `ON UPDATE CASCADE` – propagate key changes.

```sql
FOREIGN KEY (customer_id) REFERENCES customers(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
```

## 💡 Real‑world Usage
- Orders must belong to a valid customer.
- Deleting a user cascades to their posts.
- Updating a product code updates all references.

## 📌 Key Takeaway
Foreign keys maintain relational glue.
Choose referential actions that match business rules.
Always enable `PRAGMA foreign_keys = ON`.

*Relationships without enforcement are just suggestions.*