# 📘 SQLPhone Emperor v3.0 · Module 10
# 📖 L100 – Final Capstone: Imperial ERP System

---

## 🎯 OBJECTIVE — What You Will Master

> Build the ultimate database project — an Enterprise Resource Planning system that integrates HR, inventory, finance, sales, and logistics into one unified database. This is the final proof of your SQL mastery.

- 🧱 **Multi‑module schema** – 15+ tables across all business domains  
- 🧠 **Complex reporting** – cross‑domain queries, executive dashboards  
- 🧪 **Production features** – views, indexes, transactions, security  
- ⚡ **Portfolio completion** – a project that demonstrates every skill you’ve learned  

---

## 🧱 THE IMPERIAL ERP – BUSINESS REQUIREMENT

Imperial Enterprises needs a single database to manage:

- **HR:** employees, departments, salaries, attendance  
- **Inventory:** products, warehouses, stock levels, suppliers  
- **Finance:** accounts, invoices, payments, transactions  
- **Sales:** customers, orders, order_items  
- **Logistics:** shipments, carriers, routes, deliveries  

---

## 🧱 CORE SCHEMA EXCERPT (15+ tables)

```sql
CREATE TABLE departments (dept_id INTEGER PRIMARY KEY, name TEXT NOT NULL);
CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT NOT NULL, dept_id INTEGER REFERENCES departments, salary REAL CHECK(salary > 0));
CREATE TABLE suppliers (sup_id INTEGER PRIMARY KEY, name TEXT NOT NULL);
CREATE TABLE products (prod_id INTEGER PRIMARY KEY, name TEXT NOT NULL, sup_id INTEGER REFERENCES suppliers, price REAL CHECK(price > 0));
CREATE TABLE warehouses (wh_id INTEGER PRIMARY KEY, name TEXT NOT NULL);
CREATE TABLE inventory (prod_id INTEGER REFERENCES products, wh_id INTEGER REFERENCES warehouses, quantity INTEGER DEFAULT 0, PRIMARY KEY(prod_id, wh_id));
CREATE TABLE customers (cust_id INTEGER PRIMARY KEY, name TEXT NOT NULL);
CREATE TABLE orders (ord_id INTEGER PRIMARY KEY, cust_id INTEGER REFERENCES customers, order_date TEXT DEFAULT (date('now')));
CREATE TABLE order_items (ord_id INTEGER REFERENCES orders, prod_id INTEGER REFERENCES products, quantity INTEGER, PRIMARY KEY(ord_id, prod_id));
CREATE TABLE accounts (acct_id INTEGER PRIMARY KEY, name TEXT NOT NULL, balance REAL);
CREATE TABLE transactions (txn_id INTEGER PRIMARY KEY, acct_id INTEGER REFERENCES accounts, amount REAL, txn_date TEXT DEFAULT (date('now')));
CREATE TABLE carriers (carrier_id INTEGER PRIMARY KEY, name TEXT NOT NULL);
CREATE TABLE shipments (ship_id INTEGER PRIMARY KEY, ord_id INTEGER REFERENCES orders, carrier_id INTEGER REFERENCES carriers, status TEXT, ship_date TEXT);
CREATE TABLE routes (route_id INTEGER PRIMARY KEY, origin TEXT, destination TEXT, distance REAL);
CREATE TABLE deliveries (delivery_id INTEGER PRIMARY KEY, ship_id INTEGER REFERENCES shipments, route_id INTEGER REFERENCES routes, delivery_date TEXT);
```

---

## 🧱 BUSINESS REPORTS (20 required)

**1. Monthly revenue by product category**
```sql
SELECT p.category, strftime('%Y-%m', o.order_date) AS month, SUM(oi.quantity * p.price) AS revenue
FROM order_items oi
JOIN products p ON oi.prod_id = p.prod_id
JOIN orders o ON oi.ord_id = o.ord_id
GROUP BY p.category, month ORDER BY month, revenue DESC;
```

**2. Employee salary summary by department**
```sql
SELECT d.name, COUNT(e.emp_id) AS employees, AVG(e.salary) AS avg_salary, SUM(e.salary) AS total_payroll
FROM departments d
LEFT JOIN employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_id;
```

**3. Low‑stock alert across all warehouses**
```sql
SELECT p.name, w.name AS warehouse, i.quantity
FROM inventory i
JOIN products p ON i.prod_id = p.prod_id
JOIN warehouses w ON i.wh_id = w.wh_id
WHERE i.quantity < 10;
```

**4. Top 5 customers by total spend**
```sql
SELECT c.name, SUM(oi.quantity * p.price) AS total_spent
FROM customers c
JOIN orders o ON c.cust_id = o.cust_id
JOIN order_items oi ON o.ord_id = oi.ord_id
JOIN products p ON oi.prod_id = p.prod_id
GROUP BY c.cust_id
ORDER BY total_spent DESC LIMIT 5;
```

**5. Shipment on‑time delivery rate by carrier**
```sql
SELECT c.name, COUNT(*) AS total,
       SUM(CASE WHEN d.delivery_date <= s.ship_date + 5 THEN 1 ELSE 0 END) AS on_time
FROM shipments s
JOIN carriers c ON s.carrier_id = c.carrier_id
LEFT JOIN deliveries d ON s.ship_id = d.ship_id
GROUP BY c.carrier_id;
```

---

## 🧱 VIEWS AND INDEXES

```sql
CREATE VIEW executive_summary AS
SELECT ... (multi‑table aggregation for dashboard);

CREATE INDEX idx_orders_customer ON orders(cust_id);
CREATE INDEX idx_shipments_status ON shipments(status);
CREATE INDEX idx_inventory_quantity ON inventory(quantity);
```

---

## 🧱 DELIVERABLES

1. `schema.sql` – all CREATE TABLE statements with constraints  
2. `seed.sql` – realistic test data (20+ rows per domain)  
3. `queries.sql` – 20 business reports  
4. `views.sql` – 3 executive dashboard views  
5. `indexes.sql` – strategic indexes with EXPLAIN QUERY PLAN output  
6. `README.md` – project overview, schema diagram, how to run  
7. `pipeline.py` – a Python script that loads CSV data into the database  

---

## 💡 Real‑world Usage

This project directly mirrors:
- ERP software used by Fortune 500 companies  
- The backend of any e‑commerce, logistics, or financial platform  
- The exact type of system design you’d be asked to create in a senior backend interview  

---

## 🔍 Practice Preview
You will build the Imperial ERP System from scratch.

| Level | Task |
|-------|------|
| Easy | Design the schema for one domain (e.g., HR) with all constraints. |
| Medium | Integrate two domains (e.g., Sales + Inventory) with foreign keys and write 5 cross‑domain queries. |
| Hard | Build the complete ERP with all 5 domains, seed data, views, indexes, documentation, and the Python loading script. |

Run the coach:
```bash
python ii_Practice_Sheets/L100_Final_Capstone_Imperial_ERP_System.py
```

---

## 📌 Key Takeaway
- An ERP system integrates every business function into one database.  
- This capstone proves you can design, build, and query a production‑grade system.  
- You are now undeniable in SQL — ready for any backend challenge on Earth.  

*For Emperor.*