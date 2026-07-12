# 📘 SQLPhone Emperor v3.0 · Module 6
# 📖 L59 – Module Practice: Data Migration Script

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll write a complete SQL migration script — the kind that evolves a live database without losing data. This is the foundation of tools like Alembic and Django Migrations.

- 🧱 **Migration pattern** – create new schema, copy data, drop old, rename
- 🧠 **Transactional DDL** – wrapping migrations in transactions
- 🧪 **Backward compatibility** – keeping the old schema readable during migration
- ⚡ **Real‑world tooling** – this is the foundation of all database version control
- 🛡️ **Safe migration habits** – backup, test, verify

---

## 🧱 THE MIGRATION SCENARIO

The Imperial Army has a `soldiers` table that currently stores `rank` as a TEXT column. The High Command now requires `rank` to be a foreign key to a new `ranks` table, with numeric levels for sorting. You must migrate the data without losing any soldier records.

**Current schema:**
```sql
CREATE TABLE soldiers (
    soldier_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    rank TEXT
);
```

**Target schema:**
```sql
CREATE TABLE ranks (
    rank_id INTEGER PRIMARY KEY,
    rank_name TEXT UNIQUE,
    rank_level INTEGER
);

CREATE TABLE soldiers_v2 (
    soldier_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    rank_id INTEGER,
    FOREIGN KEY (rank_id) REFERENCES ranks(rank_id)
);
```

---

## 🧱 THE COMPLETE MIGRATION SCRIPT

```sql
BEGIN;

-- 1. Create the new ranks table
CREATE TABLE ranks (
    rank_id INTEGER PRIMARY KEY,
    rank_name TEXT UNIQUE,
    rank_level INTEGER
);

-- 2. Populate ranks from existing distinct rank values
INSERT INTO ranks (rank_name, rank_level)
SELECT DISTINCT rank,
    CASE rank
        WHEN 'General' THEN 1
        WHEN 'Colonel' THEN 2
        WHEN 'Major' THEN 3
        WHEN 'Private' THEN 4
        ELSE 5
    END
FROM soldiers
WHERE rank IS NOT NULL;

-- 3. Create the new soldiers table with a foreign key
CREATE TABLE soldiers_new (
    soldier_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    rank_id INTEGER,
    FOREIGN KEY (rank_id) REFERENCES ranks(rank_id)
);

-- 4. Migrate data, mapping old rank TEXT to new rank_id
INSERT INTO soldiers_new (soldier_id, name, rank_id)
SELECT s.soldier_id, s.name, r.rank_id
FROM soldiers s
LEFT JOIN ranks r ON s.rank = r.rank_name;

-- 5. Drop the old table and rename the new one
DROP TABLE soldiers;
ALTER TABLE soldiers_new RENAME TO soldiers;

COMMIT;
```

---

## 🧱 MIGRATION SAFETY CHECKLIST

**Before running the migration:**
- Back up the database (`.backup` or `.dump`)
- Test the migration on a copy of the database
- Ensure no application is writing to the database during migration
- Wrap the entire migration in `BEGIN`/`COMMIT`

**After running the migration:**
- Verify row counts match (`SELECT COUNT(*) FROM soldiers;`)
- Check foreign key integrity (`PRAGMA foreign_key_check;`)
- Run a few sample queries to confirm data integrity

---

## 🧱 COMMON MIGRATION PATTERNS

**① Add a non‑null column with a default:**
```sql
ALTER TABLE soldiers ADD COLUMN status TEXT DEFAULT 'active';
```

**② Split a full_name column into first_name and last_name:**
```sql
ALTER TABLE soldiers ADD COLUMN first_name TEXT;
ALTER TABLE soldiers ADD COLUMN last_name TEXT;
UPDATE soldiers SET
    first_name = SUBSTR(full_name, 1, INSTR(full_name, ' ') - 1),
    last_name = SUBSTR(full_name, INSTR(full_name, ' ') + 1);
-- Then drop the full_name column using the table recreation pattern
```

**③ Rename a column (SQLite 3.25+):**
```sql
ALTER TABLE soldiers RENAME COLUMN name TO full_name;
```

> ⚠️ **WARNING:** Migrations on production databases are the most dangerous operations you’ll perform. Always practice on a copy first. A bad migration can corrupt data permanently.

> 💡 **INSIGHT:** This pattern — create new → migrate data → drop old → rename — is exactly what tools like Alembic and Django generate under the hood. Understanding it gives you full control over your database’s evolution.

---

## 💡 Real‑world Usage

**Banking – splitting a full_name column into first_name and last_name**
**E‑commerce – normalizing product categories into a separate table**
**Logistics – adding a status timestamp column and backfilling from another table**
**HR – migrating from a flat employee table to a normalized department‑employee structure**
**Companion – evolving the memory schema as features grow**

---

## 🔍 Practice Preview
You will write and execute a data migration for the Imperial Army.

| Level | Task |
|-------|------|
| Easy | Create the `ranks` table and populate it from distinct soldier ranks. |
| Medium | Create the new `soldiers_new` table with the foreign key. |
| Hard | Execute the full migration script inside a transaction and verify the result with `PRAGMA foreign_key_check`. |

Run the coach:
```bash
python ii_Practice_Sheets/L59_Module_Practice_Data_Migration_Script.py
```

---

## 📌 Key Takeaway
- A migration restructures the database without losing data.
- The pattern: create new → migrate data → drop old → rename.
- Always wrap migrations in `BEGIN`/`COMMIT` and back up first.
- This is the foundation of all database version control.

*For Emperor.*