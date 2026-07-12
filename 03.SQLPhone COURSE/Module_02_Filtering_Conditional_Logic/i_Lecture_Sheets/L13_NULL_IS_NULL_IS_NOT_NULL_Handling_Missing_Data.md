# 📘 SQLPhone Emperor v3.0 · Module 2
# 📖 L13 – NULL – IS NULL, IS NOT NULL & Handling Missing Data

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll understand the most misunderstood concept in SQL — `NULL` — and learn to handle missing data safely in every query.

- 🕳️ **What NULL really means** – unknown, not zero, not empty string
- 🧪 **IS NULL / IS NOT NULL** – the only correct way to test for NULL
- ⚡ **NULL in comparisons** – why `= NULL` never works
- 🛡️ **NULL and aggregates** – how NULL affects COUNT, SUM, AVG
- 🧹 **Defensive querying** – making your reports NULL‑safe

---

## 🧱 NULL IS NOT ZERO

`NULL` represents missing or unknown information. It is not the same as `0`, an empty string `''`, or any other value. Think of it as “no data has been entered yet.”

```sql
-- A soldier with no recorded rank has NULL in that column
SELECT name, rank FROM soldiers WHERE rank IS NULL;
```

If a column allows `NULL` (no `NOT NULL` constraint), rows can have `NULL` in that column by default.

---

## 🧱 TESTING FOR NULL – IS NULL, IS NOT NULL

Because `NULL` is not a value, normal comparison operators (`=`, `<>`, `!=`) will **never** match it. You must always use `IS NULL` or `IS NOT NULL`.

```sql
-- Correct
SELECT name FROM soldiers WHERE rank IS NULL;

-- Also correct
SELECT name FROM soldiers WHERE rank IS NOT NULL;

-- WRONG – this will never return any rows
SELECT name FROM soldiers WHERE rank = NULL;
```

> ⚠️ **WARNING:** `= NULL` is a common beginner mistake that silently returns no rows instead of raising an error. Always use `IS NULL`.

---

## 🧱 NULL IN COMPARISONS AND EXPRESSIONS

Any arithmetic or string operation involving `NULL` yields `NULL`. This can silently corrupt calculations if you’re not careful.

```sql
SELECT 10 + NULL;          -- returns NULL
SELECT 'Hello' || NULL;    -- returns NULL
```

To safely handle `NULL` in expressions, use `COALESCE` (covered in Module 3) or `IFNULL`:

```sql
SELECT name, COALESCE(rank, 'Unassigned') AS rank FROM soldiers;
```

---

## 🧱 NULL AND AGGREGATES

All aggregate functions **ignore NULL values** except `COUNT(*)`.

- `COUNT(column)` counts only non‑NULL entries.
- `SUM(column)` adds only non‑NULL values.
- `AVG(column)` averages only non‑NULL values.

```sql
-- Counts all rows, regardless of NULLs
SELECT COUNT(*) FROM soldiers;

-- Counts only rows where rank is not NULL
SELECT COUNT(rank) FROM soldiers;
```

---

## 💡 Real‑world Usage

**Banking – find accounts with missing contact info**
```sql
SELECT account_id, holder
FROM accounts
WHERE email IS NULL;
```

**E‑commerce – list products without a description**
```sql
SELECT product_name
FROM products
WHERE description IS NULL OR description = '';
```

**Logistics – shipments not yet delivered (no delivery date)**
```sql
SELECT tracking_id, destination
FROM shipments
WHERE delivery_date IS NULL;
```

**HR – employees without a department assignment**
```sql
SELECT name
FROM employees
WHERE department_id IS NULL;
```

---

## 🔍 Practice Preview
You will query the Imperial Army database for missing data and learn to handle NULL safely.

| Level | Task |
|-------|------|
| Easy | Select all soldiers whose rank is NULL. |
| Medium | Count how many soldiers have a non‑NULL salary. |
| Hard | Select soldier names with their rank, replacing NULL with `'Unassigned'`. |

Run the coach:
```bash
python ii_Practice_Sheets/L13_NULL_IS_NULL_IS_NOT_NULL_Handling_Missing_Data.py
```

---

## 📌 Key Takeaway
- `NULL` means unknown – never use `=` to test it.
- Always use `IS NULL` or `IS NOT NULL`.
- NULL propagates through expressions; use `COALESCE` to guard against it.
- Aggregates ignore NULL except `COUNT(*)`.

*For Emperor.*