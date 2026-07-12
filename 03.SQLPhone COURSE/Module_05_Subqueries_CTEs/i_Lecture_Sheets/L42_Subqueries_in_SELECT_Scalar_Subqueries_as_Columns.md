# 📘 SQLPhone Emperor v3.0 · Module 5
# 📖 L42 – Subqueries in SELECT – Scalar Subqueries as Columns

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll embed subqueries directly in your `SELECT` list — adding computed reference columns to every row, like comparing each soldier’s salary to their regiment average in a single query.

- 🧱 **Scalar subquery** – a subquery that returns a single value
- 🧠 **Placement in SELECT** – each row gets the result of the inner query
- 🧪 **Correlated vs non‑correlated** – when the inner query depends on the outer row
- ⚡ **Use case** – comparative metrics, reference data, running calculations

---

## 🧱 SCALAR SUBQUERY IN SELECT

A subquery in the `SELECT` list must return exactly one row and one column — a scalar value. It is evaluated for each row of the outer query (if correlated) or once (if non‑correlated).

```sql
SELECT name,
       salary,
       (SELECT AVG(salary) FROM soldiers) AS overall_average
FROM soldiers;
```

Every row now shows the overall average alongside the soldier’s own salary.

---

## 🧱 CORRELATED SCALAR SUBQUERY

When the inner query references a column from the outer query, it becomes **correlated** — it runs once per outer row, recalculating based on that row’s values.

```sql
SELECT name,
       salary,
       (SELECT AVG(salary)
        FROM soldiers s2
        WHERE s2.regiment_id = s1.regiment_id) AS regiment_avg
FROM soldiers s1;
```

Each soldier now sees the average salary of their own regiment.

---

## 🧱 PRACTICAL USE: DEVIATION FROM AVERAGE

```sql
SELECT name,
       salary,
       salary - (SELECT AVG(salary) FROM soldiers) AS difference_from_avg
FROM soldiers;
```

Positive numbers mean above average; negative means below.

> 💡 **INSIGHT:** Correlated subqueries are powerful but can be slow on large tables. For performance, consider `JOIN` with `GROUP BY` as an alternative.

> ⚠️ **WARNING:** The subquery in `SELECT` must return exactly one row and one column. If it returns multiple rows, the query fails with an error.

---

## 💡 Real‑world Usage

**Banking – each transaction with account average**
```sql
SELECT transaction_id,
       amount,
       (SELECT AVG(amount) FROM transactions WHERE account_id = t.account_id) AS account_avg
FROM transactions t;
```

**E‑commerce – product price vs category average**
```sql
SELECT product_name,
       price,
       (SELECT AVG(price) FROM products WHERE category = p.category) AS category_avg
FROM products p;
```

**Logistics – shipment weight vs route average**
```sql
SELECT tracking_id,
       weight,
       (SELECT AVG(weight) FROM shipments WHERE route = s.route) AS route_avg
FROM shipments s;
```

**HR – employee salary vs department median**
```sql
SELECT name,
       salary,
       (SELECT AVG(salary) FROM employees WHERE department = e.department) AS dept_avg
FROM employees e;
```

---

## 🔍 Practice Preview
You will embed scalar subqueries in `SELECT` to enrich the Imperial Army data.

| Level | Task |
|-------|------|
| Easy | Show each soldier’s salary alongside the overall average salary. |
| Medium | Show each soldier’s salary alongside their regiment’s average salary (correlated). |
| Hard | Display each soldier’s name, salary, and how much their salary differs from the regiment average. |

Run the coach:
```bash
python ii_Practice_Sheets/L42_Subqueries_in_SELECT_Scalar_Subqueries_as_Columns.py
```

---

## 📌 Key Takeaway
- Scalar subqueries return a single value and can be placed in `SELECT`.
- Correlated subqueries refer to the outer row, recalculating per row.
- Use them to add comparative metrics to reports.

*For Emperor.*