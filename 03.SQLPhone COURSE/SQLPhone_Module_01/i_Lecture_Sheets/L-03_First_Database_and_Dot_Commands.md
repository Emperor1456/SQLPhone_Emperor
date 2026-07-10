# 📘 SQLPhone Emperor · Module 01  
# 📖 L‑03 – First Database & Dot‑Commands (Inspecting the Imperial Census)

---

## 🎯 OBJECTIVE  
Master SQLite dot‑commands to inspect your database without writing queries.  
You’ll build a `people` table for the Imperial Census, insert citizens, and verify everything using `.tables`, `.schema`, and the `sqlite_master` system table.

---

## 🧱 BRICK 1 – The Census Table & `.tables`

The Empire requires a census: every citizen’s name and age must be recorded.

**① Create the people table (Easy practice)**
```sql
CREATE TABLE people (name TEXT, age INT);
```
- `people` – the table name matches the practice task exactly.
- `name TEXT` – stores names as text.
- `age INT` – stores ages as integers.

Check that the table exists:

```sql
.tables
```
Output: `people`

This dot‑command lists every table in the current database. After a fresh creation, you’ll see only `people`.

> 💡 **INSIGHT:** `.tables` is your map. Before inserting, you confirm the table is there. Before dropping, you verify what you’ll lose.

---

## 🧱 BRICK 2 – Inserting Citizens & Inspecting Schema

**② Add Emperor to the census (Medium practice)**
```sql
INSERT INTO people VALUES ('Emperor', 18);
```
Now view the data:

```sql
SELECT * FROM people;
```
Output: a single row with `Emperor | 18`.

**③ Display the table’s full schema (Hard practice)**
While `.schema people` works in the CLI, the practice engine simulates this using the `sqlite_master` system table:

```sql
SELECT sql FROM sqlite_master WHERE name = 'people';
```
This returns the exact `CREATE TABLE` statement you wrote. It’s the programmatic way to inspect schema — essential for scripts and automated tools.

**④ Add more citizens**
```sql
INSERT INTO people VALUES ('Rahim', 25);
INSERT INTO people VALUES ('Karim', 30);
SELECT * FROM people;
```
Now the census has three records.

**⑤ Other key dot‑commands**
| Command | Purpose |
|---------|---------|
| `.databases` | Show attached database files |
| `.dbinfo` | Internal metadata (page count, etc.) |
| `.dump` | Export entire database as SQL |
| `.backup` | Create a safe copy |

Use `.help` to see them all.

> ⚠️ **WARNING:** Dot‑commands are **not SQL**. They don’t need semicolons. Adding one (`;`) will be ignored, but it’s a bad habit — keep them out.

> 💡 **ADVANCED TIP – Automating inspections:**  
> `.schema > census_schema.sql` writes the table definition to a file. This is how you document and version‑control your database design.

---

## 💡 Real‑world Usage

**Banking – inspect account table structure**
```bash
sqlite3 bank.db
sqlite> .tables
sqlite> .schema accounts
```

**E‑commerce – verify product catalog schema**
```bash
sqlite3 shop.db
sqlite> SELECT sql FROM sqlite_master WHERE name='products';
```

**Logistics – dump shipping database for backup**
```bash
sqlite3 cargo.db
sqlite> .dump > cargo_backup.sql
```

**HR – check all employee‑related tables**
```bash
sqlite3 hr.db
sqlite> .tables | grep emp
```

---

## 🔍 Practice Preview
You’ll build the census database and inspect it with dot‑commands.

| Level  | Task | What You’ll Write |
|--------|------|-------------------|
| Easy   | Create a table `people` with columns `name` TEXT and `age` INT. | `CREATE TABLE people (name TEXT, age INT);` |
| Medium | Insert at least one person into `people` and SELECT all rows. | `INSERT INTO people VALUES ('Emperor', 18);` `SELECT * FROM people;` |
| Hard   | Display the schema of `people` using `sqlite_master`. | `SELECT sql FROM sqlite_master WHERE name = 'people';` |

Run the coach:
```bash
python ii_Practice_Sheets/L-03_First_Database_Dot_Commands.py
```
Choose `1`, `2`, or `3`. The engine checks your tables, data, and schema query.

---

## 📌 Key Takeaway
- `.tables` lists tables; `.schema` shows definitions; `sqlite_master` is the programmatic alternative.
- Dot‑commands are your instant inspection toolkit — no SQL required.
- The census is only as accurate as its schema. Verify with `.schema` before trusting the data.
- Automate inspections early — it’s the mark of a professional.