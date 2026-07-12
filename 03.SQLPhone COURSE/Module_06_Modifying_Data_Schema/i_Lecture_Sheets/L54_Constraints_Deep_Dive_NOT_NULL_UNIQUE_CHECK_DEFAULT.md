# 📘 SQLPhone Emperor v3.0 · Module 6
# 📖 L54 – Constraints Deep Dive – NOT NULL, UNIQUE, CHECK, DEFAULT

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll master every constraint SQLite offers — building tables that reject bad data at the database level, so no application bug can ever corrupt your data.

- 🧱 **NOT NULL** – force a column to always have a value
- 🧠 **UNIQUE** – prevent duplicate values in a column or group of columns
- 🧪 **CHECK** – enforce custom business rules
- ⚡ **DEFAULT** – provide fallback values automatically
- 🛡️ **Multi‑column constraints** – table‑level rules

---

## 🧱 NOT NULL

A column with `NOT NULL` rejects any attempt to insert or update a row with `NULL` in that column. Use it for mandatory fields.

```sql
CREATE TABLE soldiers (
    soldier_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,          -- must have a name
    rank TEXT                    -- optional, can be NULL
);
```

---

## 🧱 UNIQUE

`UNIQUE` ensures that all values in a column (or combination of columns) are distinct. It can be applied to a single column or a group.

```sql
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    email TEXT UNIQUE,            -- no duplicate emails
    phone TEXT,
    UNIQUE(email, phone)          -- combination must be unique
);
```

`NULL` is considered distinct from every other NULL, so multiple NULLs are allowed in a UNIQUE column.

---

## 🧱 CHECK

`CHECK(condition)` validates that every row satisfies a logical expression. It’s your custom business rule enforcer.

```sql
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    price REAL CHECK(price > 0),           -- price must be positive
    quantity INTEGER CHECK(quantity >= 0),  -- stock can't be negative
    category TEXT CHECK(category IN ('Electronics', 'Furniture', 'Office'))
);
```

You can also reference multiple columns:

```sql
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    ship_date TEXT,
    delivery_date TEXT,
    CHECK(delivery_date >= ship_date)      -- can't deliver before shipping
);
```

---

## 🧱 DEFAULT

`DEFAULT` supplies a value when none is provided in the `INSERT`. The value can be a literal, an expression, or a function call.

```sql
CREATE TABLE soldiers (
    soldier_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    joined_date TEXT DEFAULT (date('now')),
    status TEXT DEFAULT 'active',
    rank TEXT DEFAULT 'Private'
);
```

---

## 🧱 TABLE‑LEVEL VS COLUMN‑LEVEL CONSTRAINTS

Constraints can be written after a column definition (column‑level) or at the end of the CREATE TABLE statement (table‑level). Multi‑column constraints must be table‑level.

```sql
CREATE TABLE enrollments (
    student_id INTEGER,
    course_id INTEGER,
    semester TEXT,
    PRIMARY KEY (student_id, course_id, semester),          -- table‑level
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
```

> 💡 **INSIGHT:** Constraints are your silent guardians. They run on every insert/update, so no application bug can bypass them. The more rules you define at the database level, the safer your data.

> ⚠️ **WARNING:** Constraints make writes slightly slower because they must be verified. But the cost is negligible compared to the cost of corrupt data.

---

## 💡 Real‑world Usage

**Banking – positive balance, unique account numbers**
```sql
CREATE TABLE accounts (
    account_number TEXT PRIMARY KEY,
    balance REAL CHECK(balance >= 0)
);
```

**E‑commerce – inventory cannot be negative**
```sql
CREATE TABLE inventory (
    product_id INTEGER PRIMARY KEY,
    quantity INTEGER DEFAULT 0 CHECK(quantity >= 0)
);
```

**Logistics – valid status values**
```sql
CREATE TABLE shipments (
    tracking_id TEXT PRIMARY KEY,
    status TEXT DEFAULT 'pending'
        CHECK(status IN ('pending', 'in transit', 'delivered', 'cancelled'))
);
```

**HR – email must be unique, hire date defaults to today**
```sql
CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    hire_date TEXT DEFAULT (date('now'))
);
```

---

## 🔍 Practice Preview
You will design tables with comprehensive constraints.

| Level | Task |
|-------|------|
| Easy | Create a table with a `NOT NULL` and a `UNIQUE` constraint. |
| Medium | Add a `CHECK` constraint that enforces valid values for a status column. |
| Hard | Create a table with a multi‑column `UNIQUE` constraint and a `CHECK` comparing two columns. |

Run the coach:
```bash
python ii_Practice_Sheets/L54_Constraints_Deep_Dive_NOT_NULL_UNIQUE_CHECK_DEFAULT.py
```

---

## 📌 Key Takeaway
- `NOT NULL` ensures a value is always provided.
- `UNIQUE` prevents duplicate entries in a column or combination.
- `CHECK` enforces custom business rules.
- `DEFAULT` fills in missing values automatically.
- Constraints protect your data at the database level — your last line of defense.

*For Emperor.*