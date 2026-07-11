# 📘 SQLPhone Emperor v3.0 · Module 1
# 📖 L09 – Module Practice: Build a Table and Query It

---

## 🎯 OBJECTIVE — What You Will Master

> After this lesson, you’ll integrate everything from L01–L08 into one complete, polished database workflow.

- 🏗️ **Design a table** – choose columns, types, and constraints
- ➕ **Insert test data** – seed multiple rows in one statement
- 🔍 **Query with filters** – `WHERE`, `ORDER BY`, `LIMIT`
- 📄 **Document your work** – comments and professional formatting
- 🧪 **Inspect** – use dot‑commands to verify everything

---

## 🧱 THE IMPERIAL INVENTORY CHALLENGE

The Emperor needs a warehouse inventory system.
You will create the `inventory` table from scratch, seed it with products,
and run business queries against it.

### Step 1 – Design the table
```sql
CREATE TABLE inventory (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    quantity INTEGER DEFAULT 0 CHECK(quantity >= 0),
    unit_price REAL NOT NULL CHECK(unit_price > 0),
    last_restocked TEXT DEFAULT (date('now'))
);
```

### Step 2 – Seed the table with 5 products
```sql
INSERT INTO inventory (product_name, category, quantity, unit_price)
VALUES
    ('Wireless Mouse', 'Electronics', 150, 24.99),
    ('Keyboard', 'Electronics', 85, 49.99),
    ('Notebook', 'Stationery', 300, 3.50),
    ('Desk Lamp', 'Furniture', 40, 35.00),
    ('Pen Set', 'Stationery', 500, 12.00);
```

### Step 3 – Run business queries
**① Products low in stock (less than 50 units)**
```sql
SELECT product_name, quantity
FROM inventory
WHERE quantity < 50
ORDER BY quantity ASC;
```

**② Total value of each product (quantity × price)**
```sql
SELECT product_name,
       quantity * unit_price AS total_value
FROM inventory
ORDER BY total_value DESC;
```

**③ Top 3 most expensive products**
```sql
SELECT product_name, unit_price
FROM inventory
ORDER BY unit_price DESC
LIMIT 3;
```

**④ Count of products per category**
```sql
SELECT category, COUNT(*) AS product_count
FROM inventory
GROUP BY category;
```

---

## 🧱 INSPECT & VERIFY

After creating and querying, always check your work:

```bash
sqlite> .tables
sqlite> .schema inventory
sqlite> .headers on
sqlite> .mode column
sqlite> SELECT * FROM inventory;
```

> 💡 **INSIGHT:** This workflow — **design → seed → query → inspect** — is the
> daily rhythm of every backend developer. It never changes, whether you’re
> building a phone app or a billion‑dollar platform.

---

## 💡 Real‑world Usage

**Banking – create a transactions table with seed data**
```sql
CREATE TABLE transactions ( ... );
INSERT INTO transactions VALUES ( ... ), ( ... );
SELECT * FROM transactions WHERE amount > 1000;
```

**E‑commerce – inventory with low‑stock alerts**
```sql
SELECT product_name FROM inventory WHERE quantity < 25;
```

**Logistics – seed and query shipment data**
```sql
INSERT INTO shipments VALUES ( ... );
SELECT tracking_id FROM shipments WHERE status = 'delayed';
```

---

## 🔍 Practice Preview
You will reproduce the Imperial Inventory workflow from scratch — design, seed, query, inspect.

| Level | Task |
|-------|------|
| Easy | Create the `inventory` table with all columns and constraints. |
| Medium | Insert 5 products and run a query to find all products with quantity below 50. |
| Hard | Compute the total value of each product (quantity × price) and display the top 3 by value. |

Run the coach:
```bash
python ii_Practice_Sheets/L09_Module_Practice_Build_Table_and_Query_It.py
```

---

## 📌 Key Takeaway
- A complete database task involves design, seed, query, and inspection.
- Integrate `CREATE TABLE`, `INSERT`, `SELECT`, `WHERE`, `ORDER BY`, and `LIMIT` in one workflow.
- Always use constraints to protect your data from the start.

*For Emperor.*