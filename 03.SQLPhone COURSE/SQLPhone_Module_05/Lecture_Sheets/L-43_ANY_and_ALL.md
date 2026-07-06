# 📘 SQLPhone Emperor · SQL Module 05
# 📖 L‑43 – ANY and ALL

## 🎯 OBJECTIVE
Compare a value against a set of values returned
by a subquery using `ANY` and `ALL`.

## 🧱 BRICK 1 – ANY (SOME)
`value > ANY (subquery)` is true if the value is
greater than at least one value in the subquery result.
Equivalent to `> MIN(...)` for `>`.

```sql
SELECT name, salary
FROM employees
WHERE salary > ANY (
    SELECT salary FROM employees WHERE dept = 'Sales'
);
```
Employees earning more than the lowest‑paid Sales employee.

## 🧱 BRICK 2 – ALL
`value > ALL (subquery)` is true if the value is
greater than every value in the subquery result.
Equivalent to `> MAX(...)`.

```sql
SELECT name, salary
FROM employees
WHERE salary > ALL (
    SELECT salary FROM employees WHERE dept = 'Sales'
);
```
Employees earning more than the highest‑paid Sales employee.

## 💡 Real‑world Usage
- Products priced higher than any competitor’s.
- Scores exceeding all previous records.
- Temperatures above any recorded in the region.

## 📌 Key Takeaway
`ANY` is “any one of”, `ALL` is “every single one”.
They replace multiple `OR` / `AND` conditions elegantly.
Use with care: `= ANY` is same as `IN`.

*Compare against the crowd, or against the champion.*