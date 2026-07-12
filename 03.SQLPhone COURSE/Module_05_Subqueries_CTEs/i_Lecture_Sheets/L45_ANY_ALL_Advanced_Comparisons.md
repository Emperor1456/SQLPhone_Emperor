# 📘 SQLPhone Emperor v3.0 · Module 5
# 📖 L45 – ANY & ALL – Advanced Comparisons

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll compare a single value against an entire set using `ANY` and `ALL` — unlocking a new level of expressiveness in your SQL.

- 🧱 **ANY** – true if the comparison holds for at least one value in the set
- 🧠 **ALL** – true if the comparison holds for every value in the set
- 🧪 **Combined with subqueries** – dynamic thresholds
- ⚡ **Equivalent patterns** – `ANY` ≈ `MIN`, `ALL` ≈ `MAX`

---

## 🧱 THE ANY OPERATOR

`value > ANY (subquery)` is true if `value` is greater than **at least one** value returned by the subquery.

```sql
-- Soldiers whose salary is greater than ANY salary in Regiment 5
SELECT name, salary
FROM soldiers
WHERE salary > ANY (
    SELECT salary FROM soldiers WHERE regiment_id = 5
);
```

This is equivalent to: “salary > the minimum salary in Regiment 5.”

---

## 🧱 THE ALL OPERATOR

`value > ALL (subquery)` is true if `value` is greater than **every** value returned by the subquery.

```sql
-- Soldiers whose salary is greater than ALL salaries in Regiment 5
SELECT name, salary
FROM soldiers
WHERE salary > ALL (
    SELECT salary FROM soldiers WHERE regiment_id = 5
);
```

This is equivalent to: “salary > the maximum salary in Regiment 5.”

---

## 🧱 COMMON PATTERNS

| Pattern | Meaning | Equivalent to |
|---------|---------|---------------|
| `x > ANY (set)` | x > minimum of set | `x > (SELECT MIN(...))` |
| `x > ALL (set)` | x > maximum of set | `x > (SELECT MAX(...))` |
| `x = ANY (set)` | x matches some value | `x IN (set)` |
| `x <> ALL (set)` | x matches no values | `x NOT IN (set)` (with NULL caveat) |

---

## 🧱 REAL‑WORLD EXAMPLE: EXCEEDING ALL BENCHMARKS

```sql
-- Products priced above ALL clearance items (i.e., higher than the most expensive clearance item)
SELECT product_name, price
FROM products
WHERE price > ALL (
    SELECT price FROM products WHERE category = 'Clearance'
);
```

> ⚠️ **WARNING:** `ANY` and `ALL` behave unpredictably with NULLs in the subquery result. If the set is empty, `ALL` returns true and `ANY` returns false. Always verify your subquery data.

> 💡 **INSIGHT:** While `ANY` and `ALL` are standard SQL, many developers prefer `MIN`/`MAX` subqueries for clarity. Use whichever makes your intent most obvious to the next reader.

---

## 💡 Real‑world Usage

**Banking – transactions larger than all previous**
```sql
SELECT transaction_id, amount
FROM transactions
WHERE amount > ALL (
    SELECT amount FROM transactions
    WHERE transaction_date < '2026-01-01'
);
```

**E‑commerce – products more expensive than any luxury item**
```sql
SELECT product_name, price
FROM products
WHERE price > ANY (
    SELECT price FROM products WHERE category = 'Luxury'
);
```

**Logistics – shipments heavier than all standard packages**
```sql
SELECT tracking_id, weight
FROM shipments
WHERE weight > ALL (
    SELECT weight FROM shipments WHERE service_type = 'Standard'
);
```

**HR – employees earning more than all interns**
```sql
SELECT name, salary
FROM employees
WHERE salary > ALL (
    SELECT salary FROM employees WHERE job_title = 'Intern'
);
```

---

## 🔍 Practice Preview
You will compare individual values against sets using `ANY` and `ALL`.

| Level | Task |
|-------|------|
| Easy | Select soldiers whose salary is greater than ANY soldier in Regiment 5. |
| Medium | Select soldiers whose salary is greater than ALL soldiers in Regiment 5. |
| Hard | Select products whose price is greater than ALL products in the 'Clearance' category. |

Run the coach:
```bash
python ii_Practice_Sheets/L45_ANY_ALL_Advanced_Comparisons.py
```

---

## 📌 Key Takeaway
- `ANY` tests if the condition is true for at least one set member.
- `ALL` tests if the condition is true for every set member.
- Often replaceable by `MIN`/`MAX` subqueries for clarity.

*For Emperor.*