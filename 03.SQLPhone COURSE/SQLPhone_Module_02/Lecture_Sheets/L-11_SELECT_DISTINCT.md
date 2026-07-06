# 📘 SQLPhone Emperor · SQL Module 02
# 📖 L‑11 – SELECT DISTINCT

## 🎯 OBJECTIVE
Learn to eliminate duplicate rows from result sets
using `SELECT DISTINCT`, and understand when and why
it matters in data analysis.

## 🧱 BRICK 1 – The DISTINCT Keyword
`SELECT DISTINCT` returns only unique combinations of
the specified columns. If multiple rows have the same
values for those columns, only one copy is kept.

Syntax:
```sql
SELECT DISTINCT column1, column2
FROM table_name;
```

Without `DISTINCT`, `SELECT` returns all rows, including
duplicates. `DISTINCT` applies to the entire row –
all selected columns together must be unique for a row
to appear.

Example:
```sql
SELECT DISTINCT city FROM customers;
```
Returns a list of cities where at least one customer
lives, with no repeats.

## 🧱 BRICK 2 – DISTINCT with Multiple Columns
When you select multiple columns, the combination
must be unique.

```sql
SELECT DISTINCT city, country FROM customers;
```
The pair `('Berlin', 'Germany')` appears once even
if many customers live in Berlin, Germany.

**Important behaviour:**
- `DISTINCT` processes **after** `SELECT` but before
  `ORDER BY`.
- It does not ignore NULLs – multiple NULLs are
  considered duplicate and collapsed into one row.

## 💡 Real‑world Usage
- Count unique values in a column (combine with `COUNT`).
- Find distinct categories or statuses for dropdown menus.
- Clean data by identifying unique combinations before
  deduplication.

## 📌 Key Takeaway
`DISTINCT` removes duplicate rows from your result set.
Use it when you need only unique combinations.
The keyword applies to all selected columns together.

*In a world of duplicates, DISTINCT brings clarity.*