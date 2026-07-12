# 📘 SQLPhone Emperor v3.0 · Module 8
# 📖 L72 – Creating Tables via Python

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll execute `CREATE TABLE` statements from Python, check if a table already exists, and build reusable schema‑setup functions – the first step in automating database deployment.

- 🧱 **DDL from Python** – executing `CREATE TABLE` and `ALTER TABLE`  
- 🧠 **sqlite_master** – querying the schema metadata  
- 🧪 **Safe table creation** – `IF NOT EXISTS` pattern  
- ⚡ **Dynamic DDL** – generating schema from configuration  

---

## 🧱 CREATING A TABLE

```python
import sqlite3

def create_soldiers_table(conn):
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS soldiers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            rank TEXT,
            salary REAL CHECK(salary > 0),
            joined TEXT DEFAULT (date('now'))
        )
    """)
    conn.commit()

conn = sqlite3.connect("empire.db")
create_soldiers_table(conn)
conn.close()
```

`IF NOT EXISTS` prevents errors when the table already exists – ideal for startup scripts.

---

## 🧱 CHECKING TABLE EXISTENCE

```python
def table_exists(conn, table_name):
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    return cur.fetchone() is not None

if table_exists(conn, "soldiers"):
    print("Soldiers table exists.")
else:
    create_soldiers_table(conn)
```

---

## 🧱 ALTER TABLE FROM PYTHON

```python
def add_column(conn, table, column_def):
    cur = conn.cursor()
    try:
        cur.execute(f"ALTER TABLE {table} ADD COLUMN {column_def}")
        conn.commit()
    except sqlite3.OperationalError as e:
        print(f"Could not add column: {e}")

add_column(conn, "soldiers", "email TEXT")
```

> ⚠️ **WARNING:** Never use f‑strings with user‑supplied table or column names without validation. Whitelist allowed names or use parameterized queries where possible (DDL doesn’t support parameters).

---

## 💡 Real‑world Usage

**Banking** – initialize the accounts table on first run
```python
create_table(conn, "accounts", "id INTEGER PRIMARY KEY, balance REAL")
```

**E‑commerce** – create product catalog from a config file
```python
for table_def in config["tables"]:
    create_table_from_def(conn, table_def)
```

**Logistics** – add a `tracking_number` column after a schema update
```python
add_column(conn, "shipments", "tracking_number TEXT")
```

**Companion** – create memory tables when a new user is registered
```python
create_user_memory_table(conn, user_id)
```

---

## 🔍 Practice Preview
You will create and modify tables from Python.

| Level | Task |
|-------|------|
| Easy | Connect to `:memory:`, create a `soldiers` table with three columns, and verify with `sqlite_master`. |
| Medium | Write a function `create_table_if_missing(conn, name, columns)` that creates a table only if it doesn’t exist. |
| Hard | Build a loop that reads a list of table definitions (name + column dict) and creates all of them in one script. |

Run the coach:
```bash
python ii_Practice_Sheets/L72_Creating_Tables_via_Python.py
```

---

## 📌 Key Takeaway
- `CREATE TABLE IF NOT EXISTS` is the standard safe pattern.  
- `sqlite_master` is the system catalog that stores schema metadata.  
- DDL doesn’t support parameterized placeholders; sanitize dynamic inputs.  
- Python can automate your entire schema deployment.

*For Emperor.*