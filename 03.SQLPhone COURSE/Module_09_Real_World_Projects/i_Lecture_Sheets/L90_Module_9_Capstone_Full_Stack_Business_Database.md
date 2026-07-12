# 📘 SQLPhone Emperor v3.0 · Module 9
# 📖 L90 – Module 9 Capstone: Full‑Stack Business Database

---

## 🎯 OBJECTIVE — What You Will Master

> Integrate customers, products, orders, employees, and shipping into a single, normalized business database. Produce 10 executive‑level reports, performance views, and strategic indexes — the final proof that you can design and query any operational system a company needs.

- 🧱 **Full schema design** – 10 tables across HR, inventory, sales, and logistics
- 🧠 **Complex multi‑table reports** – queries joining 5+ tables with aggregation, subqueries, and CTEs
- 🧪 **Views and indexes** – optimize for dashboards and reporting
- ⚡ **Documentation** – a README that explains your design to a development team
- 🧰 **Real‑world** – this is the project you’d present in a backend engineering interview

---

## 🧱 THE IMPERIAL ENTERPRISE – BUSINESS SCENARIO

Imperial Enterprises runs retail stores, an online shop, and a delivery fleet. They need a single database to replace five spreadsheets. The database must handle:

- **HR:** employees, departments, salaries, attendance
- **Inventory:** products, suppliers, stock levels, stock movements
- **Sales:** customers, orders, order items
- **Logistics:** shipments, carriers, delivery tracking

All domains are linked so that an order can be traced from the customer to the employee who processed it to the carrier who delivered it.

---

## 🧱 CORE SCHEMA (10 TABLES)

```sql
-- HR
CREATE TABLE departments (
    dept_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    dept_id INTEGER,
    salary REAL CHECK(salary > 0),
    hire_date TEXT DEFAULT (date('now')),
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- Inventory
CREATE TABLE suppliers (
    sup_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE products (
    prod_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    sup_id INTEGER,
    price REAL CHECK(price > 0),
    stock INTEGER DEFAULT 0 CHECK(stock >= 0),
    FOREIGN KEY (sup_id) REFERENCES suppliers(sup_id)
);

CREATE TABLE stock_movements (
    mov_id INTEGER PRIMARY KEY,
    prod_id INTEGER,
    quantity INTEGER,
    movement_type TEXT CHECK(movement_type IN ('in','out')),
    movement_date TEXT DEFAULT (datetime('now')),
    FOREIGN KEY (prod_id) REFERENCES products(prod_id)
);

-- Sales
CREATE TABLE customers (
    cust_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    join_date TEXT DEFAULT (date('now'))
);

CREATE TABLE orders (
    ord_id INTEGER PRIMARY KEY,
    cust_id INTEGER,
    emp_id INTEGER,
    order_date TEXT DEFAULT (datetime('now')),
    FOREIGN KEY (cust_id) REFERENCES customers(cust_id),
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
);

CREATE TABLE order_items (
    ord_id INTEGER,
    prod_id INTEGER,
    quantity INTEGER CHECK(quantity > 0),
    PRIMARY KEY (ord_id, prod_id),
    FOREIGN KEY (ord_id) REFERENCES orders(ord_id),
    FOREIGN KEY (prod_id) REFERENCES products(prod_id)
);

-- Logistics
CREATE TABLE carriers (
    carrier_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE shipments (
    ship_id INTEGER PRIMARY KEY,
    ord_id INTEGER UNIQUE,
    carrier_id INTEGER,
    status TEXT DEFAULT 'pending' CHECK(status IN ('pending','in transit','delivered','cancelled')),
    ship_date TEXT,
    delivery_date TEXT,
    FOREIGN KEY (ord_id) REFERENCES orders(ord_id),
    FOREIGN KEY (carrier_id) REFERENCES carriers(carrier_id)
);
```

---

## 🧱 SEED DATA (EXCERPT)

```sql
-- Departments & Employees
INSERT INTO departments VALUES (1, 'Sales'), (2, 'Logistics'), (3, 'Finance');
INSERT INTO employees VALUES (1, 'Emperor', 1, 5000, '2025-06-01');
INSERT INTO employees VALUES (2, 'Rahim', 2, 4000, '2025-08-15');

-- Suppliers & Products
INSERT INTO suppliers VALUES (1, 'TechSupplier Inc'), (2, 'OfficeDepot');
INSERT INTO products VALUES (1, 'Laptop', 1, 999.99, 50);
INSERT INTO products VALUES (2, 'Desk', 2, 249.50, 30);

-- Customers
INSERT INTO customers VALUES (1, 'Karim', 'karim@email.com', '2026-01-10');
INSERT INTO customers VALUES (2, 'Fatima', 'fatima@email.com', '2026-03-20');

-- Orders & Items
INSERT INTO orders VALUES (1, 1, 1, '2026-07-01');
INSERT INTO order_items VALUES (1, 1, 2);
INSERT INTO orders VALUES (2, 2, 1, '2026-07-02');
INSERT INTO order_items VALUES (2, 2, 1);

-- Carriers & Shipments
INSERT INTO carriers VALUES (1, 'FastShip'), (2, 'CourierX');
INSERT INTO shipments VALUES (1, 1, 1, 'in transit', '2026-07-02', NULL);
```

---

## 🧱 BUSINESS REPORTS (10 REQUIRED)

**1. Monthly revenue**
```sql
SELECT strftime('%Y-%m', o.order_date) AS month,
       SUM(oi.quantity * p.price) AS revenue
FROM orders o
JOIN order_items oi ON o.ord_id = oi.ord_id
JOIN products p ON oi.prod_id = p.prod_id
GROUP BY month ORDER BY month;
```

**2. Top 5 customers by total spend**
```sql
SELECT c.name, SUM(oi.quantity * p.price) AS total_spent
FROM customers c
JOIN orders o ON c.cust_id = o.cust_id
JOIN order_items oi ON o.ord_id = oi.ord_id
JOIN products p ON oi.prod_id = p.prod_id
GROUP BY c.cust_id ORDER BY total_spent DESC LIMIT 5;
```

**3. Employee sales performance**
```sql
SELECT e.name, COUNT(o.ord_id) AS orders_handled,
       SUM(oi.quantity * p.price) AS revenue_generated
FROM employees e
JOIN orders o ON e.emp_id = o.emp_id
JOIN order_items oi ON o.ord_id = oi.ord_id
JOIN products p ON oi.prod_id = p.prod_id
GROUP BY e.emp_id ORDER BY revenue_generated DESC;
```

**4. Low‑stock products (less than 10 units)**
```sql
SELECT name, stock FROM products WHERE stock < 10;
```

**5. Supplier performance (total units supplied)**
```sql
SELECT s.name, COUNT(p.prod_id) AS products_count,
       COALESCE(SUM(p.stock), 0) AS total_stock
FROM suppliers s
LEFT JOIN products p ON s.sup_id = p.sup_id
GROUP BY s.sup_id;
```

**6. Shipment status breakdown by carrier**
```sql
SELECT c.name AS carrier,
       sh.status,
       COUNT(*) AS shipments
FROM shipments sh
JOIN carriers c ON sh.carrier_id = c.carrier_id
GROUP BY c.carrier_id, sh.status;
```

**7. Department salary summary**
```sql
SELECT d.name, COUNT(e.emp_id) AS employees,
       ROUND(AVG(e.salary), 2) AS avg_salary,
       SUM(e.salary) AS total_payroll
FROM departments d
LEFT JOIN employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_id;
```

**8. Products never ordered**
```sql
SELECT name FROM products
WHERE prod_id NOT IN (SELECT DISTINCT prod_id FROM order_items);
```

**9. Daily revenue last 7 days**
```sql
SELECT date(o.order_date) AS day,
       SUM(oi.quantity * p.price) AS revenue
FROM orders o
JOIN order_items oi ON o.ord_id = oi.ord_id
JOIN products p ON oi.prod_id = p.prod_id
WHERE o.order_date >= date('now', '-7 days')
GROUP BY day ORDER BY day;
```

**10. Executive dashboard view (all KPIs at a glance)**
```sql
CREATE VIEW executive_summary AS
SELECT
    (SELECT COUNT(*) FROM customers) AS total_customers,
    (SELECT COUNT(*) FROM products) AS total_products,
    (SELECT COUNT(*) FROM employees) AS total_employees,
    (SELECT SUM(oi.quantity * p.price)
     FROM orders o
     JOIN order_items oi ON o.ord_id = oi.ord_id
     JOIN products p ON oi.prod_id = p.prod_id
     WHERE strftime('%Y-%m', o.order_date) = strftime('%Y-%m', 'now')
    ) AS monthly_revenue,
    (SELECT COUNT(*) FROM shipments WHERE status = 'in transit') AS active_shipments;
```

---

## 🧱 STRATEGIC INDEXES (WITH EXPLAIN QUERY PLAN)

```sql
CREATE INDEX idx_orders_customer ON orders(cust_id);
CREATE INDEX idx_orders_employee ON orders(emp_id);
CREATE INDEX idx_order_items_order ON order_items(ord_id);
CREATE INDEX idx_shipments_status ON shipments(status);
CREATE INDEX idx_products_stock ON products(stock);
```

**Verify index usage:**
```sql
EXPLAIN QUERY PLAN
SELECT c.name, SUM(oi.quantity * p.price) AS total
FROM customers c
JOIN orders o ON c.cust_id = o.cust_id
JOIN order_items oi ON o.ord_id = oi.ord_id
JOIN products p ON oi.prod_id = p.prod_id
GROUP BY c.cust_id;
```

---

## 💡 Real‑world Usage

- ERP systems (SAP, Oracle NetSuite)
- E‑commerce platforms (Shopify, Magento)
- Logistics dashboards (FedEx, DHL)
- This is the exact project you’d present in a senior backend interview

---

## 🔍 Practice Preview
You will build the complete Imperial Enterprise database.

| Level | Task |
|-------|------|
| Easy | Create all 10 tables with constraints and seed data. |
| Medium | Write 5 of the business reports, including at least one with a CTE or subquery. |
| Hard | Create the `executive_summary` view, add the strategic indexes, and run `EXPLAIN QUERY PLAN` on the top‑customer query to prove they’re used. |

Run the coach:
```bash
python ii_Practice_Sheets/L90_Module_9_Capstone_Full_Stack_Business_Database.py
```

---

## 📌 Key Takeaway
- A production database spans multiple business domains linked by foreign keys.
- Views and indexes make it fast and usable for non‑technical stakeholders.
- This capstone proves you can design, build, and optimize any business database — the defining skill of a backend engineer.

*For Emperor.*