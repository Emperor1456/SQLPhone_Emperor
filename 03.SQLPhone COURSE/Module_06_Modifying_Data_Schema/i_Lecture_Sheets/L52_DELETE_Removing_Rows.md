# 📘 SQLPhone Emperor v3.0 · Module 6
# 📖 L52 – DELETE – Removing Rows

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll remove data from tables cleanly and safely — and know how to undo mistakes. You’ll also learn the difference between DELETE, DROP, and TRUNCATE in the SQLite world.

- 🗑️ **DELETE syntax** – `DELETE FROM table WHERE condition`
- 🧠 **WHERE is crucial** – without it, the entire table is emptied
- 🧪 **DELETE with subquery** – remove rows based on another table
- ⚡ **DELETE vs DROP vs TRUNCATE** – what SQLite supports
- 🛡️ **Safe deletion patterns** – soft delete, backup first

---

## 🧱 BASIC DELETE

`DELETE` removes rows that match the `WHERE` condition. A missing `WHERE` deletes every row in the table.

```sql
-- Remove a specific soldier
DELETE FROM soldiers WHERE soldier_id = 5;

-- ⚠️ This deletes ALL soldiers:
-- DELETE FROM soldiers;
```

Always run a `SELECT` with the same `WHERE` before executing `DELETE`:

```sql
SELECT * FROM soldiers WHERE discharge_date < '2020-01-01';
-- Verify rows, then:
DELETE FROM soldiers WHERE discharge_date < '2020-01-01';
```

---

## 🧱 DELETE WITH SUBQUERY

You can use a subquery to determine which rows to delete:

```sql
-- Remove soldiers in regiments that have been disbanded
DELETE FROM soldiers
WHERE regiment_id IN (
    SELECT regiment_id FROM regiments
    WHERE status = 'disbanded'
);
```

---

## 🧱 DELETE WITH JOIN (via subquery)

```sql
-- Delete soldiers who have no deployments
DELETE FROM soldiers
WHERE soldier_id NOT IN (
    SELECT soldier_id FROM deployments
);
```

> ⚠️ **WARNING:** `NOT IN` with NULLs can produce unexpected results. Use `NOT EXISTS` for safety (see L44).

---

## 🧱 DELETE VS DROP VS TRUNCATE

| Command | What it does | Speed | Rollback possible? |
|---------|--------------|-------|--------------------|
| `DELETE FROM table` | Removes rows one by one; can have WHERE | Slow | Yes (in transaction) |
| `DELETE FROM table` (no WHERE) | Removes all rows | Slow | Yes |
| `DROP TABLE table` | Removes table and all data | Instant | No (unless in transaction) |
| `TRUNCATE` | Not supported in SQLite | – | – |

For quickly clearing a large table, `DROP TABLE` + `CREATE TABLE` is faster than `DELETE FROM`.

---

## 🧱 SOFT DELETE PATTERN

Instead of physically deleting rows, add a `deleted_at` column and mark rows as deleted:

```sql
ALTER TABLE soldiers ADD COLUMN deleted_at TEXT;
-- "Delete" by setting the timestamp
UPDATE soldiers SET deleted_at = datetime('now') WHERE soldier_id = 5;
-- All queries now filter out soft‑deleted rows:
SELECT * FROM soldiers WHERE deleted_at IS NULL;
```

This keeps data recoverable and is standard practice in production systems.

> 💡 **INSIGHT:** For critical data, never `DELETE` — soft delete. Storage is cheap; lost data is priceless.

---

## 💡 Real‑world Usage

**Banking – close inactive accounts**
```sql
DELETE FROM accounts WHERE last_activity < date('now', '-2 years') AND balance = 0;
```

**E‑commerce – remove products never ordered**
```sql
DELETE FROM products WHERE product_id NOT IN (SELECT DISTINCT product_id FROM order_items);
```

**Logistics – purge delivered shipments older than 90 days**
```sql
DELETE FROM shipments WHERE status = 'delivered' AND delivery_date < date('now', '-90 days');
```

**HR – soft‑delete terminated employees**
```sql
UPDATE employees SET deleted_at = datetime('now') WHERE status = 'terminated';
```

---

## 🔍 Practice Preview
You will safely delete rows from the Imperial Army database.

| Level | Task |
|-------|------|
| Easy | Delete a soldier by their ID. |
| Medium | Delete all soldiers in a specific regiment. |
| Hard | Delete soldiers whose regiment has been marked 'disbanded' using a subquery, wrapped in a transaction with ROLLBACK safety. |

Run the coach:
```bash
python ii_Practice_Sheets/L52_DELETE_Removing_Rows.py
```

---

## 📌 Key Takeaway
- `DELETE FROM table WHERE condition` removes matching rows.
- Always test the `WHERE` clause with `SELECT` first.
- Subqueries enable dynamic deletion based on other tables.
- Soft deletes are safer than physical deletes for critical data.

*For Emperor.*