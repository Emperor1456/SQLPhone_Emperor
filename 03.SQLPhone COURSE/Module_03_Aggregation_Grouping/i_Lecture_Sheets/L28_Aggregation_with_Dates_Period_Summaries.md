# 📘 SQLPhone Emperor v3.0 · Module 3
# 📖 L28 – Aggregation with Dates – Period Summaries

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll summarize data by time periods — daily, monthly, quarterly, yearly — to reveal trends, seasonality, and growth. This is how financial reports, sales dashboards, and analytics platforms turn raw timestamps into actionable insight.

- 🧱 **strftime for periods** – extract year, month, quarter, week
- 🧠 **GROUP BY period** – collapse rows into time buckets
- 🧪 **Running totals & period‑over‑period comparisons**
- ⚡ **Date range filtering** – focus on specific intervals
- 🧰 **Real‑world** – revenue trends, user growth, seasonal analysis

---

## 🧱 GROUPING BY YEAR AND MONTH

Use `strftime` to extract the year‑month string, then group by it.

```sql
SELECT strftime('%Y-%m', order_date) AS month,
       COUNT(*) AS orders,
       SUM(amount) AS revenue
FROM orders
GROUP BY month
ORDER BY month;
```

Each row represents a single month. The result is a clean time series ready for a chart.

---

## 🧱 QUARTERLY SUMMARIES

```sql
SELECT
    strftime('%Y', order_date) AS year,
    CASE
        WHEN CAST(strftime('%m', order_date) AS INTEGER) <= 3 THEN 'Q1'
        WHEN CAST(strftime('%m', order_date) AS INTEGER) <= 6 THEN 'Q2'
        WHEN CAST(strftime('%m', order_date) AS INTEGER) <= 9 THEN 'Q3'
        ELSE 'Q4'
    END AS quarter,
    SUM(amount) AS revenue
FROM orders
GROUP BY year, quarter
ORDER BY year, quarter;
```

The `CASE` maps month numbers to quarters. This is the standard technique for quarterly board reports.

---

## 🧱 DAILY ROLLING AVERAGES

```sql
SELECT date(order_date) AS day,
       SUM(amount) AS daily_total,
       AVG(SUM(amount)) OVER (ORDER BY date(order_date) ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS seven_day_avg
FROM orders
GROUP BY day
ORDER BY day;
```

Window functions (available in SQLite 3.25+) let you compute moving averages without subqueries.

---

## 🧱 PERIOD‑OVER‑PERIOD GROWTH

```sql
WITH monthly AS (
    SELECT strftime('%Y-%m', order_date) AS month,
           SUM(amount) AS revenue
    FROM orders
    GROUP BY month
)
SELECT month,
       revenue,
       LAG(revenue) OVER (ORDER BY month) AS prev_month,
       ROUND((revenue - LAG(revenue) OVER (ORDER BY month)) * 100.0 / LAG(revenue) OVER (ORDER BY month), 2) AS growth_pct
FROM monthly;
```

`LAG` reaches back to the previous row. The result shows month‑over‑month growth percentage.

---

## 🧱 WEEK‑OVER‑WEEK COMPARISON

```sql
SELECT strftime('%Y-%W', order_date) AS week,
       COUNT(*) AS orders
FROM orders
GROUP BY week
ORDER BY week;
```

`%W` returns the week number (00‑53). Combine with `%Y` for unique year‑week identifiers.

---

> 💡 **INSIGHT:** Always include the year when grouping by month or week. `strftime('%m')` without `%Y` will combine January 2025 with January 2026 — a classic data bug.

> ⚠️ **WARNING:** `strftime` returns strings, not numbers. When comparing periods, use string comparison (`'2026-01' < '2026-06'`) which works lexicographically, or cast to integers for arithmetic.

---

## 💡 Real‑world Usage

**Banking – monthly transaction volume**
```sql
SELECT strftime('%Y-%m', transaction_date) AS month,
       COUNT(*) AS count,
       SUM(amount) AS volume
FROM transactions
GROUP BY month;
```

**E‑commerce – daily sales trend**
```sql
SELECT date(order_date) AS day,
       SUM(quantity * unit_price) AS daily_revenue
FROM orders
JOIN order_items ON orders.id = order_items.order_id
GROUP BY day
ORDER BY day;
```

**Logistics – weekly shipment counts**
```sql
SELECT strftime('%Y-%W', dispatch_date) AS week,
       COUNT(*) AS shipments
FROM shipments
GROUP BY week;
```

**HR – hires per quarter**
```sql
SELECT strftime('%Y', hire_date) AS year,
       (CAST(strftime('%m', hire_date) AS INTEGER) + 2) / 3 AS quarter,
       COUNT(*) AS hires
FROM employees
GROUP BY year, quarter;
```

**Companion – memories created per day**
```sql
SELECT date(created_at) AS day,
       COUNT(*) AS new_memories
FROM memories
WHERE user_id = 1
GROUP BY day;
```

---

## 🔍 Practice Preview
You will create time‑based summary reports for the Imperial Army.

| Level | Task |
|-------|------|
| Easy | Group soldiers by their join year and count them. |
| Medium | Group soldiers by join year and month, showing the count per month. |
| Hard | For each quarter of each year, show the number of soldiers who joined and the average salary of those soldiers. |

Run the coach:
```bash
python ii_Practice_Sheets/L28_Aggregation_with_Dates_Period_Summaries.py
```

---

## 📌 Key Takeaway
- `strftime` extracts date parts for grouping.
- Group by year, month, quarter, or week for trend analysis.
- Combine with window functions for moving averages and period‑over‑period growth.
- Always include the year in period labels to avoid mixing data across years.

*For Emperor.*