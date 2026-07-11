# 📘 SQLPhone Emperor v3.0 · Module 1
# 📖 L04 – INSERT INTO – Single & Multi‑row, RETURNING

---

## 🎯 OBJECTIVE — What You Will Master

> After this lesson, you’ll populate your tables with data using the full power of `INSERT`.

- ➕ **Single‑row INSERT** – add one record at a time
- ✖️ **Multi‑row INSERT** – add many records in one statement
- 🔄 **RETURNING clause** – capture auto‑generated IDs instantly
- 🧪 **Column lists** – always specify columns for safety

---

## 🧱 SINGLE‑ROW INSERT

The basic syntax inserts one complete row. If you omit the column list,
you must supply values for every column in the exact order they were defined.

```sql
INSERT INTO soldiers (id, name, rank)
VALUES (1, 'Emperor', 'General');
```

If `id` is `INTEGER PRIMARY KEY`, you can pass `NULL` and SQLite will
auto‑assign the next integer:

```sql
INSERT INTO soldiers (id, name, rank)
VALUES (NULL, 'Rahim', 'Private');
```

Always list your columns explicitly — it protects your statement if the
table structure changes later.

---

## 🧱 MULTI‑ROW INSERT

Add multiple rows in a single `INSERT` for speed and clarity:

```sql
INSERT INTO soldiers (name, rank)
VALUES
    ('Karim', 'Sergeant'),
    ('Ali', 'Corporal'),
    ('Hasan', 'Private');
```

All three rows are added in one atomic operation.

---

## 🧱 THE RETURNING CLAUSE

SQLite 3.35+ supports `RETURNING`, which gives you back the generated
primary key (or any column) immediately after the insert:

```sql
INSERT INTO soldiers (name, rank)
VALUES ('Akbar', 'Major')
RETURNING id;
```

This returns a single row with the new `id`. No separate `SELECT` needed.

**Business example – create an account and get the account number:**
```sql
INSERT INTO accounts (holder, balance)
VALUES ('Emperor', 5000.00)
RETURNING account_id;
```

> ⚠️ **WARNING:** Without a column list, you must supply values for
> **all** columns, including auto‑generated ones, which is error‑prone.
> Always use explicit column lists.

> 💡 **INSIGHT:** Multi‑row inserts are **much faster** than many
> single inserts. When seeding test data or importing records,
> batch them together.

---

## 💡 Real‑world Usage

**Banking – open multiple accounts at once**
```sql
INSERT INTO accounts (holder, balance)
VALUES
    ('Emperor', 5000.00),
    ('Rahim', 3200.00),
    ('Karim', 1500.00);
```

**E‑commerce – add products to catalog**
```sql
INSERT INTO products (sku, name, price)
VALUES
    ('SKU-001', 'Wireless Mouse', 24.99),
    ('SKU-002', 'Keyboard', 49.99),
    ('SKU-003', 'Monitor', 199.99);
```

**Logistics – register new shipments**
```sql
INSERT INTO shipments (tracking_id, destination, weight_kg)
VALUES
    ('TRK-100', 'Dhaka', 12.5),
    ('TRK-101', 'Chittagong', 8.3)
RETURNING tracking_id;
```

---

## 🔍 Practice Preview
You will insert data into the Imperial Army’s database using all three techniques.

| Level | Task |
|-------|------|
| Easy | Insert one soldier with explicit column list and query the table. |
| Medium | Insert three soldiers in one multi‑row `INSERT`. |
| Hard | Insert a soldier and capture the generated `id` with `RETURNING`. |

Run the coach:
```bash
python ii_Practice_Sheets/L04_INSERT_INTO_Single_Multi_Row_RETURNING.py
```

---

## 📌 Key Takeaway
- Always use an explicit column list in `INSERT`.
- Multi‑row inserts are faster and cleaner for bulk data.
- `RETURNING` captures auto‑generated values in a single round trip.
- Populate your tables fearlessly — constraints will guard the quality.

*For Emperor.*