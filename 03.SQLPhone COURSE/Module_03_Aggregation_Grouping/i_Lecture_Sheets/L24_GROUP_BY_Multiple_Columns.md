# 📘 SQLPhone Emperor v3.0 · Module 3
# 📖 L24 – GROUP BY – Multiple Columns

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll create multi‑level summaries — breaking down data by two or more dimensions simultaneously. This is how you answer questions like “total sales per region per product category” in a single query.

- 🧱 **Multi‑column GROUP BY** – create hierarchical summaries
- 🧠 **Column order matters** – groups are nested
- 🧪 **Combining with aggregates** – deeper insights
- ⚡ **Practical use** – sales by region and product, logs by date and user
- 🛡️ **The cardinal rule** – every non‑aggregate column must be in GROUP BY

---

## 🧱 GROUPING BY TWO COLUMNS

When you list multiple columns in `GROUP BY`, the groups are formed by unique **combinations** of those columns.

```sql
SELECT rank, status, COUNT(*) AS count
FROM soldiers
GROUP BY rank, status;
```

This returns one row for every existing combination of `rank` and `status` — for example, “active Generals,” “reserve Privates,” etc.

---

## 🧱 NESTED GROUPS

The order of columns defines the hierarchy. The first column is the outer group; the second is the inner subgroup.

```sql
SELECT department, city, COUNT(*) AS staff
FROM employees
GROUP BY department, city
ORDER BY department, city;
```

Think of it as: “for each department, break down by city.” The result is a tree flattened into a table.

---

## 🧱 REAL‑WORLD EXAMPLE – SALES DASHBOARD

```sql
SELECT
    strftime('%Y-%m', order_date) AS month,
    category,
    SUM(quantity * unit_price) AS revenue,
    COUNT(*) AS orders
FROM orders
JOIN order_items ON orders.id = order_items.order_id
JOIN products ON order_items.product_id = products.id
GROUP BY month, category
ORDER BY month, revenue DESC;
```

One query replaces an entire spreadsheet. Each row shows revenue and order count for a specific category in a specific month.

---

## 🧱 THE CARDINAL RULE (MULTI‑COLUMN)

Every non‑aggregate column in `SELECT` must be in `GROUP BY`. With multiple columns, this applies to all of them.

```sql
-- WRONG: city is in SELECT but not in GROUP BY
SELECT department, city, COUNT(*) FROM employees GROUP BY department;

-- RIGHT: both non‑aggregate columns are in GROUP BY
SELECT department, city, COUNT(*) FROM employees GROUP BY department, city;
```

> 💡 **INSIGHT:** The order of columns in `GROUP BY` is purely about grouping hierarchy — it doesn’t affect correctness, only how the result is organized. But the order of columns in `SELECT` should follow the same hierarchy for readability.

> ⚠️ **WARNING:** When grouping by multiple columns, `COUNT(*)` counts rows in each unique combination. If a combination doesn’t exist, it simply doesn’t appear. Use `LEFT JOIN` and `COALESCE` (from L33) if you need to show zero‑count combinations.

---

## 💡 Real‑world Usage

**Banking – transactions by type and branch**
```sql
SELECT transaction_type, branch, COUNT(*) AS volume, SUM(amount) AS total
FROM transactions
GROUP BY transaction_type, branch;
```

**E‑commerce – orders by category and month**
```sql
SELECT category, strftime('%Y-%m', order_date) AS month, COUNT(*) AS orders
FROM orders
JOIN products ON orders.product_id = products.id
GROUP BY category, month;
```

**Logistics – shipments by carrier and status**
```sql
SELECT carrier, status, COUNT(*) AS count
FROM shipments
GROUP BY carrier, status;
```

**HR – employees by department and job title**
```sql
SELECT department, job_title, AVG(salary) AS avg_salary
FROM employees
GROUP BY department, job_title;
```

**Companion – memories by user and category**
```sql
SELECT user_id, category, COUNT(*) AS count
FROM memories
GROUP BY user_id, category;
```

---

## 🔍 Practice Preview
You will create multi‑level summaries of the Imperial Army.

| Level | Task |
|-------|------|
| Easy | Group soldiers by rank and status, counting each combination. |
| Medium | Group by rank and deployment, then show average salary per group. |
| Hard | Group soldiers by the first letter of their name and their rank, counting each subgroup. |

Run the coach:
```bash
python ii_Practice_Sheets/L24_GROUP_BY_Multiple_Columns.py
```

---

## 📌 Key Takeaway
- Multi‑column `GROUP BY` creates hierarchical group combinations.
- Column order defines the nesting structure — outer group first, inner group second.
- Combine with multiple aggregates for complete subgroup reports.
- Every non‑aggregate column in `SELECT` must appear in `GROUP BY`.

*For Emperor.*