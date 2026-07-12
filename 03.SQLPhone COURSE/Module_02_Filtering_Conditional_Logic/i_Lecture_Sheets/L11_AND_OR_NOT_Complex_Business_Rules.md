# 📘 SQLPhone Emperor v3.0 · Module 2
# 📖 L11 – AND, OR, NOT – Complex Business Rules

---

## 🎯 OBJECTIVE — What You Will Master

> Combine multiple conditions to filter data with surgical precision — the core of every business report.

- 🔗 **AND** – all conditions must be true
- 🔀 **OR** – at least one condition must be true
- 🚫 **NOT** – exclude rows that match a condition
- 🧠 **Logical precedence** – how to control evaluation order with parentheses

---

## 🧱 THE LOGICAL OPERATORS

After mastering the basic `WHERE` clause, you need to combine conditions to express real‑world business rules. SQL gives you three operators:

| Operator | Behavior |
|----------|----------|
| `AND` | Row is returned only if **both** conditions are true |
| `OR`  | Row is returned if **at least one** condition is true |
| `NOT` | Row is returned if the condition **is false** |

**Example – soldiers who are active AND high‑paid:**
```sql
SELECT name, salary
FROM soldiers
WHERE status = 'active' AND salary > 4000;
```

**Example – soldiers who are either Generals OR earn above 5000:**
```sql
SELECT name, rank, salary
FROM soldiers
WHERE rank = 'General' OR salary > 5000;
```

**Example – soldiers who are NOT deployed:**
```sql
SELECT name, deployment
FROM soldiers
WHERE NOT deployment = 'active';
```

---

## 🧱 LOGICAL PRECEDENCE & PARENTHESES

When mixing `AND` and `OR`, `AND` takes higher precedence — it “binds tighter” than `OR`. Without parentheses, you may get unexpected results.

```sql
-- This returns Generals + any high‑paid Private
SELECT name FROM soldiers
WHERE rank = 'General' OR rank = 'Private' AND salary > 3000;

-- What you probably meant: Generals or Privates, but only if salary > 3000
SELECT name FROM soldiers
WHERE (rank = 'General' OR rank = 'Private') AND salary > 3000;
```

> ⚠️ **WARNING:** Never rely on default precedence alone – always use parentheses to make your intent explicit. It protects you and anyone reading your code.

> 💡 **INSIGHT:** `NOT` negates the entire condition that follows it. `NOT (rank = 'General' AND salary > 5000)` means “not both a General and high‑paid”, which is different from `NOT rank = 'General' AND salary > 5000`.

---

## 💡 Real‑world Usage

**Banking – suspicious transactions**
```sql
SELECT transaction_id, amount
FROM transactions
WHERE (amount > 100000 OR country <> 'BD')
  AND status = 'pending';
```

**E‑commerce – clearance sale filtering**
```sql
SELECT product_name, price, stock
FROM products
WHERE (category = 'Electronics' OR category = 'Accessories')
  AND discount > 20
  AND stock > 0;
```

**Logistics – delayed or high‑priority shipments**
```sql
SELECT tracking_id, priority, status
FROM shipments
WHERE (status = 'delayed' OR priority = 'high')
  AND NOT destination = 'local';
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
You will combine multiple conditions to filter the Imperial inventory and soldier records.

| Level | Task |
|-------|------|
| Easy | Select all products that are Electronics AND in stock. |
| Medium | Select products that are either Electronics or have a discount > 20. |
| Hard | Select soldiers who are NOT deployed AND (Generals OR salary > 5000). |

Run the coach:
```bash
python ii_Practice_Sheets/L11_AND_OR_NOT_Complex_Business_Rules.py
```

---

## 📌 Key Takeaway
- `AND` requires all conditions true, `OR` requires at least one, `NOT` flips the result.
- `AND` binds tighter than `OR`; use parentheses to control precedence.
- Complex business rules become readable, executable SQL.

*For Emperor.*