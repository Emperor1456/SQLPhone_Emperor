# 📘 SQLPhone Emperor v3.0 · Module 5
# 📖 L46 – Correlated Subqueries – Row‑by‑Row Inner Queries

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll write subqueries that reference the outer row — enabling per‑row dynamic calculations like “each soldier’s salary compared to their own regiment’s average.” This is the gateway to truly intelligent SQL.

- 🧱 **What makes a subquery correlated** – it references a column from the outer query
- 🧠 **Execution model** – the inner query runs once per outer row
- 🧪 **Comparing with JOIN** – when to use correlated subqueries vs GROUP BY
- ⚡ **Performance considerations** – when they shine, when to use alternatives

---

## 🧱 CORRELATED VS NON‑CORRELATED

A **non‑correlated** subquery runs independently and returns a result used by the outer query. A **correlated** subquery depends on the outer query’s current row, running once for each outer row.

```sql
-- Correlated: find soldiers earning above their regiment's average
SELECT name, salary, regiment_id
FROM soldiers s1
WHERE salary > (
    SELECT AVG(salary)
    FROM soldiers s2
    WHERE s2.regiment_id = s1.regiment_id
);
```

For each soldier (`s1`), the inner query computes the average salary of that soldier’s regiment (`s2.regiment_id = s1.regiment_id`).

---

## 🧱 CORRELATED SUBQUERY IN SELECT

Correlated subqueries can also appear in `SELECT`, adding a computed column to every row.

```sql
SELECT name,
       salary,
       (SELECT COUNT(*) FROM soldiers s2
        WHERE s2.regiment_id = s1.regiment_id) AS regiment_size
FROM soldiers s1;
```

Each soldier now sees the total number of soldiers in their regiment.

---

## 🧱 RANKING WITH CORRELATED SUBQUERIES

A classic pattern: rank items within groups without window functions.

```sql
SELECT name, salary, regiment_id,
       (SELECT COUNT(*) FROM soldiers s2
        WHERE s2.regiment_id = s1.regiment_id
          AND s2.salary > s1.salary) + 1 AS salary_rank
FROM soldiers s1
ORDER BY regiment_id, salary_rank;
```

This counts how many soldiers in the same regiment have a higher salary, giving a rank starting from 1 (highest salary).

> 💡 **INSIGHT:** A correlated subquery with `COUNT` in `SELECT` is often replaceable by `JOIN` + `GROUP BY`, which is usually faster on large tables. Use correlated subqueries when the logic is per‑row and the dataset is moderate.

> ⚠️ **WARNING:** Because the inner query runs once per outer row, correlated subqueries can become **very slow** on large datasets. Always test with realistic data sizes and check `EXPLAIN QUERY PLAN`.

---

## 💡 Real‑world Usage

**Banking – each transaction with customer’s running total**
```sql
SELECT txn_id, amount,
       (SELECT SUM(amount) FROM transactions t2
        WHERE t2.customer_id = t1.customer_id
          AND t2.txn_date <= t1.txn_date) AS running_balance
FROM transactions t1;
```

**E‑commerce – product price vs average in its category**
```sql
SELECT product_name, price,
       (SELECT AVG(price) FROM products p2
        WHERE p2.category = p1.category) AS category_avg
FROM products p1;
```

**Logistics – each shipment’s weight vs route average**
```sql
SELECT tracking_id, weight,
       (SELECT AVG(weight) FROM shipments s2
        WHERE s2.route = s1.route) AS route_avg
FROM shipments s1;
```

**HR – employee salary rank within department**
```sql
SELECT name, salary, department,
       (SELECT COUNT(*) FROM employees e2
        WHERE e2.department = e1.department
          AND e2.salary > e1.salary) + 1 AS dept_rank
FROM employees e1;
```

---

## 🔍 Practice Preview
You will write correlated subqueries for per‑row dynamic calculations in the Imperial Army.

| Level | Task |
|-------|------|
| Easy | Show each soldier’s salary alongside their regiment’s average salary. |
| Medium | Show each soldier’s name, salary, and how many soldiers are in their regiment. |
| Hard | Rank soldiers by salary within their own regiment (1 = highest paid). |

Run the coach:
```bash
python ii_Practice_Sheets/L46_Correlated_Subqueries_Row_by_Row_Inner_Queries.py
```

---

## 📌 Key Takeaway
- Correlated subqueries reference the outer row, executing once per row.
- Use them for per‑row calculations like running totals, ranks, and group comparisons.
- For large datasets, test against `JOIN` + `GROUP BY` alternatives.

*For Emperor.*