# 📘 SQLPhone Emperor · Module 01  
# 📖 L‑07 – Basic SELECT (Imperial Supply Inventory)

---

## 🎯 OBJECTIVE  
Master the fundamental `SELECT` statement to retrieve and compute data.  
You’ll query the Imperial Supply Depot’s `inventory` table — selecting specific columns, filtering with `WHERE`, calculating line totals, and sorting results.  
Every report, dashboard, and data feed begins with a `SELECT`.

---

## 🧱 BRICK 1 – Projection: Choosing Columns

`SELECT` performs **projection** — picking which columns to return.  
Use `*` only for ad‑hoc checks; in real queries, list columns explicitly.

**① Create the inventory table and stock the depot (Easy practice)**
```sql
CREATE TABLE inventory (
    id INTEGER PRIMARY KEY,
    product TEXT,
    quantity INTEGER,
    price REAL
);

INSERT INTO inventory (product, quantity, price)
VALUES
    ('A', 10, 1.0),
    ('B', 5, 2.0),
    ('C', 0, 3.0);
```
Three products: A is well‑stocked, B has moderate stock, C is out of stock.

**② Select all columns (quick check)**
```sql
SELECT * FROM inventory;
```
You’ll see all rows. This is fine for exploration, but in production, always choose columns.

**③ Select specific columns (projection)**
```sql
SELECT product, quantity FROM inventory;
```
Now only product names and quantities appear — a focused report.

**④ Compute a column: total value of each product in stock**
```sql
SELECT product, quantity * price AS total_value
FROM inventory;
```
- `quantity * price` is an arithmetic expression calculated per row.
- `AS total_value` aliases the result column — it appears as a readable header.

> 💡 **INSIGHT:** `SELECT` can transform data on the fly. You’re not just retrieving raw columns — you’re building reports.

---

## 🧱 BRICK 2 – Selection: Filtering Rows with WHERE

`WHERE` filters rows that satisfy a condition.  
Comparison operators: `=`, `<>` (or `!=`), `<`, `>`, `<=`, `>=`.

**⑤ Show only products that are in stock (Medium practice)**
```sql
SELECT product, quantity * price AS total_value
FROM inventory
WHERE quantity > 0;
```
Rows with `quantity = 0` (product C) are excluded.  
Only A and B appear with their total values.

**⑥ Sort the report by total value, highest first (Hard practice)**
```sql
SELECT product, quantity * price AS total_value
FROM inventory
WHERE quantity > 0
ORDER BY total_value DESC;
```
- `ORDER BY total_value DESC` sorts from largest to smallest.
- Product B (total 10.0) appears before Product A (total 10.0? Actually A: 10*1.0=10, B:5*2.0=10, both 10; stable sort keeps insertion order).
- For a stronger sort, add a second column: `ORDER BY total_value DESC, product ASC`.

**⑦ Further refine: only products with total > 5**
```sql
SELECT product, quantity * price AS total_value
FROM inventory
WHERE quantity > 0 AND quantity * price > 5;
```
Now only rows where the computed total exceeds 5 appear. Both A and B qualify.

> ⚠️ **WARNING:** You cannot use column aliases in the `WHERE` clause — `WHERE total_value > 5` will fail because `total_value` is defined in the `SELECT` list, which executes after `WHERE`. Use the raw expression in `WHERE`.

> 💡 **ADVANCED TIP – `COLLATE NOCASE`:**  
> For case‑insensitive text matching, append `COLLATE NOCASE`:
> ```sql
> SELECT * FROM inventory WHERE product = 'a' COLLATE NOCASE;
> ```
> This matches 'A', 'a', etc.

---

## 💡 Real‑world Usage

**Banking – list accounts with balance over threshold**
```sql
SELECT account_id, balance
FROM accounts
WHERE balance > 1000
ORDER BY balance DESC;
```

**E‑commerce – products under $20 with stock**
```sql
SELECT name, price, quantity
FROM products
WHERE price < 20 AND quantity > 0;
```

**Logistics – shipments to a specific city**
```sql
SELECT tracking_id, weight
FROM shipments
WHERE destination = 'Dhaka'
ORDER BY weight DESC;
```

**HR – employees hired after a date**
```sql
SELECT name, department
FROM employees
WHERE hired >= '2026-01-01';
```

---

## 🔍 Practice Preview
You will query the Imperial Supply Depot’s `inventory` table.

| Level  | Task | What You’ll Write |
|--------|------|-------------------|
| Easy   | Create `inventory` (id PK, product, quantity, price). Insert 3 products. | `CREATE TABLE inventory ...` and multi‑row `INSERT` |
| Medium | Show product name and total value (`quantity*price`) for items with quantity > 0. | `SELECT product, quantity*price AS total_value FROM inventory WHERE quantity > 0;` |
| Hard   | Enhance the query: sort by total value descending, and only show products where total > 5. | `SELECT ... WHERE quantity > 0 AND quantity*price > 5 ORDER BY total_value DESC;` |

Run the coach:
```bash
python ii_Practice_Sheets/L-07_Basic_SELECT.py
```

---

## 📌 Key Takeaway
- `SELECT` columns from a table; use `*` sparingly.
- `AS` gives computed columns meaningful names.
- `WHERE` filters rows before projection and sorting.
- `ORDER BY` sorts the final result set.
- Combine projection, filtering, and sorting to build precise reports — the daily work of any data professional.