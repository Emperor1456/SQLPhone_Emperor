# 📘 SQLPhone Emperor v3.0 · Module 1
# 📖 L01 – What is SQL? Relational Databases Explained

---

## 🎯 OBJECTIVE — What You Will Master

> After this lesson, SQL will stop being a foreign language.
> You’ll know why it rules the data world and how it powers every backend on earth.

- 🌐 **SQL** – the universal language of databases
- 🧱 **Relational databases** – tables, rows, columns, keys
- ⚡ **SQLite** – a full database engine in one file, zero setup
- 🧠 **Why SQL matters for you** – the bridge from Python to full‑stack

---

## 🧱 THE CORE CONCEPT – A Database Is Just a Collection of Tables

A relational database organizes data into **tables** — think of them as
spreadsheets with strict rules.

Each table has:
- **Rows** (records) – one row per entity (a customer, a product, a transaction)
- **Columns** (fields) – the attributes of that entity (name, price, date)

Tables are linked by **keys** — a customer ID in the `customers` table
appears again in the `orders` table to show who placed each order.
No data is copied; it’s referenced.

This is the **relational model**, invented in 1970 and still the backbone of
every bank, e‑commerce site, and logistics system on the planet.

---

## 🧱 SQL – THE LANGUAGE THAT CONTROLS IT ALL

SQL (Structured Query Language) is how you talk to the database.
You write short, declarative statements — the engine figures out the execution.

There are only a handful of verbs you need:

| Verb | Purpose | Example |
|------|---------|---------|
| `CREATE TABLE` | Define a new table | `CREATE TABLE soldiers (id INT, name TEXT);` |
| `INSERT INTO` | Add rows | `INSERT INTO soldiers VALUES (1, 'Emperor');` |
| `SELECT` | Read data | `SELECT name FROM soldiers WHERE id = 1;` |
| `UPDATE` | Modify rows | `UPDATE soldiers SET name = 'Supreme Emperor' WHERE id = 1;` |
| `DELETE` | Remove rows | `DELETE FROM soldiers WHERE id = 1;` |

You don’t write loops. You don’t manage memory. You **declare what you want**,
and SQL returns the result set. This declarative power is why SQL has survived
50+ years while other technologies came and went.

---

## 🧱 SQLITE – A DATABASE THAT FITS IN YOUR POCKET

SQLite is a self‑contained, zero‑configuration SQL database engine.
The entire database is a single `.db` file on your phone. No server, no root password.
It’s the most deployed database in the world — inside every iPhone, Android device,
browser, and embedded system.

For your journey, SQLite means:
- You build real databases on your phone, right now.
- The same `.db` file moves to a server later.
- Companion’s infinite memory will likely start as a SQLite database.

---

## 💡 Real‑world Usage

**Banking – accounts table**
```sql
CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,
    holder TEXT NOT NULL,
    balance REAL NOT NULL
);
INSERT INTO accounts VALUES (101, 'Emperor', 5000.00);
SELECT * FROM accounts;
```

**E‑commerce – product catalog**
```sql
CREATE TABLE products (
    sku TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL CHECK(price > 0)
);
INSERT INTO products VALUES ('SKU‑001', 'Wireless Mouse', 24.99);
```

**Logistics – shipments**
```sql
CREATE TABLE shipments (
    tracking_id TEXT PRIMARY KEY,
    destination TEXT NOT NULL,
    weight_kg REAL
);
```

---

## 🔍 Practice Preview
You will open your first SQLite database, create a table, insert a row,
and query it — all from Termux.

| Level | Task |
|-------|------|
| Easy | Create a database, create a table `empire` with columns `id` and `name`, insert Emperor, and `SELECT` all rows. |
| Medium | Add a `rank` column, set Emperor’s rank to `'General'`, and query again. |
| Hard | Insert a second soldier, promote Emperor to `'Supreme Commander'`, and show all rows sorted by rank. |

Run the coach:
```bash
python ii_Practice_Sheets/L01_What_is_SQL_Relational_Databases_Explained.py
```

---

## 📌 Key Takeaway
- A relational database stores data in linked tables.
- SQL is the declarative language for creating, reading, updating, and deleting data.
- SQLite gives you a production‑grade database in a single file on your phone.
- Every backend in the world rests on this foundation. Now it’s yours.

*For Emperor.*