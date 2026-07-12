# 📘 SQLPhone Emperor v3.0 · Module 3
# 📖 L30 – Module 3 Capstone: Monthly Revenue Reports

---

## 🎯 OBJECTIVE — What You Will Master

> Produce a professional‑grade monthly revenue report, integrating every Module‑3 concept — the kind you’d present to a CEO, board of directors, or army General. This capstone proves you can turn raw data into executive decisions.

- 🧱 **Complete business scenario** – sales across multiple regions and categories
- 🧠 **Full aggregation pipeline** – WHERE, GROUP BY, HAVING, conditional aggregates
- 🧪 **Date grouping** – monthly and quarterly breakdowns
- ⚡ **Period‑over‑period analysis** – growth rates with window functions
- 🧰 **Real‑world deliverable** – a query ready for a BI tool or Python dashboard

---

## 🧱 THE IMPERIAL ENTERPRISE SCENARIO

Imperial Enterprises operates across three regions (North, South, East), selling products in five categories. The CEO needs a single monthly report covering revenue by region and category, quarter‑over‑quarter growth, top‑performing region per quarter, and categories with declining sales.

Three tables: `customers`, `products`, `sales`.

```sql
CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    region TEXT NOT NULL
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL
);

CREATE TABLE sales (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    quantity INTEGER CHECK(quantity > 0),
    sale_date TEXT DEFAULT (date('now')),
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);
```

---

## 🧱 SEED DATA

```sql
INSERT INTO customers VALUES (1, 'Alpha Corp', 'North'), (2, 'Beta Ltd', 'South'), (3, 'Gamma Inc', 'East');
INSERT INTO products VALUES (1, 'Laptop', 'Electronics', 1000), (2, 'Desk', 'Furniture', 500), (3, 'Mouse', 'Electronics', 50);
INSERT INTO sales VALUES (1, 1, 1, 5, '2026-01-15'), (2, 2, 2, 10, '2026-01-20'), (3, 3, 3, 20, '2026-02-10');
```

---

## 🧱 REPORT 1 – MONTHLY REVENUE BY REGION AND CATEGORY

```sql
SELECT
    strftime('%Y-%m', s.sale_date) AS month,
    c.region,
    p.category,
    SUM(s.quantity * p.price) AS revenue,
    COUNT(*) AS transactions
FROM sales s
JOIN customers c ON s.customer_id = c.id
JOIN products p ON s.product_id = p.id
GROUP BY month, c.region, p.category
HAVING revenue > 1000
ORDER BY month, revenue DESC;
```

This uses the full pipeline: JOIN → GROUP BY multiple columns → HAVING filter → ORDER BY.

---

## 🧱 REPORT 2 – QUARTERLY TOTALS WITH GROWTH

```sql
WITH quarterly AS (
    SELECT
        strftime('%Y', s.sale_date) AS year,
        (CAST(strftime('%m', s.sale_date) AS INTEGER) + 2) / 3 AS quarter,
        SUM(s.quantity * p.price) AS revenue
    FROM sales s
    JOIN products p ON s.product_id = p.id
    GROUP BY year, quarter
)
SELECT
    year || '-Q' || quarter AS period,
    revenue,
    LAG(revenue) OVER (ORDER BY year, quarter) AS prev_quarter,
    ROUND((revenue - LAG(revenue) OVER (ORDER BY year, quarter)) * 100.0 /
          LAG(revenue) OVER (ORDER BY year, quarter), 2) AS growth_pct
FROM quarterly;
```

`LAG` reaches back one row to compute quarter‑over‑quarter growth.

---

## 🧱 REPORT 3 – TOP REGION PER QUARTER

```sql
WITH quarterly_region AS (
    SELECT
        strftime('%Y', s.sale_date) AS year,
        (CAST(strftime('%m', s.sale_date) AS INTEGER) + 2) / 3 AS quarter,
        c.region,
        SUM(s.quantity * p.price) AS revenue
    FROM sales s
    JOIN customers c ON s.customer_id = c.id
    JOIN products p ON s.product_id = p.id
    GROUP BY year, quarter, c.region
),
ranked AS (
    SELECT *,
           RANK() OVER (PARTITION BY year, quarter ORDER BY revenue DESC) AS rnk
    FROM quarterly_region
)
SELECT year || '-Q' || quarter AS period, region, revenue
FROM ranked
WHERE rnk = 1;
```

`RANK()` with `PARTITION BY` isolates the top region per quarter.

---

## 🧱 REPORT 4 – CATEGORIES WITH DECLINING SALES

```sql
WITH monthly_category AS (
    SELECT
        strftime('%Y-%m', s.sale_date) AS month,
        p.category,
        SUM(s.quantity * p.price) AS revenue
    FROM sales s
    JOIN products p ON s.product_id = p.id
    GROUP BY month, p.category
),
with_growth AS (
    SELECT *,
           LAG(revenue) OVER (PARTITION BY category ORDER BY month) AS prev_rev
    FROM monthly_category
)
SELECT month, category, revenue, prev_rev,
       ROUND((revenue - prev_rev) * 100.0 / prev_rev, 2) AS change_pct
FROM with_growth
WHERE revenue < prev_rev;
```

Only categories where revenue dropped month‑over‑month appear — an early warning system for the CEO.

---

## 💡 Real‑world Usage

- Banking: monthly profit by branch
- E‑commerce: vendor performance
- Logistics: on‑time delivery rates
- HR: quarterly hiring trends

---

## 🔍 Practice Preview
You will produce the Imperial Enterprise monthly revenue report.

| Level | Task |
|-------|------|
| Easy | Create the tables and seed data, then write the monthly revenue query. |
| Medium | Add the quarterly growth calculation using `LAG`. |
| Hard | Build the top‑region‑per‑quarter report using `RANK()` with `PARTITION BY`. |

Run the coach:
```bash
python ii_Practice_Sheets/L30_Module_3_Capstone_Monthly_Revenue_Reports.py
```

---

## 📌 Key Takeaway
- A capstone report integrates all aggregation, filtering, and joining skills.
- Monthly/quarterly breakdowns with growth rates are the standard for executive dashboards.
- `LAG` and `RANK()` window functions unlock advanced analytics.
- This query is directly transferable to any data analytics role.

*For Emperor.*