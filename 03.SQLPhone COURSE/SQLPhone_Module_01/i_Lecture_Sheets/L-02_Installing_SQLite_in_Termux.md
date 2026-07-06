# 📘 SQLPhone Emperor · SQL Module 01
# 📖 L‑02 – Installing SQLite in Termux

## 🎯 OBJECTIVE
Establish a fully operational SQLite environment inside Termux.
Understand the CLI tool that will serve as your primary database interface
for the entire course.

## 🧱 BRICK 1 – The SQLite Command‑Line Interface
SQLite is distributed as a single binary: `sqlite3`.
It is an interactive shell with readline support, history, and
direct SQL execution capabilities.

**Installation (one‑time):**
```bash
pkg update && pkg upgrade -y
pkg install sqlite -y
```

**Invocation:**
```bash
sqlite3 <database_file>
```
If the file does not exist, SQLite creates it instantly.
The prompt changes to `sqlite>` – you are now inside a live database session.

**Rules inside the prompt:**
- SQL statements must be terminated with `;`.
- Dot‑commands (meta‑commands) start with `.` and do **not** need a semicolon.
- Use `Ctrl+D` or `.quit` to exit.

## 🧱 BRICK 2 – The Dot‑Command Toolkit
Dot‑commands are SQLite’s built‑in client‑side helpers.
They never touch the database schema – they interact with the CLI itself.

| Command | Purpose |
|---------|---------|
| `.tables` | List all tables in the current database |
| `.schema [table]` | Show the `CREATE` statement for a table (or all if omitted) |
| `.headers on` | Display column names in query results |
| `.mode column` | Format output in aligned columns |
| `.read <file>` | Execute SQL commands from a file |
| `.output <file>` | Redirect query output to a file |
| `.dump` | Export entire database as SQL text |
| `.backup <file>` | Backup the database to another file |
| `.help` | List all available dot‑commands |

**Standard development flow:**
```bash
sqlite3 empire.db
sqlite> .headers on
sqlite> .mode column
sqlite> CREATE TABLE ... ;
sqlite> .tables
sqlite> .schema
sqlite> .quit
```

## 💡 Industrial Context
SQLite’s CLI is used in production by embedded systems engineers,
mobile developers, and backend engineers for quick diagnostics.
It runs on Linux, macOS, Windows, Android, and iOS without modification.
There is no client‑server overhead – you interact directly with the file.
This is the fastest way to prototype, test, and debug SQL queries.

## 📌 Key Takeaway
`sqlite3` is not a toy shell – it is a professional, scriptable,
and fully capable database client.
Mastering it gives you immediate insight into any SQLite database,
whether it’s on your phone, a server, or an aircraft.

*Your command line is now your database console.*