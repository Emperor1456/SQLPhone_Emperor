# 04.SQLPhone NOTES/Module_07_Functions.md
# SQLPhone Emperor — The Best Phone‑First SQL Curriculum

# 📝 Module 07 – Date, Time & String Functions

## Date & Time
- `date('now')`, `time('now')`, `datetime('now')`
- Modifiers: `'+1 day'`, `'-1 month'`, `'start of month'`
- `strftime('%Y-%m-%d %H:%M', timestring)` for custom format.

## Mathematical Functions
- `ABS()`, `ROUND(value, decimals)`, `RANDOM()`

## String Functions
- `LENGTH()`, `UPPER()`, `LOWER()`
- `SUBSTR(str, start, length)`, `REPLACE(str, old, new)`
- `TRIM()`, `LTRIM()`, `RTRIM()`
- Concatenation: `||`
- `INSTR(str, sub)` returns position.

## Handling NULL
- `COALESCE(v1, v2, ...)` returns first non‑NULL.
- `NULLIF(a, b)` returns NULL if a equals b, else a.

## Examples
```sql
SELECT strftime('%d/%m/%Y', order_date) FROM orders;

SELECT UPPER(name), ROUND(price * 0.9, 2) FROM products;

SELECT first_name || ' ' || COALESCE(middle_name, '') || ' ' || last_name FROM contacts;
```
