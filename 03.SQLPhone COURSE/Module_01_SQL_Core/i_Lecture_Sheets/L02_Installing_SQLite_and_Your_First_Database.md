# 📘 SQLPhone Emperor v3.0 · Module 1
# 📖 L02 – Installing SQLite & Your First Database

---

## 🎯 OBJECTIVE — What You Will Master

> After this lesson, you’ll have SQLite running on your phone.
> You’ll create your first database, execute SQL, and inspect it like a professional.

- 📦 **Installation** – `pkg install sqlite` in Termux
- 💾 **Database creation** – a single `.db` file, zero server
- 🧰 **Dot‑commands** – `.tables`, `.schema`, `.headers`, `.mode`
- 🔍 **Inspection** – verifying your work instantly

---

## 🧱 INSTALLING SQLITE IN TERMUX

SQLite is a single binary. To install it, open Termux and run:

```bash
pkg update && pkg upgrade -y
pkg install sqlite -y
```

To verify:

```bash
sqlite3 --version
```

You’ll see a version number (3.35+). Now you have a full SQL engine on your phone.

---

## 🧱 YOUR FIRST DATABASE

A SQLite database is a single file. Creating one is a side effect of connecting to it:

```bash
sqlite3 empire.db
```

If `empire.db` does not exist, SQLite creates it. If it exists, SQLite opens it.
You are now inside the `sqlite>` prompt. This is where you write SQL.

Let’s create your first table:

```sql
CREATE TABLE soldiers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    rank TEXT
);
```

Insert a row:

```sql
INSERT INTO soldiers VALUES (1, 'Emperor', 'General');
```

Query it:

```sql
SELECT * FROM soldiers;
```

You’ll see:

```
1|Emperor|General
```

Exit with `.quit`.

---

## 🧱 DOT‑COMMANDS – YOUR INSPECTION TOOLKIT

Dot‑commands start with a period and work only inside the `sqlite>` shell.
They help you inspect your database without writing SQL queries.

| Command | What it does |
|---------|--------------|
| `.tables` | Lists all tables |
| `.schema soldiers` | Shows the `CREATE` statement for that table |
| `.headers on` | Shows column names in query results |
| `.mode column` | Aligns output into readable columns |
| `.quit` | Exits the shell |
| `.help` | Lists all available dot‑commands |

**Standard inspection flow:**

```bash
sqlite3 empire.db
sqlite> .headers on
sqlite> .mode column
sqlite> .tables
sqlite> .schema soldiers
sqlite> SELECT * FROM soldiers;
sqlite> .quit
```

---

## 💡 Real‑world Usage

**Banking – create an account ledger**
```bash
sqlite3 bank.db
sqlite> CREATE TABLE accounts (id INT, balance REAL);
sqlite> INSERT INTO accounts VALUES (101, 5000.00);
sqlite> .tables
sqlite> .schema accounts
```

**E‑commerce – product catalog**
```bash
sqlite3 shop.db
sqlite> CREATE TABLE products (sku TEXT, price REAL);
sqlite> INSERT INTO products VALUES ('SKU-001', 24.99);
sqlite> .headers on
sqlite> SELECT * FROM products;
```

**Logistics – shipment tracking**
```bash
sqlite3 cargo.db
sqlite> CREATE TABLE shipments (tracking_id TEXT, status TEXT);
sqlite> INSERT INTO shipments VALUES ('TRK-123', 'in transit');
sqlite> .dump
```

---

## 🔍 Practice Preview
You will install SQLite, create a database, build a table, and insert data — all in Termux.

| Level | Task |
|-------|------|
| Easy | Install SQLite, create a database `test.db`, create a table `products` with columns `id` and `name`, insert one row, and query it. |
| Medium | Add a `price` column to `products`, update the row with a price, and query with `.headers on` and `.mode column`. |
| Hard | Insert two more products, then use `.dump` to export the entire database to SQL text. |

Run the coach:
```bash
python ii_Practice_Sheets/L02_Installing_SQLite_and_Your_First_Database.py
```

---

## 📌 Key Takeaway
- SQLite is a single binary; install it once, use it forever.
- A database is just a file; you create it by connecting.
- Dot‑commands let you inspect and verify your work instantly.
- The `sqlite>` prompt is now your database command center.

*For Emperor.*