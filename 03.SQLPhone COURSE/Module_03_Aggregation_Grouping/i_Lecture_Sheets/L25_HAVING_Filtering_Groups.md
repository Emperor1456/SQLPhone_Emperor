# 📘 SQLPhone Emperor v3.0 · Module 3
# 📖 L25 – HAVING – Filtering Groups

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll filter aggregate results — keeping only the groups that matter. This is how you go from “all departments” to “departments with payroll over 50,000” or “regiments with more than 100 soldiers.”

- 🧱 **HAVING** – filter groups after aggregation
- 🧠 **WHERE vs HAVING** – row‑level vs group‑level filtering
- 🧪 **Complex HAVING conditions** – multi‑aggregate filters
- ⚡ **Execution order** – WHERE → GROUP BY → HAVING
- 🛡️ **Real‑world** – identifying top performers, underperforming segments, critical thresholds

---

## 🧱 HAVING – THE GROUP FILTER

`WHERE` filters individual rows before aggregation; `HAVING` filters the aggregated groups after `GROUP BY`.

```sql
SELECT rank, COUNT(*) AS count
FROM soldiers
GROUP BY rank
HAVING COUNT(*) > 5;
```

Only ranks that have more than 5 soldiers are returned. Ranks with 5 or fewer soldiers are excluded from the result entirely.

---

## 🧱 WHERE VS HAVING

| Clause | Filters | Applied |
|--------|---------|---------|
| `WHERE` | Individual rows | Before `GROUP BY` |
| `HAVING` | Aggregated groups | After `GROUP BY` |

```sql
-- WHERE filters rows first, HAVING filters the resulting groups
SELECT rank, AVG(salary) AS avg_salary
FROM soldiers
WHERE status = 'active'          -- only active soldiers
GROUP BY rank
HAVING AVG(salary) > 3000;       -- only ranks with high average pay
```

Step by step: (1) inactive soldiers are removed by `WHERE`, (2) remaining soldiers are grouped by rank, (3) each group’s average salary is calculated, (4) groups with average ≤ 3000 are removed by `HAVING`.

---

## 🧱 HAVING WITH MULTIPLE CONDITIONS

You can combine conditions with `AND`/`OR`, just like in `WHERE`.

```sql
SELECT regiment_id,
       COUNT(*) AS soldiers,
       AVG(salary) AS avg_sal
FROM soldiers
GROUP BY regiment_id
HAVING COUNT(*) >= 10
   AND AVG(salary) > 3500;
```

Only regiments that meet both thresholds — size and pay — appear.

---

## 🧱 HAVING VS WHERE – THE MENTAL MODEL

| If you want to filter… | Use… | Example |
|------------------------|------|---------|
| Individual rows before grouping | `WHERE` | Only active soldiers |
| Groups after aggregation | `HAVING` | Regiments with count > 10 |
| Both | `WHERE` + `HAVING` | Active soldiers → regiments with avg > 3000 |

> ⚠️ **WARNING:** You cannot use aggregate functions in `WHERE`. `WHERE AVG(salary) > 3000` is a syntax error. Aggregates must go in `HAVING`.

> 💡 **INSIGHT:** `HAVING` is named confusingly — it sounds like “having a condition,” but it specifically means “filtering groups after aggregation.” Think of it as “the WHERE clause for groups.”

---

## 💡 Real‑world Usage

**Banking – accounts with total transactions above threshold**
```sql
SELECT account_id, SUM(amount) AS total
FROM transactions
GROUP BY account_id
HAVING SUM(amount) > 100000;
```

**E‑commerce – categories with more than 50 orders**
```sql
SELECT category, COUNT(*) AS orders
FROM orders
JOIN products ON orders.product_id = products.id
GROUP BY category
HAVING COUNT(*) > 50;
```

**Logistics – destinations with at least 10 delayed shipments**
```sql
SELECT destination, COUNT(*) AS delayed
FROM shipments
WHERE status = 'delayed'
GROUP BY destination
HAVING COUNT(*) >= 10;
```

**HR – departments with average salary below 5000**
```sql
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) < 5000;
```

**Companion – users with more than 100 memories**
```sql
SELECT user_id, COUNT(*) AS memory_count
FROM memories
GROUP BY user_id
HAVING COUNT(*) > 100;
```

---

## 🔍 Practice Preview
You will filter aggregated groups in the Imperial Army.

| Level | Task |
|-------|------|
| Easy | Group soldiers by rank, show only ranks with more than 3 soldiers. |
| Medium | For active soldiers only, group by rank and show those with average salary above 4000. |
| Hard | Group by deployment region, and show only regions where the total salary exceeds 20000. |

Run the coach:
```bash
python ii_Practice_Sheets/L25_HAVING_Filtering_Groups.py
```

---

## 📌 Key Takeaway
- `HAVING` filters groups after aggregation, just as `WHERE` filters rows before.
- Combine `WHERE` and `HAVING` for precise data slicing.
- Execution order: WHERE → GROUP BY → HAVING → SELECT → ORDER BY.
- Aggregate functions (`SUM`, `AVG`, `COUNT`, etc.) belong in `HAVING`, never in `WHERE`.

*For Emperor.*