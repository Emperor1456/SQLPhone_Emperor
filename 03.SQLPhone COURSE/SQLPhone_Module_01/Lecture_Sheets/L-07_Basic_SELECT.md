# 📘 SQLPhone Emperor · SQL Module 01
# 📖 L‑07 – Basic SELECT

## 🎯 OBJECTIVE
Retrieve data from tables using the fundamental `SELECT` statement,
master column selection, and filter results with simple conditions.

## 🧱 BRICK 1 – Projection (SELECT Columns)
`SELECT` performs **projection** – choosing which columns to return.

```sql
SELECT first_name, last_name FROM customers;
```
Use `*` to return all columns (acceptable for ad‑hoc queries,
never in production code – always list columns explicitly).

**Column aliases:**
```sql
SELECT first_name AS "First Name", last_name AS "Last Name"
FROM customers;
```
The alias is used in the output; the original column name is unchanged.

**Arithmetic in SELECT:**
```sql
SELECT product_name, unit_price, quantity,
       unit_price * quantity AS line_total
FROM order_items;
```

## 🧱 BRICK 2 – Basic Filtering with WHERE
`WHERE` performs **selection** – filtering rows that satisfy a condition.

Comparison operators: `=`, `<>` (or `!=`), `<`, `>`, `<=`, `>=`.

```sql
SELECT first_name, last_name
FROM customers
WHERE signup_date >= '2025-01-01';
```

**Text comparison:** SQLite uses collation; by default, text
comparison is case‑sensitive. Use `COLLATE NOCASE` for case‑insensitive
matching:
```sql
SELECT * FROM customers
WHERE first_name = 'emperor' COLLATE NOCASE;
```

## 💡 Professional Query Writing
- Always specify needed columns, not `*`, to avoid unnecessary
  data transfer and ensure your query doesn’t break when the
  schema changes.
- Use meaningful aliases for computed columns.
- Format SQL for readability: capitalize keywords, indent clauses.

## 📌 Key Takeaway
`SELECT` is the most important SQL verb.
Master projection (columns) and selection (rows) to extract
exactly the data you need.

*Query with precision. Retrieve nothing less.*