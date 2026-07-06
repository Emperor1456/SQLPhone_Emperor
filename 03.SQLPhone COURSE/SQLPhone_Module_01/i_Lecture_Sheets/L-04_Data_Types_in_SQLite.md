# 📘 SQLPhone Emperor · SQL Module 01
# 📖 L‑04 – Data Types in SQLite

## 🎯 OBJECTIVE
Master SQLite’s flexible type system, understand storage classes,
and learn to enforce data integrity through type affinity and constraints.

## 🧱 BRICK 1 – Storage Classes
SQLite does not have fixed column types. Instead, every value
carries one of five storage classes:

| Storage Class | Description |
|---------------|-------------|
| NULL | Missing or unknown value |
| INTEGER | Signed whole number, up to 8 bytes |
| REAL | 8‑byte IEEE floating‑point number |
| TEXT | Character string, stored in database encoding (UTF‑8/UTF‑16) |
| BLOB | Binary large object, stored exactly as input |

The column’s declared type (e.g., `VARCHAR(255)`) is just a
**type affinity** suggestion. SQLite stores whatever value fits
the affinity rule, not strictly enforcing the declared type.

## 🧱 BRICK 2 – Type Affinity & Practical Impact
When you create a column with a type like `INT`, `CHAR`, `VARCHAR`,
`FLOAT`, SQLite maps it to one of five affinities:

- TEXT affinity: `CHAR`, `CLOB`, `TEXT`
- NUMERIC affinity: no type specified, or `NUMERIC`, `BOOLEAN`, `DATE`, `DATETIME`
- INTEGER affinity: `INT`, `INTEGER`, `TINYINT`, `SMALLINT`, `MEDIUMINT`, `BIGINT`, `UNSIGNED BIG INT`
- REAL affinity: `REAL`, `FLOAT`, `DOUBLE`
- BLOB affinity: `BLOB`, no type specified

**Example:** A column declared `INT` will try to convert inserted
text values to integers if possible, storing the integer if
successful. This flexibility can be powerful but dangerous;
always validate data in application code.

To enforce strict typing, use `STRICT` tables (SQLite 3.37+):
```sql
CREATE TABLE ledger (
    id INTEGER PRIMARY KEY,
    amount REAL NOT NULL,
    description TEXT
) STRICT;
```

## 💡 Production Considerations
- Financial applications: use `STRICT` tables and parameterized
  queries to prevent type coercion bugs.
- Data import pipelines: always sanitize inputs; don’t rely on
  type affinity to correct malformed data.
- Migrating to PostgreSQL/MySQL: note that other DBMS enforce types
  strictly; code written for SQLite’s flexible typing may break.

## 📌 Key Takeaway
SQLite’s type system is dynamic and flexible.
Understand affinities to predict storage behavior.
Use `STRICT` tables when data integrity is critical.

*Flexibility is a feature; integrity is a requirement.*