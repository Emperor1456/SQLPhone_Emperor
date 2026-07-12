# 📘 SQLPhone Emperor v3.0 · Module 4
# 📖 L33 – LEFT JOIN – All from Left, Match from Right

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll keep every row from the left table, even when there’s no match — essential for completeness reports like “all products, including those never ordered.”

- 🧱 **LEFT JOIN syntax** – `LEFT JOIN table ON condition`
- 🧠 **NULL for missing matches** – how the right side fills with NULL
- 🧪 **Finding unmatched rows** – `WHERE right_column IS NULL`
- ⚡ **Comparison with INNER JOIN** – when to use which
- 🛡️ **Real‑world** – completeness checks, audit reports

---

## 🧱 LEFT JOIN EXPLAINED

`LEFT JOIN` returns all rows from the left table, plus matching rows from the right table. If there’s no match, the right columns are filled with NULL.

```sql
SELECT s.name, r.regiment_name
FROM soldiers s
LEFT JOIN regiments r ON s.regiment_id = r.regiment_id;
```

Soldiers without a regiment still appear — their `regiment_name` is NULL. Regiments without soldiers do **not** appear.

---

## 🧱 FINDING UNMATCHED ROWS

A classic pattern: find all left‑side rows that have no counterpart.

```sql
SELECT s.name
FROM soldiers s
LEFT JOIN regiments r ON s.regiment_id = r.regiment_id
WHERE r.regiment_id IS NULL;
```

These are soldiers assigned to a non‑existent regiment (or unassigned if `regiment_id` is NULL).

---

## 🧱 LEFT JOIN WITH AGGREGATION

```sql
SELECT r.regiment_name, COUNT(s.soldier_id) AS soldier_count
FROM regiments r
LEFT JOIN soldiers s ON r.regiment_id = s.regiment_id
GROUP BY r.regiment_id;
```

This includes regiments with zero soldiers — impossible with `INNER JOIN`.

> 💡 **INSIGHT:** `LEFT JOIN` is also called `LEFT OUTER JOIN`. The `OUTER` keyword is optional and does not change behavior.

> ⚠️ **WARNING:** When filtering on a right‑table column, `WHERE right_col = 'value'` will remove rows where the right table is NULL (i.e., unmatched rows). To keep them, filter in the `ON` clause instead.

---

## 💡 Real‑world Usage

**Banking – customers with and without accounts**
```sql
SELECT c.name, a.account_id
FROM customers c
LEFT JOIN accounts a ON c.id = a.customer_id;
```

**E‑commerce – products never ordered**
```sql
SELECT p.product_name
FROM products p
LEFT JOIN orders o ON p.id = o.product_id
WHERE o.order_id IS NULL;
```

**Logistics – shipments not yet delivered**
```sql
SELECT s.tracking_id
FROM shipments s
LEFT JOIN deliveries d ON s.tracking_id = d.tracking_id
WHERE d.delivery_id IS NULL;
```

**HR – departments with no employees**
```sql
SELECT d.department_name
FROM departments d
LEFT JOIN employees e ON d.id = e.dept_id
WHERE e.emp_id IS NULL;
```

---

## 🔍 Practice Preview
You will use LEFT JOIN to create complete lists and identify gaps.

| Level | Task |
|-------|------|
| Easy | Show all soldiers with their regiment name, including soldiers without a regiment. |
| Medium | Find all soldiers who are not assigned to any regiment. |
| Hard | Show all regiments with the count of soldiers, including regiments with zero soldiers. |

Run the coach:
```bash
python ii_Practice_Sheets/L33_LEFT_JOIN_All_from_Left_Match_from_Right.py
```

---

## 📌 Key Takeaway
- `LEFT JOIN` keeps every row from the left table.
- Unmatched right columns are NULL.
- Use `WHERE right_column IS NULL` to find rows without a match.

*For Emperor.*