# 📘 SQLPhone Emperor · Module 01  
# 📖 L‑05 – CREATE TABLE (The Imperial Personnel File)

---

## 🎯 OBJECTIVE  
Write robust `CREATE TABLE` statements that enforce data integrity.  
Build the Imperial HR database — an `employees` table with primary keys, `NOT NULL` fields, `UNIQUE` emails, `CHECK` constraints on salary, and `DEFAULT` timestamps.  
The database itself will reject bad data before your application ever sees it.

---

## 🧱 BRICK 1 – Table Structure & Core Constraints

`CREATE TABLE` defines the blueprint for a relation.  
Every column receives a name, a type, and optional constraints.

**① The Emperor’s employee record (Easy practice)**
```sql
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    salary REAL CHECK(salary > 0),
    hired TEXT DEFAULT (datetime('now'))
);
```
- `id INTEGER PRIMARY KEY` – unique row identifier. Insert NULL and SQLite auto‑assigns the next integer.
- `name TEXT NOT NULL` – every employee must have a name.
- `email TEXT UNIQUE NOT NULL` – no duplicate emails allowed, and it must always be provided.
- `salary REAL CHECK(salary > 0)` – salary must be a positive number. The constraint blocks zero or negative values.
- `hired TEXT DEFAULT (datetime('now'))` – if no hire date is given, SQLite fills in the current date and time automatically.

**② Verify the schema**
```sql
.tables
.schema employees
```
You’ll see the exact `CREATE` statement. This is the Imperial Personnel File — a table that enforces business rules at the database level.

> 💡 **INSIGHT:** Constraints are not cosmetic. They are the first line of defence. A `CHECK` on salary prevents a payroll disaster. `UNIQUE` on email prevents duplicate identities. The database guards the empire 24/7.

---

## 🧱 BRICK 2 – Inserting Data & Letting Constraints Work

**③ Hire two employees (Medium practice)**
Insert one with all columns specified, and one that relies on the default hire date:

```sql
INSERT INTO employees (name, email, salary, hired)
VALUES ('Alice', 'a@x.com', 50000, '2026-01-01');

INSERT INTO employees (name, email, salary)
VALUES ('Bob', 'b@x.com', 60000);
```
- Alice gets the explicit date `2026-01-01`.
- Bob omits `hired`, so `DEFAULT` kicks in and stamps the current datetime.

Check the data:
```sql
SELECT * FROM employees;
```
You’ll see two rows, Bob’s `hired` column filled automatically.

**④ Attempt duplicate email (Hard practice)**
The `UNIQUE` constraint on `email` means this should fail:

```sql
INSERT INTO employees (name, email, salary)
VALUES ('Charlie', 'a@x.com', 70000);
```
SQLite responds with an error: `UNIQUE constraint failed: employees.email`.  
Charlie is not added. The empire’s identity system remains unbroken.

After the failed insert, verify that the table still has exactly two rows:
```sql
SELECT * FROM employees;
```

**⑤ Explicitly test the salary CHECK**
```sql
INSERT INTO employees (name, email, salary)
VALUES ('Dave', 'd@x.com', -500);
```
This also fails — `CHECK constraint failed: salary > 0`. The database refuses to pay someone a negative salary.

> ⚠️ **WARNING:** Constraints are enforced on every `INSERT` and `UPDATE`. You cannot bypass them without altering the table. This is the power of database‑level rules: they cannot be forgotten or skipped by buggy application code.

> 💡 **ADVANCED TIP – Composite primary keys:**  
> For tables that don’t need a separate ID, you can combine multiple columns into a primary key:
> ```sql
> CREATE TABLE assignment (
>     employee_id INTEGER,
>     project_id INTEGER,
>     role TEXT,
>     PRIMARY KEY (employee_id, project_id)
> );
> ```
> This ensures no employee is assigned to the same project twice.

---

## 💡 Real‑world Usage

**Banking – accounts with positive balance**
```sql
CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,
    owner TEXT NOT NULL,
    balance REAL CHECK(balance >= 0)
);
```

**E‑commerce – unique product SKUs**
```sql
CREATE TABLE products (
    sku TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL CHECK(price > 0)
);
```

**Logistics – shipment with default status**
```sql
CREATE TABLE shipments (
    tracking_id TEXT PRIMARY KEY,
    destination TEXT NOT NULL,
    status TEXT DEFAULT 'pending'
);
```

**HR – employee ID card**
```sql
CREATE TABLE badges (
    badge_id INTEGER PRIMARY KEY,
    employee_id INTEGER UNIQUE NOT NULL,
    issued TEXT DEFAULT (datetime('now'))
);
```

---

## 🔍 Practice Preview
You will build the Imperial Personnel File — a fully constrained employee table.

| Level  | Task | What You’ll Write |
|--------|------|-------------------|
| Easy   | Create table `employees` (id INT PK, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, salary REAL CHECK(salary>0), hired TEXT DEFAULT (datetime('now'))). | `CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, salary REAL CHECK(salary>0), hired TEXT DEFAULT (datetime('now')));` |
| Medium | Insert two rows: one with all columns, one omitting `hired` (let default work). | Two `INSERT INTO employees …` statements |
| Hard   | Attempt inserting a duplicate email (should be rejected). Then show all current rows with `SELECT *`. | `INSERT INTO employees …` (will fail) then `SELECT * FROM employees;` |

Run the coach:
```bash
python ii_Practice_Sheets/L-05_CREATE_TABLE.py
```

---

## 📌 Key Takeaway
- `CREATE TABLE` defines columns, types, and constraints.
- `PRIMARY KEY`, `NOT NULL`, `UNIQUE`, `CHECK`, and `DEFAULT` enforce data integrity.
- Constraints work at the database level — they cannot be circumvented by application code.
- The Imperial Personnel File is now a fortress. Bad data dies at the gate.