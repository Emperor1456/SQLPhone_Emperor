# 📘 SQLPhone Emperor v3.0 · Module 4
# 📖 L37 – UNION & UNION ALL – Stacking Results

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll stack query results vertically — merging similar datasets from different tables or conditions. This is the SQL way to combine separate sources into one unified list.

- 🧱 **UNION** – combine results, remove duplicates
- 🧠 **UNION ALL** – combine results, keep all rows (faster)
- 🧪 **Column count & order** – must match between queries
- ⚡ **Practical use** – combining historical and current data, multiple branches
- 🛡️ **Rules and pitfalls** – when UNION fails silently

---

## 🧱 UNION VS UNION ALL

`UNION` merges the output of two or more `SELECT` statements into a single result set. It removes duplicate rows (like `DISTINCT` across the combined set).

`UNION ALL` does the same but **keeps** all rows, even duplicates. It’s faster because no deduplication step is needed.

```sql
SELECT name, 'Soldier' AS role FROM soldiers
UNION ALL
SELECT name, 'Officer' AS role FROM officers;
```

Every soldier and every officer appear in one list, with a `role` column identifying their origin.

---

## 🧱 RULES FOR UNION

- Each `SELECT` must return the same number of columns.
- Column types should be compatible (SQLite is flexible but other databases are strict).
- Column names come from the **first** `SELECT`.

```sql
-- Combine current and archived orders
SELECT order_id, customer_id, order_date FROM orders
UNION ALL
SELECT order_id, customer_id, order_date FROM archived_orders;
```

---

## 🧱 WHEN TO USE UNION vs UNION ALL

| Criteria | UNION | UNION ALL |
|----------|-------|-----------|
| Speed | Slower (deduplication) | Faster |
| Duplicates | Removed | Kept |
| Use case | When duplicates are meaningless (e.g., unique IDs) | When every row matters (e.g., logs, events) |

> ⚠️ **WARNING:** `UNION` without `ALL` performs an expensive sort to remove duplicates. Use `UNION ALL` unless you specifically need deduplication.

> 💡 **INSIGHT:** `UNION ALL` is the standard for combining partitioned data — for example, sales from different regions stored in separate tables with identical structures.

---

## 🧱 ORDERING UNION RESULTS

To sort the final combined result, place `ORDER BY` at the very end:

```sql
SELECT name, 'active' AS status FROM active_soldiers
UNION ALL
SELECT name, 'reserve' AS status FROM reserve_soldiers
ORDER BY name;
```

---

## 💡 Real‑world Usage

**Banking – combine checking and savings transactions**
```sql
SELECT transaction_id, amount, 'checking' AS account_type FROM checking_txns
UNION ALL
SELECT transaction_id, amount, 'savings' AS account_type FROM savings_txns;
```

**E‑commerce – unified product catalog from multiple suppliers**
```sql
SELECT sku, name, price FROM supplier_a_products
UNION ALL
SELECT sku, name, price FROM supplier_b_products;
```

**Logistics – merge domestic and international shipments**
```sql
SELECT tracking_id, destination, 'domestic' AS type FROM domestic_shipments
UNION ALL
SELECT tracking_id, destination, 'international' AS type FROM international_shipments;
```

**HR – all staff from multiple branches**
```sql
SELECT name, department FROM branch1_employees
UNION ALL
SELECT name, department FROM branch2_employees;
```

**Companion – combine conversation logs from different memory partitions**
```sql
SELECT message, timestamp FROM memory_partition_1
UNION ALL
SELECT message, timestamp FROM memory_partition_2
ORDER BY timestamp;
```

---

## 🔍 Practice Preview
You will stack data from multiple Imperial Army sources using UNION and UNION ALL.

| Level | Task |
|-------|------|
| Easy | UNION ALL two tables: `active_soldiers` and `reserve_soldiers`. |
| Medium | Add a literal column to distinguish the source table in the result. |
| Hard | Use UNION ALL to combine soldiers and officers into one personnel list, then sort by name. |

Run the coach:
```bash
python ii_Practice_Sheets/L37_UNION_UNION_ALL_Stacking_Results.py
```

---

## 📌 Key Takeaway
- `UNION ALL` stacks result sets with no deduplication — fast and safe.
- Each `SELECT` must have the same column count and compatible types.
- Use `UNION` only when you need duplicate removal.
- `ORDER BY` goes at the very end of the entire UNION statement.

*For Emperor.*