# 📘 SQLPhone Emperor · SQL Module 02
# 📖 L‑14 – ORDER BY

## 🎯 OBJECTIVE
Sort query results in ascending or descending order
using one or more columns.

## 🧱 BRICK 1 – Single‑Column Sorting
`ORDER BY` arranges rows by the values in a specified column.

```sql
SELECT name, salary FROM employees
ORDER BY salary DESC;
```
- `ASC` (default) – smallest to largest.
- `DESC` – largest to smallest.

For text, `ASC` sorts alphabetically (A→Z).

## 🧱 BRICK 2 – Multiple Columns & Expressions
Sort by more than one column; ties in the first column
are resolved by the second.

```sql
SELECT department, name FROM employees
ORDER BY department ASC, name ASC;
```

You can sort by an expression or alias:
```sql
SELECT name, salary * 12 AS annual
FROM employees
ORDER BY annual DESC;
```

`NULL` values appear first or last depending on the DB;
in SQLite, `NULL` is considered smaller than any value for `ASC`.

## 💡 Real‑world Usage
- Display top‑selling products.
- Sort log entries by timestamp (most recent first).
- Organise reports alphabetically.

## 📌 Key Takeaway
`ORDER BY` controls the presentation order.
Use multiple columns for fine‑grained sorting.
Explicit `ASC`/`DESC` avoids ambiguity.

*Sorted data is readable data.*