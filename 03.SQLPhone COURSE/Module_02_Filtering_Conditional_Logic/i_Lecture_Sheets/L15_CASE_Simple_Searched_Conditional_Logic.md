# 📘 SQLPhone Emperor v3.0 · Module 2
# 📖 L15 – CASE – Simple & Searched Conditional Logic

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll embed if‑then‑else logic directly inside your SQL queries — no Python required. This is how you classify customers, categorize products, and label transactions in a single pass.

- 🧠 **Simple CASE** – compare a single expression against a list of values
- 🔍 **Searched CASE** – evaluate multiple independent conditions
- 🧪 **Use cases** – dynamic labels, conditional aggregation, data categorization
- ⚡ **CASE in SELECT, WHERE, ORDER BY** – versatile placement
- 🛡️ **Execution order** – stops at the first matching `WHEN`

---

## 🧱 SIMPLE CASE – ONE EXPRESSION, MANY MATCHES

The simple `CASE` form evaluates one expression and returns the first matching `WHEN` result. If no match, the `ELSE` clause (if provided) kicks in. Without `ELSE`, unmatched rows return `NULL`.

```sql
SELECT name,
       CASE rank
           WHEN 'General' THEN 'Top Brass'
           WHEN 'Colonel' THEN 'Senior Officer'
           WHEN 'Private' THEN 'Enlisted'
           ELSE 'Other'
       END AS category
FROM soldiers;
```

This reads: “Look at the `rank` column. If it’s 'General', return 'Top Brass', etc.”

---

## 🧱 SEARCHED CASE – MULTIPLE CONDITIONS

The searched `CASE` form evaluates each `WHEN` condition independently; the first true condition’s result is returned.

```sql
SELECT name, salary,
       CASE
           WHEN salary >= 5000 THEN 'High'
           WHEN salary >= 3000 THEN 'Medium'
           ELSE 'Low'
       END AS pay_band
FROM soldiers;
```

You can combine multiple columns in the conditions:

```sql
SELECT product_name, quantity,
       CASE
           WHEN quantity = 0 THEN 'Out of Stock'
           WHEN quantity < 20 THEN 'Low Stock'
           WHEN quantity < 50 THEN 'Moderate'
           ELSE 'Well Stocked'
       END AS stock_status
FROM inventory;
```

---

## 🧱 CASE IN OTHER CLAUSES

**In ORDER BY – custom sorting:**
```sql
SELECT name, rank
FROM soldiers
ORDER BY
    CASE rank
        WHEN 'General' THEN 1
        WHEN 'Colonel' THEN 2
        WHEN 'Private' THEN 3
        ELSE 4
    END;
```

**In WHERE – complex conditional filtering (use sparingly):**
```sql
SELECT * FROM soldiers
WHERE CASE
    WHEN rank = 'General' THEN salary > 4000
    ELSE salary > 2000
END;
```

> ⚠️ **WARNING:** `CASE` stops evaluating at the first true `WHEN`. Order your conditions carefully, just like `if‑elif‑else` in Python. Put the most specific conditions first.

> 💡 **INSIGHT:** `CASE` returns a value — you can use it anywhere a value is expected: `SELECT`, `WHERE`, `ORDER BY`, even inside aggregate functions (see L27).

---

## 💡 Real‑world Usage

**Banking – categorize transactions**
```sql
SELECT amount,
       CASE
           WHEN amount > 10000 THEN 'Large'
           WHEN amount > 5000 THEN 'Medium'
           ELSE 'Small'
       END AS txn_size
FROM transactions;
```

**E‑commerce – seasonal discount labeling**
```sql
SELECT product_name,
       CASE
           WHEN discount >= 30 THEN 'Clearance'
           WHEN discount >= 15 THEN 'Sale'
           ELSE 'Regular Price'
       END AS promotion
FROM products;
```

**Logistics – delivery priority**
```sql
SELECT tracking_id,
       CASE
           WHEN priority = 'high' AND status = 'delayed' THEN 'Critical'
           WHEN priority = 'high' THEN 'Rush'
           ELSE 'Standard'
       END AS handling
FROM shipments;
```

**HR – tenure classification**
```sql
SELECT name, hire_date,
       CASE
           WHEN hire_date <= '2020-01-01' THEN 'Senior'
           WHEN hire_date <= '2023-01-01' THEN 'Mid'
           ELSE 'Junior'
       END AS tenure
FROM employees;
```

---

## 🔍 Practice Preview
You will apply `CASE` logic to label, categorize, and sort data.

| Level | Task |
|-------|------|
| Easy | Write a simple `CASE` to map soldier ranks to categories (Top Brass, Senior Officer, Enlisted). |
| Medium | Write a searched `CASE` to classify salaries into High, Medium, Low. |
| Hard | Use `CASE` inside `ORDER BY` to sort soldiers by rank priority (General first, Private last). |

Run the coach:
```bash
python ii_Practice_Sheets/L15_CASE_Simple_Searched_Conditional_Logic.py
```

---

## 📌 Key Takeaway
- Simple `CASE` compares one expression; searched `CASE` evaluates multiple conditions.
- `CASE` returns a value — use it anywhere in a query.
- Order `WHEN` clauses from most specific to least specific.
- This is the SQL equivalent of Python’s `if‑elif‑else`.

*For Emperor.*