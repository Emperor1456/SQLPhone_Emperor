# 📘 SQLPhone Emperor · SQL Module 02
# 📖 L‑12 – WHERE Clause

## 🎯 OBJECTIVE
Filter rows based on conditions using comparison
operators in the `WHERE` clause.

## 🧱 BRICK 1 – Basic WHERE Syntax
The `WHERE` clause selects only rows that satisfy
a given condition.

```sql
SELECT column1, column2
FROM table_name
WHERE condition;
```

Comparison operators:
- `=`  equal
- `<>` or `!=`  not equal
- `<`  less than
- `>`  greater than
- `<=` less than or equal
- `>=` greater than or equal

Example:
```sql
SELECT name, salary FROM employees
WHERE salary > 50000;
```

## 🧱 BRICK 2 – Filtering on Text and Dates
Text strings are compared lexicographically (dictionary order).
Use single quotes for string literals.
```sql
SELECT name FROM employees
WHERE last_name = 'Smith';
```

Date comparisons work similarly if the date format is
consistent (e.g., ISO‑8601 `YYYY-MM-DD`):
```sql
SELECT * FROM orders
WHERE order_date >= '2026-01-01';
```

**Best practice:** put the column name on the left,
the operator, and the value on the right.
Always test edge cases.

## 💡 Real‑world Usage
- Extract all transactions above a threshold.
- Find users registered after a specific date.
- Retrieve products with zero stock.

## 📌 Key Takeaway
`WHERE` filters rows before aggregation or sorting.
Use precise comparisons to get exactly the subset you need.

*The WHERE clause is the gatekeeper of your data.*