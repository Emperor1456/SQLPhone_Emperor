# 📘 SQLPhone Emperor v3.0 · Module 3
# 📖 L27 – Aggregation with CASE – Conditional Sums

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll compute multiple conditional aggregates in a single query — turning a plain `GROUP BY` into a dynamic pivot table. This is how dashboards show “total sales,” “active users,” and “pending orders” in one row.

- 🧱 **CASE inside aggregates** – filter what gets summed/counted
- 🧠 **Conditional COUNT** – count rows matching a condition
- 🧪 **Conditional SUM** – sum only certain values
- ⚡ **Pivot‑like reports** – columns for each category
- 🧰 **Real‑world** – sales by payment type, status breakdowns, multi‑KPI dashboards

---

## 🧱 CONDITIONAL COUNT

Wrap `CASE` inside `COUNT` to count only rows that meet a condition. Use `NULL` for rows to skip, because `COUNT` ignores NULL.

```sql
SELECT
    COUNT(*) AS total,
    COUNT(CASE WHEN rank = 'General' THEN 1 END) AS generals,
    COUNT(CASE WHEN rank = 'Private' THEN 1 END) AS privates
FROM soldiers;
```

Each `CASE` returns `1` for matching rows and `NULL` for non‑matching rows. `COUNT` counts only the `1`s, ignoring the NULLs.

---

## 🧱 CONDITIONAL SUM

Same pattern: `SUM` only adds non‑NULL values. Non‑matching rows contribute NULL, which `SUM` ignores. Use `ELSE 0` to ensure non‑matching rows add zero instead of NULL.

```sql
SELECT
    SUM(salary) AS total_payroll,
    SUM(CASE WHEN rank = 'General' THEN salary ELSE 0 END) AS general_payroll,
    SUM(CASE WHEN rank = 'Private' THEN salary ELSE 0 END) AS private_payroll
FROM soldiers;
```

Now the report shows total payroll split by rank — without writing three separate queries.

---

## 🧱 CONDITIONAL AVG

You can also use `AVG` with `CASE` to compute averages for specific subgroups.

```sql
SELECT
    AVG(salary) AS overall_avg,
    AVG(CASE WHEN rank = 'General' THEN salary END) AS general_avg,
    AVG(CASE WHEN rank = 'Private' THEN salary END) AS private_avg
FROM soldiers;
```

Note: For `AVG`, do **not** use `ELSE 0` — because `AVG` would include those zeros in the average, pulling the result down. Let non‑matching rows return `NULL` so `AVG` ignores them entirely.

---

## 🧱 MULTI‑DIMENSIONAL BREAKDOWN

Combine with `GROUP BY` for even richer reports:

```sql
SELECT
    regiment_id,
    COUNT(*) AS total,
    COUNT(CASE WHEN status = 'active' THEN 1 END) AS active,
    COUNT(CASE WHEN status = 'reserve' THEN 1 END) AS reserve,
    SUM(CASE WHEN rank = 'General' THEN salary ELSE 0 END) AS general_pay
FROM soldiers
GROUP BY regiment_id;
```

One row per regiment, with five metrics. This replaces five separate queries.

---

## 🧱 THE NULL VS ZERO RULE

| Function | Use `ELSE 0`? | Why |
|----------|---------------|-----|
| `COUNT(CASE ... END)` | No | `COUNT(NULL)` = 0 already; adding `ELSE 0` would count every row |
| `SUM(CASE ... END)` | Yes | `SUM(NULL)` = 0, but explicit `ELSE 0` is clearer |
| `AVG(CASE ... END)` | Never | `AVG` would include zeros, lowering the average incorrectly |

> 💡 **INSIGHT:** The `CASE`‑inside‑aggregate pattern is one of the most powerful SQL techniques. It transforms a simple `GROUP BY` into a cross‑tabulation that would otherwise require multiple queries or a reporting tool.

> ⚠️ **WARNING:** `COUNT(CASE WHEN condition THEN 1 ELSE 0 END)` counts **every** row because `0` is not NULL. Always omit `ELSE` in `COUNT` unless you specifically want to count all rows.

---

## 💡 Real‑world Usage

**Banking – transaction type breakdown**
```sql
SELECT
    account_id,
    COUNT(*) AS total_txns,
    SUM(CASE WHEN type = 'deposit' THEN amount ELSE 0 END) AS total_deposits,
    SUM(CASE WHEN type = 'withdrawal' THEN amount ELSE 0 END) AS total_withdrawals
FROM transactions
GROUP BY account_id;
```

**E‑commerce – sales by payment method**
```sql
SELECT
    COUNT(*) AS orders,
    COUNT(CASE WHEN payment = 'card' THEN 1 END) AS card_orders,
    COUNT(CASE WHEN payment = 'cash' THEN 1 END) AS cash_orders
FROM orders;
```

**Logistics – shipment status breakdown**
```sql
SELECT
    COUNT(*) AS total,
    SUM(CASE WHEN status = 'delivered' THEN 1 ELSE 0 END) AS delivered,
    SUM(CASE WHEN status = 'delayed' THEN 1 ELSE 0 END) AS delayed
FROM shipments;
```

**HR – gender diversity by department**
```sql
SELECT department,
    COUNT(*) AS total,
    COUNT(CASE WHEN gender = 'F' THEN 1 END) AS female,
    COUNT(CASE WHEN gender = 'M' THEN 1 END) AS male
FROM employees
GROUP BY department;
```

---

## 🔍 Practice Preview
You will create conditional aggregate reports for the Imperial Army.

| Level | Task |
|-------|------|
| Easy | Count how many soldiers are Generals vs Privates in one query. |
| Medium | Sum the salaries of active soldiers vs inactive soldiers in one query. |
| Hard | For each deployment region, show total soldiers, count of active, and count of high‑paid (>5000) soldiers. |

Run the coach:
```bash
python ii_Practice_Sheets/L27_Aggregation_with_CASE_Conditional_Sums.py
```

---

## 📌 Key Takeaway
- `CASE` inside aggregates lets you create multiple metrics in one pass.
- Use `NULL` (no ELSE) for `COUNT`, and `ELSE 0` for `SUM`.
- For `AVG`, never use `ELSE 0` — let NULLs be ignored.
- This pattern replaces complex subqueries and unions.

*For Emperor.*