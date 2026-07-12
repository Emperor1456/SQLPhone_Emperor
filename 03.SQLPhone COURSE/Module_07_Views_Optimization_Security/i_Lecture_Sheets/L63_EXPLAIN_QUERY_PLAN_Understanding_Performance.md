# 📘 SQLPhone Emperor v3.0 · Module 7
# 📖 L63 – EXPLAIN QUERY PLAN – Understanding Performance

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll inspect how SQLite executes your queries — and learn to spot and fix performance bottlenecks before they cripple your application.

- 🧱 **EXPLAIN QUERY PLAN** – see the execution strategy  
- 🧠 **SCAN vs SEARCH** – the difference between slow and fast  
- 🧪 **Using indexes** – how to verify they’re being used  
- ⚡ **Reading the output** – making sense of the plan  

---

## 🧱 WHAT IS A QUERY PLAN?

A query plan is the step‑by‑step strategy the database engine uses to execute your `SELECT`. `EXPLAIN QUERY PLAN` shows you that strategy without running the query.

```sql
EXPLAIN QUERY PLAN
SELECT * FROM soldiers WHERE name = 'Emperor';
```

---

## 🧱 SCAN VS SEARCH

| Term | Meaning | Performance |
|------|---------|-------------|
| `SCAN TABLE` | Reads every row in the table | Slow on large tables |
| `SEARCH TABLE USING INDEX` | Uses an index to jump directly to matching rows | Fast |

```sql
-- Before index: SCAN TABLE soldiers
EXPLAIN QUERY PLAN SELECT * FROM soldiers WHERE name = 'Emperor';

-- Create index
CREATE INDEX idx_soldiers_name ON soldiers(name);

-- After index: SEARCH TABLE soldiers USING INDEX idx_soldiers_name
EXPLAIN QUERY PLAN SELECT * FROM soldiers WHERE name = 'Emperor';
```

---

## 🧱 ANALYZING A JOIN QUERY

```sql
EXPLAIN QUERY PLAN
SELECT s.name, r.regiment_name
FROM soldiers s
JOIN regiments r ON s.regiment_id = r.id
WHERE s.status = 'active';
```

You’ll see the order of table scans/searches. If one of the tables is scanned, adding an index on the join column can turn it into a search.

> 💡 **INSIGHT:** Always `EXPLAIN` your queries before deploying them to production. A `SCAN` on a million‑row table will bring your API to its knees.

---

## 💡 Real‑world Usage

**Banking – check that transaction lookup uses an index**
```sql
EXPLAIN QUERY PLAN
SELECT * FROM transactions WHERE account_id = 101;
```

**E‑commerce – ensure product search uses index**
```sql
EXPLAIN QUERY PLAN
SELECT * FROM products WHERE category = 'Electronics';
```

**Logistics – verify shipment status query is optimized**
```sql
EXPLAIN QUERY PLAN
SELECT * FROM shipments WHERE status = 'delayed';
```

**HR – check employee join performance**
```sql
EXPLAIN QUERY PLAN
SELECT e.name, d.dept_name
FROM employees e JOIN departments d ON e.dept_id = d.id;
```

---

## 🔍 Practice Preview
You will analyze query plans and add indexes to eliminate full table scans.

| Level | Task |
|-------|------|
| Easy | Run `EXPLAIN QUERY PLAN` on a simple `SELECT` without an index. |
| Medium | Create an index and verify the plan changes from `SCAN` to `SEARCH`. |
| Hard | Write a join query, analyze its plan, and add indexes to make all searches use indexes. |

Run the coach:
```bash
python ii_Practice_Sheets/L63_EXPLAIN_QUERY_PLAN_Understanding_Performance.py
```

---

## 📌 Key Takeaway
- `EXPLAIN QUERY PLAN` reveals how your query is executed.  
- `SCAN TABLE` is slow; `SEARCH TABLE USING INDEX` is fast.  
- Always verify indexes are being used before production deployment.

*For Emperor.*