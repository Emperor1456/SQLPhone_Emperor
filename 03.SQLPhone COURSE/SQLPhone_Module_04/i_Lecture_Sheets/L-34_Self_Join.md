# 📘 SQLPhone Emperor · SQL Module 04
# 📖 L‑34 – Self‑Join

## 🎯 OBJECTIVE
Join a table to itself to compare rows within the same table.

## 🧱 BRICK 1 – Self‑Join Concept
A self‑join uses the same table twice, with different aliases,
to relate rows within that table.

Classic example: employees and their managers.
```sql
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.employee_id;
```
Here `e` and `m` are aliases for the same `employees` table.

## 🧱 BRICK 2 – Practical Scenarios
- Hierarchical data (organisational charts).
- Sequential data (compare a row with the next row).
- Finding duplicate records.

When writing a self‑join, always use table aliases and
treat the two copies as if they were separate tables.

## 💡 Real‑world Usage
- "Who reports to whom?" queries.
- Time series comparisons.
- Network graphs (friends of friends).

## 📌 Key Takeaway
A self‑join connects a table to itself.
Aliases are mandatory to distinguish the two roles.
It’s the key to hierarchical and comparative queries.

*Look inward – the answers are in your own table.*