# 📘 SQLPhone Emperor · SQL Module 01
# 📖 L‑08 – Comments in SQL

## 🎯 OBJECTIVE
Use comments to document SQL code, explain complex logic,
and make scripts maintainable for teams and your future self.

## 🧱 BRICK 1 – Single‑Line Comments
Start a comment with `--`. Everything after `--` until the end
of the line is ignored.

```sql
-- Select all active customers
SELECT first_name, last_name
FROM customers
WHERE status = 'active'; -- only active rows
```

**Inline comments:** placed at the end of a line to explain
a specific clause or condition.

## 🧱 BRICK 2 – Multi‑Line Comments (Block Comments)
Enclose text within `/*` and `*/`. This can span multiple lines
and is useful for header documentation or temporarily disabling
blocks of code.

```sql
/*
 * Query: Monthly revenue report
 * Author: Emperor
 * Date: 2026-07-05
 * Description: Sums order amounts grouped by month.
 */
SELECT strftime('%Y-%m', order_date) AS month,
       SUM(amount) AS total_revenue
FROM orders
GROUP BY month;
```

**Commenting out code for debugging:**
```sql
SELECT first_name, last_name
-- , email, phone
FROM customers;
```
The extra columns are ignored; you can quickly toggle them back.

## 💡 Documentation Standards
- Every `.sql` file should start with a header block explaining
  purpose, author, date, and parameters (if any).
- Use inline comments for non‑obvious business logic (e.g.,
  "exclude VAT‑exempt transactions").
- Avoid obvious comments (`-- select all rows`). Comments
  should add insight, not noise.

## 📌 Key Takeaway
Comments are for humans, not the database engine.
Write them to explain *why*, not *what*.
Well‑commented SQL is a mark of professional engineering.

*Code tells you how; comments tell you why.*