# 📘 SQLPhone Emperor v3.0 · Module 9
# 📖 L82 – E‑commerce Inventory Tracker

---

## 🎯 OBJECTIVE — What You Will Master

> Build a complete inventory management system for an online store — tracking products, stock movements, and low‑stock alerts, just like Shopify or Amazon.

- 🧱 **Tables** – products, categories, suppliers, stock_movements  
- 🧠 **Triggers** – auto‑update stock on a sale  
- 🧪 **Reports** – low‑stock alerts, supplier performance  
- ⚡ **Real‑world** – the backbone of every e‑commerce platform  

---

## 🧱 THE IMPERIAL STORE – BUSINESS REQUIREMENT

The Emperor’s online store sells electronics and office supplies. Every time a product is sold, the stock must decrease automatically. The purchasing team needs a daily low‑stock report.

---

## 🧱 SCHEMA

```sql
CREATE TABLE suppliers (
    supplier_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    supplier_id INTEGER,
    price REAL CHECK(price > 0),
    stock INTEGER DEFAULT 0 CHECK(stock >= 0),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

CREATE TABLE stock_movements (
    movement_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    quantity INTEGER,
    movement_type TEXT CHECK(movement_type IN ('in','out')),
    movement_date TEXT DEFAULT (datetime('now')),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

---

## 🧱 TRIGGER – AUTO‑UPDATE STOCK

```sql
CREATE TRIGGER after_stock_out
AFTER INSERT ON stock_movements
FOR EACH ROW
WHEN NEW.movement_type = 'out'
BEGIN
    UPDATE products
    SET stock = stock - NEW.quantity
    WHERE product_id = NEW.product_id;
END;
```

Now, any insert into `stock_movements` with `movement_type='out'` automatically reduces the stock.

---

## 🧱 SEED DATA & A SALE

```sql
INSERT INTO suppliers VALUES (1, 'TechSupplier Inc.');
INSERT INTO products VALUES (1, 'Wireless Mouse', 1, 24.99, 150);

-- Record a sale of 3 units
INSERT INTO stock_movements (product_id, quantity, movement_type)
VALUES (1, 3, 'out');

-- Stock is now 147
SELECT name, stock FROM products WHERE product_id = 1;
```

---

## 🧱 KEY QUERIES

**① Low‑stock alert (less than 10 units)**
```sql
SELECT name, stock FROM products WHERE stock < 10;
```

**② Supplier performance (total units supplied)**
```sql
SELECT s.name, COUNT(p.product_id) AS products_supplied
FROM suppliers s
LEFT JOIN products p ON s.supplier_id = p.supplier_id
GROUP BY s.supplier_id;
```

**③ Daily stock movement summary**
```sql
SELECT date(movement_date) AS day,
       movement_type,
       SUM(quantity) AS total_quantity
FROM stock_movements
GROUP BY day, movement_type;
```

**④ Products never sold (no 'out' movement)**
```sql
SELECT p.name
FROM products p
WHERE p.product_id NOT IN (
    SELECT product_id FROM stock_movements WHERE movement_type = 'out'
);
```

---

## 💡 Real‑world Usage

- Shopify backend – inventory tracking  
- Warehouse management systems  
- Retail POS systems  
- Any app that needs real‑time stock updates  

---

## 🔍 Practice Preview
You will build an e‑commerce inventory tracker.

| Level | Task |
|-------|------|
| Easy | Create tables and seed data for 5 products. |
| Medium | Write the low‑stock alert query. |
| Hard | Implement the trigger that auto‑updates stock on a sale, then test it. |

Run the coach:
```bash
python ii_Practice_Sheets/L82_Ecommerce_Inventory_Tracker.py
```

---

## 📌 Key Takeaway
- `CHECK` constraints prevent negative stock.  
- Triggers automate business logic at the database level.  
- `stock_movements` provides a complete audit trail.  
- Low‑stock reports keep the business from losing sales.

*For Emperor.*