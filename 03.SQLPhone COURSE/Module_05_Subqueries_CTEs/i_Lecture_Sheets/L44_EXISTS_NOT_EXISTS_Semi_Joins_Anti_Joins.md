# 📘 SQLPhone Emperor v3.0 · Module 5
# 📖 L44 – EXISTS & NOT EXISTS – Semi‑Joins & Anti‑Joins

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll use `EXISTS` to check for the presence of related rows — the safer, faster alternative to `IN` that every senior developer reaches for first.

- 🧱 **EXISTS** – returns true if the subquery returns any rows
- 🧠 **NOT EXISTS** – returns true if the subquery returns no rows
- 🧪 **Correlated EXISTS** – referencing the outer query for dynamic checks
- ⚡ **Why EXISTS beats IN** – no NULL trap, better performance on large tables

---

## 🧱 EXISTS – CHECKING FOR RELATED ROWS

`EXISTS` tests whether a subquery yields at least one row. The actual data returned by the subquery is irrelevant — only the existence of rows matters.

```sql
-- Regiments that have at least one soldier
SELECT regiment_name
FROM regiments r
WHERE EXISTS (
    SELECT 1 FROM soldiers s
    WHERE s.regiment_id = r.regiment_id
);
```

The `SELECT 1` is a convention — you’re not retrieving data, just checking existence.

---

## 🧱 NOT EXISTS – FINDING ORPHANED RECORDS

`NOT EXISTS` is the safest way to find rows that have no match in another table. Unlike `NOT IN`, it handles NULLs correctly and consistently.

```sql
-- Regiments with no soldiers
SELECT regiment_name
FROM regiments r
WHERE NOT EXISTS (
    SELECT 1 FROM soldiers s
    WHERE s.regiment_id = r.regiment_id
);
```

---

## 🧱 EXISTS WITH ADDITIONAL CONDITIONS

You can add more filters inside the subquery for precise checks.

```sql
-- Soldiers who have at least one deployment in the current year
SELECT name
FROM soldiers s
WHERE EXISTS (
    SELECT 1 FROM deployments d
    WHERE d.soldier_id = s.soldier_id
      AND strftime('%Y', d.deployment_date) = strftime('%Y', 'now')
);
```

> 💡 **INSIGHT:** `EXISTS` stops scanning the inner query as soon as it finds a match. This makes it faster than `IN` for large datasets, especially when an index exists on the join column.

> ⚠️ **WARNING:** `NOT IN` with a subquery that contains NULL returns zero rows — always. `NOT EXISTS` never has this problem. This is why `NOT EXISTS` is the standard for anti‑joins.

---

## 💡 Real‑world Usage

**Banking – customers who have made a transaction this year**
```sql
SELECT name FROM customers c
WHERE EXISTS (
    SELECT 1 FROM transactions t
    WHERE t.customer_id = c.id
      AND t.txn_date >= '2026-01-01'
);
```

**E‑commerce – products currently in stock**
```sql
SELECT product_name FROM products p
WHERE EXISTS (
    SELECT 1 FROM inventory i
    WHERE i.product_id = p.id AND i.quantity > 0
);
```

**Logistics – carriers with active shipments**
```sql
SELECT carrier_name FROM carriers c
WHERE EXISTS (
    SELECT 1 FROM shipments s
    WHERE s.carrier_id = c.id AND s.status = 'in transit'
);
```

**HR – departments with no employees**
```sql
SELECT department_name FROM departments d
WHERE NOT EXISTS (
    SELECT 1 FROM employees e
    WHERE e.dept_id = d.id
);
```

---

## 🔍 Practice Preview
You will use `EXISTS` and `NOT EXISTS` to query related and orphaned records.

| Level | Task |
|-------|------|
| Easy | Select all regiments that have at least one soldier (use `EXISTS`). |
| Medium | Select all regiments that have no soldiers (use `NOT EXISTS`). |
| Hard | Select soldiers who are in a regiment that has been deployed at least once (use `EXISTS` with two‑level correlation). |

Run the coach:
```bash
python ii_Practice_Sheets/L44_EXISTS_NOT_EXISTS_Semi_Joins_Anti_Joins.py
```

---

## 📌 Key Takeaway
- `EXISTS` checks for the presence of related rows — faster and safer than `IN`.
- `NOT EXISTS` correctly handles NULLs where `NOT IN` fails.
- Use `SELECT 1` inside `EXISTS` — you don’t need actual column data.

*For Emperor.*