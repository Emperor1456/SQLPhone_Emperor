# 04.SQLPhone NOTES/Module_01_Foundations.md
# SQLPhone Emperor — The Best Phone‑First SQL Curriculum

# 📝 Module 01 – Foundations & First Queries

## Core Concepts
- SQL is a declarative language (you say *what*, not *how*).
- Relational databases store data in **tables** (rows = records, columns = fields).
- SQLite is a zero‑configuration, single‑file database engine.

## Essential SQL Commands
| Command | Description |
|---------|-------------|
| `CREATE TABLE t (col TYPE constraints);` | Define a new table |
| `INSERT INTO t (cols) VALUES (...);` | Add rows |
| `SELECT cols FROM t WHERE condition;` | Retrieve data |
| `DROP TABLE IF EXISTS t;` | Remove table safely |

## Dot‑Commands (SQLite CLI)
| Command | Purpose |
|---------|---------|
| `.tables` | List tables |
| `.schema t` | Show CREATE statement for table `t` |
| `.headers on` | Show column headers in output |
| `.mode column` | Align output |
| `.read file.sql` | Execute SQL from file |
| `.quit` | Exit |

## Data Types & Constraints
- Storage classes: `NULL`, `INTEGER`, `REAL`, `TEXT`, `BLOB`
- Type affinity rather than strict typing (use `STRICT` table for enforcement)
- Constraints: `NOT NULL`, `UNIQUE`, `CHECK`, `DEFAULT`, `PRIMARY KEY`, `FOREIGN KEY`

## Best Practices
- Always specify column list in `INSERT`.
- Use `IF NOT EXISTS` / `IF EXISTS` for safe DDL.
- Comment with `--` (line) or `/* */` (block).
- Format SQL for readability (uppercase keywords, line breaks).

## Quick Reference
```sql
-- Create a simple table
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE
);

-- Insert a row
INSERT INTO users (name, email) VALUES ('Emperor', 'emperor@sqlphone.dev');

-- Query all rows
SELECT * FROM users;
```
