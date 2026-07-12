# 📘 SQLPhone Emperor v3.0 · Module 4
# 📖 L38 – Join Challenges – Complex Business Reports

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll solve multi‑table business problems that require every join skill from this module — the kind of reports that executives actually request.

- 🧱 **Multi‑join patterns** – 3+ tables with mixed join types
- 🧠 **Aggregation with joins** – counts, sums across related tables
- 🧪 **Self‑join + other joins** – combining hierarchy with additional data
- ⚡ **Performance awareness** – which join order matters
- 🛡️ **Real‑world scenarios** – exactly what you’ll build in your first backend job

---

## 🧱 CHALLENGE 1 – Regimental Strength Report

Goal: for each regiment, show the regiment name, number of soldiers, and the location of its most recent deployment.

```sql
SELECT
    r.regiment_name,
    COUNT(s.soldier_id) AS strength,
    d.location
FROM regiments r
LEFT JOIN soldiers s ON r.regiment_id = s.regiment_id
LEFT JOIN deployments d ON r.regiment_id = d.regiment_id
GROUP BY r.regiment_id
ORDER BY strength DESC;
```

`LEFT JOIN` ensures regiments with zero soldiers still appear. The deployment location comes from the deployments table; if a regiment has never been deployed, that column is NULL.

---

## 🧱 CHALLENGE 2 – Employees with Subordinates Count

Goal: list every employee and how many direct reports they have (including zero).

```sql
SELECT
    m.name AS manager,
    COUNT(e.emp_id) AS team_size
FROM employees m
LEFT JOIN employees e ON m.emp_id = e.manager_id
GROUP BY m.emp_id
ORDER BY team_size DESC;
```

A self‑join with aggregation — one of the most common HR queries. The `LEFT JOIN` ensures the CEO (who has no manager) appears as a manager with their team size.

---

## 🧱 CHALLENGE 3 – Products with Total Revenue (including products with no sales)

```sql
SELECT
    p.product_name,
    COALESCE(SUM(oi.quantity * p.price), 0) AS total_revenue
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_id;
```

`COALESCE` replaces NULL with 0 for products that never sold. This is the definitive "include zeros" pattern.

---

## 🧱 CHALLENGE 4 – Multi‑Department Employee Directory with Managers

Goal: show each employee's name, their department, their manager's name, and their manager's department.

```sql
SELECT
    e.name AS employee,
    ed.dept_name AS emp_dept,
    m.name AS manager,
    md.dept_name AS mgr_dept
FROM employees e
JOIN departments ed ON e.dept_id = ed.dept_id
LEFT JOIN employees m ON e.manager_id = m.emp_id
LEFT JOIN departments md ON m.dept_id = md.dept_id
ORDER BY ed.dept_name, e.name;
```

Four tables joined, mixing `INNER JOIN` (employee must have a department) and `LEFT JOIN` (manager and their department are optional).

---

## 🧱 CHALLENGE 5 – Full Order Fulfillment Report

Goal: for each order, show customer name, product name, quantity, order date, shipment status, and carrier name. Orders without shipments should still appear.

```sql
SELECT
    c.name AS customer,
    p.product_name,
    oi.quantity,
    o.order_date,
    COALESCE(sh.status, 'Not shipped') AS status,
    COALESCE(cr.carrier_name, 'N/A') AS carrier
FROM orders o
JOIN customers c ON o.customer_id = c.id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
LEFT JOIN shipments sh ON o.order_id = sh.order_id
LEFT JOIN carriers cr ON sh.carrier_id = cr.carrier_id
ORDER BY o.order_date DESC;
```

Five tables, mixing `INNER JOIN` for required relationships and `LEFT JOIN` for optional logistics data.

> 💡 **INSIGHT:** When a report requires "include zeros" or "show all, even if missing," the pattern is always `LEFT JOIN` + `COALESCE`. When it requires "only show matches," use `INNER JOIN`. Mastering this distinction is the key to professional SQL.

> ⚠️ **WARNING:** With many joins, performance can degrade quickly. Always index foreign key columns, and test with realistic data volumes. The difference between a query that takes 0.1 seconds and one that takes 10 seconds is often a single missing index.

---

## 💡 Real‑world Usage

**Banking – customer profitability with account and transaction summaries**
**E‑commerce – category performance with supplier and inventory data**
**Logistics – hub throughput with shipment and carrier details**
**HR – full employee profile with department, manager, and project assignments**

---

## 🔍 Practice Preview
You will solve five complex business report challenges using multi‑table joins.

| Level | Task |
|-------|------|
| Easy | Regimental strength report: count soldiers per regiment. |
| Medium | Employee team size: count direct reports per manager, including zero. |
| Hard | Full order fulfillment report joining 5 tables with mixed INNER and LEFT JOINs. |

Run the coach:
```bash
python ii_Practice_Sheets/L38_Join_Challenges_Complex_Business_Reports.py
```

---

## 📌 Key Takeaway
- Complex reports require multiple joins, aggregation, and conditional logic.
- `LEFT JOIN` + `GROUP BY` is the standard pattern for “include zeros.”
- Self‑joins unlock hierarchical analysis.
- `COALESCE` converts NULLs to meaningful defaults.
- Always index join columns for performance.

*For Emperor.*