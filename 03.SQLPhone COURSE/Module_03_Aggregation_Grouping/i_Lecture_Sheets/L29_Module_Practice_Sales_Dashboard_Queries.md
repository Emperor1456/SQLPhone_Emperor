# 📘 SQLPhone Emperor v3.0 · Module 3
# 📖 L29 – Module Practice: Sales Dashboard Queries

---

## 🎯 OBJECTIVE — What You Will Master

> Build a complete sales dashboard using every Module‑3 aggregation skill — the kind that a CEO or General would review every morning. You'll combine `WHERE`, `GROUP BY`, `HAVING`, conditional aggregates, and date grouping into a single, powerful analytics workflow.

- 📊 **Full pipeline** – WHERE → GROUP BY → HAVING → conditional aggregates
- 🧠 **Multi‑metric reports** – multiple KPIs in one query
- 🧪 **Date grouping** – monthly and quarterly breakdowns
- ⚡ **Real‑world scenario** – Imperial Commerce sales analytics
- 🧰 **Dashboard thinking** – one query, many answers

---

## 🧱 THE IMPERIAL COMMERCE SCENARIO

The Emperor's trading company has three tables: `customers`, `products`, and `orders` (with `order_items`). The daily briefing must answer:

- Monthly revenue and order count
- Average order value
- Unique customers per month
- Top‑selling product categories
- Month‑over‑month growth

All in a handful of queries that run in milliseconds.

```sql
-- Tables (simplified)
CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    region TEXT
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT,
    price REAL
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

CREATE TABLE order_items (
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);
```

---

## 🧱 THE MASTER DASHBOARD QUERY

```sql
SELECT
    strftime('%Y-%m', o.order_date) AS month,
    COUNT(*) AS order_count,
    COUNT(DISTINCT o.customer_id) AS unique_customers,
    SUM(oi.quantity * p.price) AS revenue,
    ROUND(AVG(oi.quantity * p.price), 2) AS avg_order_value
FROM orders o
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id
GROUP BY month
ORDER BY month;
```

Five KPIs, one query. This is the first slide of the morning briefing.

---

## 🧱 ADDING CONDITIONAL METRICS

Enhance the report with category breakdowns — no subqueries needed:

```sql
SELECT
    strftime('%Y-%m', o.order_date) AS month,
    COUNT(*) AS total_orders,
    SUM(CASE WHEN p.category = 'Electronics' THEN oi.quantity * p.price ELSE 0 END) AS electronics_revenue,
    SUM(CASE WHEN p.category = 'Furniture' THEN oi.quantity * p.price ELSE 0 END) AS furniture_revenue,
    SUM(CASE WHEN p.category = 'Office' THEN oi.quantity * p.price ELSE 0 END) AS office_revenue
FROM orders o
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id
GROUP BY month;
```

Now the General can see exactly which categories are driving growth.

---

## 🧱 MONTH‑OVER‑MONTH GROWTH

```sql
WITH monthly_revenue AS (
    SELECT
        strftime('%Y-%m', o.order_date) AS month,
        SUM(oi.quantity * p.price) AS revenue
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY month
)
SELECT
    month,
    revenue,
    LAG(revenue) OVER (ORDER BY month) AS prev_month,
    ROUND((revenue - LAG(revenue) OVER (ORDER BY month)) * 100.0 /
          LAG(revenue) OVER (ORDER BY month), 2) AS growth_pct
FROM monthly_revenue;
```

`LAG` reaches back one row. The result shows whether revenue is accelerating or declining.

---

## 🧱 TOP CATEGORIES PER MONTH

```sql
SELECT
    strftime('%Y-%m', o.order_date) AS month,
    p.category,
    SUM(oi.quantity * p.price) AS revenue
FROM orders o
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id
GROUP BY month, p.category
HAVING revenue > 1000
ORDER BY month, revenue DESC;
```

Only categories with meaningful revenue appear, sorted by performance within each month.

> 💡 **INSIGHT:** A dashboard is not one query — it's a collection of queries that tell a story. Start with totals, then break down by dimensions, then add time comparisons. Each query answers one specific question.

> ⚠️ **WARNING:** When joining orders, items, and products, a missing `JOIN` condition can create a Cartesian product — every order matched with every product. Always verify row counts after adding a new join.

---

## 💡 Real‑world Usage

**Banking – monthly branch performance**
```sql
SELECT branch, strftime('%Y-%m', txn_date) AS month,
       COUNT(*) AS txns, SUM(amount) AS volume
FROM transactions
GROUP BY branch, month;
```

**E‑commerce – product performance dashboard**
```sql
SELECT product_id, COUNT(*) AS sold,
       SUM(quantity) AS units,
       SUM(quantity * price) AS revenue
FROM order_items
GROUP BY product_id;
```

**Logistics – carrier performance report**
```sql
SELECT carrier, strftime('%Y-%m', dispatch_date) AS month,
       COUNT(*) AS shipments,
       AVG(delivery_days) AS avg_delivery_time
FROM shipments
GROUP BY carrier, month;
```

---

## 🔍 Practice Preview
You will build a sales dashboard for Imperial Commerce.

| Level | Task |
|-------|------|
| Easy | Create a monthly order count report. |
| Medium | Add total revenue and average order value to the monthly report. |
| Hard | Add conditional revenue breakdown by product category and compute month‑over‑month growth. |

Run the coach:
```bash
python ii_Practice_Sheets/L29_Module_Practice_Sales_Dashboard_Queries.py
```

---

## 📌 Key Takeaway
- A dashboard query combines grouping, aggregates, and conditional metrics.
- `COUNT(DISTINCT)` measures unique entities.
- Conditional aggregates add dimension to your reports.
- `LAG` enables period‑over‑period comparisons without subqueries.
- Build dashboards incrementally: totals → breakdowns → trends.

*For Emperor.*