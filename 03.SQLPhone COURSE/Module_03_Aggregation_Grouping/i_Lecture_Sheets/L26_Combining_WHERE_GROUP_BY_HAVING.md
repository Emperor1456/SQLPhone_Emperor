# 📘 SQLPhone Emperor v3.0 · Module 3
# 📖 L26 – Combining WHERE, GROUP BY & HAVING

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll chain row filters, grouping, and group filters into a single, powerful query pipeline. This is the complete data analysis workflow — the exact pattern used in every business intelligence report.

- 🧱 **Full pipeline** – WHERE → GROUP BY → HAVING → SELECT → ORDER BY
- 🧠 **Logical order vs written order** – why it matters
- 🧪 **Real‑world reports** – multi‑step data analysis
- ⚡ **Debugging tips** – when your results don’t match expectations
- 🛡️ **The complete mental model** – every clause has a specific job

---

## 🧱 THE COMPLETE QUERY STRUCTURE

The logical execution order of a `SELECT` statement is **not** the order you write it. Understanding this sequence is the key to debugging any query.

```
1. FROM / JOIN   – gather raw data
2. WHERE         – filter rows
3. GROUP BY      – form groups
4. HAVING        – filter groups
5. SELECT        – compute output columns
6. ORDER BY      – sort results
7. LIMIT/OFFSET  – paginate
```

You write `SELECT` first, but it executes near the end. This is why you can’t use column aliases in `WHERE` — the alias doesn’t exist yet.

---

## 🧱 FULL PIPELINE EXAMPLE

```sql
SELECT rank,
       COUNT(*) AS soldier_count,
       AVG(salary) AS avg_sal
FROM soldiers
WHERE status = 'active'
GROUP BY rank
HAVING COUNT(*) > 2
ORDER BY avg_sal DESC;
```

**Step‑by‑step execution:**
1. `FROM soldiers` — start with all rows in the table.
2. `WHERE status = 'active'` — discard inactive soldiers.
3. `GROUP BY rank` — organize remaining soldiers into rank buckets.
4. `HAVING COUNT(*) > 2` — discard ranks with 2 or fewer soldiers.
5. `SELECT rank, COUNT(*), AVG(salary)` — compute the output columns.
6. `ORDER BY avg_sal DESC` — sort the results by average salary, highest first.

---

## 🧱 ANOTHER REAL‑WORLD EXAMPLE

```sql
SELECT category,
       COUNT(*) AS product_count,
       AVG(price) AS avg_price
FROM products
WHERE stock > 0
GROUP BY category
HAVING AVG(price) < 100
ORDER BY product_count DESC;
```

1. Only in‑stock products.
2. Group by category.
3. Only categories with average price under $100.
4. Show category, count, and average price, sorted by most products first.

---

## 🧱 DEBUGGING WHEN RESULTS DON’T MATCH EXPECTATIONS

| Symptom | Likely cause |
|---------|--------------|
| Rows are missing | `WHERE` or `HAVING` is too strict — test each clause separately |
| Wrong aggregate values | `WHERE` is filtering rows you meant to include — check the order |
| Duplicate rows in output | You may need `DISTINCT` or a different `GROUP BY` |
| Column not found error | You used an alias in `WHERE` — use the original expression instead |

> 💡 **INSIGHT:** Always build complex queries step by step. Start with just `FROM` + `WHERE`. Check row counts. Add `GROUP BY`. Check group counts. Add `HAVING`. Only then add `SELECT` and `ORDER BY`. This incremental approach catches errors immediately.

> ⚠️ **WARNING:** `HAVING` without `GROUP BY` treats the entire result as a single group. This is valid SQL but rarely what you intend — it’s a common beginner mistake.

---

## 💡 Real‑world Usage

**Banking – high‑value customer segments**
```sql
SELECT customer_id, COUNT(*) AS txns, SUM(amount) AS total
FROM transactions
WHERE date >= '2026-01-01'
GROUP BY customer_id
HAVING SUM(amount) > 50000
ORDER BY total DESC;
```

**E‑commerce – underperforming product categories**
```sql
SELECT category, AVG(price) AS avg_price, COUNT(*) AS products
FROM products
WHERE stock > 0
GROUP BY category
HAVING COUNT(*) < 5
ORDER BY avg_price ASC;
```

**Logistics – problematic delivery routes**
```sql
SELECT route, COUNT(*) AS delays
FROM shipments
WHERE status = 'delayed'
GROUP BY route
HAVING COUNT(*) > 3;
```

**HR – departments with senior staff shortage**
```sql
SELECT department, COUNT(*) AS senior_count
FROM employees
WHERE tenure >= 5
GROUP BY department
HAVING COUNT(*) < 2;
```

---

## 🔍 Practice Preview
You will build full‑pipeline queries against the Imperial Army database.

| Level | Task |
|-------|------|
| Easy | Group active soldiers by rank, showing count per group. |
| Medium | Add a `HAVING` clause to show only ranks with more than 2 active soldiers, sorted by count. |
| Hard | Filter soldiers with salary > 3000, group by deployment region, and show only regions where total salary exceeds 10000. |

Run the coach:
```bash
python ii_Practice_Sheets/L26_Combining_WHERE_GROUP_BY_HAVING.py
```

---

## 📌 Key Takeaway
- The full pipeline filters rows, groups them, filters groups, then selects output.
- Logical execution order differs from written order.
- `WHERE` filters rows, `HAVING` filters groups — they work at different stages.
- Build complex queries incrementally: WHERE → GROUP BY → HAVING → SELECT → ORDER BY.

*For Emperor.*