# 📘 SQLPhone Emperor v3.0 · Module 3
# 📖 L21 – COUNT, SUM, AVG – Basic Aggregates

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll summarize massive datasets with a single line of SQL — the heart of every business dashboard. From “how many soldiers?” to “total payroll” to “average salary,” you’ll produce instant answers.

- 🔢 **COUNT** – count rows or non‑NULL values
- ➕ **SUM** – total a numeric column
- 📊 **AVG** – average of a numeric column
- 🧪 **Combining them** – multiple aggregates in one query
- ⚡ **NULL handling** – how aggregates ignore NULL
- 🧰 **DISTINCT with aggregates** – count unique values

---

## 🧱 THE THREE MUSKETEERS OF AGGREGATION

SQL aggregates collapse many rows into a single summary value. They’re the first thing an executive asks for.

| Function | What it does | Example |
|----------|--------------|---------|
| `COUNT(*)` | Count all rows | `SELECT COUNT(*) FROM soldiers;` |
| `COUNT(column)` | Count non‑NULL values | `SELECT COUNT(rank) FROM soldiers;` |
| `SUM(column)` | Sum of all values | `SELECT SUM(salary) FROM soldiers;` |
| `AVG(column)` | Average of all values | `SELECT AVG(salary) FROM soldiers;` |

```sql
-- Total payroll and average salary
SELECT
    COUNT(*) AS total_soldiers,
    SUM(salary) AS total_payroll,
    AVG(salary) AS average_salary
FROM soldiers;
```

---

## 🧱 NULL BEHAVIOR

All aggregates except `COUNT(*)` ignore NULL values. This can lead to surprises if you’re not aware.

```sql
-- If some soldiers have NULL salary, they are excluded from SUM and AVG
SELECT
    COUNT(*) AS all_rows,
    COUNT(salary) AS counted_salaries,
    SUM(salary) AS total,
    AVG(salary) AS average
FROM soldiers;
```

`COUNT(*)` counts every row. `COUNT(salary)` counts only rows where salary is not NULL. If those numbers differ, you have missing data.

---

## 🧱 DISTINCT WITH AGGREGATES

`COUNT(DISTINCT column)` counts unique non‑NULL values — perfect for finding the number of unique ranks or regiments.

```sql
-- How many unique ranks exist?
SELECT COUNT(DISTINCT rank) AS unique_ranks FROM soldiers;

-- How many unique regiments have soldiers?
SELECT COUNT(DISTINCT regiment_id) AS active_regiments FROM soldiers;
```

---

## 🧱 AGGREGATES WITH WHERE

Filter rows before aggregating to focus on specific groups:

```sql
-- Total payroll for active soldiers only
SELECT SUM(salary) AS active_payroll
FROM soldiers
WHERE status = 'active';

-- Average salary of Generals
SELECT AVG(salary) AS general_avg
FROM soldiers
WHERE rank = 'General';
```

> ⚠️ **WARNING:** `AVG` returns NULL if all values in the group are NULL. Use `COALESCE(AVG(salary), 0)` to default to zero in reports.

> 💡 **INSIGHT:** These three functions — COUNT, SUM, AVG — power every dashboard on Earth. They’re simple, but they’re the first thing a CEO or general asks for. Master them completely.

---

## 💡 Real‑world Usage

**Banking – daily transaction summary**
```sql
SELECT
    COUNT(*) AS txn_count,
    SUM(amount) AS total_volume,
    AVG(amount) AS avg_txn
FROM transactions
WHERE date(transaction_date) = date('now');
```

**E‑commerce – product statistics**
```sql
SELECT
    COUNT(*) AS product_count,
    AVG(price) AS avg_price,
    SUM(stock) AS total_inventory
FROM products;
```

**Logistics – shipment weight analysis**
```sql
SELECT
    COUNT(*) AS shipments,
    SUM(weight_kg) AS total_weight,
    AVG(weight_kg) AS avg_weight
FROM shipments;
```

**HR – employee salary report**
```sql
SELECT
    COUNT(*) AS employees,
    SUM(salary) AS payroll,
    AVG(salary) AS avg_salary
FROM employees
WHERE status = 'active';
```

**Companion – memory statistics**
```sql
SELECT
    COUNT(*) AS total_memories,
    AVG(LENGTH(content)) AS avg_length
FROM memories
WHERE user_id = 1;
```

---

## 🔍 Practice Preview
You will summarize the Imperial Army's data with aggregate functions.

| Level | Task |
|-------|------|
| Easy | Count the total number of soldiers. |
| Medium | Calculate the total payroll (SUM of salary). |
| Hard | Compute the average salary of soldiers who have a rank assigned (non‑NULL), alongside the count of distinct ranks. |

Run the coach:
```bash
python ii_Practice_Sheets/L21_COUNT_SUM_AVG_Basic_Aggregates.py
```

---

## 📌 Key Takeaway
- `COUNT`, `SUM`, `AVG` summarize rows into single values.
- `COUNT(*)` counts all rows; `COUNT(column)` counts non‑NULL.
- Aggregates ignore NULLs — plan accordingly.
- `COUNT(DISTINCT column)` counts unique values.
- These three functions power every dashboard on Earth.

*For Emperor.*