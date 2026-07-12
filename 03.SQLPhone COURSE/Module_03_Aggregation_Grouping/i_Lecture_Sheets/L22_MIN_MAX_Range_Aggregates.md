# 📘 SQLPhone Emperor v3.0 · Module 3
# 📖 L22 – MIN, MAX – Range Aggregates

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll find the extremes in your data — the highest, the lowest, and the span between them. These are the metrics that define boundaries: top performer, earliest date, smallest shipment.

- 📈 **MAX** – largest value in a column
- 📉 **MIN** – smallest value in a column
- 🧪 **Combining with GROUP BY** (preview)
- ⚡ **Practical use** – salary ranges, date ranges, stock limits
- 🧰 **MIN/MAX on text and dates** – alphabetical order and chronology

---

## 🧱 MAX AND MIN BASICS

`MAX` and `MIN` work on numbers, text, and dates. They return the single largest or smallest value in that column.

```sql
-- Highest and lowest salary
SELECT MAX(salary) AS highest_salary,
       MIN(salary) AS lowest_salary
FROM soldiers;
```

For text columns, `MAX` returns the lexicographically largest (alphabetically last) value, and `MIN` the smallest (alphabetically first).

```sql
SELECT MAX(name) AS last_name_alphabetically FROM soldiers;
```

For dates, `MAX` gives the most recent date, `MIN` the earliest.

```sql
SELECT MIN(join_date) AS first_joined,
       MAX(join_date) AS last_joined
FROM soldiers;
```

---

## 🧱 RANGE CALCULATION

The spread of data is simply `MAX - MIN`.

```sql
SELECT MAX(salary) - MIN(salary) AS salary_range
FROM soldiers;
```

This tells you the gap between the highest and lowest paid soldier — a single number that summarizes pay inequality across the entire army.

---

## 🧱 MIN/MAX WITH FILTERING

Combine with `WHERE` to find extremes within a subset:

```sql
-- Highest salary among Privates
SELECT MAX(salary) AS top_private_salary
FROM soldiers
WHERE rank = 'Private';
```

---

## 🧱 MIN/MAX ON CALCULATED VALUES

```sql
-- Most valuable inventory item (price × stock)
SELECT MAX(unit_price * quantity) AS max_inventory_value
FROM inventory;
```

> 💡 **INSIGHT:** `MIN` and `MAX` work on any expression, not just raw columns. You can compute a value and immediately find its extreme.

> ⚠️ **WARNING:** If all values in the column are NULL, `MAX` and `MIN` return NULL. Use `COALESCE(MAX(salary), 0)` to default to zero in reports where NULL is misleading.

---

## 💡 Real‑world Usage

**Banking – largest and smallest transaction today**
```sql
SELECT MAX(amount) AS largest, MIN(amount) AS smallest
FROM transactions
WHERE date(transaction_date) = date('now');
```

**E‑commerce – most and least expensive products**
```sql
SELECT MAX(price) AS most_expensive, MIN(price) AS cheapest
FROM products;
```

**Logistics – earliest and latest shipment**
```sql
SELECT MIN(dispatch_date) AS first_dispatched,
       MAX(dispatch_date) AS last_dispatched
FROM shipments;
```

**HR – highest and lowest salary by department (GROUP BY preview)**
```sql
SELECT department,
       MAX(salary) AS top_salary,
       MIN(salary) AS bottom_salary
FROM employees
GROUP BY department;
```

**Companion – first and last memory timestamp**
```sql
SELECT MIN(created_at) AS oldest_memory,
       MAX(created_at) AS newest_memory
FROM memories
WHERE user_id = 1;
```

---

## 🔍 Practice Preview
You will find the extremes in the Imperial Army’s data.

| Level | Task |
|-------|------|
| Easy | Find the highest salary among all soldiers. |
| Medium | Find the earliest and latest join dates. |
| Hard | Calculate the salary range (max − min) for soldiers who have a rank assigned. |

Run the coach:
```bash
python ii_Practice_Sheets/L22_MIN_MAX_Range_Aggregates.py
```

---

## 📌 Key Takeaway
- `MAX` and `MIN` find extremes in numeric, text, and date columns.
- The range `MAX - MIN` gives the spread.
- They work seamlessly with `WHERE` and `GROUP BY`.
- Use `COALESCE` when NULL values could distort a report.

*For Emperor.*