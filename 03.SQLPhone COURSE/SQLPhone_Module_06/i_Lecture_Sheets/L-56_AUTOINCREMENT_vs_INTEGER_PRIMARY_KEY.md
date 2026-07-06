# 📘 SQLPhone Emperor · SQL Module 06
# 📖 L‑56 – AUTOINCREMENT vs INTEGER PRIMARY KEY

## 🎯 OBJECTIVE
Understand the difference between `AUTOINCREMENT` and
standard `INTEGER PRIMARY KEY` in SQLite, and choose
the right one.

## 🧱 BRICK 1 – Standard INTEGER PRIMARY KEY
When you define `INTEGER PRIMARY KEY`, it becomes an alias
for the built‑in `rowid`. If you insert `NULL`, SQLite
assigns the next highest integer (max used + 1) or a random
one if the max exceeds 2^63-1.

```sql
CREATE TABLE t (id INTEGER PRIMARY KEY, name TEXT);
INSERT INTO t (name) VALUES ('A'), ('B');
-- id will be 1, 2.
```

## 🧱 BRICK 2 – AUTOINCREMENT Keyword
Adding `AUTOINCREMENT` guarantees that new IDs will always
be higher than any previously used ID, even if you delete
the row with the highest ID. It uses an internal table to
track the maximum.

```sql
CREATE TABLE t (id INTEGER PRIMARY KEY AUTOINCREMENT, ...);
```

**Cost:** Slightly slower and uses extra storage.
**Use case:** When you must ensure IDs are never reused
(e.g., legal document numbers, sequential invoice numbers).

## 💡 Real‑world Usage
- Most cases: simple `INTEGER PRIMARY KEY` is sufficient.
- `AUTOINCREMENT` when IDs must be unique over time, not
  just within the current table state.

## 📌 Key Takeaway
Default to `INTEGER PRIMARY KEY`.
Only use `AUTOINCREMENT` if re‑use of IDs would be a
business logic problem.

*Keys should be unique; AUTOINCREMENT adds a guarantee of monotonicity.*