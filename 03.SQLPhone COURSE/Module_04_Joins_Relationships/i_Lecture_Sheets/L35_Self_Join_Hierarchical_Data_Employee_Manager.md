# 📘 SQLPhone Emperor v3.0 · Module 4
# 📖 L35 – Self‑Join – Hierarchical Data (Employee‑Manager)

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll query hierarchical relationships within a single table — the key to org charts, category trees, and chain‑of‑command reports.

- 🧱 **Self‑join concept** – joining a table to itself
- 🧠 **Aliases are mandatory** – differentiate left and right sides
- 🧪 **Employee‑Manager pattern** – classic organizational hierarchy
- ⚡ **Finding top‑level rows** – WHERE manager_id IS NULL
- 🛡️ **LEFT JOIN in self‑joins** – include the CEO who has no manager

---

## 🧱 WHY SELF‑JOIN?

When a table contains a column that references its own primary key (e.g., `manager_id` references `employee_id` in the same table), you need to join the table with itself to resolve the reference.

```sql
CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    manager_id INTEGER,
    FOREIGN KEY (manager_id) REFERENCES employees(emp_id)
);
```

---

## 🧱 BASIC SELF‑JOIN

```sql
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.emp_id;
```

Each row pairs an employee with their manager. The table appears twice: `e` for the employee role, `m` for the manager role. A `LEFT JOIN` ensures employees without a manager (the CEO) still appear.

---

## 🧱 FINDING TOP‑LEVEL EMPLOYEES

Employees with no manager:

```sql
SELECT name FROM employees
WHERE manager_id IS NULL;
```

---

## 🧱 FINDING MANAGERS (employees who have at least one direct report)

```sql
SELECT DISTINCT m.name
FROM employees e
JOIN employees m ON e.manager_id = m.emp_id;
```

---

## 🧱 COUNTING DIRECT REPORTS

```sql
SELECT m.name, COUNT(e.emp_id) AS team_size
FROM employees m
LEFT JOIN employees e ON m.emp_id = e.manager_id
GROUP BY m.emp_id
ORDER BY team_size DESC;
```

> 💡 **INSIGHT:** Self‑joins are essential for any data with parent‑child relationships. They’re the foundation of recursive CTEs (L48).

> ⚠️ **WARNING:** Without `LEFT JOIN`, the CEO (who has no manager) disappears from the result. Always use `LEFT JOIN` when you want to include top‑level rows.

---

## 💡 Real‑world Usage

**Banking – chain of approval for transactions**
```sql
SELECT txn.id, approver.name AS approved_by, supervisor.name AS supervisor
FROM transactions txn
LEFT JOIN users approver ON txn.approved_by = approver.id
LEFT JOIN users supervisor ON approver.manager_id = supervisor.id;
```

**E‑commerce – product category hierarchy**
```sql
SELECT c.name AS category, p.name AS parent_category
FROM categories c
LEFT JOIN categories p ON c.parent_id = p.id;
```

**Logistics – package forwarding chain**
**HR – entire org chart with levels**

---

## 🔍 Practice Preview
You will query the Imperial Army’s chain of command using self‑joins.

| Level | Task |
|-------|------|
| Easy | Create an `employees` table with a `manager_id` self‑reference and insert hierarchical data. |
| Medium | Write a self‑join to show each employee with their manager’s name. |
| Hard | Find all employees who are managers (their ID appears as someone else’s `manager_id`) and count their direct reports. |

Run the coach:
```bash
python ii_Practice_Sheets/L35_Self_Join_Hierarchical_Data_Employee_Manager.py
```

---

## 📌 Key Takeaway
- Self‑join uses two aliases for the same table.
- Essential for hierarchical data: org charts, category trees, referral chains.
- `LEFT JOIN` preserves top‑level rows with no parent.

*For Emperor.*