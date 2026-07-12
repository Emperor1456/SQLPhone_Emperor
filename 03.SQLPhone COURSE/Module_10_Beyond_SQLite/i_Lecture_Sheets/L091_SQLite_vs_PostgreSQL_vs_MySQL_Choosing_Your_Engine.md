# 📘 SQLPhone Emperor v3.0 · Module 10
# 📖 L91 – SQLite vs PostgreSQL vs MySQL – Choosing Your Engine

---

## 🎯 OBJECTIVE — What You Will Master

> After this lesson, you’ll know exactly which database engine to use for any project — from a phone‑side AI companion to a high‑traffic cloud API.

- 🧱 **SQLite** – the embedded, zero‑configuration workhorse
- 🧠 **PostgreSQL** – the advanced, enterprise‑grade relational engine
- 🧪 **MySQL** – the speed‑focused, widely‑hosted alternative
- ⚡ **Decision framework** – matching the engine to the job
- 🧰 **Real‑world scenarios** – banking, e‑commerce, mobile, analytics

---

## 🧱 SQLITE – THE POCKET DATABASE

SQLite is a serverless, self‑contained SQL engine. The entire database lives in a single file. It’s the most deployed database in the world – inside every Android and iOS device, browsers, and embedded systems.

**When to choose SQLite:**
- Mobile apps and games
- Desktop tools (editors, note‑taking apps)
- Prototyping and learning
- Single‑user applications (like Companion’s early versions)
- Anywhere you need zero configuration and absolute portability

```sql
-- SQLite: create a database by simply connecting
sqlite3 empire.db
```

**Limitations:**
- Only one writer at a time (concurrent reads are fine)
- No built‑in user authentication
- Limited support for advanced data types (arrays, JSON functions are available but limited)

---

## 🧱 POSTGRESQL – THE ENTERPRISE FORTRESS

PostgreSQL is a powerful, object‑relational database with strict typing, transactional DDL, and a vast ecosystem of extensions (PostGIS, pgvector, etc.). It’s the default choice for startups and scale‑ups that need reliability and advanced features.

**When to choose PostgreSQL:**
- Multi‑user web applications and APIs
- Applications needing complex queries, window functions, CTEs
- Storing and querying JSON documents alongside relational data
- Geospatial applications (with PostGIS)
- Any project that will eventually need to scale

```sql
-- PostgreSQL: strict typing, rich functions
CREATE TABLE soldiers (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    salary NUMERIC(10,2) CHECK(salary > 0)
);
```

**What PostgreSQL gives you that SQLite doesn’t:**
- True concurrent writers (MVCC)
- Advanced indexing (GIN, GiST, BRIN)
- Built‑in full‑text search
- Role‑based access control
- Stored procedures in multiple languages

---

## 🧱 MYSQL – THE WEB STALWART

MySQL is known for its speed, replication, and massive hosting support. It powers a huge share of the web (WordPress, Facebook, etc.). Its SQL dialect is slightly different, but the core concepts are the same.

**When to choose MySQL:**
- Existing infrastructure already uses MySQL
- Shared hosting that only provides MySQL
- Read‑heavy applications where simple replication is needed

```sql
-- MySQL: similar structure, minor syntax differences
CREATE TABLE soldiers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    salary DECIMAL(10,2) CHECK(salary > 0)
);
```

---

## 🧱 DECISION TABLE

| Scenario | Recommended Engine |
|----------|-------------------|
| Companion (local AI, single‑user) | SQLite |
| E‑commerce backend with 10,000 users | PostgreSQL |
| Blog hosted on cheap shared server | MySQL |
| Mobile game storing player progress | SQLite |
| Real‑time analytics dashboard | PostgreSQL |
| Prototyping a database schema on your phone | SQLite |
| Large enterprise ERP with 100+ tables | PostgreSQL |
| Legacy WordPress site | MySQL |

---

## 💡 Real‑world Usage

**Banking – PostgreSQL with ACID transactions and audit trails**
**E‑commerce – PostgreSQL with JSONB for flexible product attributes**
**Logistics – PostgreSQL with PostGIS for route optimization**
**Mobile – SQLite for offline‑first order‑taking app**
**Companion – SQLite for initial memory, PostgreSQL when you need multi‑user access**

---

## 🔍 Practice Preview
You will evaluate database engines for different business needs.

| Level | Task |
|-------|------|
| Easy | List the three engines and their primary use cases. |
| Medium | Write a comparison table covering at least 5 criteria. |
| Hard | Given a project description (e.g., “a real‑time chat application with 100k users”), choose the best engine and justify your choice with technical arguments. |

Run the coach:
```bash
python ii_Practice_Sheets/L91_SQLite_vs_PostgreSQL_vs_MySQL_Choosing_Your_Engine.py
```

---

## 📌 Key Takeaway
- SQLite is for embedded, single‑user, and learning.
- PostgreSQL is the professional choice for web apps and complex systems.
- MySQL remains a viable option for legacy and hosted environments.
- Your choice of database engine shapes the architecture of your entire application.

*For Emperor.*