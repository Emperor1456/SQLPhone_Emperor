# 📘 SQLPhone Emperor v3.0 · Module 6
# 📖 L55 – Primary Keys & Composite Keys

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll design the unique identifier system that every table depends on — single and multi‑column primary keys. You’ll also understand the critical difference between natural and surrogate keys.

- 🧱 **Primary key** – uniquely identifies each row
- 🧠 **Composite key** – a primary key made of two or more columns
- 🧪 **Natural vs surrogate keys** – when to use what
- ⚡ **`INTEGER PRIMARY KEY` in SQLite** – the special auto‑increment alias
- 🛡️ **Best practices** – every table must have a primary key

---

## 🧱 SINGLE‑COLUMN PRIMARY KEY

A primary key guarantees uniqueness and provides the fastest way to look up a row. In SQLite, `INTEGER PRIMARY KEY` is special — it maps directly to the internal `rowid`, enabling auto‑increment behaviour without the `AUTOINCREMENT` keyword.

```sql
CREATE TABLE soldiers (
    soldier_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
```

Insert `NULL` and SQLite assigns the next integer automatically:

```sql
INSERT INTO soldiers (soldier_id, name) VALUES (NULL, 'Emperor');
-- soldier_id is auto‑assigned (e.g., 1)
```

---

## 🧱 COMPOSITE PRIMARY KEY

When no single column uniquely identifies a row, combine two or more columns into a composite key. This is common in join tables (many‑to‑many relationships).

```sql
CREATE TABLE regiment_assignments (
    soldier_id INTEGER,
    regiment_id INTEGER,
    assigned_date TEXT,
    PRIMARY KEY (soldier_id, regiment_id),
    FOREIGN KEY (soldier_id) REFERENCES soldiers(soldier_id),
    FOREIGN KEY (regiment_id) REFERENCES regiments(regiment_id)
);
```

A soldier can be assigned to the same regiment only once, because the combination `(soldier_id, regiment_id)` is unique.

---

## 🧱 NATURAL VS SURROGATE KEYS

| Type | Example | When to use |
|------|---------|-------------|
| **Surrogate** | `INTEGER PRIMARY KEY` (auto‑generated) | Most cases — stable, simple, never changes |
| **Natural** | `email` or `passport_number` | When a real‑world identifier already exists and is guaranteed unique and immutable |

```sql
-- Surrogate key (recommended for most tables)
CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    email TEXT UNIQUE NOT NULL
);

-- Natural key (use only if the value is guaranteed to never change)
CREATE TABLE countries (
    country_code TEXT PRIMARY KEY,  -- 'BD', 'US', etc.
    country_name TEXT NOT NULL
);
```

> 💡 **INSIGHT:** Prefer surrogate keys for most tables — they never change, even if the business data does. Use natural keys only when you need to enforce uniqueness at the business level on an immutable value.

> ⚠️ **WARNING:** If you use a natural key and the value changes (e.g., a user changes their email), you must cascade that change to every table that references it. Surrogate keys avoid this entirely.

---

## 🧱 INTEGER PRIMARY KEY VS AUTOINCREMENT

| Feature | `INTEGER PRIMARY KEY` | `AUTOINCREMENT` |
|---------|-----------------------|-----------------|
| ID uniqueness | Yes | Yes |
| ID reuse after delete | Possible (if max row deleted) | Never |
| Performance | Faster | Slightly slower |
| Use case | Most applications | When ID reuse is unacceptable (audit trails) |

For most of your projects, `INTEGER PRIMARY KEY` is sufficient and preferred.

---

## 💡 Real‑world Usage

**Banking – account numbers as natural primary key**
```sql
CREATE TABLE accounts (account_number TEXT PRIMARY KEY, customer_id INTEGER NOT NULL);
```

**E‑commerce – order items with composite key**
```sql
CREATE TABLE order_items (
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    PRIMARY KEY (order_id, product_id)
);
```

**Logistics – shipment tracking as natural key**
```sql
CREATE TABLE shipments (tracking_id TEXT PRIMARY KEY, status TEXT);
```

**HR – employee‑project assignment with composite key**
```sql
CREATE TABLE project_assignments (
    emp_id INTEGER,
    project_id INTEGER,
    role TEXT,
    PRIMARY KEY (emp_id, project_id)
);
```

---

## 🔍 Practice Preview
You will design primary keys for Imperial Army tables.

| Level | Task |
|-------|------|
| Easy | Create a table with a single `INTEGER PRIMARY KEY`. |
| Medium | Create a join table with a composite primary key (two columns). |
| Hard | Choose between a surrogate and natural key for a `passports` table and justify your choice with comments. |

Run the coach:
```bash
python ii_Practice_Sheets/L55_Primary_Keys_Composite_Keys.py
```

---

## 📌 Key Takeaway
- Every table should have a primary key.
- Composite keys uniquely identify rows using multiple columns.
- `INTEGER PRIMARY KEY` in SQLite is an auto‑incrementing surrogate key.
- Prefer surrogate keys; use natural keys only for immutable, unique identifiers.

*For Emperor.*