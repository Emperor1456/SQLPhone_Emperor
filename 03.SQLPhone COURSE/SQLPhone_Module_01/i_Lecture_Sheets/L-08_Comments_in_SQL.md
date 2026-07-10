# 📘 SQLPhone Emperor · Module 01  
# 📖 L‑08 – Comments in SQL (The Imperial Communication Logs)

---

## 🎯 OBJECTIVE  
Master SQL comments to document your code, explain business rules, and temporarily disable statements.  
You’ll build the Imperial Communication Logs — a `logs` table where every dispatch is recorded with clear, professional annotations.  
Comments are for humans; the database ignores them. Write them like your future self depends on it.

---

## 🧱 BRICK 1 – Single‑Line Comments (`--`)

A single‑line comment starts with `--`. Everything after it until the end of the line is ignored.

**① Create the logs table with a descriptive comment (Easy practice)**
```sql
-- This is the Imperial communication log table
CREATE TABLE logs (
    id INTEGER,
    msg TEXT
);
```
The comment explains the table’s purpose. The engine skips it entirely.

**② Insert the first dispatch**
```sql
-- Add initial test message
INSERT INTO logs VALUES (1, 'test');
```

**③ Verify the table and data**
```sql
SELECT * FROM logs;
```
You’ll see a single row with id=1 and msg='test'.  
The comments were never stored — they exist only in the SQL source file.

**④ Use an inline comment to explain a specific value (Medium practice)**
```sql
INSERT INTO logs VALUES (2, 'second entry'); -- adding more data
```
The inline comment clarifies the insert. The statement executes exactly as if the comment weren’t there.

> 💡 **INSIGHT:** Comments should answer *why*, not *what*. Don’t write `-- inserting row` — the code already says that. Write `-- daily heartbeat signal from outpost 7` to convey business context.

---

## 🧱 BRICK 2 – Multi‑Line Block Comments (`/* */`)

Block comments span multiple lines. Use them for file headers, module descriptions, or temporarily disabling large code sections.

**⑤ Insert a third row with a block comment (Hard practice)**
```sql
/* Table: logs
   Purpose: Stores system messages from all imperial outposts.
   Last updated: 2026-07-09 by Emperor.
*/
INSERT INTO logs VALUES (3, 'block comment test');
```
The entire block between `/*` and `*/` is ignored. The insert still works.

**⑥ Temporarily disable a query during debugging**
```sql
SELECT id, msg FROM logs;
-- SELECT msg FROM logs WHERE id = 2;   -- disabled for now
```
The second `SELECT` is commented out and will not run. This is the standard way to isolate queries during development.

**⑦ Comment out a block of code**
```sql
/*
DELETE FROM logs;
DROP TABLE logs;
*/
SELECT * FROM logs;
```
The dangerous operations inside the block comment never execute. All rows are safe.

> ⚠️ **WARNING:** Block comments do **not** nest. Putting `/*` inside another `/* */` will break. Stick to `--` for quick toggles, `/* */` for headers and large sections.

> 💡 **ADVANCED TIP – Header template for every `.sql` file:**
```sql
/*
 * Project: Imperial Communication Network
 * Author: Emperor
 * Date: 2026-07-09
 * Purpose: Define and seed the logs table.
 */
```
This is the professional standard. Every script you write for Companion will start with such a header.

---

## 💡 Real‑world Usage

**Banking – explain a complex fee calculation**
```sql
-- Apply 2% fee only to international transactions
UPDATE accounts SET balance = balance - amount * 0.02
WHERE transaction_type = 'international';
```

**E‑commerce – document a product filter**
```sql
/* Seasonal promotion: only show winter collection items */
SELECT name, price FROM products
WHERE category = 'winter';
```

**Logistics – disable a route temporarily**
```sql
SELECT tracking_id, destination FROM shipments;
-- WHERE destination = 'Dhaka';  -- hold: route under maintenance
```

---

## 🔍 Practice Preview
You will build and annotate the Imperial Communication Logs table.

| Level  | Task | What You’ll Write |
|--------|------|-------------------|
| Easy   | Create table `logs` (id INT, msg TEXT) and insert one row. Include at least one comment. | `-- comment` `CREATE TABLE logs ...` `INSERT INTO logs ...` |
| Medium | Add another log entry. Use an inline comment to explain the insert. | `INSERT INTO logs VALUES (2, 'second entry'); -- inline comment` |
| Hard   | Insert a third row and include a multi‑line block comment describing the table. | `/* table description */` `INSERT INTO logs VALUES (3, 'block comment test');` |

Run the coach:
```bash
python ii_Practice_Sheets/L-08_Comments.py
```

---

## 📌 Key Takeaway
- `--` starts a single‑line comment; `/* */` spans multiple lines.
- Comments explain *why*, not *what* — they carry business context.
- Use them for file headers, inline clarifications, and disabling code during debugging.
- The database ignores them; your future self and your team will thank you.