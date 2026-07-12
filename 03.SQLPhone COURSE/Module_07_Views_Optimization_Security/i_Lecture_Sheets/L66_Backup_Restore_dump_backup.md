# 📘 SQLPhone Emperor v3.0 · Module 7
# 📖 L66 – Backup & Restore – .dump & .backup

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll protect your database against disaster — creating backups and restoring them with two simple commands. You’ll also learn to automate backups from Python, because manual backups are forgotten backups.

- 🧱 **`.dump`** – export the entire database as SQL text
- 🧠 **`.backup`** – create a binary copy instantly
- 🧪 **Restore from `.dump`** – replay the SQL into a fresh database
- ⚡ **Restore from `.backup`** – swap the file and you’re live
- 🧰 **Automated backups in Python** – daily, timestamped, safe

---

## 🧱 .DUMP – SQL TEXT BACKUP

The `.dump` command outputs every SQL statement needed to recreate the database from scratch. It’s human‑readable, editable, and portable across SQLite versions.

```bash
sqlite3 empire.db ".dump" > empire_backup.sql
```

The resulting file contains all `CREATE TABLE`, `INSERT`, and index statements. You can email it, version‑control it, or run it on another machine.

**Filter a dump to a single table:**
```bash
sqlite3 empire.db ".dump soldiers" > soldiers_backup.sql
```

---

## 🧱 .BACKUP – BINARY BACKUP

The `.backup` command creates an identical, byte‑for‑byte copy of the database file. It’s faster than `.dump` and ideal for quick, complete snapshots.

```bash
sqlite3 empire.db ".backup empire_backup.db"
```

The backup file is a fully functional SQLite database. You can open it directly with `sqlite3` and query it immediately.

---

## 🧱 RESTORING

**From `.dump`:**
```bash
sqlite3 new_empire.db < empire_backup.sql
```

**From `.backup`:**
```bash
cp empire_backup.db empire.db
```

For binary backups, you can also use the `.restore` command inside the shell:
```bash
sqlite3 new_empire.db ".restore empire_backup.db"
```

> ⚠️ **WARNING:** Restoring overwrites the target database completely. Always restore into a new file first, verify the data, then replace the original.

---

## 🧱 AUTOMATED BACKUP IN PYTHON

Manual backups are fragile. A Python script that runs daily (or on every startup) is the professional solution.

```python
import sqlite3
import shutil
from datetime import datetime
import os

def backup_db(source, backup_dir="backups"):
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = f"{backup_dir}/empire_{timestamp}.db"

    # Open source, use SQLite's backup API
    src = sqlite3.connect(source)
    dst = sqlite3.connect(dest)
    src.backup(dst)
    src.close()
    dst.close()
    print(f"Backup saved: {dest}")

    # Rotate old backups – keep only the last 7
    backups = sorted(os.listdir(backup_dir))
    while len(backups) > 7:
        os.remove(os.path.join(backup_dir, backups.pop(0)))

backup_db("empire.db")
```

This creates a timestamped backup, and automatically deletes the oldest backups, keeping only the last 7.

---

## 🧱 BACKUP BEFORE MIGRATION – A CRITICAL HABIT

Always back up before any schema change:

```python
def safe_migration(db_path, migration_sql):
    backup_db(db_path)
    try:
        conn = sqlite3.connect(db_path)
        conn.executescript(migration_sql)
        conn.commit()
        conn.close()
        print("Migration successful.")
    except sqlite3.Error as e:
        print(f"Migration failed: {e}")
        print("Restore from the backup file created before this run.")
```

> 💡 **INSIGHT:** The `.dump` format is also ideal for version‑controlling your schema. Check `schema.sql` into Git, and you can track every structural change over time.

---

## 💡 Real‑world Usage

**Banking – nightly backup before batch processing**
```bash
sqlite3 bank.db ".backup nightly_backup.db"
```

**E‑commerce – export catalog for migration**
```bash
sqlite3 shop.db ".dump" > catalog.sql
```

**Logistics – archive old shipments**
```bash
sqlite3 logistics.db ".dump" | gzip > archive.sql.gz
```

**HR – pre‑upgrade backup**
```bash
sqlite3 hr.db ".backup hr_pre_upgrade.db"
```

**Companion – backup user memories every hour**
```python
backup_db("companion_memory.db", "memory_backups")
```

---

## 🔍 Practice Preview
You will back up and restore the Imperial Army database.

| Level | Task |
|-------|------|
| Easy | Dump the database to a `.sql` file using `.dump`. |
| Medium | Create a binary backup using `.backup` and verify it by opening it. |
| Hard | Write a Python script that automates daily backups with timestamped filenames and keeps only the last 7. |

Run the coach:
```bash
python ii_Practice_Sheets/L66_Backup_Restore_dump_backup.py
```

---

## 📌 Key Takeaway
- `.dump` creates a SQL text backup; `.backup` creates a binary copy.
- Restore from `.dump` with `sqlite3 db < file.sql`.
- Automate backups with Python to prevent data loss.
- Always back up before migrations or dangerous operations.

*For Emperor.*