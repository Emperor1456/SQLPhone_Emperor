# 📘 SQLPhone Emperor v3.0 · Module 4
# 📖 L36 – Joining More Than Two Tables

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll chain three or more tables into a single query — the backbone of every real‑world business report. This is where databases reveal their true power: bringing together scattered data into one complete picture.

- 🧱 **Multi‑table JOIN chain** – one join after another
- 🧠 **Join order** – how the database builds intermediate results
- 🧪 **Mixing join types** – INNER, LEFT across many tables
- ⚡ **Alias management** – keeping long queries readable
- 🛡️ **Performance** – why indexes on foreign keys are critical

---

## 🧱 JOINING THREE TABLES

Each additional table is joined by another `JOIN … ON` clause. The result is a combined row across all matched records.

```sql
SELECT s.name AS soldier,
       r.regiment_name AS regiment,
       d.location AS deployed_to
FROM soldiers s
JOIN regiments r ON s.regiment_id = r.regiment_id
JOIN deployments d ON s.deployment_id = d.deployment_id;
```

Execution: first, `soldiers` and `regiments` are joined. The intermediate result is then joined with `deployments`.

---

## 🧱 JOINING FOUR TABLES

```sql
SELECT s.name, r.regiment_name, d.location, b.battalion_name
FROM soldiers s
JOIN regiments r ON s.regiment_id = r.regiment_id
JOIN deployments d ON s.deployment_id = d.deployment_id
JOIN battalions b ON r.battalion_id = b.battalion_id;
```

Each `JOIN` adds another layer of data, building a rich composite record from multiple sources.

---

## 🧱 MIXING JOIN TYPES

You can use `LEFT JOIN` for optional relationships and `INNER JOIN` for mandatory ones in the same query.

```sql
SELECT s.name, r.regiment_name, d.location
FROM soldiers s
LEFT JOIN regiments r ON s.regiment_id = r.regiment_id
LEFT JOIN deployments d ON s.deployment_id = d.deployment_id;
```

Now soldiers appear even if they have no regiment or deployment. But be careful: a `LEFT JOIN` after an `INNER JOIN` may still exclude rows if the first `INNER JOIN` filters them out.

```sql
-- This still drops soldiers without a regiment (INNER JOIN comes first)
SELECT s.name, r.regiment_name, d.location
FROM soldiers s
JOIN regiments r ON s.regiment_id = r.regiment_id   -- INNER
LEFT JOIN deployments d ON s.deployment_id = d.deployment_id;  -- LEFT
```

> 💡 **INSIGHT:** The order of joins matters. When mixing `INNER` and `LEFT`, put `INNER JOIN`s first for required relationships, then `LEFT JOIN`s for optional ones. But remember: an earlier `INNER JOIN` can eliminate rows before the `LEFT JOIN` even runs.

> ⚠️ **WARNING:** With many joins, the result set can explode if join conditions are not precise. Always verify your row counts before trusting the output.

---

## 💡 Real‑world Usage

**Banking – customer → account → transactions**
```sql
SELECT c.name, a.account_id, t.amount
FROM customers c
JOIN accounts a ON c.id = a.customer_id
JOIN transactions t ON a.account_id = t.account_id;
```

**E‑commerce – order → customer → product**
```sql
SELECT o.order_id, c.name, p.product_name
FROM orders o
JOIN customers c ON o.customer_id = c.id
JOIN products p ON o.product_id = p.id;
```

**Logistics – shipment → warehouse → city**
```sql
SELECT s.tracking_id, w.name, c.city_name
FROM shipments s
JOIN warehouses w ON s.warehouse_id = w.id
JOIN cities c ON w.city_id = c.id;
```

**HR – employee → department → location → region**
```sql
SELECT e.name, d.dept_name, l.city, r.region_name
FROM employees e
JOIN departments d ON e.dept_id = d.id
JOIN locations l ON d.location_id = l.id
JOIN regions r ON l.region_id = r.id;
```

---

## 🔍 Practice Preview
You will join three and four Imperial Army tables for complete reports.

| Level | Task |
|-------|------|
| Easy | Join `soldiers` → `regiments` → `deployments` (INNER JOIN all). |
| Medium | Use LEFT JOINs to show all soldiers with regiment and deployment, including those missing one. |
| Hard | Join four tables: `soldiers` → `regiments` → `deployments` → `battalions`, selecting relevant columns and handling NULLs. |

Run the coach:
```bash
python ii_Practice_Sheets/L36_Joining_More_Than_Two_Tables.py
```

---

## 📌 Key Takeaway
- Chain `JOIN … ON` clauses to combine many tables.
- Use aliases to keep multi‑table queries readable.
- Mix `INNER JOIN` and `LEFT JOIN` carefully to preserve needed rows.
- Index foreign key columns for fast multi‑table queries.

*For Emperor.*