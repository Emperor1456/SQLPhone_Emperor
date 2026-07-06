# 📘 SQLPhone Emperor · SQL Module 01
# 📖 L‑09 – SQL Syntax Rules & Best Practices

## 🎯 OBJECTIVE
Learn the formal syntax rules of SQL, coding conventions
used in top‑tier engineering teams, and how to write
maintainable, readable, and portable SQL.

## 🧱 BRICK 1 – Syntax Rules (The Language Itself)
- SQL statements are terminated by a semicolon `;`.
  In SQLite’s CLI, a missing semicolon shows a continuation prompt.
- Keywords are case‑insensitive (`SELECT`, `select`, `Select` are
  identical), but the **convention** is to write keywords in UPPERCASE.
- Identifiers (table/column names) are case‑insensitive for ASCII,
  but case‑sensitive for Unicode characters. Always quote identifiers
  that conflict with keywords: `"Order"`.
- String literals use single quotes: `'Emperor'`. Double quotes
  are for identifiers. Never mix them.
- SQLite accepts both line comments (`--`) and block comments (`/* */`).

## 🧱 BRICK 2 – Professional Conventions
**Formatting:**
- Break clauses onto separate lines:
  ```sql
  SELECT column1, column2
  FROM table_name
  WHERE condition
  ORDER BY column1;
  ```
- Indent subclauses with two or four spaces.
- Use a comma‑first style for large column lists to simplify diffs:
  ```sql
  SELECT first_name
       , last_name
       , email
  FROM customers;
  ```
- Keep lines under 80 characters for phone‑friendly readability.

**Naming:**
- Use `snake_case` for table and column names (`order_items`, `customer_id`).
- Use descriptive, singular table names (`customer`, not `customers`).
- Prefix primary key columns with the table name: `customer_id`.

**Portability:**
- Avoid SQLite‑specific functions where possible (e.g., `datetime('now')`
  instead of `strftime()` for simple date retrieval) to ease future
  migration to PostgreSQL or MySQL.

## 💡 Code Review Standards
When your SQL is reviewed, the first things checked are
readability, naming conventions, and comments.
Writing sloppy SQL is a signal of sloppy thinking.
Professional code is a craft.

## 📌 Key Takeaway
SQL syntax is simple; SQL style is an art.
Adopt strict conventions now, and you will produce code
that others can read, trust, and maintain.

*Clarity is the ultimate sophistication.*