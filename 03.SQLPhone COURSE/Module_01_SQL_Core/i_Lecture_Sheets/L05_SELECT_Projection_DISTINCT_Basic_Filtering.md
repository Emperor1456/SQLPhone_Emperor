# 📘 SQLPhone Emperor v3.0 · Module 1
# 📖 L05 – SELECT – Projection, DISTINCT, Basic Filtering

---

## 🎯 OBJECTIVE — What You Will Master

> After this lesson, you’ll retrieve exactly the data you need — no more, no less.

- 📊 **Projection** – choosing which columns to return
- 🧹 **DISTINCT** – eliminating duplicate rows
- 🔍 **Basic WHERE** – filtering rows with conditions
- 🧪 **The `*` wildcard** – when to use it, when to avoid it

---

## 🧱 PROJECTION – PICKING COLUMNS

`SELECT` performs **projection**: it returns only the columns you request.
The `*` wildcard returns all columns, but in production code you should always
list exactly what you need.

```sql
-- BAD: returns all columns, wastes memory, breaks if schema changes
SELECT * FROM soldiers;

-- GOOD: explicit columns, clear intent
SELECT name, rank FROM soldiers;
```

**Business example – report only soldier names and ranks:**
```sql
SELECT name, rank FROM soldiers;
```

---

## 🧱 DISTINCT – REMOVE DUPLICATES

When the same value appears in multiple rows, `DISTINCT` returns each unique
value only once.

```sql
SELECT DISTINCT rank FROM soldiers;
```

This is essential for generating dropdown lists, unique category filters,
or deduplicating data before aggregation.

**Business example – list all unique ranks in the army:**
```sql
SELECT DISTINCT rank FROM soldiers;
```

> ⚠️ **WARNING:** `DISTINCT` applies to **all** columns in the `SELECT` list.
> `SELECT DISTINCT rank, name FROM soldiers` will return unique combinations
> of rank and name, not unique ranks.

---

## 🧱 BASIC WHERE – FILTERING ROWS

`WHERE` restricts which rows are returned based on a condition.
Comparison operators: `=`, `<>` (or `!=`), `<`, `>`, `<=`, `>=`.

```sql
SELECT name, rank FROM soldiers
WHERE rank = 'General';
```

**Business example – find all soldiers with a salary above 1000:**
```sql
SELECT name, salary FROM soldiers
WHERE salary > 1000;
```

**Text comparison** is case‑sensitive by default. Use `COLLATE NOCASE`
for case‑insensitive matching:

```sql
SELECT * FROM soldiers
WHERE name = 'emperor' COLLATE NOCASE;
```

> 💡 **INSIGHT:** `WHERE` runs **before** `SELECT` – you’re filtering rows,
> not the columns you see. The database engine uses this order to optimize
> your query.

---

## 💡 Real‑world Usage

**Banking – list accounts with balance over 10,000**
```sql
SELECT account_id, holder, balance
FROM accounts
WHERE balance > 10000;
```

**E‑commerce – show distinct product categories**
```sql
SELECT DISTINCT category FROM products;
```

**Logistics – find shipments to a specific city**
```sql
SELECT tracking_id, status
FROM shipments
WHERE destination = 'Dhaka';
```

**HR – list active employees only**
```sql
SELECT name, department
FROM employees
WHERE status = 'active';
```

---

## 🔍 Practice Preview
You will write `SELECT` queries to project, deduplicate, and filter data
from the Imperial Army’s database.

| Level | Task |
|-------|------|
| Easy | Select all columns from `soldiers`. |
| Medium | Select distinct ranks from `soldiers`. |
| Hard | Select name and rank of all soldiers with rank `'General'`. |

Run the coach:
```bash
python ii_Practice_Sheets/L05_SELECT_Projection_DISTINCT_Basic_Filtering.py
```

---

## 📌 Key Takeaway
- Use explicit column lists, not `*`, for reliable queries.
- `DISTINCT` removes duplicate rows from your result set.
- `WHERE` filters rows before they’re returned – use it to narrow your data.

*For Emperor.*