# 📘 SQLPhone Emperor · SQL Module 02
# 📖 L‑20 – Aliases (AS)

## 🎯 OBJECTIVE
Assign temporary names to columns or tables using aliases
to make query output clearer and queries more readable.

## 🧱 BRICK 1 – Column Aliases
Give a column a new name in the result set.
```sql
SELECT first_name AS "First Name", last_name AS "Last Name"
FROM employees;
```
The alias appears as the column header. Use double quotes
for aliases with spaces or special characters.

You can also alias computed columns:
```sql
SELECT salary * 12 AS annual_salary FROM employees;
```

`AS` is optional but recommended for clarity.

## 🧱 BRICK 2 – Table Aliases
Shorten table names to simplify queries (especially joins).
```sql
SELECT e.name, d.name
FROM employees AS e
JOIN departments AS d ON e.dept_id = d.id;
```
Here `e` is an alias for `employees`.

Table aliases become mandatory in self‑joins and correlated subqueries.
They also improve readability when table names are long.

## 💡 Real‑world Usage
- Clean up report columns with user‑friendly names.
- Make complex join queries shorter.
- Rename aggregated columns for downstream processing.

## 📌 Key Takeaway
Aliases rename things for the duration of the query.
Use column aliases to beautify output.
Use table aliases to tame long table names.

*A good alias is a bridge between raw data and meaning.*