# 📘 SQLPhone Emperor · SQL Module 03
# 📖 L‑23 – MIN and MAX

## 🎯 OBJECTIVE
Find the smallest and largest values in a column
using `MIN` and `MAX`.

## 🧱 BRICK 1 – MIN
`MIN(column)` returns the smallest value (for numbers)
or the earliest (for text/dates).
```sql
SELECT MIN(salary) FROM employees;
```
With text, `MIN` returns the first value in alphabetical order.
With dates, the oldest date.

## 🧱 BRICK 2 – MAX
`MAX(column)` returns the largest or latest value.
```sql
SELECT MAX(score) FROM exam_results;
```

Both can be used with multiple columns or subqueries,
but you cannot directly get the whole row containing
the min/max without a subquery or join.

**Tip:** To find the employee with the highest salary
(and return their name), use a subquery (Module 05)
or `ORDER BY` + `LIMIT`.

## 💡 Real‑world Usage
- Highest/lowest product price.
- Earliest registration date.
- Peak sensor reading.

## 📌 Key Takeaway
`MIN` and `MAX` locate the extremes.
They work on numbers, text, and dates.
Combine with other clauses to retrieve the full row.

*Extremes tell you the boundaries of your data.*