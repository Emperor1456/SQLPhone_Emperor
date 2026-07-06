# 📘 SQLPhone Emperor · SQL Module 01
# 📖 L‑03 – First Database & Dot‑Commands

## 🎯 OBJECTIVE
Create your first SQLite database, build a table,
and use dot‑commands to inspect and verify the schema.

## 🧱 BRICK 1 – Creating a Database
In SQLite, a database is a single file.
Creating one is a side effect of connecting to it:

```bash
sqlite3 empire.db
```

If `empire.db` does not exist, SQLite creates it in the current working directory.
If it already exists, SQLite opens it.
There is no `CREATE DATABASE` statement.

Once inside, you can immediately create tables:
```sql
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    salary REAL
);
```

The database now holds a schema – the table definition – and is ready for data.

## 🧱 BRICK 2 – Schema Inspection Dot‑Commands
Dot‑commands are your schema inspection toolkit:

| Command | Purpose |
|---------|---------|
| `.tables` | List all table names in the database |
| `.schema` | Display the `CREATE` statements for all tables |
| `.schema employees` | Display the `CREATE` statement for a specific table |
| `.databases` | Show attached database files (main, temp, etc.) |
| `.dbinfo` | Display internal database metadata (page count, etc.) |

Example workflow:
```
sqlite> .tables
employees
sqlite> .schema employees
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    salary REAL
);
sqlite> .databases
main: /data/data/com.termux/files/home/empire.db
```

These commands let you verify that your DDL executed correctly
without needing to query system tables.

## 💡 Professional Usage
Engineers use dot‑commands for:
- Debugging schema issues before code deployment.
- Documenting database structure via `.schema > schema.sql`.
- Quick inspection of unfamiliar databases.
- Validating migration scripts.

## 📌 Key Takeaway
A SQLite database is just a file.
Dot‑commands give you immediate visibility into its structure.
You never guess what’s inside – you inspect it.

*Trust the schema, but verify with `.schema`.*