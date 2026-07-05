# 📚 SQLPhone Emperor — Complete SQL Curriculum

**12 Modules · 98 Lessons · One Phone**

This document lays out the full battle plan for achieving database mastery from an Android device. Each module builds on the last, following the “two bricks at a time” principle.

---

## MODULE 01 – FOUNDATIONS & FIRST QUERIES
*10 Lessons | Goal: Understand relational databases and write your first SQL statements.*

- L‑01: What is SQL? Relational database concepts, tables, rows, columns.
- L‑02: Installing SQLite in Termux and opening the CLI.
- L‑03: Creating databases, `.tables`, `.schema`, `.quit`.
- L‑04: SQLite data types (NULL, INTEGER, REAL, TEXT, BLOB).
- L‑05: `CREATE TABLE` – column definitions, `PRIMARY KEY`, `AUTOINCREMENT`.
- L‑06: `INSERT INTO` – single rows, multiple rows, omitting columns.
- L‑07: Basic `SELECT` – all columns (`*`), specific columns, arithmetic in queries.
- L‑08: Single‑line (`--`) and multi‑line (`/* */`) comments.
- L‑09: SQL syntax rules, case sensitivity, statement terminators, best practices.
- L‑10: Practice set – design a simple table, insert data, and run queries.

---

## MODULE 02 – READING & FILTERING DATA
*10 Lessons | Goal: Retrieve exactly the data you need from a database.*

- L‑11: `SELECT DISTINCT` – eliminating duplicates.
- L‑12: `WHERE` clause – comparison operators (`=`, `<>`, `<`, `>`, `<=`, `>=`).
- L‑13: Logical operators `AND`, `OR`, `NOT` and combining conditions.
- L‑14: `ORDER BY` – sorting by one or more columns, `ASC` and `DESC`.
- L‑15: `LIMIT` and `OFFSET` – pagination.
- L‑16: `BETWEEN` – range filtering.
- L‑17: `IN` – matching against a list of values.
- L‑18: `LIKE` – pattern matching with `%` and `_`, case‑insensitive with `COLLATE NOCASE`.
- L‑19: Handling `NULL` – `IS NULL`, `IS NOT NULL`.
- L‑20: Aliases (`AS`) for columns and tables.

---

## MODULE 03 – AGGREGATION & GROUPING
*8 Lessons | Goal: Summarise and analyse data with aggregate functions.*

- L‑21: `COUNT` – counting rows.
- L‑22: `SUM` and `AVG` – summing and averaging numeric columns.
- L‑23: `MIN` and `MAX` – finding extremes.
- L‑24: `GROUP BY` – grouping data by a single column.
- L‑25: `GROUP BY` multiple columns – nested aggregation.
- L‑26: `HAVING` – filtering groups after aggregation.
- L‑27: Combining `WHERE`, `GROUP BY`, and `HAVING` in a single query.
- L‑28: Challenge set – aggregation problems.

---

## MODULE 04 – JOINS & UNIONS
*10 Lessons | Goal: Combine data from multiple tables like a pro.*

- L‑29: Introduction to relationships and foreign keys.
- L‑30: `INNER JOIN` – matching rows between tables.
- L‑31: `LEFT JOIN` – all rows from left table plus matches.
- L‑32: Simulating `RIGHT JOIN` with `LEFT JOIN`.
- L‑33: Simulating `FULL OUTER JOIN` with `LEFT JOIN` + `UNION`.
- L‑34: Self‑join – joining a table to itself.
- L‑35: `UNION` and `UNION ALL` – stacking result sets.
- L‑36: Joining three or more tables.
- L‑37: Real‑world join challenges.
- L‑38: Enforcing foreign keys in SQLite (`PRAGMA foreign_keys = ON`).

---

## MODULE 05 – SUBQUERIES & ADVANCED FILTERING
*8 Lessons | Goal: Write nested queries and use powerful filtering techniques.*

- L‑39: Subqueries inside `WHERE` clause.
- L‑40: Scalar subqueries inside `SELECT`.
- L‑41: `IN` and `NOT IN` with subqueries.
- L‑42: `EXISTS` and `NOT EXISTS` – testing for presence.
- L‑43: `ANY` and `ALL` operators.
- L‑44: Correlated subqueries – referencing outer query.
- L‑45: Common Table Expressions (`WITH` clause).
- L‑46: Subquery practice and patterns.

---

## MODULE 06 – MODIFYING DATA & SCHEMA
*10 Lessons | Goal: Change data and table structures safely.*

- L‑47: `UPDATE` – modifying existing rows.
- L‑48: `DELETE` – removing rows.
- L‑49: `DROP TABLE` – deleting entire tables.
- L‑50: `ALTER TABLE` – renaming, adding columns (SQLite limitations).
- L‑51: Constraints deep dive: `NOT NULL`, `UNIQUE`, `CHECK`.
- L‑52: `DEFAULT` values for columns.
- L‑53: `PRIMARY KEY` – single and composite keys.
- L‑54: `FOREIGN KEY` – referential integrity in action.
- L‑55: `CREATE INDEX` – speeding up queries.
- L‑56: `AUTOINCREMENT` vs `INTEGER PRIMARY KEY` (SQLite internals).

---

## MODULE 07 – DATE, TIME & BUILT‑IN FUNCTIONS
*8 Lessons | Goal: Manipulate dates, strings, and numbers with built‑in functions.*

- L‑57: `date()`, `time()`, `datetime()` – getting current date/time.
- L‑58: `strftime()` – custom date/time formatting.
- L‑59: Mathematical functions: `ABS()`, `ROUND()`, `RANDOM()`, `RANDOMBLOB()`.
- L‑60: String functions: `SUBSTR()`, `REPLACE()`, `TRIM()`, `LENGTH()`, `UPPER()`, `LOWER()`.
- L‑61: Concatenation with `||`.
- L‑62: `CAST` – converting between data types.
- L‑63: `COALESCE` – returning the first non‑null value.
- L‑64: `NULLIF` – returning NULL if two expressions are equal.

---

## MODULE 08 – CONDITIONAL LOGIC & VIEWS
*6 Lessons | Goal: Add decision logic to queries and create reusable virtual tables.*

- L‑65: `CASE` expressions – simple and searched forms.
- L‑66: `CASE` in `ORDER BY`, `GROUP BY`, and `WHERE`.
- L‑67: Views – creating, querying, dropping.
- L‑68: Updatable views – what works and what doesn’t.
- L‑69: Materialized views (SQLite lacks them; alternative approaches).
- L‑70: Exporting query results to CSV (`.mode csv`, `.output`).

---

## MODULE 09 – PYTHON + SQLITE INTEGRATION
*10 Lessons | Goal: Connect Python to SQLite and build data‑driven apps.*

- L‑71: `import sqlite3` – connecting to a database from Python.
- L‑72: Creating tables programmatically.
- L‑73: Inserting data safely with parameterized queries.
- L‑74: Retrieving data: `fetchone()`, `fetchall()`, `fetchmany()`.
- L‑75: `UPDATE` and `DELETE` via Python.
- L‑76: Executing `.sql` files from Python.
- L‑77: Error handling in database operations (`try/except`).
- L‑78: Building a reusable database helper module.
- L‑79: Interactive practice coach – task engine for SQL (Python script).
- L‑80: Mini‑project – a command‑line contact book with full CRUD.

---

## MODULE 10 – SECURITY, OPTIMIZATION & BEST PRACTICES
*6 Lessons | Goal: Write secure, fast, and maintainable SQL.*

- L‑81: Preventing SQL injection – parameterized queries deep dive.
- L‑82: Effective index usage – when and how to create indexes.
- L‑83: `EXPLAIN QUERY PLAN` – understanding query execution.
- L‑84: Transactions – `BEGIN`, `COMMIT`, `ROLLBACK` for data integrity.
- L‑85: Database backup and restoration in SQLite (`.backup`, `.dump`).
- L‑86: Schema design best practices and naming conventions.

---

## MODULE 11 – REAL‑WORLD PROJECTS
*8 Lessons | Goal: Build complete database solutions from scratch.*

- L‑87: Student Management System
- L‑88: E‑commerce inventory tracker
- L‑89: Library management with borrowing logs
- L‑90: Employee payroll database
- L‑91: Blog database (posts, comments, users)
- L‑92: Expense tracker with monthly reports
- L‑93: Movie rating system (many‑to‑many relationships)
- L‑94: Custom project – your own idea, fully designed and implemented

---

## MODULE 12 – BEYOND SQLITE & NEXT STEPS
*4 Lessons | Goal: Understand the wider database world and plan your future.*

- L‑95: Differences between SQLite, PostgreSQL, MySQL – when to use which.
- L‑96: Installing PostgreSQL in Termux (optional, proot‑based).
- L‑97: Connecting Python to PostgreSQL with `psycopg2`.
- L‑98: Roadmap – ORMs (SQLAlchemy), migrations (Alembic), cloud databases (AWS RDS, Supabase).

---

*The curriculum is the map. The discipline is the engine.  
Master these 98 lessons, and you’ll never need permission to call yourself a database engineer.*

*Built on a phone. Built for the future.*