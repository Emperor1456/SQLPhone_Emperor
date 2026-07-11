# 📘 SQLPhone Emperor v3.0 · Module 1
# 📖 L03 – CREATE TABLE – Columns, Data Types & Constraints

---

## 🎯 OBJECTIVE — What You Will Master

> After this lesson, you’ll design database tables that reject bad data at the gate.

- 🏗️ **CREATE TABLE** – define the blueprint of a relation
- 🧱 **Columns & data types** – `INTEGER`, `TEXT`, `REAL`, `BLOB`, `NULL`
- 🔒 **Constraints** – `NOT NULL`, `UNIQUE`, `CHECK`, `DEFAULT`, `PRIMARY KEY`
- 🧪 **SQLite’s flexible typing** – when to use `STRICT` tables

---

## 🧱 THE ANATOMY OF A TABLE

A table is defined by its columns — each with a name, a storage class, and
optional constraints that protect the integrity of your data.

The simplest `CREATE TABLE` statement for the Imperial Army’s personnel file:

```sql
CREATE TABLE soldiers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    rank TEXT,
    salary REAL CHECK(salary > 0),
    joined TEXT DEFAULT (date('now'))
);
```

Let’s break it down:

- `id INTEGER PRIMARY KEY` – unique identifier, auto‑assigns if you insert `NULL`.
- `name TEXT NOT NULL` – every soldier must have a name.
- `rank TEXT` – can be NULL (rank unknown).
- `salary REAL CHECK(salary > 0)` – salary must be positive.
- `joined TEXT DEFAULT (date('now'))` – if no date supplied, today’s date is used.

---

## 🧱 DATA TYPES IN SQLITE

SQLite has five storage classes. Unlike other databases, the declared type
is just a **suggestion** (affinity). This flexibility can be powerful, but also dangerous.

| Storage Class | Affinity from declaration | Use for |
|---------------|---------------------------|---------|
| `NULL` | (none) | Missing data |
| `INTEGER` | `INT`, `INTEGER`, `TINYINT`, `BIGINT` | Whole numbers, IDs |
| `REAL` | `REAL`, `FLOAT`, `DOUBLE` | Decimal values, currency |
| `TEXT` | `TEXT`, `CHAR`, `VARCHAR` | Names, descriptions, codes |
| `BLOB` | `BLOB` | Binary data, images |

If you need **strict** type enforcement (like PostgreSQL), use `STRICT` tables
(SQLite 3.37+):

```sql
CREATE TABLE ledger (
    id INTEGER PRIMARY KEY,
    amount REAL NOT NULL,
    description TEXT
) STRICT;
```

---

## 🧱 CONSTRAINTS – YOUR FIRST LINE OF DEFENCE

Constraints prevent bad data from entering your database. Apply them at the
table level, and every insert/update is automatically validated.

| Constraint | Purpose |
|------------|---------|
| `PRIMARY KEY` | Uniquely identifies each row |
| `NOT NULL` | Rejects NULL values |
| `UNIQUE` | Prevents duplicate values in a column |
| `CHECK(condition)` | Enforces a logical rule (e.g., `salary > 0`) |
| `DEFAULT value` | Supplies a value when none is provided |

**Example – Product Catalog:**
```sql
CREATE TABLE products (
    sku TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL CHECK(price > 0),
    quantity INTEGER DEFAULT 0
);
```

> ⚠️ **WARNING:** Without constraints, your application code must enforce
> every rule. That’s fragile — a single bug can corrupt your data.
> Constraints are your silent guardians.

> 💡 **INSIGHT:** Use `INTEGER PRIMARY KEY` for auto‑incrementing IDs.
> It’s faster and simpler than `AUTOINCREMENT` in most cases.

---

## 💡 Real‑world Usage

**Banking – account table**
```sql
CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,
    holder TEXT NOT NULL,
    balance REAL CHECK(balance >= 0),
    opened TEXT DEFAULT (date('now'))
);
```

**E‑commerce – order items**
```sql
CREATE TABLE order_items (
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER CHECK(quantity > 0),
    PRIMARY KEY (order_id, product_id)
);
```

**Logistics – shipment tracking**
```sql
CREATE TABLE shipments (
    tracking_id TEXT PRIMARY KEY,
    destination TEXT NOT NULL,
    weight_kg REAL CHECK(weight_kg > 0),
    status TEXT DEFAULT 'pending'
);
```

---

## 🔍 Practice Preview
You will design and create tables with full constraints for the Imperial Empire.

| Level | Task |
|-------|------|
| Easy | Create a `soldiers` table with `id` (PRIMARY KEY) and `name` (NOT NULL). |
| Medium | Add `rank`, `salary` (CHECK > 0), and `joined` (DEFAULT today) columns. |
| Hard | Create a `products` table with `sku` PRIMARY KEY, `name` NOT NULL, `price` CHECK > 0, `quantity` DEFAULT 0. |

Run the coach:
```bash
python ii_Practice_Sheets/L03_CREATE_TABLE_Columns_Data_Types_Constraints.py
```

---

## 📌 Key Takeaway
- `CREATE TABLE` defines columns, types, and constraints.
- Constraints (`NOT NULL`, `UNIQUE`, `CHECK`, `DEFAULT`, `PRIMARY KEY`) enforce data integrity.
- SQLite’s flexible typing can be locked down with `STRICT` tables.
- The database itself should reject bad data — never rely solely on application code.

*For Emperor.*