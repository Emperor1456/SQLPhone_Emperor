# 📘 SQLPhone Emperor v3.0 · Module 6
# 📖 L57 – CREATE INDEX – Speed Up Queries

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll make slow queries lightning‑fast by creating the right indexes — a skill that separates junior and senior developers.

- 🧱 **What an index is** – a fast lookup structure, like a book’s index
- 🧠 **Creating indexes** – `CREATE INDEX name ON table(columns)`
- 🧪 **When to index** – columns used in `WHERE`, `JOIN`, `ORDER BY`
- ⚡ **The cost of indexes** – they speed up reads but slow down writes
- 🛡️ **Composite indexes** – ordering matters, and you get a prefix index for free
- 🔍 **Verification** – using `EXPLAIN QUERY PLAN` to confirm index usage

---

## 🧱 WHAT IS AN INDEX?

An index is a separate data structure that the database maintains for a table. It allows the engine to find rows without scanning the entire table. Without an index, SQLite reads every row sequentially — fine for hundreds of rows, devastating for millions.

Think of it like the index at the back of a textbook. You look up “foreign keys” in the index, find the page numbers, and jump directly there. Without it, you’d flip through every page.

---

## 🧱 CREATING AN INDEX

```sql
-- Speed up lookups by name
CREATE INDEX idx_soldiers_name ON soldiers(name);

-- Speed up queries filtering by regiment and status
CREATE INDEX idx_soldiers_reg_status ON soldiers(regiment_id, status);
```

Once created, the database automatically uses the index when it improves query performance. You don’t need to change your queries.

---

## 🧱 WHEN TO INDEX

Index any column that appears in these clauses:

| Clause | Example | Why |
|--------|---------|-----|
| `WHERE` | `WHERE name = 'Emperor'` | Jump directly to matching rows |
| `JOIN … ON` | `ON s.regiment_id = r.id` | Speeds up matching between tables |
| `ORDER BY` | `ORDER BY joined_date` | Returns sorted results without a separate sort |
| `GROUP BY` | `GROUP BY regiment_id` | Aggregates without scanning entire table |

---

## 🧱 WHEN NOT TO INDEX

Avoid indexes on:

- **Low‑cardinality columns** – very few unique values (e.g., `gender`, `boolean flags`). The index won’t narrow the search enough to be worth it.
- **Columns that are rarely queried** – indexing unused columns wastes space and slows down writes.
- **Columns that are heavily updated** – every `UPDATE` also updates the index, adding overhead.

---

## 🧱 COMPOSITE INDEX STRATEGY

For multi‑column indexes, put the **most selective** column (highest cardinality) first.

```sql
-- Good: name is highly selective, status is less selective
CREATE INDEX idx_soldiers_name_status ON soldiers(name, status);

-- Less effective: status first, then name
CREATE INDEX idx_soldiers_status_name ON soldiers(status, name);
```

> 💡 **INSIGHT:** A composite index on `(A, B)` also serves as an index on `(A)` alone. It does **not** serve as an index on `(B)` alone. So if you have queries filtering on `B` only, you need a separate index on `(B)`.

---

## 🧱 VERIFYING INDEX USAGE

Use `EXPLAIN QUERY PLAN` to see whether your query is using an index:

```sql
EXPLAIN QUERY PLAN
SELECT * FROM soldiers WHERE name = 'Emperor';
-- Should show: SEARCH TABLE soldiers USING INDEX idx_soldiers_name
```

If you see `SCAN TABLE`, the index is not being used — either because it doesn’t exist, or the query planner determined a scan would be faster (common on very small tables).

---

## 💡 Real‑world Usage

**Banking – index on transaction dates for monthly reports**
```sql
CREATE INDEX idx_txn_date ON transactions(transaction_date);
```

**E‑commerce – index on product category for filtering**
```sql
CREATE INDEX idx_products_category ON products(category);
```

**Logistics – index on shipment status for dashboards**
```sql
CREATE INDEX idx_shipments_status ON shipments(status);
```

**HR – composite index on department and status for headcount queries**
```sql
CREATE INDEX idx_emp_dept_status ON employees(department, status);
```

**Companion – index on conversation timestamps for chronological retrieval**
```sql
CREATE INDEX idx_conversations_ts ON conversations(user_id, timestamp);
```

---

## 🔍 Practice Preview
You will create indexes and observe their impact on query performance.

| Level | Task |
|-------|------|
| Easy | Create a simple index on the `name` column of `soldiers`. |
| Medium | Create a composite index on `regiment_id` and `status`. |
| Hard | Use `EXPLAIN QUERY PLAN` before and after creating an index to see the difference from `SCAN` to `SEARCH`. |

Run the coach:
```bash
python ii_Practice_Sheets/L57_CREATE_INDEX_Speed_Up_Queries.py
```

---

## 📌 Key Takeaway
- Indexes dramatically speed up read queries.
- Create indexes on columns used in `WHERE`, `JOIN`, `ORDER BY`, and `GROUP BY`.
- Each index slows down writes — index strategically.
- Composite indexes give you a “free” index on the first column.
- Always `EXPLAIN` to confirm indexes are used.

*For Emperor.*