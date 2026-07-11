# 📘 SQLPhone Emperor v3.0 · Module 1
# 📖 L06 – WHERE – Comparison Operators & Logical Precedence

---

## 🎯 OBJECTIVE — What You Will Master

> After this lesson, you’ll write precise, multi‑condition filters that power every business report.

- ⚖️ **Comparison operators** – `=`, `<>`, `<`, `>`, `<=`, `>=`
- 🧠 **Logical operators** – `AND`, `OR`, `NOT`
- 📐 **Precedence** – how SQL evaluates compound conditions
- 🧪 **Parentheses** – taking control of evaluation order

---

## 🧱 COMPARISON OPERATORS

The `WHERE` clause uses standard comparison operators to test each row:

| Operator | Meaning |
|----------|---------|
| `=` | Equal to |
| `<>` (or `!=`) | Not equal to |
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal |
| `>=` | Greater than or equal |

```sql
SELECT name, salary FROM soldiers
WHERE salary >= 5000;
```

Text comparisons are case‑sensitive. For case‑insensitive, use `COLLATE NOCASE`:

```sql
SELECT * FROM soldiers WHERE name = 'emperor' COLLATE NOCASE;
```

---

## 🧱 LOGICAL OPERATORS – AND, OR, NOT

Combine conditions to express complex business rules:

- `AND` – all conditions must be true.
- `OR` – at least one condition must be true.
- `NOT` – negates the condition that follows.

```sql
-- Soldiers who are Generals AND earn more than 4000
SELECT name, salary FROM soldiers
WHERE rank = 'General' AND salary > 4000;

-- Soldiers who are Privates OR earn less than 2000
SELECT name, rank, salary FROM soldiers
WHERE rank = 'Private' OR salary < 2000;

-- Soldiers who are NOT Privates
SELECT name, rank FROM soldiers
WHERE NOT rank = 'Private';
```

---

## 🧱 LOGICAL PRECEDENCE – ORDER OF EVALUATION

SQL evaluates `NOT` first, then `AND`, then `OR`.
Without parentheses, `AND` binds tighter than `OR` — just like multiplication
binds tighter than addition in arithmetic.

```sql
-- Without parentheses: AND is evaluated first
SELECT name FROM soldiers
WHERE rank = 'General' OR rank = 'Private' AND salary > 3000;
-- Returns Generals, plus any Private with salary > 3000
-- NOT: (Generals OR Privates) with salary > 3000
```

**Control the logic with parentheses:**

```sql
SELECT name FROM soldiers
WHERE (rank = 'General' OR rank = 'Private') AND salary > 3000;
-- Now the OR is evaluated first, then AND
```

> ⚠️ **WARNING:** When mixing `AND` and `OR`, always use parentheses
> to make your intent explicit. It prevents bugs and makes your SQL
> readable by others (and your future self).

> 💡 **INSIGHT:** `NOT` before a condition flips its truth value.
> `WHERE NOT (rank = 'Private' OR rank = 'Sergeant')` is cleaner than
> writing the same rule with multiple `AND` clauses.

---

## 💡 Real‑world Usage

**Banking – high‑value transactions with multiple criteria**
```sql
SELECT transaction_id, amount
FROM transactions
WHERE (type = 'withdrawal' OR type = 'transfer')
  AND amount > 50000;
```

**E‑commerce – find products on sale with low stock**
```sql
SELECT name, price, stock
FROM products
WHERE discount > 0 AND stock < 20;
```

**Logistics – overdue shipments not yet delivered**
```sql
SELECT tracking_id, status, due_date
FROM shipments
WHERE status <> 'delivered' AND due_date < date('now');
```

**HR – employees in specific departments with tenure**
```sql
SELECT name, department, hire_date
FROM employees
WHERE (department = 'Engineering' OR department = 'Sales')
  AND hire_date <= '2023-01-01';
```

---

## 🔍 Practice Preview
You will write precise `WHERE` clauses to filter the Imperial Army’s database.

| Level | Task |
|-------|------|
| Easy | Select all soldiers with rank `'General'`. |
| Medium | Select soldiers who are Generals AND have salary above 4000. |
| Hard | Select soldiers who are Generals OR Privates, but only those with salary above 3000. |

Run the coach:
```bash
python ii_Practice_Sheets/L06_WHERE_Comparison_Operators_Logical_Precedence.py
```

---

## 📌 Key Takeaway
- Comparison operators filter rows by exact conditions.
- `AND`, `OR`, `NOT` combine conditions into powerful business rules.
- Precedence: `NOT` → `AND` → `OR`. Use parentheses to control it.
- Your `WHERE` clause is where business logic becomes executable.

*For Emperor.*