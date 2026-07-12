# 📘 SQLPhone Emperor v3.0 · Module 5
# 📖 L41 – Subqueries in WHERE – Filtering with Sub‑selects

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll use the output of one query as input to another — the first step toward building truly intelligent filters.

- 🧱 **Subquery in WHERE** – `SELECT … WHERE column IN (SELECT …)`
- 🧠 **Scalar vs list subqueries** – single value vs multiple values
- 🧪 **Comparison operators with subqueries** – `=`, `>`, `<`, `IN`
- ⚡ **Execution order** – the inner query runs first

---

## 🧱 SUBQUERY IN WHERE – THE PATTERN

A subquery is a `SELECT` nested inside another statement. When placed in `WHERE`, it provides a list or value for filtering.

```sql
-- Find soldiers whose salary is greater than the average
SELECT name, salary
FROM soldiers
WHERE salary > (SELECT AVG(salary) FROM soldiers);
```

The inner query computes a single number — the average salary. The outer query returns every soldier who earns above that threshold.

---

## 🧱 SUBQUERY WITH IN

When the subquery returns multiple values, use `IN` instead of `=`.

```sql
-- Find soldiers assigned to regiments stationed in the capital
SELECT name
FROM soldiers
WHERE regiment_id IN (
    SELECT regiment_id FROM regiments
    WHERE location = 'Capital'
);
```

The subquery returns a list of regiment IDs; the outer query returns soldiers in those regiments.

---

## 🧱 SUBQUERY WITH COMPARISON OPERATORS

You can pair a subquery with any comparison operator, provided it returns a single value.

```sql
-- Find the soldier(s) with the maximum salary
SELECT name, salary
FROM soldiers
WHERE salary = (SELECT MAX(salary) FROM soldiers);
```

> ⚠️ **WARNING:** If a subquery used with `=` returns more than one row, SQLite throws an error. Use `IN` when multiple values are expected.

> 💡 **INSIGHT:** Subqueries execute from the inside out. Think of the inner query as preparing a temporary result set that the outer query consumes.

---

## 💡 Real‑world Usage

**Banking – transactions above customer’s average**
```sql
SELECT transaction_id, amount
FROM transactions t
WHERE amount > (
    SELECT AVG(amount) FROM transactions
    WHERE customer_id = t.customer_id
);
```

**E‑commerce – products priced above category average**
```sql
SELECT product_name, price
FROM products p
WHERE price > (
    SELECT AVG(price) FROM products
    WHERE category = p.category
);
```

**Logistics – shipments heavier than average for their destination**
```sql
SELECT tracking_id, weight
FROM shipments s
WHERE weight > (
    SELECT AVG(weight) FROM shipments
    WHERE destination = s.destination
);
```

**HR – employees earning above department average**
```sql
SELECT name, salary, department
FROM employees e
WHERE salary > (
    SELECT AVG(salary) FROM employees
    WHERE department = e.department
);
```

---

## 🔍 Practice Preview
You will filter the Imperial Army using subqueries inside `WHERE`.

| Level | Task |
|-------|------|
| Easy | Select soldiers whose salary is above the overall average. |
| Medium | Select soldiers in regiments located in the 'Capital' (use subquery with `IN`). |
| Hard | Select soldiers whose salary is the maximum within their own regiment (correlated subquery preview). |

Run the coach:
```bash
python ii_Practice_Sheets/L41_Subqueries_in_WHERE_Filtering_with_Subselects.py
```

---

## 📌 Key Takeaway
- Subqueries in `WHERE` provide dynamic filter values.
- Use `=` for single‑value subqueries, `IN` for multi‑value subqueries.
- The inner query executes first, feeding the outer query.

*For Emperor.*