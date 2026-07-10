# 📘 SQLPhone Emperor · Module 01  
# 📖 L‑04 – Data Types in SQLite (The Imperial Supply Depot)

---

## 🎯 OBJECTIVE  
Master SQLite’s five storage classes and type affinity system.  
Build the Imperial Supply Depot’s `products` table — a real inventory schema with integers, text, real numbers, and binary blobs.  
You’ll understand exactly how SQLite stores each value and how to protect your data with strict typing.

---

## 🧱 BRICK 1 – The Five Storage Classes & Your First Depot Table

SQLite doesn’t have rigid column types like other databases.  
Instead, every value belongs to one of five **storage classes**:

| Storage Class | What It Holds | Depot Example |
|---------------|---------------|---------------|
| NULL | Missing or unknown | A product with no photo yet |
| INTEGER | Whole number | `id`, `quantity` |
| REAL | Decimal number | `price` |
| TEXT | Character string | `name` |
| BLOB | Binary data exactly as given | `photo` (e.g., X-ray image of the item) |

**① Create the imperial products table (Easy practice)**
```sql
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL,
    quantity INTEGER,
    photo BLOB
);
```
- `id INTEGER PRIMARY KEY` – unique item identifier, auto‑assigns if you insert NULL.
- `name TEXT NOT NULL` – every product must have a name.
- `price REAL` – decimal numbers for currency.
- `quantity INTEGER` – whole units in stock.
- `photo BLOB` – binary image data (we’ll use `X'0000'` as a placeholder).

**② Check the table structure**
```sql
.tables
.schema products
```
You’ll see the exact `CREATE` statement above.

> 💡 **INSIGHT:** The column types (`INTEGER`, `TEXT`, `REAL`, `BLOB`) are **affinity suggestions**, not hard rules. SQLite will try to store whatever you give it in the most appropriate way — but relying on this flexibility can lead to dirty data.

---

## 🧱 BRICK 2 – Type Affinity in Practice & Strict Tables

**③ Insert a real product (Medium practice)**
```sql
INSERT INTO products VALUES (1, 'Widget', 9.99, 100, X'0000');
```
- `X'0000'` is a hex literal — a tiny BLOB.
- `9.99` is stored as REAL.
- `100` is stored as INTEGER.

Verify:
```sql
SELECT * FROM products;
```
You’ll see the row exactly as inserted.

**④ Insert a second product and sort by price (Hard practice)**
```sql
INSERT INTO products VALUES (2, 'Gadget', 19.99, 50, X'1111');
```
Now view all products sorted from most expensive to cheapest:
```sql
SELECT * FROM products ORDER BY price DESC;
```
Because `price` has REAL affinity, numeric ordering works correctly — Gadget (19.99) comes before Widget (9.99).

**⑤ What happens if you misuse types?**
SQLite’s flexibility means this “works”:
```sql
INSERT INTO products VALUES (3, 'Sprocket', 'cheap', 'many', NULL);
```
- `'cheap'` stored as TEXT in the `price` column.
- `'many'` stored as TEXT in the `quantity` column.
- No error is thrown — but sorting by price now breaks, and arithmetic fails.

**⑥ Enforce strict typing with `STRICT` tables (SQLite 3.37+)**
```sql
CREATE TABLE products_strict (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL,
    quantity INTEGER,
    photo BLOB
) STRICT;
```
Now inserting `'cheap'` into a REAL column raises an error. The depot rejects bad supplies.

> ⚠️ **WARNING:** The `products` table in your practice is **not** strict — it’s the default flexible mode. For Companion’s memory database, use `STRICT` to guarantee data integrity.

> 💡 **ADVANCED TIP – BLObs for Companion’s memory:**  
> BLOB columns can store embeddings, audio snippets, or encrypted memory fragments. That’s how Companion will store the raw data behind its infinite memory.

---

## 💡 Real‑world Usage

**Banking – strict account ledger**
```sql
CREATE TABLE accounts (
    id INTEGER PRIMARY KEY,
    balance REAL NOT NULL
) STRICT;
INSERT INTO accounts VALUES (1, 5000.00);
```

**E‑commerce – flexible product catalog**
```sql
CREATE TABLE catalog (
    sku TEXT,
    price REAL,
    description TEXT
);
INSERT INTO catalog VALUES ('SKU-1', 24.99, 'Wireless Mouse');
```

**Logistics – binary document storage**
```sql
CREATE TABLE scans (
    tracking_id TEXT,
    document BLOB
);
INSERT INTO scans VALUES ('TRK-123', X'FFD8FFE0'); -- JPEG header
```

---

## 🔍 Practice Preview
You’ll manage the Imperial Supply Depot’s product inventory.

| Level  | Task | What You’ll Write |
|--------|------|-------------------|
| Easy   | Create table `products` (id INT PK, name TEXT NOT NULL, price REAL, quantity INT, photo BLOB). | `CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, price REAL, quantity INTEGER, photo BLOB);` |
| Medium | Insert one row: `(1, 'Widget', 9.99, 100, X'0000')`. | `INSERT INTO products VALUES (1, 'Widget', 9.99, 100, X'0000');` |
| Hard   | Insert a second product `(2, 'Gadget', 19.99, 50, X'1111')`. Then SELECT all products sorted by price descending. | `INSERT INTO products VALUES (2, 'Gadget', 19.99, 50, X'1111');` `SELECT * FROM products ORDER BY price DESC;` |

Run the coach:
```bash
python ii_Practice_Sheets/L-04_Data_Types.py
```

---

## 📌 Key Takeaway
- SQLite’s five storage classes: NULL, INTEGER, REAL, TEXT, BLOB.
- Column types are affinities — suggestions, not hard rules — unless you use `STRICT`.
- The `products` table uses every major type; insert and sort demonstrate real behavior.
- For Companion’s memory integrity, use `STRICT` tables to reject bad data at the gate.