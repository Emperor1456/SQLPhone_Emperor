# 📘 SQLPhone Emperor v3.0 · Module 8
# 📖 L78 – Reusable Database Helper Module

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll build your own database utility module — a single file that every project can import for clean, consistent database access. This is the professional pattern used in Flask, FastAPI, and Django backends.

- 🧱 **Connection factory** – function that returns a configured connection
- 🧠 **Context manager** – automatic cleanup and commit/rollback
- 🧪 **Row factory** – return dictionaries instead of tuples
- ⚡ **Configurable** – path, pragmas, and settings
- 🧰 **Reusable across projects** – one module, every database

---

## 🧱 A REUSABLE HELPER MODULE (`db.py`)

```python
import sqlite3
from contextlib import contextmanager

def get_connection(db_path="empire.db"):
    """Return a connection with row_factory set and foreign keys enabled."""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row   # dict-like access
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

@contextmanager
def connect(db_path="empire.db"):
    """Context manager that yields a connection and handles commit/rollback."""
    conn = get_connection(db_path)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
```

---

## 🧱 USAGE

```python
from db import connect

with connect("empire.db") as conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM soldiers WHERE rank = ?", ("General",))
    for row in cur.fetchall():
        print(row["name"], row["salary"])
```

No more manual `commit()`, `rollback()`, or `close()`. The context manager handles everything.

---

## 🧱 EXTENDING THE MODULE

Add a function to execute SQL files, or a helper for common query patterns:

```python
def fetch_all(conn, sql, params=()):
    """Execute a SELECT and return all rows as a list of dicts."""
    cur = conn.cursor()
    cur.execute(sql, params)
    return [dict(row) for row in cur.fetchall()]

def execute(conn, sql, params=()):
    """Execute an INSERT/UPDATE/DELETE and return rowcount."""
    cur = conn.cursor()
    cur.execute(sql, params)
    return cur.rowcount
```

Usage:

```python
with connect() as conn:
    soldiers = fetch_all(conn, "SELECT * FROM soldiers WHERE salary > ?", (3000,))
    count = execute(conn, "UPDATE soldiers SET rank = ? WHERE id = ?", ("General", 1))
    print(f"Updated {count} row(s).")
```

---

## 💡 Real‑world Usage

**Banking** – `get_connection("bank.db")` in every backend service
**E‑commerce** – `connect("shop.db")` with custom pragmas for WAL mode
**Logistics** – reuse the same `db.py` across microservices
**Companion** – consistent row factory for all memory queries

---

## 🔍 Practice Preview
You will create your own reusable database helper module.

| Level | Task |
|-------|------|
| Easy | Write a `get_connection()` function that returns a connection with `row_factory`. |
| Medium | Write a context manager that yields a connection and auto‑commits on success. |
| Hard | Extend the helper with `fetch_all()` and `execute()` functions, then use them to insert and query soldiers. |

Run the coach:
```bash
python ii_Practice_Sheets/L78_Reusable_Database_Helper_Module.py
```

---

## 📌 Key Takeaway
- Encapsulate connection logic in a reusable module.  
- Use `row_factory = sqlite3.Row` for dict‑like row access.  
- A context manager ensures cleanup and commit/rollback.  
- This pattern scales to every database‑driven application you’ll ever build.

*For Emperor.*