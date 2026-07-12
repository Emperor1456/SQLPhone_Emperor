# 📘 SQLPhone Emperor v3.0 · Module 4
# 📖 L40 – Module 4 Capstone: Supply Chain Database

---

## 🎯 OBJECTIVE — What You Will Master

> Design, build, and query a complete supply chain database — the exact type of system that runs Amazon, Walmart, and every logistics empire on Earth.

- 🧱 **Full schema design** – suppliers, products, warehouses, shipments, shipment_items
- 🧠 **Join chains** – up to 5 tables in a single report
- 🧪 **Aggregation across joins** – total shipped, total received, inventory levels
- ⚡ **Real‑world deliverable** – a supply chain analyst’s daily dashboard
- 🛡️ **Production readiness** – composite keys, cascading deletes, full constraints

---

## 🧱 THE IMPERIAL SUPPLY CHAIN – BUSINESS REQUIREMENT

The Imperial Logistics Corps must track products from supplier to warehouse. Suppliers ship products in bulk; each shipment goes to a specific warehouse and contains multiple products. The system must answer:

- How much of each product has been shipped to each warehouse?
- Which suppliers have shipped the most?
- Which products have never been shipped?
- What is the most recent shipment to each warehouse?

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
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

CREATE TABLE warehouses (
    warehouse_id INTEGER PRIMARY KEY,
    warehouse_name TEXT NOT NULL
);

CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY,
    supplier_id INTEGER,
    warehouse_id INTEGER,
    ship_date TEXT DEFAULT (date('now')),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id),
    FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id)
);

CREATE TABLE shipment_items (
    shipment_id INTEGER,
    product_id INTEGER,
    quantity INTEGER CHECK(quantity > 0),
    PRIMARY KEY (shipment_id, product_id),
    FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

The composite primary key on `shipment_items` ensures the same product cannot appear twice in a single shipment.

---

## 🧱 SEED DATA

```sql
INSERT INTO suppliers VALUES (1, 'TechSupplier Inc.'), (2, 'OfficeDepot');
INSERT INTO products VALUES (1, 'Laptop', 1), (2, 'Mouse', 1), (3, 'Desk', 2);
INSERT INTO warehouses VALUES (1, 'Dhaka Central'), (2, 'Chittagong Depot');
INSERT INTO shipments VALUES (1, 1, 1, '2026-07-01'), (2, 2, 1, '2026-07-02'), (3, 1, 2, '2026-07-03');
INSERT INTO shipment_items VALUES (1, 1, 10), (1, 2, 50), (2, 3, 20), (3, 2, 30);
```

---

## 🧱 KEY BUSINESS QUERIES

**① Total quantity of each product shipped to each warehouse**
```sql
SELECT p.product_name,
       w.warehouse_name,
       SUM(si.quantity) AS total_shipped
FROM shipment_items si
JOIN products p ON si.product_id = p.product_id
JOIN shipments s ON si.shipment_id = s.shipment_id
JOIN warehouses w ON s.warehouse_id = w.warehouse_id
GROUP BY p.product_id, w.warehouse_id
ORDER BY p.product_name, w.warehouse_name;
```

**② Suppliers with total units shipped (including those with zero)**
```sql
SELECT sup.supplier_name,
       COALESCE(SUM(si.quantity), 0) AS total_units
FROM suppliers sup
LEFT JOIN shipments s ON sup.supplier_id = s.supplier_id
LEFT JOIN shipment_items si ON s.shipment_id = si.shipment_id
GROUP BY sup.supplier_id
ORDER BY total_units DESC;
```

**③ Most recent shipment per warehouse**
```sql
SELECT w.warehouse_name,
       MAX(s.ship_date) AS last_shipment
FROM warehouses w
LEFT JOIN shipments s ON w.warehouse_id = s.warehouse_id
GROUP BY w.warehouse_id;
```

**④ Products never shipped**
```sql
SELECT p.product_name
FROM products p
LEFT JOIN shipment_items si ON p.product_id = si.product_id
WHERE si.shipment_id IS NULL;
```

**⑤ Full shipment manifest (5‑table join)**
```sql
SELECT sh.shipment_id,
       sup.supplier_name,
       p.product_name,
       si.quantity,
       w.warehouse_name,
       sh.ship_date
FROM shipments sh
JOIN suppliers sup ON sh.supplier_id = sup.supplier_id
JOIN shipment_items si ON sh.shipment_id = si.shipment_id
JOIN products p ON si.product_id = p.product_id
JOIN warehouses w ON sh.warehouse_id = w.warehouse_id
ORDER BY sh.ship_date DESC;
```

---

## 🧱 STRATEGIC INDEXES

```sql
CREATE INDEX idx_shipments_supplier ON shipments(supplier_id);
CREATE INDEX idx_shipments_warehouse ON shipments(warehouse_id);
CREATE INDEX idx_shipment_items_product ON shipment_items(product_id);
```

---

## 💡 Real‑world Usage

This schema directly mirrors:
- Amazon’s inbound shipment tracking
- Walmart’s distribution center management
- Hospital supply chain logistics
- Military ordnance supply tracking

---

## 🔍 Practice Preview
You will build the Imperial Supply Chain database and answer business questions.

| Level | Task |
|-------|------|
| Easy | Create all five tables with foreign keys and insert seed data. |
| Medium | Write a query showing total quantity of each product shipped to each warehouse. |
| Hard | Write a query identifying products that have never been shipped, and the supplier name for each. |

Run the coach:
```bash
python ii_Practice_Sheets/L40_Module_4_Capstone_Supply_Chain_Database.py
```

---

## 📌 Key Takeaway
- A supply chain database models real‑world logistics with multiple joins.
- Five‑table joins are common in enterprise reporting.
- The capstone proves you can design and query a complete business system.
- Composite keys and cascading deletes protect data integrity.

*For Emperor.*