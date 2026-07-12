# 📘 SQLPhone Emperor v3.0 · Module 2
# 📖 L19 – Mathematical Functions & CAST

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll perform numeric calculations and convert data types directly in SQL — turning raw numbers into rounded prices, absolute values, and formatted strings without any Python code.

- 🧮 **Built‑in math functions** – `ABS`, `ROUND`, `MAX`, `MIN`, `RANDOM`
- 🔄 **CAST** – change one data type to another
- 🧪 **Type affinity vs explicit conversion** – when to cast
- ⚡ **Combining math with other clauses** – computed columns, sorting, filtering
- 🛡️ **Precision** – avoiding floating‑point surprises

---

## 🧱 BUILT‑IN MATHEMATICAL FUNCTIONS

SQLite provides a compact set of math functions that work inside any `SELECT`:

| Function | Purpose | Example |
|----------|---------|---------|
| `ABS(x)` | Absolute value | `ABS(-150)` → `150` |
| `ROUND(x, d)` | Round to `d` decimal places | `ROUND(24.995, 1)` → `25.0` |
| `MAX(x, y, …)` | Largest value in the list | `MAX(price, 100)` |
| `MIN(x, y, …)` | Smallest value | `MIN(stock, reorder_limit)` |
| `RANDOM()` | Random integer | Often used with `ABS` and `%` |

```sql
SELECT name,
       salary,
       ROUND(salary * 1.1, 2) AS raised_salary,
       ABS(salary - 5000) AS distance_from_target
FROM soldiers;
```

---

## 🧱 CAST – CONVERTING DATA TYPES

`CAST(expression AS target_type)` explicitly converts one type to another. This is essential when you need to mix types or control how data is interpreted.

```sql
-- Convert an integer to text for concatenation
SELECT 'Employee #' || CAST(id AS TEXT) FROM soldiers;

-- Convert a string to a number before arithmetic
SELECT CAST(price_text AS REAL) * 1.1 FROM imported_products;

-- Convert a float to an integer (truncates, doesn't round)
SELECT CAST(unit_price AS INTEGER) FROM inventory;
```

**Use `CAST` when:**
- Concatenating numbers with strings.
- Performing arithmetic on data imported as TEXT.
- Ensuring the correct type for comparison or sorting.

---

## 🧱 TYPE AFFINITY VS EXPLICIT CONVERSION

SQLite’s type affinity often handles conversions automatically — but relying on this can cause subtle bugs. `CAST` makes your intent explicit and your queries portable.

```sql
-- Affinity: SQLite may convert automatically (fragile)
SELECT '5' * 3;   -- works, returns 15

-- CAST: explicit, portable, safe
SELECT CAST('5' AS INTEGER) * 3;
```

> 💡 **INSIGHT:** `ROUND` is not just for display — use it to control precision in financial calculations. `ROUND(amount * rate, 2)` ensures you never lose a fraction of a taka.

> ⚠️ **WARNING:** `RANDOM()` returns a signed 64‑bit integer — values can be negative. Use `ABS(RANDOM()) % n` to get a positive integer between 0 and n‑1.

---

## 💡 Real‑world Usage

**Banking – round interest calculations**
```sql
SELECT account_id,
       ROUND(balance * rate, 2) AS interest
FROM accounts;
```

**E‑commerce – compute discount and cast to display**
```sql
SELECT product_name,
       CAST(price * (1 - discount/100.0) AS TEXT) || ' USD' AS sale_price
FROM products;
```

**Logistics – calculate volumetric weight and round**
```sql
SELECT tracking_id,
       ROUND((length * width * height) / 5000.0, 1) AS vol_weight
FROM packages;
```

**HR – convert IDs for badge formatting**
```sql
SELECT 'EMP-' || CAST(employee_id AS TEXT) AS badge
FROM employees;
```

**Companion – generate random memory prompts**
```sql
SELECT prompt FROM prompts
ORDER BY RANDOM() LIMIT 1;
```

---

## 🔍 Practice Preview
You will use math functions and casting to transform numeric and text data.

| Level | Task |
|-------|------|
| Easy | Round all salaries to the nearest integer using `ROUND`. |
| Medium | Compute a 10% bonus, then cast it to TEXT and concatenate with a label. |
| Hard | Use `ABS` and `RANDOM` to generate a random number between 1 and 100. |

Run the coach:
```bash
python ii_Practice_Sheets/L19_Mathematical_Functions_CAST.py
```

---

## 📌 Key Takeaway
- `ROUND`, `ABS`, `MAX`, `MIN` handle common math operations.
- `CAST` explicitly converts types — essential for safe arithmetic and concatenation.
- Math functions combine seamlessly with other SQL clauses.
- For precise financial calculations, use `ROUND` to control decimal places.

*For Emperor.*