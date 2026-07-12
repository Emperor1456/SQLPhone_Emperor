# 📘 SQLPhone Emperor v3.0 · Module 6
# 📖 L53 – ALTER TABLE & DROP TABLE – Schema Evolution

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll modify your database structure after it’s live — adding columns, renaming tables and columns, and removing tables entirely. This is how real databases evolve over time.

- 🧱 **ALTER TABLE** – add columns, rename tables, rename columns (SQLite 3.25+)
- 🧠 **DROP TABLE** – permanently delete a table and all its data
- 🧪 **Safe migration patterns** – back up before you alter
- ⚡ **Limitations in SQLite** – what you can and cannot alter
- 🛡️ **Simulating DROP COLUMN** – the SQLite workaround

---

## 🧱 ADDING A COLUMN

You can add new columns to an existing table. The new column is appended at the end; existing rows get `NULL` unless a `DEFAULT` is specified.

```sql
ALTER TABLE soldiers ADD COLUMN email TEXT;
```

To add a column with a default value:

```sql
ALTER TABLE soldiers ADD COLUMN status TEXT DEFAULT 'active';
```

---

## 🧱 RENAMING A TABLE

SQLite allows renaming tables directly — useful when refactoring your schema.

```sql
ALTER TABLE soldiers RENAME TO imperial_army;
```

---

## 🧱 RENAMING A COLUMN (SQLite 3.25+)

```sql
ALTER TABLE soldiers RENAME COLUMN name TO full_name;
```

---

## 🧱 DROPPING A TABLE

`DROP TABLE` permanently deletes a table and all its rows. This action cannot be undone.

```sql
DROP TABLE IF EXISTS old_logs;
```

`IF EXISTS` prevents errors if the table doesn’t exist.

---

## 🧱 SIMULATING DROP COLUMN

SQLite does **not** support `ALTER TABLE … DROP COLUMN` directly. To remove a column, you must:

1. Create a new table without that column.
2. Copy data from the old table to the new table.
3. Drop the old table.
4. Rename the new table to the original name.

```sql
BEGIN;
-- 1. Create new table without the column
CREATE TABLE soldiers_new (
    soldier_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    rank TEXT
    -- email column omitted
);

-- 2. Copy data
INSERT INTO soldiers_new (soldier_id, name, rank)
SELECT soldier_id, name, rank FROM soldiers;

-- 3. Drop old table
DROP TABLE soldiers;

-- 4. Rename new table
ALTER TABLE soldiers_new RENAME TO soldiers;
COMMIT;
```

> ⚠️ **WARNING:** This operation must be wrapped in a transaction. If any step fails, the entire migration rolls back.

> 💡 **INSIGHT:** Before any `ALTER` or `DROP`, always run `.schema` to review the current structure and `.dump` to back up your data.

---

## 💡 Real‑world Usage

**Banking – add a new account type column**
```sql
ALTER TABLE accounts ADD COLUMN account_type TEXT DEFAULT 'checking';
```

**E‑commerce – rename a product table for clarity**
```sql
ALTER TABLE products RENAME TO catalog;
```

**Logistics – drop an obsolete shipments archive**
```sql
DROP TABLE IF EXISTS shipment_archive_2023;
```

**HR – rename a column for consistency**
```sql
ALTER TABLE employees RENAME COLUMN emp_name TO full_name;
```

**Companion – evolve memory schema as features grow**
```sql
ALTER TABLE memories ADD COLUMN embedding BLOB;
```

---

## 🔍 Practice Preview
You will evolve the Imperial Army schema.

| Level | Task |
|-------|------|
| Easy | Add an `email` column to the `soldiers` table. |
| Medium | Rename the `soldiers` table to `imperial_army`, then rename it back. |
| Hard | Simulate dropping a column by creating a new table without that column and copying data, wrapped in a transaction. |

Run the coach:
```bash
python ii_Practice_Sheets/L53_ALTER_TABLE_DROP_TABLE_Schema_Evolution.py
```

---

## 📌 Key Takeaway
- `ALTER TABLE` adds columns, renames tables, and renames columns.
- `DROP TABLE` permanently deletes a table.
- SQLite has limited `ALTER` capabilities — plan schema changes carefully.
- The DROP COLUMN simulation pattern is essential for real projects.

*For Emperor.*