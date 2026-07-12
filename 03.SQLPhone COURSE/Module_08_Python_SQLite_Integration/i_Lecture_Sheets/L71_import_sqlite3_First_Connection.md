# 📘 SQLPhone Emperor v3.0 · Module 8
# 📖 L71 – import sqlite3 – First Connection

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll open a SQLite database from Python, create a cursor, and execute your first query. This is the bridge that turns a standalone database into an application backend.

- 🧱 **The sqlite3 module** – built‑in, zero‑install database driver  
- 🧠 **Connection object** – your handle to the database file  
- 🧪 **Cursor object** – the tool that sends SQL and fetches results  
- ⚡ **In‑memory databases** – temporary databases for testing  
- 🧰 **Context manager pattern** – safe, automatic cleanup  

---

## 🧱 FIRST CONNECTION

```python
import sqlite3

# Connect – creates empire.db if it doesn't exist
conn = sqlite3.connect("empire.db")
print("Connection opened.")

# Create a cursor
cursor = conn.cursor()

# Execute a simple query
cursor.execute("SELECT sqlite_version()")
version = cursor.fetchone()
print(f"SQLite version: {version[0]}")

# Close
cursor.close()
conn.close()
print("Connection closed.")
```

---

## 🧱 IN‑MEMORY DATABASE

For testing and throw‑away experiments, use `":memory:"`. The database vanishes when the connection closes.

```python
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("CREATE TABLE test (id INTEGER, value TEXT)")
cursor.execute("INSERT INTO test VALUES (1, 'Emperor')")
cursor.execute("SELECT * FROM test")
print(cursor.fetchall())  # [(1, 'Emperor')]
conn.close()
```

---

## 🧱 CONNECTION AS CONTEXT MANAGER

Using `with` automatically closes the connection (even on error). However, you must still `commit()` manually.

```python
with sqlite3.connect("empire.db") as conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS soldiers (id INTEGER PRIMARY KEY, name TEXT)")
    cur.execute("INSERT INTO soldiers (name) VALUES (?)", ("Emperor",))
    conn.commit()
# Connection is closed here automatically
```

> 💡 **INSIGHT:** `sqlite3` is part of Python’s standard library — it’s always available, even on a phone. No `pip install` required.

> ⚠️ **WARNING:** Without `commit()`, your changes are lost when the connection closes. Always commit after INSERT, UPDATE, or DELETE.

---

## 💡 Real‑world Usage

**Banking** – open a connection to the accounts database
```python
conn = sqlite3.connect("bank.db")
```

**E‑commerce** – use `:memory:` to write tests without touching production data
```python
conn = sqlite3.connect(":memory:")
```

**Logistics** – check database health with `SELECT 1`
```python
cursor.execute("SELECT 1")
```

**Companion** – connect to the memory store
```python
conn = sqlite3.connect("companion_memory.db")
```

---

## 🔍 Practice Preview
You will connect Python to SQLite and run your first queries.

| Level | Task |
|-------|------|
| Easy | Connect to `:memory:`, create a table, insert a row, fetch it, and print. |
| Medium | Connect to a file database, create a table, insert a row, commit, close, then reconnect and verify the data persists. |
| Hard | Write a function `get_connection(path)` that returns a connection with `row_factory = sqlite3.Row` and use it to query. |

Run the coach:
```bash
python ii_Practice_Sheets/L71_import_sqlite3_First_Connection.py
```

---

## 📌 Key Takeaway
- `sqlite3.connect()` opens a file database or creates it.  
- Use `:memory:` for fast, disposable test databases.  
- The cursor executes SQL and fetches results.  
- `with` closes the connection, but you must commit writes.

*For Emperor.*