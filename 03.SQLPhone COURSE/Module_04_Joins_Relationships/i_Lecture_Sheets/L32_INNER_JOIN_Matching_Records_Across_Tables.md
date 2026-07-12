# 📘 SQLPhone Emperor v3.0 · Module 4
# 📖 L32 – INNER JOIN – Matching Records Across Tables

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll combine rows from two tables based on matching keys — the most common join in all of SQL, used in every report that spans multiple tables.

- 🧱 **INNER JOIN syntax** – `FROM table1 JOIN table2 ON condition`
- 🧠 **Matching mechanism** – only rows with a match appear
- 🧪 **Aliases** – shortening table names in joins
- ⚡ **Multi‑table JOIN** – chaining joins for complex reports
- 🛡️ **Performance** – the importance of indexes on join columns

---

## 🧱 BASIC INNER JOIN

An `INNER JOIN` returns rows where the join condition is true in both tables. Rows without a match are excluded.

```sql
SELECT s.name, r.regiment_name
FROM soldiers s
JOIN regiments r ON s.regiment_id = r.regiment_id;
```

If a soldier has no regiment (NULL), that row is dropped. If a regiment has no soldiers, it does not appear.

---

## 🧱 TABLE ALIASES IN JOINS

Aliases make join queries readable, especially with long table names.

```sql
SELECT s.name AS soldier, r.regiment_name AS regiment
FROM soldiers s
JOIN regiments r ON s.regiment_id = r.regiment_id;
```

---

## 🧱 JOINING THREE TABLES

Chain another `JOIN` to pull in more data:

```sql
SELECT s.name, r.regiment_name, d.location
FROM soldiers s
JOIN regiments r ON s.regiment_id = r.regiment_id
JOIN deployments d ON s.deployment_id = d.deployment_id;
```

---

## 🧱 INNER JOIN WITH ADDITIONAL FILTERS

```sql
SELECT s.name, r.regiment_name
FROM soldiers s
JOIN regiments r ON s.regiment_id = r.regiment_id
WHERE s.status = 'active'
  AND r.location = 'North';
```

> 💡 **INSIGHT:** `INNER JOIN` is the default join; you can write just `JOIN`. Both are identical. Use `INNER JOIN` when you want to be explicit.

> ⚠️ **WARNING:** Without an index on the join columns, `INNER JOIN` can become very slow on large tables. Always index foreign key columns.

---

## 💡 Real‑world Usage

**Banking – customer with their accounts**
```sql
SELECT c.name, a.account_id, a.balance
FROM customers c
JOIN accounts a ON c.id = a.customer_id;
```

**E‑commerce – order details with product info**
```sql
SELECT o.order_id, p.product_name, o.quantity
FROM orders o
JOIN products p ON o.product_id = p.id;
```

**Logistics – shipments with carrier name**
```sql
SELECT s.tracking_id, c.carrier_name
FROM shipments s
JOIN carriers c ON s.carrier_id = c.id;
```

**HR – employees with department name**
```sql
SELECT e.name, d.department_name
FROM employees e
JOIN departments d ON e.dept_id = d.id;
```

---

## 🔍 Practice Preview
You will join Imperial Army tables to produce enriched reports.

| Level | Task |
|-------|------|
| Easy | Join `soldiers` with `regiments` to show each soldier’s regiment name. |
| Medium | Join `orders` with `customers` to show customer name alongside order details. |
| Hard | Join three tables: `soldiers`, `regiments`, and `deployments` to show soldier name, regiment name, and deployment location. |

Run the coach:
```bash
python ii_Practice_Sheets/L32_INNER_JOIN_Matching_Records_Across_Tables.py
```

---

## 📌 Key Takeaway
- `INNER JOIN` returns rows with matching keys in both tables.
- Aliases keep join queries clean and readable.
- The most frequently used join in all of backend development.

*For Emperor.*