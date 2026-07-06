# 📘 SQLPhone Emperor · SQL Module 07
# 📖 L‑63 – COALESCE

## 🎯 OBJECTIVE
Return the first non‑NULL value from a list using `COALESCE`.

## 🧱 BRICK 1 – COALESCE Basics
`COALESCE(value1, value2, ...)` evaluates arguments left to right
and returns the first non‑NULL.

```sql
SELECT COALESCE(phone, 'No phone') FROM contacts;
```

If all arguments are NULL, it returns NULL.

## 🧱 BRICK 2 – Practical Patterns
- Provide fallback values:
  ```sql
  SELECT COALESCE(nickname, first_name) AS display_name
  FROM users;
  ```
- Compute with alternatives:
  ```sql
  SELECT COALESCE(hourly_rate * 40, salary) AS weekly_pay
  FROM payroll;
  ```
- Replace NULLs in aggregations:
  ```sql
  SELECT SUM(COALESCE(bonus, 0)) FROM employees;
  ```

## 💡 Real‑world Usage
- Default display text when data is missing.
- Safe arithmetic with nullable columns.
- Merge multiple optional columns.

## 📌 Key Takeaway
`COALESCE` is the NULL‑safe fallback.
It makes your queries robust against missing data.
Always consider what should appear instead of NULL.

*When data is absent, COALESCE fills the void.*