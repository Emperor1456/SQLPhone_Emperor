# 📘 SQLPhone Emperor · SQL Module 05
# 📖 L‑39 – Subqueries in WHERE

## 🎯 OBJECTIVE
Use a subquery inside the `WHERE` clause to filter
rows based on the result of another query.

## 🧱 BRICK 1 – Subquery Basics
A subquery is a `SELECT` statement nested inside
another SQL statement. When placed in `WHERE`,
it returns a value (or list) used for comparison.

```sql
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```
The inner query runs first, returning the average
salary, then the outer query uses it.

## 🧱 BRICK 2 – Single‑Row vs Multi‑Row
- **Scalar subquery** returns exactly one value (one column,
  one row). Use with `=`, `>`, `<`, etc.
- **Multi‑row subquery** returns a column of values.
  Must be used with `IN`, `ANY`, `ALL`, or `EXISTS`.

If a scalar subquery returns more than one row,
the database throws an error.

## 💡 Real‑world Usage
- Find employees earning above the departmental average.
- Products priced higher than the overall average.
- Orders placed after the latest shipment date.

## 📌 Key Takeaway
Subqueries in `WHERE` let you compare against
a dynamically computed value.
Always ensure the subquery returns the expected
number of rows.

*Let one query feed another.*