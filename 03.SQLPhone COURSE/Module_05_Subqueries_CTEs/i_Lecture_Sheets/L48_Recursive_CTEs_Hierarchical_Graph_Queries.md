# 📘 SQLPhone Emperor v3.0 · Module 5
# 📖 L48 – Recursive CTEs – Hierarchical & Graph Queries

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll traverse trees, org charts, and networks using recursive Common Table Expressions — the tool that turns SQL into a graph query language.

- 🧱 **Recursive CTE syntax** – `WITH RECURSIVE name AS (...)`
- 🧠 **Anchor member + recursive member** – the base case and the loop
- 🧪 **Termination condition** – preventing infinite loops
- ⚡ **Use cases** – org charts, bill of materials, category trees
- 🛡️ **Safety** – depth limits and cycle detection

---

## 🧱 THE RECURSIVE CTE STRUCTURE

A recursive CTE has two parts separated by `UNION ALL`:

1. **Anchor member** – the initial query (base case).
2. **Recursive member** – references the CTE itself, called repeatedly until no new rows are returned.

```sql
WITH RECURSIVE cnt(x) AS (
    SELECT 1                    -- anchor
    UNION ALL
    SELECT x + 1 FROM cnt       -- recursive
    WHERE x < 5                 -- termination condition
)
SELECT * FROM cnt;
```

Returns: 1, 2, 3, 4, 5.

---

## 🧱 EMPLOYEE HIERARCHY (ORG CHART)

The most common real‑world use: traversing a chain of command.

```sql
WITH RECURSIVE org AS (
    -- Anchor: top‑level employees (no manager)
    SELECT emp_id, name, manager_id, 1 AS level
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    -- Recursive: employees reporting to the previous level
    SELECT e.emp_id, e.name, e.manager_id, o.level + 1
    FROM employees e
    JOIN org o ON e.manager_id = o.emp_id
)
SELECT * FROM org
ORDER BY level, name;
```

The `level` column tracks depth. The anchor selects the CEO (no manager); each recursive step finds their direct reports.

---

## 🧱 CATEGORY TREE (E‑COMMERCE)

```sql
WITH RECURSIVE cat_tree AS (
    SELECT id, name, parent_id, 0 AS depth
    FROM categories WHERE parent_id IS NULL

    UNION ALL

    SELECT c.id, c.name, c.parent_id, ct.depth + 1
    FROM categories c
    JOIN cat_tree ct ON c.parent_id = ct.id
)
SELECT * FROM cat_tree
ORDER BY depth, name;
```

---

## 🧱 REPORTING CHAIN (UPWARD TRACE)

Trace from a specific employee all the way to the CEO:

```sql
WITH RECURSIVE chain AS (
    SELECT emp_id, name, manager_id
    FROM employees WHERE emp_id = 42  -- start here

    UNION ALL

    SELECT e.emp_id, e.name, e.manager_id
    FROM employees e
    JOIN chain c ON e.emp_id = c.manager_id
)
SELECT * FROM chain;
```

> ⚠️ **WARNING:** Without a termination condition (like a depth limit), a recursive CTE with cycles can run forever. Use `WHERE depth < 50` or a similar guard.

> 💡 **INSIGHT:** Recursive CTEs are one of SQL’s most powerful features. They let you query hierarchical data without writing procedural code. Use them for any data with parent‑child relationships.

---

## 💡 Real‑world Usage

**E‑commerce – category breadcrumb trail**
```sql
WITH RECURSIVE breadcrumb AS (
    SELECT id, name, parent_id, name AS path
    FROM categories WHERE id = 5   -- target category
    UNION ALL
    SELECT c.id, c.name, c.parent_id, c.name || ' > ' || b.path
    FROM categories c
    JOIN breadcrumb b ON c.id = b.parent_id
)
SELECT path FROM breadcrumb WHERE parent_id IS NULL;
```

**Logistics – route tracing with maximum segments**
```sql
WITH RECURSIVE route AS (
    SELECT from_city, to_city, distance, 1 AS segments
    FROM routes WHERE from_city = 'Dhaka'
    UNION ALL
    SELECT r.from_city, r.to_city, r.distance, rt.segments + 1
    FROM routes r
    JOIN route rt ON r.from_city = rt.to_city
    WHERE rt.segments < 5
)
SELECT * FROM route;
```

**HR – all subordinates of a manager**
```sql
WITH RECURSIVE subordinates AS (
    SELECT emp_id, name, manager_id FROM employees WHERE manager_id = 10
    UNION ALL
    SELECT e.emp_id, e.name, e.manager_id
    FROM employees e
    JOIN subordinates s ON e.manager_id = s.emp_id
)
SELECT * FROM subordinates;
```

**Companion – threaded conversation replies**
```sql
WITH RECURSIVE thread AS (
    SELECT id, parent_id, message, 0 AS depth
    FROM messages WHERE parent_id IS NULL AND conversation_id = 1
    UNION ALL
    SELECT m.id, m.parent_id, m.message, t.depth + 1
    FROM messages m
    JOIN thread t ON m.parent_id = t.id
)
SELECT * FROM thread ORDER BY depth;
```

---

## 🔍 Practice Preview
You will traverse hierarchical data using recursive CTEs.

| Level | Task |
|-------|------|
| Easy | Create a recursive CTE that generates numbers from 1 to 10. |
| Medium | Build the employee org chart showing each employee's name, manager, and depth level. |
| Hard | Trace the reporting chain from a Private all the way to the General. |

Run the coach:
```bash
python ii_Practice_Sheets/L48_Recursive_CTEs_Hierarchical_Graph_Queries.py
```

---

## 📌 Key Takeaway
- `WITH RECURSIVE` enables querying hierarchical data directly in SQL.
- The anchor provides the starting rows; the recursive member references the CTE itself.
- Always include a termination condition to avoid infinite loops.
- This is the foundation for querying any tree or graph structure.

*For Emperor.*