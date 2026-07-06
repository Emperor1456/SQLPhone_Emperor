# 📘 SQLPhone Emperor · SQL Module 02
# 📖 L‑19 – NULL Values

## 🎯 OBJECTIVE
Understand the special meaning of `NULL` and how to
filter or handle missing data using `IS NULL` and
`IS NOT NULL`.

## 🧱 BRICK 1 – What is NULL?
`NULL` represents missing, unknown, or inapplicable
information. It is not zero, not an empty string.
Any arithmetic or comparison with `NULL` yields `NULL`.

```sql
SELECT * FROM employees WHERE manager_id IS NULL;
-- Finds employees without a manager.
```

You cannot use `= NULL`; the result would be `NULL`,
which is treated as false.

## 🧱 BRICK 2 – Functions Handling NULL
- `COALESCE(value, default)` returns the first non‑NULL argument.
- `IFNULL(value, default)` (SQLite specific) works similarly.
- `NULLIF(a, b)` returns `NULL` if a equals b, else a.

Example:
```sql
SELECT name, COALESCE(phone, 'N/A') AS contact
FROM contacts;
```

To count only non‑NULL values: `COUNT(column)` ignores NULLs.

## 💡 Real‑world Usage
- Identify incomplete records.
- Fill missing values with defaults in reports.
- Exclude rows where a critical field is not yet set.

## 📌 Key Takeaway
`NULL` is the absence of a value.
Always use `IS NULL` or `IS NOT NULL` to test for it.
Use `COALESCE` to provide fallback values.

*Emptiness is not zero – it's unknown.*