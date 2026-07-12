# 📘 SQLPhone Emperor v3.0 · Module 7
# 📖 L64 – Index Usage Strategy – When to Index, When Not

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll know exactly which columns to index — and which to leave alone — for a perfectly balanced database.

- 🧱 **Columns that benefit from indexes** – WHERE, JOIN, ORDER BY, GROUP BY  
- 🧠 **Columns that don’t** – low‑cardinality, rarely queried, heavily updated  
- 🧪 **Composite index strategy** – column order matters  
- ⚡ **The trade‑off** – faster reads, slower writes, more storage  

---

## 🧱 WHEN TO INDEX

Index these columns immediately:

| Pattern | Example |
|---------|---------|
| Primary key | Already indexed automatically |
| Foreign key columns | `regiment_id` in soldiers |
| Columns in WHERE | `status`, `name` |
| Columns in JOIN … ON | `s.regiment_id = r.regiment_id` |
| Columns in ORDER BY | `joined_date` |
| Columns in GROUP BY | `regiment_id` |

---

## 🧱 WHEN NOT TO INDEX

Avoid indexes on:

- **Low‑cardinality columns** – columns with very few unique values (e.g., `gender`, `boolean flags`). The index won’t narrow the search enough.
- **Columns that are rarely queried** – indexing unused columns wastes space and write performance.
- **Columns that are heavily updated** – every `UPDATE` also updates the index, slowing down writes.

---

## 🧱 COMPOSITE INDEX STRATEGY

For multi‑column indexes, put the **most selective** column (highest cardinality, most unique values) first.

```sql
-- Good: name is highly selective, status is less selective
CREATE INDEX idx_soldiers_name_status ON soldiers(name, status);

-- Less effective: status first, then name
CREATE INDEX idx_soldiers_status_name ON soldiers(status, name);
```

> 💡 **INSIGHT:** A composite index on `(A, B)` also serves as an index on `(A)` alone. It does **not** serve as an index on `(B)` alone.

---

## 💡 Real‑world Usage

**Banking – index on transaction date for monthly reports**
**E‑commerce – composite index on (category, price) for filtered browsing**
**Logistics – index on (carrier_id, status) for carrier dashboards**
**HR – index on (department, hire_date) for tenure analysis**

---

## 🔍 Practice Preview
You will design an indexing strategy for the Imperial Army database.

| Level | Task |
|-------|------|
| Easy | Identify which columns in the `soldiers` table need indexes and create one. |
| Medium | Create a composite index on two columns and explain the column order. |
| Hard | Analyze a given query workload, decide which indexes to add and which to avoid, and justify each decision. |

Run the coach:
```bash
python ii_Practice_Sheets/L64_Index_Usage_Strategy_When_to_Index_When_Not.py
```

---

## 📌 Key Takeaway
- Index columns used in WHERE, JOIN, ORDER BY, and GROUP BY.  
- Avoid indexing low‑cardinality or rarely‑queried columns.  
- In composite indexes, put the most selective column first.

*For Emperor.*