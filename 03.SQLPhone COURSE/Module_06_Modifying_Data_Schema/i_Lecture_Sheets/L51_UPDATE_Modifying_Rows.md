# 📘 SQLPhone Emperor v3.0 · Module 6
# 📖 L51 – UPDATE – Modifying Rows

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll change existing data safely and precisely — a critical skill for any production database. You’ll also learn to verify affected rows and protect against catastrophic mistakes.

- ✏️ **UPDATE syntax** – `UPDATE table SET col = value WHERE condition`
- 🧠 **WHERE is mandatory** – without it, every row is changed
- 🧪 **Multi‑column updates** – change several columns at once
- ⚡ **Update with subquery** – dynamic values from other tables
- 🛡️ **Safe update patterns** – test with SELECT first, use transactions

---

## 🧱 BASIC UPDATE

`UPDATE` modifies the values of specified columns in rows that match the `WHERE` clause. If you omit `WHERE`, the change applies to **all rows** — a common and dangerous mistake.

```sql
-- Promote a specific soldier
UPDATE soldiers
SET rank = 'General'
WHERE soldier_id = 1;
```

Always test your `WHERE` with a `SELECT` first to see which rows will be affected:

```sql
SELECT * FROM soldiers WHERE soldier_id = 1;
-- If that returns the expected row, then run the UPDATE
```

---

## 🧱 UPDATING MULTIPLE COLUMNS

You can change several columns in one statement, separated by commas:

```sql
UPDATE soldiers
SET rank = 'Colonel', salary = 6000
WHERE soldier_id = 2;
```

---

## 🧱 UPDATE WITH SUBQUERY (DYNAMIC VALUES)

Set a column to a value derived from a subquery. The subquery must return a single value per row.

```sql
-- Raise each soldier's salary to 10% above their regiment's average
UPDATE soldiers
SET salary = (
    SELECT AVG(s2.salary) * 1.1
    FROM soldiers s2
    WHERE s2.regiment_id = soldiers.regiment_id
)
WHERE regiment_id IS NOT NULL;
```

---

## 🧱 UPDATE WITH JOIN (via subquery in SET)

SQLite does not support `UPDATE ... FROM`, but you can use a correlated subquery to pull data from another table:

```sql
-- Set soldier rank based on a lookup table
UPDATE soldiers
SET rank = (
    SELECT new_rank FROM promotions
    WHERE promotions.old_rank = soldiers.rank
)
WHERE EXISTS (
    SELECT 1 FROM promotions WHERE promotions.old_rank = soldiers.rank
);
```

> ⚠️ **WARNING:** If the subquery returns no rows, the column is set to NULL. Always pair a subquery UPDATE with `WHERE EXISTS` to avoid wiping out data.

> 💡 **INSIGHT:** Wrap large UPDATEs in a transaction. If something goes wrong, `ROLLBACK` saves you.

---

## 🧱 SAFETY PATTERNS

**① Test with SELECT first:**
```sql
SELECT * FROM soldiers WHERE rank = 'Private' AND salary < 2000;
-- Verify rows, then:
UPDATE soldiers SET salary = 2500 WHERE rank = 'Private' AND salary < 2000;
```

**② Use a transaction:**
```sql
BEGIN;
UPDATE soldiers SET salary = salary * 1.1 WHERE regiment_id = 3;
-- If something looks wrong:
-- ROLLBACK;
-- Otherwise:
COMMIT;
```

**③ Check rowcount (in Python):**
```python
cursor.execute("UPDATE soldiers SET salary = ? WHERE id = ?", (5000, 1))
print(f"Rows updated: {cursor.rowcount}")
```

---

## 💡 Real‑world Usage

**Banking – apply interest to all savings accounts**
```sql
UPDATE accounts SET balance = balance * 1.05 WHERE account_type = 'savings';
```

**E‑commerce – bulk price increase for a category**
```sql
UPDATE products SET price = price * 1.1 WHERE category = 'Electronics';
```

**Logistics – mark all delayed shipments**
```sql
UPDATE shipments SET status = 'delayed'
WHERE delivery_date < date('now') AND status = 'in transit';
```

**HR – give a raise to all employees in a department**
```sql
UPDATE employees SET salary = salary * 1.08 WHERE department = 'Engineering';
```

**Companion – update memory tags**
```sql
UPDATE memories SET tag = 'important' WHERE content LIKE '%promise%';
```

---

## 🔍 Practice Preview
You will modify soldier records using `UPDATE`.

| Level | Task |
|-------|------|
| Easy | Promote one soldier to 'General' by ID. |
| Medium | Increase the salary of all soldiers in regiment 3 by 500. |
| Hard | Set each soldier's salary to the average salary of their regiment using a correlated subquery, with transaction safety. |

Run the coach:
```bash
python ii_Practice_Sheets/L51_UPDATE_Modifying_Rows.py
```

---

## 📌 Key Takeaway
- `UPDATE` changes existing rows; always use `WHERE`.
- Update multiple columns with a comma‑separated list.
- Correlated subqueries can supply dynamic values for each row.
- Always test with `SELECT`, wrap in `BEGIN`/`COMMIT`, and check `rowcount`.

*For Emperor.*