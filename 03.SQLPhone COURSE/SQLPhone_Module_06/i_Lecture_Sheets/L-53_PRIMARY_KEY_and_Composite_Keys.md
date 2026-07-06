# 📘 SQLPhone Emperor · SQL Module 06
# 📖 L‑53 – PRIMARY KEY & Composite Keys

## 🎯 OBJECTIVE
Understand the role of primary keys and how composite
keys work for many‑to‑many relationships.

## 🧱 BRICK 1 – The Power of INTEGER PRIMARY KEY
In SQLite, `INTEGER PRIMARY KEY` is an alias for the
internal `rowid`. It auto‑increments without `AUTOINCREMENT`.

A primary key uniquely identifies each row.
```sql
CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    name TEXT
);
```

## 🧱 BRICK 2 – Composite Primary Keys
When a single column isn’t enough, combine columns:
```sql
CREATE TABLE order_items (
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    PRIMARY KEY (order_id, product_id)
);
```
The combination must be unique. This is the standard
way to model many‑to‑many relationships.

Composite keys also serve as indexes for fast lookups.

## 💡 Real‑world Usage
- Junction tables (enrollments, assignments).
- Natural composite keys like `(country_code, phone_number)`.

## 📌 Key Takeaway
Primary keys are identity.
Composite keys combine columns for uniqueness.
Choose keys that reflect the real‑world identifier.

*Every row needs a fingerprint.*