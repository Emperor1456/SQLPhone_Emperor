# 📘 SQLPhone Emperor · SQL Module 06
# 📖 L‑47 – UPDATE – Modifying Rows

## 🎯 OBJECTIVE
Change existing data in a table safely using the
`UPDATE` statement, with a focus on precise `WHERE`
clauses.

## 🧱 BRICK 1 – UPDATE Syntax
`UPDATE` modifies values in existing rows.
```sql
UPDATE table_name
SET column1 = value1, column2 = value2
WHERE condition;
```

Without `WHERE`, **all rows** are updated – a common
and dangerous mistake. Always filter.

Example:
```sql
UPDATE employees
SET salary = salary * 1.10
WHERE department = 'Sales';
```

## 🧱 BRICK 2 – Updating Multiple Columns & Subqueries
Set several columns at once:
```sql
UPDATE products
SET price = price * 0.9, stock = stock - 1
WHERE id = 42;
```

You can use a subquery to compute the new value:
```sql
UPDATE employees
SET salary = (SELECT AVG(salary) FROM employees)
WHERE id = 1;
```

**Best practice:** Run a `SELECT` with the same `WHERE`
first to preview which rows will be affected.

## 💡 Real‑world Usage
- Adjust prices during a sale.
- Correct misspelled names.
- Archive old records by setting a status flag.

## 📌 Key Takeaway
`UPDATE` changes data permanently.
Never omit `WHERE` unless you mean to alter every row.
Preview with `SELECT` before executing.

*Update with caution; you can’t undo a careless SET.*