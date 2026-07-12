# 📘 SQLPhone Emperor v3.0 · Module 2
# 📖 L16 – CASE in Clauses – Sorting, Grouping, Filtering

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll use `CASE` to control the flow of entire queries — not just individual values. Sort by custom rules, group by dynamic categories, and even filter with conditional logic.

- 📊 **CASE in ORDER BY** – custom sort sequences
- 📋 **CASE in GROUP BY** – create dynamic grouping categories
- 🧪 **CASE in WHERE** – conditional filtering logic
- ⚡ **Combining CASE with aggregates** – build complex summaries
- 🛡️ **Real‑world** – priority queues, dynamic dashboards, business rule engines

---

## 🧱 CASE IN ORDER BY – CUSTOM SORTING

Sometimes alphabetical or numeric order isn’t enough. You need a business‑defined sequence — for example, sorting shipments by priority: “High”, “Medium”, “Low”.

```sql
SELECT name, rank
FROM soldiers
ORDER BY
    CASE rank
        WHEN 'General' THEN 1
        WHEN 'Colonel' THEN 2
        WHEN 'Major' THEN 3
        ELSE 4
    END;
```

**Multi‑level custom sort:**
```sql
SELECT name, status, priority
FROM shipments
ORDER BY
    CASE priority WHEN 'High' THEN 1 WHEN 'Medium' THEN 2 ELSE 3 END,
    CASE status WHEN 'delayed' THEN 1 WHEN 'pending' THEN 2 ELSE 3 END;
```

---

## 🧱 CASE IN GROUP BY – DYNAMIC CATEGORIES

You can group data by the output of a `CASE` expression. This lets you aggregate on calculated categories without creating a separate table.

```sql
SELECT
    CASE
        WHEN salary >= 5000 THEN 'High Earners'
        WHEN salary >= 3000 THEN 'Mid Earners'
        ELSE 'Low Earners'
    END AS pay_group,
    COUNT(*) AS count,
    AVG(salary) AS avg_sal
FROM soldiers
GROUP BY pay_group;
```

**Sales by quarter:**
```sql
SELECT
    CASE
        WHEN strftime('%m', sale_date) IN ('01','02','03') THEN 'Q1'
        WHEN strftime('%m', sale_date) IN ('04','05','06') THEN 'Q2'
        WHEN strftime('%m', sale_date) IN ('07','08','09') THEN 'Q3'
        ELSE 'Q4'
    END AS quarter,
    SUM(amount) AS total_sales
FROM transactions
GROUP BY quarter;
```

---

## 🧱 CASE IN WHERE – CONDITIONAL FILTERING

Although less common, you can place `CASE` inside `WHERE` to create dynamic filter logic. The `CASE` must return a value that can be compared.

```sql
SELECT * FROM soldiers
WHERE CASE
    WHEN rank = 'General' THEN salary > 4000
    ELSE salary > 2000
END;
```

> ⚠️ **WARNING:** Complex `CASE` inside `WHERE` can be hard to read. Often a combination of `AND`/`OR` is clearer for pure filtering. Reserve this pattern for situations where the logic truly depends on row values.

---

## 🧱 CASE WITH AGGREGATES – CONDITIONAL SUMMARIES

Combine `CASE` with aggregate functions for powerful summaries:

```sql
SELECT
    regiment_id,
    COUNT(*) AS total,
    SUM(CASE WHEN status = 'active' THEN 1 ELSE 0 END) AS active_count,
    SUM(CASE WHEN salary > 4000 THEN salary ELSE 0 END) AS high_salary_payroll
FROM soldiers
GROUP BY regiment_id;
```

> 💡 **INSIGHT:** `CASE` inside `GROUP BY` lets you collapse continuous values into meaningful bands — salaries into pay grades, ages into generations, distances into zones. This is the foundation of cohort analysis and segmentation.

---

## 💡 Real‑world Usage

**Banking – categorize and count accounts**
```sql
SELECT
    CASE
        WHEN balance >= 100000 THEN 'VIP'
        WHEN balance >= 10000 THEN 'Standard'
        ELSE 'Basic'
    END AS tier,
    COUNT(*) AS customers
FROM accounts
GROUP BY tier;
```

**E‑commerce – sort products by seasonal relevance**
```sql
SELECT name, season FROM products
ORDER BY CASE season
    WHEN 'Spring' THEN 1 WHEN 'Summer' THEN 2
    WHEN 'Fall' THEN 3 ELSE 4 END;
```

**Logistics – group shipments by urgency**
```sql
SELECT
    CASE
        WHEN priority = 'High' AND status = 'delayed' THEN 'Critical'
        ELSE 'Routine'
    END AS urgency,
    COUNT(*) AS count
FROM shipments
GROUP BY urgency;
```

**HR – custom department hierarchy**
```sql
SELECT department, COUNT(*) AS headcount
FROM employees
GROUP BY department
ORDER BY CASE department
    WHEN 'Engineering' THEN 1 WHEN 'Sales' THEN 2 ELSE 3 END;
```

---

## 🔍 Practice Preview
You will embed `CASE` in multiple query clauses to control sorting, grouping, and filtering.

| Level | Task |
|-------|------|
| Easy | Sort soldiers by rank priority using `CASE` in `ORDER BY`. |
| Medium | Group soldiers into pay bands using `CASE` in `GROUP BY` and count each group. |
| Hard | Filter soldiers where the condition depends on rank (use `CASE` in `WHERE`). |

Run the coach:
```bash
python ii_Practice_Sheets/L16_CASE_in_Clauses_Sorting_Grouping_Filtering.py
```

---

## 📌 Key Takeaway
- `CASE` controls sorting, grouping, and filtering logic dynamically.
- Custom sort orders are easy with `CASE` inside `ORDER BY`.
- Grouping on computed categories lets you summarize data on the fly.
- Use `CASE` in `WHERE` sparingly — prefer `AND`/`OR` for simpler conditions.

*For Emperor.*