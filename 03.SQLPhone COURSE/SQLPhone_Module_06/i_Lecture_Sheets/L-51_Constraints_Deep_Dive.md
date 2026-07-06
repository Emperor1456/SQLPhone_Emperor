# 📘 SQLPhone Emperor · SQL Module 06
# 📖 L‑51 – Constraints Deep Dive

## 🎯 OBJECTIVE
Master all constraint types to enforce data integrity
at the database level.

## 🧱 BRICK 1 – Column‑Level Constraints
- `NOT NULL` – must have a value.
- `UNIQUE` – no duplicate values in the column.
- `CHECK` – custom condition (`CHECK(age >= 0)`).
- `DEFAULT` – fallback value if none provided.

```sql
CREATE TABLE accounts (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    balance REAL NOT NULL DEFAULT 0.0,
    CHECK(balance >= 0)
);
```

## 🧱 BRICK 2 – Table‑Level Constraints
Constraints that span multiple columns:
- `PRIMARY KEY (col1, col2)` – composite key.
- `FOREIGN KEY (...) REFERENCES ...`
- `UNIQUE (col1, col2)` – composite unique.
- `CHECK(expression)` – can reference multiple columns.

```sql
CREATE TABLE enrollments (
    student_id INTEGER,
    course_id INTEGER,
    PRIMARY KEY(student_id, course_id),
    FOREIGN KEY(student_id) REFERENCES students(id),
    FOREIGN KEY(course_id) REFERENCES courses(id)
);
```

## 💡 Real‑world Usage
- Prevent negative inventory.
- Enforce unique email addresses.
- Guarantee parent‑child relationships.

## 📌 Key Takeaway
Constraints are the database’s immune system.
They catch bad data before it’s stored.
Use them aggressively in production schemas.

*The database is your last line of data defense.*