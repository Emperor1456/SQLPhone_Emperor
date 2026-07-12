# 📘 SQLPhone Emperor v3.0 · Module 2
# 📖 L12 – BETWEEN, IN, LIKE – Range, Membership, Patterns

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll filter data with elegance — using ranges, lists, and wildcard patterns instead of long chains of `OR` conditions.

- 📏 **BETWEEN** – filter within a range (numbers and dates)
- 📋 **IN** – match against a list of values
- 🔍 **LIKE** – pattern matching with wildcards (`%`, `_`)
- 🧪 **Combining them** – building powerful, readable `WHERE` clauses

---

## 🧱 BETWEEN – RANGE FILTERING

`BETWEEN` checks if a value falls within a range, inclusive of both ends.

```sql
-- Soldiers with salary between 3000 and 5000
SELECT name, salary
FROM soldiers
WHERE salary BETWEEN 3000 AND 5000;
```

It also works with dates:

```sql
-- Registrations between two dates
SELECT citizen_id, registration_date
FROM registrations
WHERE registration_date BETWEEN '2026-01-01' AND '2026-06-30';
```

> 💡 **INSIGHT:** `BETWEEN` is equivalent to `value >= low AND value <= high`. It’s cleaner and less error‑prone than writing both comparisons manually.

---

## 🧱 IN – MEMBERSHIP CHECKING

`IN` tests whether a value appears in a given list. It replaces multiple `OR` conditions.

```sql
-- Soldiers with specific ranks
SELECT name, rank
FROM soldiers
WHERE rank IN ('General', 'Colonel', 'Major');
```

You can also use a subquery inside `IN` (covered in Module 5):

```sql
SELECT name FROM soldiers
WHERE rank IN (SELECT DISTINCT rank FROM officers);
```

> ⚠️ **WARNING:** `IN` with a long list can be slower than joining to a lookup table. For a handful of values, it’s perfect.

---

## 🧱 LIKE – PATTERN MATCHING

`LIKE` searches for patterns in text. Two wildcards are available:

| Wildcard | Meaning |
|----------|---------|
| `%` | Zero or more characters |
| `_` | Exactly one character |

```sql
-- Names starting with 'Em'
SELECT name FROM soldiers WHERE name LIKE 'Em%';

-- Names ending with 'er'
SELECT name FROM soldiers WHERE name LIKE '%er';

-- Names with exactly 5 characters
SELECT name FROM soldiers WHERE name LIKE '_____';
```

**Case sensitivity** – by default, `LIKE` is case‑insensitive for ASCII in SQLite, but `LIKE` binary is case‑sensitive. Use `COLLATE NOCASE` to be safe:

```sql
SELECT * FROM soldiers WHERE name LIKE 'em%' COLLATE NOCASE;
```

> 💡 **INSIGHT:** `%` can be slow on large tables if used at the start of a pattern (`%something`) because the database cannot use an index. Use full‑text search (FTS5) for heavy text search.

---

## 💡 Real‑world Usage

**Banking – transactions in a date range**
```sql
SELECT transaction_id, amount
FROM transactions
WHERE transaction_date BETWEEN '2026-01-01' AND '2026-01-31';
```

**E‑commerce – products in specific categories**
```sql
SELECT name, price
FROM products
WHERE category IN ('Electronics', 'Accessories', 'Stationery');
```

**Logistics – tracking IDs starting with a prefix**
```sql
SELECT tracking_id, status
FROM shipments
WHERE tracking_id LIKE 'TRK-%';
```

**HR – find employees with email pattern**
```sql
SELECT name, email
FROM employees
WHERE email LIKE '%@pyphone.com';
```

---

## 🔍 Practice Preview
You will filter the Imperial database using ranges, lists, and wildcards.

| Level | Task |
|-------|------|
| Easy | Select soldiers with salary between 3000 and 5000. |
| Medium | Select soldiers whose rank is General, Colonel, or Major using `IN`. |
| Hard | Select soldiers whose name starts with 'A' and has exactly 5 characters using `LIKE`. |

Run the coach:
```bash
python ii_Practice_Sheets/L12_BETWEEN_IN_LIKE_Range_Membership_Patterns.py
```

---

## 📌 Key Takeaway
- `BETWEEN` filters inclusive ranges — simpler than two comparisons.
- `IN` replaces multiple `OR` conditions with a clean list.
- `LIKE` searches patterns with `%` (any) and `_` (one char).
- Combine them to create precise, readable `WHERE` clauses.

*For Emperor.*