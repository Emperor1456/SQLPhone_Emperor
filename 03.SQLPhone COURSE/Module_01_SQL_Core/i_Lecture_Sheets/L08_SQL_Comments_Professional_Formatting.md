# 📘 SQLPhone Emperor v3.0 · Module 1
# 📖 L08 – SQL Comments & Professional Formatting

---

## 🎯 OBJECTIVE — What You Will Master

> After this lesson, your SQL will be readable, maintainable, and professional.

- 📝 **Single‑line comments** – `--` for quick notes
- 📄 **Block comments** – `/* */` for headers and multi‑line explanations
- 🧹 **Formatting standards** – uppercase keywords, line breaks, indentation
- 🧪 **Why style matters** – code is read far more than it is written

---

## 🧱 SINGLE‑LINE COMMENTS

A single‑line comment starts with `--`. Everything after it is ignored by the database.

```sql
-- Select all active soldiers
SELECT name, rank FROM soldiers
WHERE status = 'active';
```

You can also place an inline comment at the end of a line:

```sql
SELECT name FROM soldiers
WHERE rank = 'General';  -- only top brass
```

> 💡 **INSIGHT:** Comments should explain *why*, not *what*. The code already
> shows *what* you’re doing. Use comments for business context, assumptions,
> and non‑obvious logic.

---

## 🧱 BLOCK COMMENTS

Enclose multi‑line text between `/*` and `*/`. Use them for file headers
or to temporarily disable a section of SQL during development.

```sql
/*
 * Imperial Army Database – Personnel Schema
 * Author: Emperor
 * Date: 2026-07-12
 * Purpose: Define and seed the soldiers table.
 */
CREATE TABLE soldiers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    rank TEXT
);
```

**Commenting out a block for debugging:**

```sql
/*
DELETE FROM soldiers;
DROP TABLE soldiers;
*/
SELECT * FROM soldiers;
```

> ⚠️ **WARNING:** Block comments do **not** nest. If you wrap a section
> that already contains a `/* */` pair, the first `*/` closes the entire comment.

---

## 🧱 PROFESSIONAL FORMATTING STANDARDS

Consistent formatting makes SQL instantly readable by your team, your
instructors, and your future self.

| Rule | Example |
|------|---------|
| **UPPERCASE** keywords | `SELECT`, `FROM`, `WHERE`, `ORDER BY` |
| **lowercase** identifiers | `soldiers`, `name`, `rank` |
| One clause per line | `SELECT` on its own line, `FROM` on the next |
| Indent sub‑clauses | Two or four spaces before column lists |
| Keep lines short | Under 80 characters for phone‑friendliness |

**Formatted query example:**

```sql
SELECT name, rank, salary
FROM soldiers
WHERE salary > 3000
  AND status = 'active'
ORDER BY salary DESC;
```

---

## 💡 Real‑world Usage

**Banking – transaction report header**
```sql
/*
 * Monthly Fee Summary
 * Parameters: month = '2026-07'
 */
SELECT account_id, SUM(fee) AS total_fees
FROM fees
WHERE strftime('%Y-%m', charged_date) = '2026-07'
GROUP BY account_id;
```

**E‑commerce – temporarily disable a dangerous query**
```sql
/*
DELETE FROM products WHERE quantity = 0;
*/
SELECT * FROM products;
```

**Logistics – documented delivery query**
```sql
-- Fetch shipments overdue by more than 3 days
SELECT tracking_id, due_date
FROM shipments
WHERE status <> 'delivered'
  AND due_date < date('now', '-3 days');
```

---

## 🔍 Practice Preview
You will add comments and apply formatting standards to existing SQL queries.

| Level | Task |
|-------|------|
| Easy | Add a single‑line comment to a `SELECT` query. |
| Medium | Add a multi‑line block comment header to a `CREATE TABLE` statement. |
| Hard | Reformat a messy query with uppercase keywords and proper line breaks. |

Run the coach:
```bash
python ii_Practice_Sheets/L08_SQL_Comments_Professional_Formatting.py
```

---

## 📌 Key Takeaway
- `--` starts a single‑line comment; `/* */` spans multiple lines.
- Comments explain *why*, not *what*.
- Consistent formatting (uppercase keywords, line breaks) is a professional signature.
- Well‑styled SQL earns respect in code reviews.

*For Emperor.*