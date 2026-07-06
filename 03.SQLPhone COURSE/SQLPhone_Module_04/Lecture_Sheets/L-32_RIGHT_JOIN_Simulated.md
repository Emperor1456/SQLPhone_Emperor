# 📘 SQLPhone Emperor · SQL Module 04
# 📖 L‑32 – RIGHT JOIN (Simulated)

## 🎯 OBJECTIVE
Understand `RIGHT JOIN` and how to simulate it in SQLite
using `LEFT JOIN`.

## 🧱 BRICK 1 – What RIGHT JOIN Does
`RIGHT JOIN` is the mirror of `LEFT JOIN`: it keeps every
row from the **right** table and puts NULLs for missing
left‑table matches.

SQLite does not natively support `RIGHT JOIN`, but it can
be simulated by swapping the table order and using `LEFT JOIN`.

## 🧱 BRICK 2 – Simulation Technique
Instead of:
```sql
SELECT ... FROM A RIGHT JOIN B ON ...
```
Write:
```sql
SELECT ... FROM B LEFT JOIN A ON ...
```

The result is identical. You simply reverse the roles.

## 💡 Real‑world Usage
- When you need all rows from the second table but
  the DB doesn’t support `RIGHT JOIN`.
- Database‑agnostic SQL writing.

## 📌 Key Takeaway
`RIGHT JOIN` is just a `LEFT JOIN` with tables swapped.
Always simulate it that way in SQLite.
This keeps your SQL portable.

*No RIGHT? Just LEFT from the other side.*