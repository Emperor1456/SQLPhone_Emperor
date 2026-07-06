# 📘 SQLPhone Emperor · SQL Module 04
# 📖 L‑33 – FULL OUTER JOIN (Simulated)

## 🎯 OBJECTIVE
Combine all rows from both tables, with NULLs where
there is no match, using a `UNION` of `LEFT JOIN`s.

## 🧱 BRICK 1 – Concept of FULL OUTER JOIN
`FULL OUTER JOIN` returns all rows from both tables.
If a match exists, columns from both sides are populated;
if not, the missing side gets NULLs.

SQLite does not support `FULL OUTER JOIN` directly.

## 🧱 BRICK 2 – Simulation with UNION
```sql
SELECT A.*, B.*
FROM A LEFT JOIN B ON A.key = B.key
UNION
SELECT A.*, B.*
FROM B LEFT JOIN A ON B.key = A.key
WHERE A.key IS NULL;
```
The first `LEFT JOIN` gets matched rows + A‑only rows.
The second `LEFT JOIN` (with swapped tables) gets B‑only rows
(where A.key IS NULL). `UNION` removes duplicates.

## 💡 Real‑world Usage
- Compare two lists for full differences.
- Merge datasets without losing any records.

## 📌 Key Takeaway
`FULL OUTER JOIN` is the union of both `LEFT JOIN`s.
Simulate with `LEFT JOIN` + `UNION` + `IS NULL` filter.
It’s a powerful tool for data reconciliation.

*When you need everything from both sides, simulate FULL.*