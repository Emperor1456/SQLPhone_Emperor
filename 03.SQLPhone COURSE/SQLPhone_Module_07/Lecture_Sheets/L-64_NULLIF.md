# 📘 SQLPhone Emperor · SQL Module 07
# 📖 L‑64 – NULLIF

## 🎯 OBJECTIVE
Return NULL if two expressions are equal; otherwise
return the first expression.

## 🧱 BRICK 1 – NULLIF Syntax
`NULLIF(expr1, expr2)` compares the two values.
If they are equal, returns NULL; else returns expr1.

```sql
SELECT NULLIF(5, 5);     -- NULL
SELECT NULLIF(5, 3);     -- 5
```

## 🧱 BRICK 2 – Practical Uses
- Avoid division by zero:
  ```sql
  SELECT amount / NULLIF(quantity, 0) FROM orders;
  ```
- Mark zero values as missing:
  ```sql
  SELECT NULLIF(discount, 0) AS real_discount
  FROM products;
  ```
- Clean data: convert empty strings to NULL:
  ```sql
  SELECT NULLIF(TRIM(input), '') FROM forms;
  ```

## 💡 Real‑world Usage
- Prevent calculation errors.
- Distinguish between “no value” and “zero”.
- Sanitise input during import.

## 📌 Key Takeaway
`NULLIF` is a precise tool for turning specific values
into NULL.
It’s especially useful with arithmetic and data cleaning.

*When equality means emptiness, NULLIF makes it NULL.*