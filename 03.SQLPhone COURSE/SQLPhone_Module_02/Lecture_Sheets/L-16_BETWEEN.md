# 📘 SQLPhone Emperor · SQL Module 02
# 📖 L‑16 – BETWEEN

## 🎯 OBJECTIVE
Filter rows within a range of values using `BETWEEN`.

## 🧱 BRICK 1 – The BETWEEN Operator
`BETWEEN` checks if a value lies within an inclusive range:
```sql
SELECT * FROM products
WHERE price BETWEEN 10 AND 50;
```
This includes price = 10 and price = 50.

It works with numbers, text, and dates:
```sql
SELECT * FROM orders
WHERE order_date BETWEEN '2026-01-01' AND '2026-01-31';
```

Equivalent to `value >= low AND value <= high`.

## 🧱 BRICK 2 – NOT BETWEEN
Exclude a range by using `NOT BETWEEN`:
```sql
SELECT * FROM products
WHERE price NOT BETWEEN 10 AND 50;
```

`NOT BETWEEN` is equivalent to `value < low OR value > high`.

**Important:** The range boundaries are inclusive.
If you need exclusive, adjust the values or use `>` and `<`.

## 💡 Real‑world Usage
- Find transactions within a fiscal quarter.
- Retrieve products in a price bracket.
- Filter dates in a reporting period.

## 📌 Key Takeaway
`BETWEEN` simplifies range conditions.
Always remember the inclusive nature.
For exclusive ranges, fall back to `>` and `<`.

*Between two points lies a clear condition.*