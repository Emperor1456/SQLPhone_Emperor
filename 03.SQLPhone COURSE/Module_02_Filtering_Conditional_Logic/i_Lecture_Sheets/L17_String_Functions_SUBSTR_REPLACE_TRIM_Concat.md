# 📘 SQLPhone Emperor v3.0 · Module 2
# 📖 L17 – String Functions – SUBSTR, REPLACE, TRIM, ||

---

## 🎯 OBJECTIVE — What You Will Master

> You’ll manipulate text data directly in SQL — cleaning, extracting, and formatting strings without any Python code. This is how you standardize phone numbers, generate slugs, and build readable reports from raw data.

- ✂️ **SUBSTR** – extract portions of a string
- 🔄 **REPLACE** – swap characters or substrings
- 🧹 **TRIM** – remove unwanted spaces
- ➕ **Concatenation (`||`)** – join strings together
- 🧪 **Combining functions** – powerful text transformations

---

## 🧱 SUBSTR – EXTRACTING TEXT

`SUBSTR(string, start, length)` returns a substring. The first character is position 1 (not 0, unlike Python).

```sql
-- Extract first three characters of a product code
SELECT SUBSTR(product_code, 1, 3) AS prefix FROM inventory;
```

You can omit `length` to get everything from `start` to the end:

```sql
SELECT SUBSTR(email, 5) AS domain_part FROM users;
```

**Business use – extract carrier code from tracking number:**
```sql
SELECT SUBSTR(tracking_id, 1, 3) AS carrier FROM shipments;
```

---

## 🧱 REPLACE – SWAPPING TEXT

`REPLACE(string, old, new)` replaces all occurrences of `old` with `new`.

```sql
-- Standardize phone number format (remove hyphens)
SELECT REPLACE(phone, '-', '') AS clean_phone FROM contacts;

-- Fix product slugs (replace spaces with hyphens)
SELECT REPLACE(product_name, ' ', '-') AS slug FROM products;
```

---

## 🧱 TRIM – REMOVING PADDING

`TRIM(string)` removes leading and trailing spaces. `LTRIM` and `RTRIM` remove only left or right spaces.

```sql
-- Clean user input stored as raw data
SELECT TRIM(raw_input) AS clean_input FROM form_data;
```

---

## 🧱 CONCATENATION (`||`) – JOINING STRINGS

SQLite uses `||` to concatenate strings. Combine columns, literals, and functions in one expression.

```sql
-- Full address from separate fields
SELECT street || ', ' || city || ', ' || country AS full_address FROM households;

-- Generate email addresses
SELECT first_name || '.' || last_name || '@empire.com' AS email FROM citizens;
```

> 💡 **INSIGHT:** String functions let you clean and format data at the database level, ensuring consistent output regardless of which application consumes it. This is far more efficient than fetching raw data and processing in Python.

> ⚠️ **WARNING:** In SQLite, `||` returns NULL if any operand is NULL. Use `COALESCE(first_name, '') || COALESCE(last_name, '')` to avoid losing the entire concatenation due to a single NULL column.

---

## 💡 Real‑world Usage

**Banking – mask account numbers**
```sql
SELECT '****' || SUBSTR(account_number, -4) AS masked FROM accounts;
```

**E‑commerce – generate clean SKU codes**
```sql
SELECT 'SKU-' || REPLACE(UPPER(product_name), ' ', '-') AS sku FROM products;
```

**Logistics – extract carrier from tracking code**
```sql
SELECT SUBSTR(tracking_id, 1, 3) AS carrier FROM shipments;
```

**HR – format employee badge**
```sql
SELECT UPPER(last_name) || ', ' || first_name AS badge_name FROM employees;
```

**Companion – clean conversation text for analysis**
```sql
SELECT TRIM(REPLACE(message, '  ', ' ')) AS clean_message FROM conversations;
```

---

## 🔍 Practice Preview
You will clean and transform text data directly inside SQL queries.

| Level | Task |
|-------|------|
| Easy | Use `||` to concatenate first and last name into a full name. |
| Medium | Extract the first 3 characters of a product code using `SUBSTR`. |
| Hard | Clean a phone number by removing all hyphens with `REPLACE`, then format it as `(XXX) XXX-XXXX` using `SUBSTR` and `||`. |

Run the coach:
```bash
python ii_Practice_Sheets/L17_String_Functions_SUBSTR_REPLACE_TRIM_Concat.py
```

---

## 📌 Key Takeaway
- SQLite string functions let you transform text without leaving the database.
- `SUBSTR`, `REPLACE`, `TRIM`, and `||` are your daily drivers.
- Combine them to build powerful text pipelines in pure SQL.
- Always handle NULL with `COALESCE` when concatenating.

*For Emperor.*