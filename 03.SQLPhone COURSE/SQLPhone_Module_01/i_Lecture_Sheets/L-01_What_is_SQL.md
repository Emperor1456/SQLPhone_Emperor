# 📘 SQLPhone Emperor · Module 01  
# 📖 L‑01 – What is SQL? (Building the Imperial Database)

---

## 🎯 OBJECTIVE  
Understand what SQL is and why relational databases rule the data world.  
You’ll write your first SQL statements — `CREATE TABLE`, `INSERT`, and `SELECT` — to build the Emperor’s army database.  
No theory without practice. By the end, you’ll have a working `empire` table with soldiers.

---

## 🧱 BRICK 1 – SQL: Your First Command Center

SQL (Structured Query Language) is how you talk to databases.  
You write statements; the database executes them.  
Behind every app — banking, logistics, Companion — there’s a `SELECT` fetching data and an `INSERT` saving it.

**① Create a table for the Emperor’s soldiers**  
The army needs a database. Start with a table named `empire` that stores each soldier’s ID and name.

```sql
CREATE TABLE empire (
    id INTEGER,
    name TEXT
);
```
- `CREATE TABLE empire (...)` – creates a new table called `empire`.
- `id INTEGER` – a column for the soldier’s unique number.
- `name TEXT` – a column for the soldier’s name.
- Semicolons (`;`) end every SQL statement. Forgetting them causes errors.

> 💡 **INSIGHT:** SQLite is a single file database — your whole empire lives in one `.db` file. Perfect for Companion’s local memory.

**② Insert Emperor himself into the table**  
The army begins with its commander.

```sql
INSERT INTO empire VALUES (1, 'Emperor');
```
- `INSERT INTO empire VALUES (...)` adds one row.
- The values are in the same order as the columns: `id` first, then `name`.
- Text values must be enclosed in single quotes (`'Emperor'`).

**③ See what’s inside**  
After inserting, check your work.

```sql
SELECT * FROM empire;
```
- `SELECT *` means “give me all columns”.
- `FROM empire` means “from the empire table”.
- You’ll see a table with the row you just inserted.

These three statements are the Easy practice task.  
You’ll type them exactly, and the practice engine will verify your table.

> ⚠️ **WARNING:** SQL is case‑insensitive for keywords (`SELECT`, `from`, `CrEaTe` all work), but table and column names are case‑sensitive depending on the operating system. Stick to lowercase for safety.

---

## 🧱 BRICK 2 – Evolving the Schema

An empire grows. You need to track ranks.

**④ Add a rank column**  
You can modify an existing table with `ALTER TABLE`.

```sql
ALTER TABLE empire ADD COLUMN rank TEXT;
```
- `ALTER TABLE empire` – modifies the empire table.
- `ADD COLUMN rank TEXT` – adds a new column called `rank` that stores text.
- Now every soldier can have a rank (e.g., General, Private).

**⑤ Promote Emperor to General**  
You don’t need to re‑insert rows; change existing ones with `UPDATE`.

```sql
UPDATE empire SET rank = 'General' WHERE id = 1;
```
- `UPDATE empire` – modify the empire table.
- `SET rank = 'General'` – change the rank column.
- `WHERE id = 1` – only affect the row with id = 1 (Emperor).
- Without `WHERE`, you’d change *every* row — dangerous in a real army.

**⑥ Recruit a second soldier**  
The army expands.

```sql
INSERT INTO empire (id, name, rank) VALUES (2, 'Soldier', 'Private');
```
- This time we specify the column list `(id, name, rank)` before `VALUES`.  
  It’s safer — if the table’s column order changes, your insert still works.

**⑦ View all troops, sorted by rank**  
A general must see the chain of command.

```sql
SELECT * FROM empire ORDER BY rank;
```
- `ORDER BY rank` sorts the rows alphabetically by rank.  
- `ORDER BY rank DESC` would sort highest to lowest.

**⑧ Make Emperor the Supreme Commander**  
He deserves a promotion.

```sql
UPDATE empire SET rank = 'Supreme Commander' WHERE id = 1;
```

Then run the sorted view again — Emperor should now appear at the top.

These statements form the Medium and Hard practice tasks.

> 💡 **ADVANCED TIP – SQLite is serverless:**  
> Unlike MySQL or PostgreSQL, SQLite doesn’t require a running server. Your entire database is a single `.db` file. This makes it perfect for embedding into Companion, your AI that never forgets.

> ⚠️ **WARNING:** `UPDATE` without `WHERE` updates *every row*. Always double‑check your `WHERE` clause before executing — this is the SQL equivalent of “rm -rf /”.

---

## 💡 Real‑world Usage

SQL powers every data‑driven system. Here are concrete examples you’ll write in this course:

**Banking – create an accounts table**
```sql
CREATE TABLE accounts (
    account_id INTEGER,
    holder TEXT,
    balance REAL
);
INSERT INTO accounts VALUES (101, 'Emperor', 5000.00);
SELECT * FROM accounts;
```

**E‑commerce – product catalog**
```sql
CREATE TABLE products (
    sku TEXT,
    name TEXT,
    price REAL
);
INSERT INTO products VALUES ('SKU-001', 'Wireless Mouse', 24.99);
SELECT name, price FROM products;
```

**Logistics – tracking shipments**
```sql
CREATE TABLE shipments (
    tracking_id TEXT,
    destination TEXT,
    weight_kg REAL
);
INSERT INTO shipments VALUES ('TRK-123', 'Dhaka', 12.5);
SELECT * FROM shipments;
```

**HR – employee directory**
```sql
CREATE TABLE employees (
    emp_id INTEGER,
    name TEXT,
    department TEXT
);
INSERT INTO employees VALUES (1, 'Emperor', 'Engineering');
SELECT * FROM employees WHERE department = 'Engineering';
```

*Every time you open an app, SQL is running behind the screen.*

---

## 🔍 Practice Preview
You will build the Emperor’s army database step by step.

| Level  | Task | What You’ll Write |
|--------|------|-------------------|
| Easy   | Create `empire` table with `id` and `name`, insert Emperor, and select all rows. | `CREATE TABLE`, `INSERT`, `SELECT *` |
| Medium | Add a `rank` column, set Emperor’s rank to `'General'`, and select all rows. | `ALTER TABLE`, `UPDATE`, `SELECT` |
| Hard   | Insert a second soldier with a different rank, promote Emperor to `'Supreme Commander'`, and show all rows sorted by rank. | `INSERT`, `UPDATE`, `SELECT ... ORDER BY` |

Run the practice coach:
```bash
python ii_Practice_Sheets/L-01_What_is_SQL.py
```
Choose `1` (Easy), `2` (Medium), or `3` (Hard).  
Type each SQL statement; the engine checks your database.  
Use `:hint` if you get stuck — no shame, only progress.

---

## 📌 Key Takeaway
- SQL is the universal language of data — you declare what you want, the database figures out how.
- `CREATE TABLE` defines structure; `INSERT` adds rows; `SELECT` reads data.
- `ALTER TABLE` evolves the schema; `UPDATE` modifies existing rows.
- SQLite is a single‑file, serverless database — ideal for phone‑first development and Companion’s eternal memory.
- Every empire starts with a single query. Today, you ran your first.