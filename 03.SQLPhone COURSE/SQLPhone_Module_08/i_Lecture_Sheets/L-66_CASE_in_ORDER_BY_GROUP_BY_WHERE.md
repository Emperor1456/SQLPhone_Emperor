# 📘 SQLPhone Emperor · SQL Module 08
# 📖 L‑66 – CASE in ORDER BY, GROUP BY, WHERE

## 🎯 OBJECTIVE
Use `CASE` in other clauses to create dynamic ordering,
filtering, and grouping.

## 🧱 BRICK 1 – CASE in ORDER BY
Sort with custom logic:
```sql
SELECT name, priority
FROM tasks
ORDER BY CASE priority
  WHEN 'urgent' THEN 1
  WHEN 'high'   THEN 2
  ELSE 3
END;
```
This sorts urgent first, then high, then the rest.

## 🧱 BRICK 2 – CASE in WHERE and GROUP BY
**WHERE:**
```sql
SELECT * FROM products
WHERE CASE
  WHEN category = 'Electronics' THEN price > 500
  ELSE price > 100
END;
```
**GROUP BY:**
```sql
SELECT CASE WHEN age < 30 THEN 'Young' ELSE 'Mature' END AS age_group, COUNT(*)
FROM users
GROUP BY age_group;
```

## 💡 Real‑world Usage
- Custom sort orders for UI.
- Conditional filters without dynamic SQL.
- Dynamic grouping for pivot‑like reports.

## 📌 Key Takeaway
`CASE` isn't just for `SELECT` columns.
It makes `ORDER BY`, `WHERE`, and `GROUP BY` dynamic.
Keep logic readable; complex conditions belong in app code.

*CASE anywhere logic is needed.*