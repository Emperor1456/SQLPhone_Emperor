# 📘 SQLPhone Emperor v3.0 · Module 5
# 📖 L47 – WITH Clause – Common Table Expressions (CTEs)

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll write queries that read like a story — using named temporary result sets for clarity, reusability, and modularity. CTEs are the professional alternative to deeply nested subqueries.

- 🧱 **CTE syntax** – `WITH name AS (SELECT …) SELECT …`
- 🧠 **Why CTEs** – readability, modularity, self‑documentation
- 🧪 **Multiple CTEs** – chaining several CTEs in one query
- ⚡ **CTE vs subquery** – when to use which
- 🧰 **Real‑world patterns** – simplifying complex business reports

---

## 🧱 BASIC CTE

A Common Table Expression defines a temporary named query that you can reference later in the same statement — as if it were a table.

```sql
WITH high_paid AS (
    SELECT name, salary FROM soldiers WHERE salary > 4000
)
SELECT * FROM high_paid;
```

The CTE `high_paid` acts as a temporary view visible only to the query that follows.

---

## 🧱 WHY CTEs BEAT NESTED SUBQUERIES

Compare two approaches for the same problem: find regiments where the average salary exceeds the overall average.

**Nested subquery (harder to read):**
```sql
SELECT regiment_id, AVG(salary) AS avg_sal
FROM soldiers
GROUP BY regiment_id
HAVING AVG(salary) > (SELECT AVG(salary) FROM soldiers);
```

**CTE (step‑by‑step, self‑documenting):**
```sql
WITH overall_avg AS (
    SELECT AVG(salary) AS avg_sal FROM soldiers
),
regiment_avgs AS (
    SELECT regiment_id, AVG(salary) AS avg_sal
    FROM soldiers
    GROUP BY regiment_id
)
SELECT r.regiment_id, r.avg_sal
FROM regiment_avgs r
JOIN overall_avg o ON r.avg_sal > o.avg_sal;
```

---

## 🧱 MULTIPLE CTEs

You can define multiple CTEs by separating them with commas. Each CTE can reference any CTE defined before it.

```sql
WITH
    regiment_stats AS (
        SELECT regiment_id, AVG(salary) AS avg_sal
        FROM soldiers GROUP BY regiment_id
    ),
    high_avg_regiments AS (
        SELECT regiment_id FROM regiment_stats WHERE avg_sal > 3500
    )
SELECT name FROM soldiers
WHERE regiment_id IN (SELECT regiment_id FROM high_avg_regiments);
```

This modularity makes complex queries much easier to write, debug, and maintain.

---

## 🧱 CTE VS SUBQUERY – WHEN TO USE WHICH

| Feature | Subquery | CTE |
|---------|----------|-----|
| Readability | Harder when nested deeply | Linear, step‑by‑step |
| Reusability | Must be repeated if used multiple times | Referenced by name multiple times |
| Debugging | Difficult to isolate | Each CTE can be tested independently |
| Performance | Typically inlined by SQLite | Also inlined — same as subquery |

> 💡 **INSIGHT:** Use CTEs when your query is complex, when you reuse the same subquery, or when you want others to understand your logic at a glance. SQLite treats CTEs as optimized subqueries under the hood.

> ⚠️ **WARNING:** CTEs are evaluated each time they are referenced (unless the optimizer caches). If you reference a large CTE multiple times, consider materializing the results into a temporary table for performance.

---

## 💡 Real‑world Usage

**Banking – customer summary then filter**
```sql
WITH customer_totals AS (
    SELECT customer_id, SUM(amount) AS total_spent
    FROM transactions
    GROUP BY customer_id
)
SELECT c.name, ct.total_spent
FROM customers c
JOIN customer_totals ct ON c.id = ct.customer_id
WHERE ct.total_spent > 10000;
```

**E‑commerce – top categories by revenue**
```sql
WITH category_sales AS (
    SELECT category, SUM(quantity * price) AS revenue
    FROM order_items
    JOIN products ON order_items.product_id = products.id
    GROUP BY category
)
SELECT * FROM category_sales
ORDER BY revenue DESC
LIMIT 5;
```

**Logistics – delayed shipments by carrier**
```sql
WITH delayed AS (
    SELECT carrier_id, COUNT(*) AS delayed_count
    FROM shipments
    WHERE status = 'delayed'
    GROUP BY carrier_id
)
SELECT c.carrier_name, d.delayed_count
FROM carriers c
JOIN delayed d ON c.id = d.carrier_id;
```

**HR – department salary budgets**
```sql
WITH dept_payroll AS (
    SELECT department, SUM(salary) AS total_payroll
    FROM employees
    GROUP BY department
)
SELECT * FROM dept_payroll
WHERE total_payroll > 500000;
```

---

## 🔍 Practice Preview
You will use CTEs to structure complex queries in the Imperial Army database.

| Level | Task |
|-------|------|
| Easy | Create a CTE for soldiers with salary > 4000, then select from it. |
| Medium | Create two CTEs: regiment average salaries, then regiments with average > 3500, then list soldiers in those regiments. |
| Hard | Use a CTE to compute each regiment’s average salary, then join it with soldiers to show each soldier’s salary compared to their regiment average. |

Run the coach:
```bash
python ii_Practice_Sheets/L47_WITH_Clause_Common_Table_Expressions_CTEs.py
```

---

## 📌 Key Takeaway
- `WITH` defines named, temporary result sets for clarity.
- Multiple CTEs can be chained, each building on the last.
- CTEs make complex queries readable and maintainable.
- Use them whenever a query becomes hard to follow with nested subqueries.

*For Emperor.*