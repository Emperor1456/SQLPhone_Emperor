# 📘 SQLPhone Emperor v3.0 · Module 10
# 📖 L93 – Connecting Python to PostgreSQL (psycopg2)

---

## 🎯 OBJECTIVE — What You Will Master

> After this lesson, you’ll connect your Python backend to a PostgreSQL database using `psycopg2` — the most trusted PostgreSQL driver in the Python ecosystem. You will execute queries, handle transactions, and build a reusable connection module.

- 🔌 **Installation** – `pip install psycopg2-binary` in Termux/proot  
- 🧱 **Connection object** – `psycopg2.connect()`  
- 🧠 **Cursor** – executing SQL and fetching results  
- 🧪 **Parameterized queries** – using `%s` placeholders to prevent injection  
- ⚡ **Best practices** – connection pooling, error handling, context managers  

---

## 🧱 WHY PSYCOPG2?

`psycopg2` is the standard Python adapter for PostgreSQL. It’s fast, secure, and used by frameworks like Django, Flask, and FastAPI under the hood. Learning it directly gives you complete control over your database interactions.

**Installation (inside proot Debian or a compatible environment):**
```bash
pip install psycopg2-binary
```

If you’re running it from Termux’s native Python, you may need to install system dependencies first:
```bash
pkg install postgresql-libs python-dev
pip install psycopg2-binary
```

---

## 🧱 YOUR FIRST CONNECTION

Create a Python script (`connect_pg.py`) and establish a connection:

```python
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="empire",
    user="postgres",
    password="your_password"
)

cursor = conn.cursor()
cursor.execute("SELECT version()")
print(cursor.fetchone())

cursor.close()
conn.close()
```

Replace `your_password` with the actual password of the `postgres` user. If you haven’t set one, run `ALTER USER postgres PASSWORD 'your_password';` inside `psql`.

---

## 🧱 INSERT AND SELECT WITH PARAMETERS

Always use parameterized queries. PostgreSQL uses `%s` as the placeholder (not `?` like SQLite).

```python
cursor.execute(
    "INSERT INTO soldiers (name, rank, salary) VALUES (%s, %s, %s)",
    ("Emperor", "General", 5000.00)
)
conn.commit()

cursor.execute("SELECT * FROM soldiers WHERE salary > %s", (3000,))
for row in cursor.fetchall():
    print(row)
```

> ⚠️ **WARNING:** Never use f‑strings or `.format()` to embed values into SQL. This opens the door to SQL injection. Always use `%s` and a tuple of values.

---

## 🧱 BUILDING A REUSABLE CONNECTION HELPER

A professional codebase wraps the connection logic into a function or context manager. Here’s a minimal `db.py` module:

```python
import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="empire",
        user="postgres",
        password="your_password"
    )

from contextlib import contextmanager

@contextmanager
def connect():
    conn = get_connection()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
```

Now use it anywhere:
```python
with connect() as conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM soldiers")
    for row in cur.fetchall():
        print(row)
```

---

## 🧱 HANDLING ERRORS

Always catch database-specific exceptions:

```python
import psycopg2
from psycopg2 import OperationalError, IntegrityError

try:
    with connect() as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO soldiers (id, name) VALUES (1, 'Duplicate')")
except IntegrityError as e:
    print(f"Integrity violation: {e}")
except OperationalError as e:
    print(f"Connection failed: {e}")
```

---

## 💡 Real‑world Usage

**Banking – safely transfer funds with transactional integrity**
```python
with connect() as conn:
    cur = conn.cursor()
    cur.execute("UPDATE accounts SET balance = balance - 500 WHERE id = 1")
    cur.execute("UPDATE accounts SET balance = balance + 500 WHERE id = 2")
```

**E‑commerce – search products with dynamic filters**
```python
cur.execute(
    "SELECT * FROM products WHERE category = %s AND price < %s",
    ("Electronics", 500)
)
```

**Logistics – batch insert tracking updates**
```python
records = [("TRK1","delivered"), ("TRK2","in transit")]
cur.executemany(
    "UPDATE shipments SET status = %s WHERE tracking_id = %s",
    records
)
conn.commit()
```

**Companion – store and retrieve conversation logs**
```python
cur.execute(
    "INSERT INTO conversations (user_id, message, timestamp) VALUES (%s, %s, NOW())",
    (1, "Hello, Companion")
)
```

---

## 🔍 Practice Preview
You will connect Python to PostgreSQL and build a mini‑application.

| Level | Task |
|-------|------|
| Easy | Install psycopg2 and test the connection by fetching the PostgreSQL version. |
| Medium | Create a table from Python, insert 5 rows, and retrieve them with a filtered query. |
| Hard | Build a reusable `db.py` module with a context manager, then use it to perform a transactional fund transfer between two accounts. |

Run the coach:
```bash
python ii_Practice_Sheets/L93_Connecting_Python_to_PostgreSQL_psycopg2.py
```

---

## 📌 Key Takeaway
- `psycopg2` is the bridge between Python and PostgreSQL.  
- Use `%s` placeholders for all data — never format strings.  
- A reusable connection helper keeps your code clean and safe.  
- The pattern (connect → cursor → execute → commit → close) is identical in concept to SQLite, but now you have the full power of an enterprise database.

*For Emperor.*