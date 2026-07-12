# 📘 SQLPhone Emperor v3.0 · Module 8
# 📖 L77 – Database Error Handling – try/except Patterns

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll wrap every database operation in robust error handling, ensuring your application never crashes on a database error and always leaves data in a consistent state.

- 🧱 **Common exceptions** – `sqlite3.OperationalError`, `IntegrityError`, `DatabaseError`
- 🧠 **try/except around DB calls** – catch, log, and respond
- 🧪 **Rollback on failure** – undo partial transactions
- ⚡ **Retry logic** – handle locked databases gracefully
- 🧰 **Production‑grade patterns** – error logging, graceful degradation

---

## 🧱 BASIC ERROR HANDLING

```python
import sqlite3

conn = sqlite3.connect("empire.db")
try:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO soldiers (name) VALUES (?)", ("Emperor",))
    conn.commit()
except sqlite3.IntegrityError as e:
    print(f"Integrity violation: {e}")
    conn.rollback()
except sqlite3.Error as e:
    print(f"Database error: {e}")
finally:
    conn.close()
```

---

## 🧱 COMMON SQLITE3 EXCEPTIONS

| Exception | Trigger |
|-----------|---------|
| `IntegrityError` | UNIQUE constraint, foreign key violation, CHECK failure |
| `OperationalError` | Database locked, disk I/O error, malformed SQL |
| `ProgrammingError` | Incorrect number of bindings, table not found |
| `DataError` | Value out of range |

---

## 🧱 ROLLBACK ON FAILURE

```python
try:
    conn.execute("BEGIN")
    cursor.execute("UPDATE accounts SET balance = balance - 500 WHERE id = 1")
    cursor.execute("UPDATE accounts SET balance = balance + 500 WHERE id = 2")
    conn.commit()
except sqlite3.Error as e:
    conn.rollback()
    print(f"Transfer failed, rolled back: {e}")
```

> 💡 **INSIGHT:** Always begin a multi‑step operation with an explicit `BEGIN`. If anything fails, a single `ROLLBACK` undoes everything since the `BEGIN`, keeping your data consistent.

---

## 🧱 RETRY ON DATABASE LOCKED

SQLite locks the entire database on writes. If another connection is writing, you get `OperationalError: database is locked`. A retry loop can solve this:

```python
import time

def execute_with_retry(conn, sql, params, max_retries=5):
    for attempt in range(max_retries):
        try:
            conn.execute(sql, params)
            conn.commit()
            return
        except sqlite3.OperationalError as e:
            if "locked" in str(e) and attempt < max_retries - 1:
                time.sleep(0.2 * (attempt + 1))  # exponential backoff
            else:
                raise
```

---

## 💡 Real‑world Usage

**Banking** – prevent overdraft via exception handling
```python
try:
    cursor.execute("UPDATE accounts SET balance = balance - ? WHERE id = ? AND balance >= ?", (amt, acc_id, amt))
    if cursor.rowcount == 0:
        raise ValueError("Insufficient funds")
    conn.commit()
except ValueError as e:
    print(e)
```

**E‑commerce** – handle duplicate SKU gracefully
```python
try:
    cursor.execute("INSERT INTO products (sku, name) VALUES (?, ?)", (sku, name))
except IntegrityError:
    print(f"Product with SKU {sku} already exists.")
```

**Logistics** – retry on database locked during high‑volume tracking updates
```python
execute_with_retry(conn, "UPDATE shipments SET status = ? WHERE tracking_id = ?", (status, tid))
```

**Companion** – log and alert on schema migration failure
```python
try:
    execute_sql_file(conn, "migration.sql")
except sqlite3.Error as e:
    logging.critical(f"Migration failed: {e}")
    raise
```

---

## 🔍 Practice Preview
You will wrap database operations in error‑handling blocks.

| Level | Task |
|-------|------|
| Easy | Catch an `IntegrityError` when inserting a duplicate primary key and print a friendly message. |
| Medium | Use a try/except/finally to ensure the connection is always closed, even on error. |
| Hard | Implement a retry loop for `OperationalError` (database locked), with exponential backoff. |

Run the coach:
```bash
python ii_Practice_Sheets/L77_Database_Error_Handling_try_except_Patterns.py
```

---

## 📌 Key Takeaway
- Wrap database operations in `try/except` to prevent crashes.  
- Rollback on error to maintain data integrity.  
- Retry on transient errors like database locked.  
- Always close the connection in `finally` or use a context manager.

*For Emperor.*