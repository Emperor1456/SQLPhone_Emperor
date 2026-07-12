# 📘 SQLPhone Emperor v3.0 · Module 4
# 📖 L31 – Foreign Keys & Referential Integrity

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll link tables together with foreign keys and protect your data relationships forever — the foundation of every multi‑table database on Earth.

- 🔗 **Foreign keys** – how one table references another
- 🛡️ **Referential integrity** – preventing orphan rows
- 🧠 **ON DELETE / ON UPDATE** – cascading actions
- 🧪 **Enabling foreign keys in SQLite** – `PRAGMA foreign_keys = ON`
- ⚡ **Real‑world** – accounts → customers, orders → products

---

## 🧱 WHAT IS A FOREIGN KEY?

A foreign key is a column that points to the primary key of another table. It creates a relationship between two tables, ensuring that data stays consistent across them.

```sql
CREATE TABLE regiments (
    regiment_id INTEGER PRIMARY KEY,
    regiment_name TEXT NOT NULL
);

CREATE TABLE soldiers (
    soldier_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    regiment_id INTEGER,
    FOREIGN KEY (regiment_id) REFERENCES regiments(regiment_id)
);
```

A soldier’s `regiment_id` must exist in the `regiments` table. If you try to insert a soldier with a non‑existent regiment, SQLite rejects it.

---

## 🧱 ENABLING FOREIGN KEYS IN SQLITE

SQLite does **not** enforce foreign keys by default. You must turn them on every session:

```sql
PRAGMA foreign_keys = ON;
```

Without this, foreign key constraints are parsed but ignored. Always enable it before executing DDL.

---

## 🧱 CASCADING ACTIONS

Define what happens when a referenced row is deleted or updated:

| Action | Behavior |
|--------|----------|
| `ON DELETE CASCADE` | Delete child rows automatically |
| `ON DELETE SET NULL` | Set foreign key to NULL |
| `ON DELETE RESTRICT` | Prevent deletion if children exist |
| `ON DELETE SET DEFAULT` | Set to default value |

```sql
CREATE TABLE soldiers (
    soldier_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    regiment_id INTEGER,
    FOREIGN KEY (regiment_id) REFERENCES regiments(regiment_id)
        ON DELETE SET NULL
);
```

Now if a regiment is disbanded, its soldiers are not deleted — their `regiment_id` becomes NULL.

> ⚠️ **WARNING:** `CASCADE` can delete large amounts of data silently. Use it only when you’re sure child rows have no meaning without the parent.

> 💡 **INSIGHT:** Foreign keys are your database’s immune system. They prevent orphan records and ensure relationships always point to valid data.

---

## 💡 Real‑world Usage

**Banking – accounts linked to customers**
```sql
CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE
);
```

**E‑commerce – orders referencing products**
```sql
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE RESTRICT
);
```

**Logistics – shipments referencing warehouses**
```sql
CREATE TABLE shipments (
    tracking_id TEXT PRIMARY KEY,
    warehouse_id INTEGER,
    FOREIGN KEY (warehouse_id) REFERENCES warehouses(id) ON DELETE SET NULL
);
```

**HR – employees referencing departments**
```sql
CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    dept_id INTEGER,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);
```

---

## 🔍 Practice Preview
You will design related tables and enforce referential integrity.

| Level | Task |
|-------|------|
| Easy | Create a `regiments` table and a `soldiers` table with a foreign key, enabling `PRAGMA foreign_keys`. |
| Medium | Insert soldiers with a valid regiment, then attempt to insert one with an invalid regiment (observe the error). |
| Hard | Add `ON DELETE CASCADE` to the foreign key, then delete a regiment and verify soldiers are deleted. |

Run the coach:
```bash
python ii_Practice_Sheets/L31_Foreign_Keys_Referential_Integrity.py
```

---

## 📌 Key Takeaway
- Foreign keys link tables and enforce valid relationships.
- Always enable `PRAGMA foreign_keys = ON` in SQLite.
- Cascading actions control what happens when parent rows are modified.

*For Emperor.*