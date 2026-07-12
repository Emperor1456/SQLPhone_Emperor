# 📘 SQLPhone Emperor v3.0 · Module 7
# 📖 L69 – Module Practice: Secure Reporting Views

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll build a complete reporting layer that combines views for security, indexes for performance, and parameterized queries for safety — the exact stack used in production analytics systems.

- 🧱 **Views for reporting** – abstract complex joins into simple names
- 🧠 **Security through views** – limit column exposure by role
- 🧪 **Indexes for performance** – make those views fast
- ⚡ **Parameterized access** – safe querying from applications
- 🧰 **Complete workflow** – from raw tables to executive dashboard

---

## 🧱 THE IMPERIAL REPORTING SCENARIO

The Imperial High Command needs a reporting system with three access levels:

| Role | Can see |
|------|---------|
| Junior Officer | Soldier names, regiments (no salary) |
| Senior Officer | Everything – name, rank, salary, deployment |
| Analyst | Aggregated summaries only (counts, averages) |

All reports must be fast and injection‑proof.

---

## 🧱 SECURE VIEWS

```sql
-- Junior officer view: no salary
CREATE VIEW v_public_soldiers AS
SELECT s.name, r.regiment_name, s.status
FROM soldiers s
JOIN regiments r ON s.regiment_id = r.id;

-- Senior officer view: full detail
CREATE VIEW v_full_soldiers AS
SELECT s.name, r.regiment_name, s.rank, s.salary, s.status, d.location
FROM soldiers s
JOIN regiments r ON s.regiment_id = r.id
LEFT JOIN deployments d ON s.deployment_id = d.id;

-- Analyst view: aggregated only
CREATE VIEW v_regiment_summary AS
SELECT r.regiment_name, COUNT(*) AS soldiers, AVG(s.salary) AS avg_salary
FROM soldiers s
JOIN regiments r ON s.regiment_id = r.id
GROUP BY r.regiment_id;
```

---

## 🧱 PERFORMANCE INDEXES

```sql
CREATE INDEX idx_soldiers_regiment ON soldiers(regiment_id);
CREATE INDEX idx_soldiers_status ON soldiers(status);
CREATE INDEX idx_soldiers_deployment ON soldiers(deployment_id);
```

Verify with `EXPLAIN QUERY PLAN`:

```sql
EXPLAIN QUERY PLAN SELECT * FROM v_full_soldiers WHERE status = 'active';
```

You should see `SEARCH TABLE soldiers USING INDEX idx_soldiers_status` – not a full table scan.

---

## 🧱 SAFE QUERYING FROM PYTHON

```python
import sqlite3

def query_for_role(role, filter_value=None):
    conn = sqlite3.connect("empire.db")
    conn.row_factory = sqlite3.Row

    if role == "junior":
        sql = "SELECT * FROM v_public_soldiers WHERE status = ?"
        params = (filter_value,)
    elif role == "senior":
        sql = "SELECT * FROM v_full_soldiers WHERE salary > ?"
        params = (filter_value,)
    elif role == "analyst":
        sql = "SELECT * FROM v_regiment_summary WHERE soldiers > ?"
        params = (filter_value,)
    else:
        raise ValueError("Unknown role")

    cur = conn.execute(sql, params)
    return [dict(row) for row in cur.fetchall()]

# Example: junior officer checking active soldiers
results = query_for_role("junior", "active")
```

> 💡 **INSIGHT:** The view + parameterized query pattern gives you both security and performance. The view enforces column‑level access; the parameterized query prevents injection; the index makes it fast.

---

## 💡 Real‑world Usage

**Banking – teller view (no credit score) vs manager view (full)**
**E‑commerce – public product view (no cost price) vs admin view**
**Logistics – customer tracking view (no internal notes) vs operations view**
**HR – employee directory (no salary) vs payroll view**

---

## 🔍 Practice Preview
You will build the Imperial reporting layer.

| Level | Task |
|-------|------|
| Easy | Create a public view that hides salary. |
| Medium | Create a full view for senior officers and add performance indexes. |
| Hard | Write a Python function that selects the correct view based on role and queries it safely with parameters. |

Run the coach:
```bash
python ii_Practice_Sheets/L69_Module_Practice_Secure_Reporting_Views.py
```

---

## 📌 Key Takeaway
- Views enforce column‑level security.  
- Indexes keep reporting views fast.  
- Parameterized queries protect against injection.  
- Role‑based access control through views is a production‑ready pattern.

*For Emperor.*