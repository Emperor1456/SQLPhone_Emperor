# 📘 SQLPhone Emperor · SQL Module 07
# 📖 L‑62 – CAST

## 🎯 OBJECTIVE
Convert values between data types using `CAST`.

## 🧱 BRICK 1 – CAST Syntax
`CAST(expression AS type)` converts the result to the
target type.

```sql
SELECT CAST('123' AS INTEGER);       -- 123
SELECT CAST(3.14 AS TEXT);           -- '3.14'
SELECT CAST('2026-07-06' AS TEXT);   -- same
```

Type affinity still applies; `CAST` forces a conversion
if possible. If not possible (e.g., `CAST('abc' AS INTEGER)`),
the result is 0 in SQLite (no error).

## 🧱 BRICK 2 – Real‑world Use Cases
- Ensure numeric sorting (cast string to number).
- Convert dates stored as text to a date format.
- Format numbers for concatenation.

```sql
SELECT order_id || ': $' || CAST(amount AS TEXT)
FROM orders;
```

## 💡 Real‑world Usage
- Data cleaning in migration scripts.
- Dynamic SQL generation.
- Normalise imported data.

## 📌 Key Takeaway
`CAST` explicitly changes data type.
It prevents unexpected type coercion.
Use it when you need a value to be treated as a different type.

*Type conversion is a choice – make it explicit.*