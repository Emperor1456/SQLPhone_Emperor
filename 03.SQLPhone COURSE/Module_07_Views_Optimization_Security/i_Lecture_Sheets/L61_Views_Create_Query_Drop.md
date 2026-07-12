# 📘 SQLPhone Emperor v3.0 · Module 7
# 📖 L61 – Views – Create, Query & Drop

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll create virtual tables that simplify complex queries, hide sensitive columns, and make your database easier to maintain — all without duplicating a single row of data.

- 🧱 **What a view is** – a saved query that behaves like a table  
- 🧠 **CREATE VIEW** – define a view once, use it everywhere  
- 🧪 **Querying a view** – exactly like a table, including joins and filters  
- ⚡ **DROP VIEW** – remove a view when no longer needed  
- 🛡️ **Security through views** – expose only the columns users should see  

---

## 🧱 CREATING A VIEW

A view is a stored `SELECT` statement. It doesn’t hold data itself; it just remembers the query. When you query the view, SQLite runs the underlying `SELECT`.

```sql
CREATE VIEW active_soldiers AS
SELECT name, rank, regiment_id
FROM soldiers
WHERE status = 'active';
```

Now you can use `active_soldiers` like a table:

```sql
SELECT * FROM active_soldiers WHERE rank = 'General';
```

---

## 🧱 WHY USE VIEWS?

- **Simplify complex queries** – hide multi‑table joins behind a simple name.  
- **Security** – grant access to the view but not the underlying tables (e.g., show employee names but not salaries).  
- **Consistency** – if the logic changes, update the view; all queries that use it automatically pick up the change.

**Example – hide salaries from junior analysts:**
```sql
CREATE VIEW public_employees AS
SELECT name, department, hire_date
FROM employees;
```

Junior analysts can query `public_employees` but never see the `salary` column.

---

## 🧱 MODIFYING AND DROPPING VIEWS

To replace an existing view, drop it first, then recreate:

```sql
DROP VIEW IF EXISTS active_soldiers;
CREATE VIEW active_soldiers AS
SELECT name, rank, regiment_id, salary
FROM soldiers
WHERE status = 'active';
```

Or use `CREATE OR REPLACE VIEW` (not supported in SQLite – you must drop manually).

> ⚠️ **WARNING:** Views in SQLite are read‑only by default. You cannot `INSERT`, `UPDATE`, or `DELETE` directly on a view unless it meets strict criteria (see L62 on updatable views).

> 💡 **INSIGHT:** Think of a view as a permanent alias for a query. If you find yourself writing the same `JOIN` or `WHERE` clause repeatedly, create a view.

---

## 💡 Real‑world Usage

**Banking – customer account summary view**
```sql
CREATE VIEW customer_balances AS
SELECT c.name, a.account_number, a.balance
FROM customers c
JOIN accounts a ON c.id = a.customer_id;
```

**E‑commerce – active product catalog (in‑stock only)**
```sql
CREATE VIEW available_products AS
SELECT * FROM products WHERE stock > 0;
```

**Logistics – pending shipments view**
```sql
CREATE VIEW pending_shipments AS
SELECT tracking_id, destination, status
FROM shipments
WHERE status IN ('pending', 'in transit');
```

**HR – employee directory without salary**
```sql
CREATE VIEW employee_directory AS
SELECT name, department, email
FROM employees;
```

---

## 🔍 Practice Preview
You will create views for the Imperial Army to simplify common queries.

| Level | Task |
|-------|------|
| Easy | Create a view `active_soldiers` showing only soldiers with status `'active'`. |
| Medium | Create a view `regiment_summary` that joins soldiers with regiments and shows regiment name and soldier count. |
| Hard | Create a view that shows each soldier's name, regiment, and deployment location, then query it with a `WHERE` filter. |

Run the coach:
```bash
python ii_Practice_Sheets/L61_Views_Create_Query_Drop.py
```

---

## 📌 Key Takeaway
- A view is a saved query that acts like a virtual table.  
- Use views to simplify complex joins, enforce column‑level security, and ensure consistency.  
- Views are read‑only unless strict conditions are met.

*For Emperor.*