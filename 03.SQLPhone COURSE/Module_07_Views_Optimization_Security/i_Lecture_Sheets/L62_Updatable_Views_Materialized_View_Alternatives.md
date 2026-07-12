# 📘 SQLPhone Emperor v3.0 · Module 7
# 📖 L62 – Updatable Views & Materialized View Alternatives

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll learn when a view can be updated directly — and how to simulate materialized views for high‑performance dashboards in SQLite.

- 🧱 **Updatable views** – strict rules for direct INSERT/UPDATE/DELETE  
- 🧠 **INSTEAD OF triggers** – making complex views updatable  
- 🧪 **Materialized view concept** – pre‑computed result sets stored on disk  
- ⚡ **Simulating materialized views** – using a summary table + refresh pattern  

---

## 🧱 WHEN IS A VIEW UPDATABLE?

A view can be updated directly (INSERT, UPDATE, DELETE) only if:
- It references **exactly one** table or updatable view.
- It does **not** use `DISTINCT`, `GROUP BY`, `HAVING`, `LIMIT`, `UNION`, or aggregate functions.
- All columns not in the view have defaults or allow NULL.

```sql
CREATE VIEW simple_soldiers AS
SELECT id, name, rank FROM soldiers;

-- This works: the view maps directly to the underlying table
UPDATE simple_soldiers SET rank = 'Colonel' WHERE id = 1;
```

---

## 🧱 INSTEAD OF TRIGGERS – MAKING COMPLEX VIEWS UPDATABLE

For views that are not natively updatable, use an `INSTEAD OF` trigger to intercept writes and translate them into operations on the base tables.

```sql
CREATE VIEW soldier_regiment AS
SELECT s.id, s.name, r.regiment_name
FROM soldiers s
JOIN regiments r ON s.regiment_id = r.id;

CREATE TRIGGER update_soldier_regiment
INSTEAD OF UPDATE ON soldier_regiment
BEGIN
    UPDATE soldiers SET name = NEW.name WHERE id = OLD.id;
END;
```

Now `UPDATE soldier_regiment SET name = 'New Name' WHERE id = 1;` works.

---

## 🧱 MATERIALIZED VIEW ALTERNATIVE

SQLite has no native `MATERIALIZED VIEW`. The standard workaround is a table that stores pre‑computed results, refreshed on demand.

```sql
-- Create a summary table
CREATE TABLE regiment_summary (
    regiment_id INTEGER PRIMARY KEY,
    soldier_count INTEGER,
    avg_salary REAL
);

-- Refresh the summary
DELETE FROM regiment_summary;
INSERT INTO regiment_summary
SELECT regiment_id, COUNT(*), AVG(salary)
FROM soldiers
GROUP BY regiment_id;
```

> 💡 **INSIGHT:** Use this pattern for dashboards or reports that run frequently but change infrequently. Refresh the materialized table on a schedule or after bulk data changes.

---

## 💡 Real‑world Usage

**Banking – materialized daily balance for fast customer dashboard**
```sql
CREATE TABLE daily_balances (account_id, balance, as_of_date);
-- Refresh nightly
```

**E‑commerce – materialized top‑selling products for homepage**
```sql
CREATE TABLE top_products (product_id, sales_count);
-- Refresh hourly
```

**Logistics – materialized route performance**
```sql
CREATE TABLE route_stats (route_id, avg_delivery_days, total_shipments);
-- Refresh weekly
```

---

## 🔍 Practice Preview
You will create updatable views and simulate materialized views.

| Level | Task |
|-------|------|
| Easy | Create a simple view on one table and update a row through it. |
| Medium | Create a complex view joining two tables, then write an INSTEAD OF trigger to make it updatable. |
| Hard | Create a materialized summary table for regiment statistics and write the refresh query. |

Run the coach:
```bash
python ii_Practice_Sheets/L62_Updatable_Views_Materialized_View_Alternatives.py
```

---

## 📌 Key Takeaway
- Simple views on a single table are updatable directly.  
- `INSTEAD OF` triggers enable writes on complex views.  
- Materialized views are simulated with summary tables and refresh queries.

*For Emperor.*