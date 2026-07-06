# 📘 SQLPhone Emperor · SQL Module 04
# 📖 L‑35 – UNION and UNION ALL

## 🎯 OBJECTIVE
Combine result sets from multiple SELECT statements
vertically using `UNION` and `UNION ALL`.

## 🧱 BRICK 1 – UNION
`UNION` stacks the results of two queries, removing duplicates.
```sql
SELECT name FROM employees
UNION
SELECT name FROM contractors;
```
Both SELECTs must have the same number of columns and
compatible data types.

## 🧱 BRICK 2 – UNION ALL
`UNION ALL` does not remove duplicates – it’s faster.
```sql
SELECT name FROM employees
UNION ALL
SELECT name FROM contractors;
```
Use `UNION ALL` when duplicates are acceptable or impossible.

**Important:** `ORDER BY` applies to the final result,
not to the individual SELECTs (unless wrapped in subqueries).

## 💡 Real‑world Usage
- Merge data from archive and live tables.
- Combine similar reports from different regions.
- Create a master list from multiple sources.

## 📌 Key Takeaway
`UNION` combines results vertically.
Columns must match in number and type.
Use `UNION ALL` for better performance if duplicates are fine.

*Stack results, not confusion.*