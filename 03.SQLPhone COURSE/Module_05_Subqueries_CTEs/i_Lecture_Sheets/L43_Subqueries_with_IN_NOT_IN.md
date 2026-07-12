# 📘 SQLPhone Emperor v3.0 · Module 5
# 📖 L43 – Subqueries with IN & NOT IN

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll filter rows by checking membership against a dynamic list produced by another query — the classic “find records that appear (or don’t appear) in another table” pattern.

- 🧱 **IN with subquery** – match against a set of values from another table
- 🧠 **NOT IN with subquery** – exclude rows that appear in another table
- 🧪 **NULL safety** – why `NOT IN` can be dangerous with NULLs
- ⚡ **Real‑world use** – finding records with/without related entries

---

## 🧱 IN WITH SUBQUERY

Use `IN` when you want rows whose column value appears in the result of a subquery.

```sql
-- Soldiers in regiments that have been deployed
SELECT name
FROM soldiers
WHERE regiment_id IN (
    SELECT regiment_id FROM deployments
);
```

The subquery returns a list of regiment IDs; the outer query returns soldiers in those regiments.

---

## 🧱 NOT IN WITH SUBQUERY

`NOT IN` returns rows whose column value does **not** appear in the subquery result.

```sql
-- Soldiers in regiments that have NEVER been deployed
SELECT name
FROM soldiers
WHERE regiment_id NOT IN (
    SELECT regiment_id FROM deployments
);
```

---

## 🧱 THE NULL TRAP

If the subquery returns any `NULL` value, `NOT IN` returns **no rows at all**. This is one of the most notorious SQL traps.

```sql
-- DANGEROUS: if deployments contains a NULL regiment_id,
-- this query returns zero rows, even if there are valid matches
SELECT name FROM soldiers
WHERE regiment_id NOT IN (
    SELECT regiment_id FROM deployments
);
```

**The safe alternative: `NOT EXISTS` (see L44)**

```sql
SELECT name FROM soldiers s
WHERE NOT EXISTS (
    SELECT 1 FROM deployments d WHERE d.regiment_id = s.regiment_id
);
```

> ⚠️ **WARNING:** Always ensure the subquery column is `NOT NULL` when using `NOT IN`, or use `NOT EXISTS` which handles NULLs correctly.

> 💡 **INSIGHT:** `IN` with a subquery is often replaceable by an `INNER JOIN`, but `IN` is more readable for simple membership checks.

---

## 💡 Real‑world Usage

**Banking – customers with active accounts**
```sql
SELECT name FROM customers
WHERE id IN (SELECT customer_id FROM accounts WHERE status = 'active');
```

**E‑commerce – products never ordered**
```sql
SELECT product_name FROM products
WHERE product_id NOT IN (SELECT DISTINCT product_id FROM order_items);
```

**Logistics – shipments to premium destinations**
```sql
SELECT tracking_id FROM shipments
WHERE destination_id IN (SELECT id FROM destinations WHERE tier = 'premium');
```

**HR – employees not assigned to any project**
```sql
SELECT name FROM employees
WHERE emp_id NOT IN (SELECT emp_id FROM project_assignments);
```

---

## 🔍 Practice Preview
You will filter rows using dynamic membership lists from subqueries.

| Level | Task |
|-------|------|
| Easy | Select soldiers whose regiment has been deployed (use `IN`). |
| Medium | Select soldiers whose regiment has NEVER been deployed (use `NOT IN`). |
| Hard | Select products that have never been ordered, ensuring the subquery handles NULL safely (use `NOT EXISTS`). |

Run the coach:
```bash
python ii_Practice_Sheets/L43_Subqueries_with_IN_NOT_IN.py
```

---

## 📌 Key Takeaway
- `IN` checks if a value exists in the subquery’s result set.
- `NOT IN` checks if a value is absent — but can break on NULLs.
- Prefer `NOT EXISTS` when NULLs are possible.

*For Emperor.*