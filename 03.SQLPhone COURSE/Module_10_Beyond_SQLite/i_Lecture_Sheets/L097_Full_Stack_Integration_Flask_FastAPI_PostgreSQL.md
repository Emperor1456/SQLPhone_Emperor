# 📘 SQLPhone Emperor v3.0 · Module 10
# 📖 L97 – Full‑Stack Integration – Flask/FastAPI + PostgreSQL

---

## 🎯 OBJECTIVE — What You Will Master

> After this lesson, you’ll connect a Python web framework to PostgreSQL and serve data over HTTP — completing the loop from database to browser.

- 🧱 **Flask & FastAPI** – Python’s most popular web frameworks  
- 🧠 **Database per‑request pattern** – opening connections safely  
- 🧪 **Building a REST API** – endpoints that return JSON  
- ⚡ **Connection pooling** – production‑grade performance  
- 🧰 **Full‑stack architecture** – database → backend → API → frontend  

---

## 🧱 FLASK + POSTGRESQL

Flask is minimal and flexible. You manage the database connection yourself.

```python
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def get_db():
    return psycopg2.connect("postgresql://user:pass@localhost/empire")

@app.route("/soldiers")
def list_soldiers():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, name, rank FROM soldiers")
    rows = [{"id": r[0], "name": r[1], "rank": r[2]} for r in cur.fetchall()]
    cur.close()
    conn.close()
    return jsonify(rows)

if __name__ == "__main__":
    app.run()
```

---

## 🧱 FASTAPI + POSTGRESQL

FastAPI is modern, async‑first, and auto‑generates API documentation.

```python
from fastapi import FastAPI
import psycopg2

app = FastAPI()

@app.get("/soldiers")
def list_soldiers():
    conn = psycopg2.connect("postgresql://user:pass@localhost/empire")
    cur = conn.cursor()
    cur.execute("SELECT id, name, rank FROM soldiers")
    rows = [{"id": r[0], "name": r[1], "rank": r[2]} for r in cur.fetchall()]
    cur.close()
    conn.close()
    return rows
```

---

## 🧱 CONNECTION POOLING

Opening a connection per request is slow. Use a connection pool:

```python
from psycopg2.pool import SimpleConnectionPool

pool = SimpleConnectionPool(1, 10, "postgresql://user:pass@localhost/empire")

@app.get("/soldiers")
def list_soldiers():
    conn = pool.getconn()
    cur = conn.cursor()
    cur.execute("SELECT id, name, rank FROM soldiers")
    rows = [{"id": r[0], "name": r[1], "rank": r[2]} for r in cur.fetchall()]
    cur.close()
    pool.putconn(conn)
    return rows
```

> 💡 **INSIGHT:** In production, always use a pool. For larger applications, SQLAlchemy’s engine handles pooling automatically.

---

## 💡 Real‑world Usage

**Banking – API endpoints for account balance and transactions**  
**E‑commerce – product catalog API with search and filtering**  
**Logistics – shipment tracking API with real‑time status**  
**Companion – REST API that returns memory entries, accepts new conversations**

---

## 🔍 Practice Preview
You will build a simple API backed by a database.

| Level | Task |
|-------|------|
| Easy | Install FastAPI and create a `/health` endpoint that returns `{"status": "ok"}`. |
| Medium | Connect to PostgreSQL and return all soldiers as JSON. |
| Hard | Add a POST endpoint to create a new soldier, with validation and error handling. |

Run the coach:
```bash
python ii_Practice_Sheets/L97_Full_Stack_Integration_Flask_FastAPI_PostgreSQL.py
```

---

## 📌 Key Takeaway
- Flask and FastAPI are the bridges between your database and the web.  
- Always use connection pools in production.  
- A REST API turns your SQL queries into live, accessible services.  
- This is the full‑stack loop: Database → Python → API → User.

*For Emperor.*