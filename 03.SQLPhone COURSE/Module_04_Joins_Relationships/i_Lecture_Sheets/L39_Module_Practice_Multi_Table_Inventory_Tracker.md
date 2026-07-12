# 📘 SQLPhone Emperor v3.0 · Module 4
# 📖 L39 – Module Practice: Multi‑Table Inventory Tracker

---

## 🎯 OBJECTIVE — What You Will Master

> Build a complete inventory tracking system spanning suppliers, products, warehouses, and stock levels — all joined together into a single, queryable business system.

- 🧱 **Schema design** – four related tables with full constraints
- 🧠 **Full join queries** – suppliers → products → warehouses → stock
- 🧪 **Aggregation with joins** – total stock per warehouse, per supplier
- ⚡ **Business dashboard** – low‑stock alerts, supplier performance
- 🛡️ **Production patterns** – foreign keys, CHECK constraints, composite keys

---

## 🧱 THE IMPERIAL INVENTORY SCENARIO

The Imperial Logistics Corps needs to track every product, who supplies it, which warehouses store it, and how much is in stock at each location. A single product can be stored in multiple warehouses, and each warehouse holds products from many suppliers.

**Tables:**
- `suppliers` – who provides the products
- `products` – what is being stocked, linked to a supplier
- `warehouses` – where items are stored
- `stock` – how much of each product is in each warehouse

---

## 🧱 SCHEMA

```sql
CREATE TABLE suppliers (
    supplier_id INTEGER PRIMARY KEY,
    supplier_name TEXT NOT NULL
);

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    supplier_id INTEGER,
    unit_price REAL CHECK(unit_price > 0),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

CREATE TABLE warehouses (
    warehouse_id INTEGER PRIMARY KEY,
    warehouse_name TEXT NOT NULL,
    location TEXT
);

CREATE TABLE stock (
    stock_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    warehouse_id INTEGER,
    quantity INTEGER DEFAULT 0 CHECK(quantity >= 0),
    last_updated TEXT DEFAULT (datetime('now')),
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id),
    UNIQUE(product_id, warehouse_id)
);
```

The `UNIQUE(product_id, warehouse_id)` constraint ensures we never have duplicate stock records for the same product in the same warehouse.

---

## 🧱 SEED DATA

```sql
INSERT INTO suppliers VALUES (1, 'TechSupplier Inc.'), (2, 'OfficeDepot');
INSERT INTO products VALUES (1, 'Wireless Mouse', 1, 24.99), (2, 'Keyboard', 1, 49.99), (3, 'Notebook', 2, 3.50);
INSERT INTO warehouses VALUES (1, 'Dhaka Central', 'Dhaka'), (2, 'Chittagong Depot', 'Chittagong');
INSERT INTO stock VALUES (1, 1, 1, 150, '2026-07-01'), (2, 1, 2, 80, '2026-07-01'), (3, 2, 1, 45, '2026-07-01'), (4, 3, 1, 300, '2026-07-02'), (5, 3, 2, 120, '2026-07-02');
```

---

## 🧱 KEY REPORTS

**① Total stock per product across all warehouses**
```sql
SELECT p.product_name,
       SUM(s.quantity) AS total_stock
FROM products p
LEFT JOIN stock s ON p.product_id = s.product_id
GROUP BY p.product_id
ORDER BY total_stock DESC;
```

**② Stock per warehouse for a specific product**
```sql
SELECT w.warehouse_name, s.quantity
FROM stock s
JOIN warehouses w ON s.warehouse_id = w.warehouse_id
WHERE s.product_id = 1;
```

**③ Products supplied by each supplier**
```sql
SELECT sup.supplier_name, p.product_name
FROM suppliers sup
JOIN products p ON sup.supplier_id = p.supplier_id
ORDER BY sup.supplier_name;
```

**④ Low‑stock alert (total stock < 10)**
```sql
SELECT p.product_name, SUM(s.quantity) AS total_stock
FROM products p
JOIN stock s ON p.product_id = s.product_id
GROUP BY p.product_id
HAVING SUM(s.quantity) < 10;
```

**⑤ Warehouse utilization (total units across all products)**
```sql
SELECT w.warehouse_name, SUM(s.quantity) AS total_units
FROM warehouses w
LEFT JOIN stock s ON w.warehouse_id = s.warehouse_id
GROUP BY w.warehouse_id
ORDER BY total_units DESC;
```

**⑥ Supplier performance (total units supplied to all warehouses)**
```sql
SELECT sup.supplier_name,
       COUNT(p.product_id) AS products,
       COALESCE(SUM(s.quantity), 0) AS total_units
FROM suppliers sup
LEFT JOIN products p ON sup.supplier_id = p.supplier_id
LEFT JOIN stock s ON p.product_id = s.product_id
GROUP BY sup.supplier_id;
```

---

## 💡 Real‑world Usage

- Warehouse management systems (WMS)
- Retail inventory dashboards
- Hospital supply tracking
- Amazon fulfillment center logic

---

## 🔍 Practice Preview
You will build the Imperial Inventory system and run multi‑table reports.

| Level | Task |
|-------|------|
| Easy | Create the four tables with foreign keys and insert seed data. |
| Medium | Write a query showing total stock per product across all warehouses. |
| Hard | Produce a low‑stock alert report: products with total stock below 10 across all warehouses, with supplier names. |

Run the coach:
```bash
python ii_Practice_Sheets/L39_Module_Practice_Multi_Table_Inventory_Tracker.py
```

---

## 📌 Key Takeaway
- Multi‑table inventory systems are the backbone of logistics and retail.
- Joining across four tables provides complete visibility.
- Aggregation + `HAVING` identifies critical business conditions.
- `UNIQUE(product_id, warehouse_id)` prevents duplicate stock records.

*For Emperor.*