# 📘 SQLPhone Emperor v3.0 · Module 2
# 📖 L14 – Aliases (AS) & Computed Columns

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll rename columns and create calculated fields directly in your queries — making your reports readable and your logic portable.

- 🏷️ **Column aliases** – rename output columns with `AS`
- 🏗️ **Table aliases** – shorten table names in complex queries
- 🧮 **Computed columns** – perform calculations on the fly
- 🧪 **Aliases in `ORDER BY` and `GROUP BY`** – how they interact
- ⚠️ **WHERE clause limitation** – aliases are not visible there

---

## 🧱 COLUMN ALIASES WITH `AS`

An alias gives a temporary name to a column in your result set. It does not change the underlying table; it only affects how the output is displayed.

```sql
SELECT name AS soldier_name, salary AS monthly_pay
FROM soldiers;
```

**Business example – make reports human‑readable:**
```sql
SELECT product_name AS Product,
       unit_price AS Price,
       quantity AS Stock
FROM inventory;
```

Aliases can contain spaces if enclosed in double quotes, but for phone‑friendly code, use underscores.

```sql
SELECT product_name AS "Product Name" FROM inventory;
```

---

## 🧱 TABLE ALIASES

When you join multiple tables, table aliases shorten your code and improve readability. They are declared right after the table name in the `FROM` clause.

```sql
SELECT s.name, s.rank
FROM soldiers AS s
WHERE s.salary > 3000;
```

`AS` is optional for table aliases; you can simply write `FROM soldiers s`. But using `AS` is clearer for learning.

---

## 🧱 COMPUTED COLUMNS

You can perform arithmetic, string concatenation, and function calls directly in the `SELECT` list. The result appears as a new column in the output.

```sql
-- Calculate annual salary
SELECT name, salary * 12 AS annual_salary
FROM soldiers;

-- Total value of each inventory item
SELECT product_name,
       quantity * unit_price AS total_value
FROM inventory;

-- Concatenate strings
SELECT first_name || ' ' || last_name AS full_name
FROM citizens;
```

> 💡 **INSIGHT:** Computed columns are not stored in the database; they are calculated every time the query runs. For frequently used calculations, consider a **generated column** (SQLite 3.31+) or a **view** (Module 7).

> ⚠️ **WARNING:** You cannot use a column alias in the `WHERE` clause of the same query. The `WHERE` is evaluated before the `SELECT`. You must repeat the expression: `WHERE quantity * unit_price > 100`.

---

## 💡 Real‑world Usage

**Banking – show balance in multiple currencies**
```sql
SELECT holder,
       balance AS balance_usd,
       balance * 0.85 AS balance_eur
FROM accounts;
```

**E‑commerce – compute order totals**
```sql
SELECT order_id,
       quantity * unit_price AS line_total
FROM order_items;
```

**Logistics – calculate volumetric weight**
```sql
SELECT tracking_id,
       length * width * height / 5000 AS volumetric_weight
FROM packages;
```

**HR – generate email addresses**
```sql
SELECT first_name || '.' || last_name || '@company.com' AS email
FROM employees;
```

---

## 🔍 Practice Preview
You will rename columns and compute new values directly in your queries.

| Level | Task |
|-------|------|
| Easy | Select soldier names with an alias `soldier_name`. |
| Medium | Compute `annual_salary` as `salary * 12` and display alongside name. |
| Hard | Concatenate `first_name` and `last_name` into `full_name`, then sort by it. |

Run the coach:
```bash
python ii_Practice_Sheets/L14_Aliases_AS_Computed_Columns.py
```

---

## 📌 Key Takeaway
- `AS` renames columns or tables in query output.
- Computed columns calculate values on the fly without altering the table.
- Use underscores in aliases for phone‑friendly code.
- Aliases are not available in `WHERE` – repeat the expression there.

*For Emperor.*