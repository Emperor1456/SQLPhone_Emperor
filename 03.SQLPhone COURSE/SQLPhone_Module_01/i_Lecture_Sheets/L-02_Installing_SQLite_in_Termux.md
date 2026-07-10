# 📘 SQLPhone Emperor · Module 01  
# 📖 L‑02 – Installing SQLite & Your First Table (Imperial Arsenal)

---

## 🎯 OBJECTIVE  
Install SQLite in Termux, open your first database, and create a real table.  
You’ll build the **Imperial Arsenal** — a test range where the Emperor’s engineers log prototype weapon IDs.  
By the end, you’ll have a live SQLite database and a `test` table with data.

---

## 🧱 BRICK 1 – Installation & First Database File

SQLite is a single binary. Install it once:

```bash
pkg update && pkg upgrade -y
pkg install sqlite -y
```

Open a database by naming it. If the file doesn’t exist, SQLite creates it instantly:

```bash
sqlite3 arsenal.db
```

You are now inside the SQLite prompt (`sqlite>`).  
The file `arsenal.db` holds your entire database.

**① Create the first table – weapon test records**  
The engineers need a place to log test IDs. A simple `test` table will do:

```sql
CREATE TABLE test (id INT);
```
- `CREATE TABLE test` — the table name matches the practice task exactly.
- `id INT` — a single column for integer test IDs.

Verify the table exists:

```sql
.tables
```
Output: `test`

Check its structure:

```sql
.schema test
```
Output: `CREATE TABLE test (id INT);`

These dot‑commands are your inspection kit. They never touch the data.

> 💡 **INSIGHT:** SQLite’s `.tables` and `.schema` commands are the equivalent of `ls` and `cat` for databases. Use them constantly.

---

## 🧱 BRICK 2 – Inserting & Viewing Data

**② Insert the first test ID (Medium practice)**  
A prototype weapon gets ID 42.

```sql
INSERT INTO test VALUES (42);
```

Now read it back:

```sql
SELECT * FROM test;
```
Output: a row containing `42`.

The practice engine will check that you created the table and successfully inserted this exact row.

**③ Insert two more rows (Hard practice)**  
The arsenal expands. Add any two more IDs, e.g., 7 and 100:

```sql
INSERT INTO test VALUES (7);
INSERT INTO test VALUES (100);
```

View all three:

```sql
SELECT * FROM test;
```
You should see three rows.

**④ Inspect the table’s physical storage**  
Use `.databases` to see where the file lives, and `.dbinfo` to check page count — both prove the data is real and persisted.

> ⚠️ **WARNING:** Every SQL statement must end with a semicolon. If you forget, the prompt changes to a continuation line (`...>`). Type `;` and press Enter to execute, or Ctrl+C to cancel.

> 💡 **ADVANCED TIP – Scriptability:** You can put all the above SQL in a `.sql` file and run it with `sqlite3 arsenal.db < script.sql`. This is how you’ll automate database setup later.

---

## 💡 Real‑world Usage

**Banking – create an account ledger**
```bash
sqlite3 bank.db
sqlite> CREATE TABLE accounts (id INT, balance REAL);
sqlite> INSERT INTO accounts VALUES (101, 5000.00);
sqlite> SELECT * FROM accounts;
```

**E‑commerce – product catalog setup**
```bash
sqlite3 shop.db
sqlite> CREATE TABLE products (sku TEXT, price REAL);
sqlite> INSERT INTO products VALUES ('SKU-001', 24.99);
sqlite> .tables
```

**Logistics – tracking test shipments**
```bash
sqlite3 cargo.db
sqlite> CREATE TABLE shipments (tracking_id TEXT);
sqlite> INSERT INTO shipments VALUES ('TRK-123');
sqlite> .schema
```

---

## 🔍 Practice Preview
You’ll use the practice engine to build and query the `test` table.

| Level  | Task | What You’ll Write |
|--------|------|-------------------|
| Easy   | Create a table named `test` with column `id` INT. | `CREATE TABLE test (id INT);` |
| Medium | Insert a row with value 42 and SELECT all rows. | `INSERT INTO test VALUES (42);` `SELECT * FROM test;` |
| Hard   | Insert two more rows (any values). Then SELECT all to see three rows. | `INSERT INTO test VALUES (7);` `INSERT INTO test VALUES (100);` `SELECT * FROM test;` |

Run the coach:
```bash
python ii_Practice_Sheets/L-02_Installing_SQLite.py
```
Choose your level, type the SQL, and the engine verifies your database.

---

## 📌 Key Takeaway
- `pkg install sqlite` puts a full database engine on your phone.
- `sqlite3 filename.db` opens/creates a database.
- `CREATE TABLE`, `INSERT`, `SELECT` are your first three verbs.
- Dot‑commands (`.tables`, `.schema`) inspect without modifying.
- Every empire needs a testing ground. Yours is now live.