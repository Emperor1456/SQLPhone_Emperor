# 📘 SQLPhone Emperor v3.0 · Module 3
# 📖 L23 – GROUP BY – Single Column

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll collapse rows into groups and run aggregates per group — the foundation of every summary report. From “how many soldiers per rank?” to “total payroll per regiment,” GROUP BY is the engine behind every dashboard.

- 🧱 **GROUP BY** – collapse rows by a column
- 🔢 **Aggregates per group** – COUNT, SUM, AVG, MAX, MIN
- 🧠 **Execution order** – FROM → WHERE → GROUP BY → SELECT
- 🧪 **GROUP BY on expressions** – grouping by calculated values
- ⚡ **The cardinal rule** – every non‑aggregate column must be in GROUP BY

---

## 🧱 THE GROUP BY CLAUSE

`GROUP BY` splits the table into buckets — one bucket for each unique value in the specified column. Aggregate functions then operate on each bucket independently.

```sql
SELECT rank, COUNT(*) AS count
FROM soldiers
GROUP BY rank;
```

This returns one row per unique `rank`, with a count of soldiers in each.

---

## 🧱 MULTIPLE AGGREGATES PER GROUP

You can apply as many aggregates as you need in a single `GROUP BY` query.

```sql
SELECT rank,
       COUNT(*) AS soldiers,
       AVG(salary) AS avg_salary,
       MAX(salary) AS top_salary,
       MIN(salary) AS low_salary
FROM soldiers
GROUP BY rank;
```

One query, one row per rank, five metrics. This is a complete personnel summary.

---

## 🧱 THE CARDINAL RULE OF GROUP BY

Every column in the `SELECT` list must either be:
1. In the `GROUP BY` clause, or
2. Wrapped in an aggregate function.

```sql
-- WRONG: name is neither in GROUP BY nor an aggregate
SELECT name, rank, COUNT(*) FROM soldiers GROUP BY rank;

-- RIGHT: rank is in GROUP BY, the rest are aggregates
SELECT rank, COUNT(*) AS soldiers, AVG(salary) AS avg_pay FROM soldiers GROUP BY rank;
```

If you violate this rule, SQLite returns an arbitrary value from the group — a silent bug that corrupts your results.

---

## 🧱 GROUPING BY EXPRESSIONS

You can group by a calculated value:

```sql
-- Group soldiers by the first letter of their name
SELECT SUBSTR(name, 1, 1) AS first_letter,
       COUNT(*) AS count
FROM soldiers
GROUP BY SUBSTR(name, 1, 1)
ORDER BY first_letter;
```

This returns how many soldiers have names starting with each letter.

---

## 🧱 GROUP BY WITH WHERE

Filter rows before grouping with `WHERE`:

```sql
SELECT regiment_id, COUNT(*) AS active_soldiers
FROM soldiers
WHERE status = 'active'
GROUP BY regiment_id;
```

The `WHERE` clause runs first, filtering out inactive soldiers. Then `GROUP BY` collapses the remaining rows.

> 💡 **INSIGHT:** `GROUP BY` is the bridge between raw data and actionable reports. Every “total by category,” “average by department,” or “count by status” report uses it.

> ⚠️ **WARNING:** The order of columns in `GROUP BY` doesn’t matter for a single column, but it will matter when you use multiple columns (L24).

---

## 💡 Real‑world Usage

**Banking – count accounts by status**
```sql
SELECT status, COUNT(*) AS accounts
FROM accounts
GROUP BY status;
```

**E‑commerce – total sales per category**
```sql
SELECT category, SUM(quantity * unit_price) AS revenue
FROM products
JOIN order_items ON products.id = order_items.product_id
GROUP BY category;
```

**Logistics – shipments per destination**
```sql
SELECT destination, COUNT(*) AS total_shipments
FROM shipments
GROUP BY destination;
```

**HR – employees per department**
```sql
SELECT department, COUNT(*) AS headcount
FROM employees
GROUP BY department;
```

**Companion – memories per user**
```sql
SELECT user_id, COUNT(*) AS memory_count
FROM memories
GROUP BY user_id;
```

---

## 🔍 Practice Preview
You will summarize the Imperial Army by grouping on a single column.

| Level | Task |
|-------|------|
| Easy | Count soldiers per rank using `GROUP BY rank`. |
| Medium | For each rank, show the average salary alongside the count. |
| Hard | Group by an expression: extract the first letter of the name and count how many soldiers start with each letter. |

Run the coach:
```bash
python ii_Practice_Sheets/L23_GROUP_BY_Single_Column.py
```

---

## 📌 Key Takeaway
- `GROUP BY` collapses rows into groups for aggregate calculations.
- Every non‑aggregate column must appear in `GROUP BY`.
- Use multiple aggregates to get a complete picture of each group.
- `WHERE` filters rows before grouping; `HAVING` (L25) filters groups after.

*For Emperor.*