# 📘 SQLPhone Emperor v3.0 · Module 8
# 📖 L76 – Executing .sql Files from Python

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll run entire SQL scripts from Python — the bridge between manually written SQL files and automated database setup, seeding, and migration.

- 🧱 **Reading .sql files** – load SQL statements from disk
- 🧠 **executescript()** – run multiple statements at once
- 🧪 **Atomic execution** – wrapping scripts in transactions
- ⚡ **Use cases** – schema deployment, test fixtures, data seeding
- 🧰 **Robust error handling** – catching and reporting script failures

---

## 🧱 EXECUTING A .SQL FILE

```python
import sqlite3

def execute_sql_file(conn, filepath):
    """Read a .sql file and execute all statements."""
    with open(filepath, 'r', encoding='utf-8') as f:
        sql = f.read()
    conn.executescript(sql)
    conn.commit()

conn = sqlite3.connect("empire.db")
execute_sql_file(conn, "schema.sql")
conn.close()
```

The function reads the entire file, passes the text to `executescript()`, and commits. This is the standard pattern for deploying a schema.

---

## 🧱 SPLITTING STATEMENTS MANUALLY

If you need more control — for example, to execute statements one by one and report progress — you can split on semicolons:

```python
def execute_sql_file_verbose(conn, filepath):
    with open(filepath, 'r') as f:
        sql = f.read()
    statements = [s.strip() for s in sql.split(';') if s.strip()]
    for i, stmt in enumerate(statements, 1):
        try:
            conn.execute(stmt)
            print(f"Statement {i} executed.")
        except sqlite3.Error as e:
            print(f"Error in statement {i}: {e}")
            raise
    conn.commit()
```

> ⚠️ **WARNING:** Splitting on `;` is fragile — it can break if semicolons appear inside string literals or comments. For production, use `executescript()`.

---

## 🧱 WRAPPING IN A TRANSACTION

To ensure all statements succeed or none do, wrap the entire file execution in a transaction:

```python
def execute_sql_file_atomic(conn, filepath):
    with open(filepath, 'r') as f:
        sql = f.read()
    try:
        conn.execute("BEGIN")
        conn.executescript(sql)
        conn.commit()
        print("Script executed successfully.")
    except sqlite3.Error as e:
        conn.rollback()
        print(f"Script failed, rolled back: {e}")
```

---

## 🧱 SEEDING A DATABASE FROM A .SQL FILE

A typical `seed.sql` file contains `INSERT` statements:

```sql
-- seed.sql
INSERT INTO soldiers (name, rank, salary) VALUES ('Emperor', 'General', 5000);
INSERT INTO soldiers (name, rank, salary) VALUES ('Rahim', 'Colonel', 4000);
INSERT INTO soldiers (name, rank, salary) VALUES ('Karim', 'Private', 2000);
```

Load it with:

```python
conn = sqlite3.connect("empire.db")
execute_sql_file_atomic(conn, "seed.sql")
conn.close()
```

---

## 💡 Real‑world Usage

**Banking** – run a monthly interest calculation script
```bash
python apply_interest.py  # internally executes "monthly_interest.sql"
```

**E‑commerce** – reset test database before each test suite
```python
execute_sql_file(conn, "reset_test_db.sql")
```

**Logistics** – apply a migration file to add a new column
```python
execute_sql_file(conn, "migration_003_add_delivery_notes.sql")
```

**Companion** – initialize memory schema on first launch
```python
execute_sql_file(conn, "companion_schema.sql")
```

---

## 🔍 Practice Preview
You will execute SQL scripts from Python.

| Level | Task |
|-------|------|
| Easy | Write a script that executes a single `CREATE TABLE` statement from a file. |
| Medium | Create a `seed.sql` file with three INSERT statements and load it atomically. |
| Hard | Build a function that takes a directory of `.sql` files, sorts them alphabetically, and executes each in order (a simple migration runner). |

Run the coach:
```bash
python ii_Practice_Sheets/L76_Executing_sql_Files_from_Python.py
```

---

## 📌 Key Takeaway
- `executescript()` runs multiple SQL statements from a string.  
- Load `.sql` files with `open()` and pass to `executescript()`.  
- Wrapping in a transaction ensures atomicity.  
- This pattern is the foundation of automated schema deployment and data seeding.

*For Emperor.*