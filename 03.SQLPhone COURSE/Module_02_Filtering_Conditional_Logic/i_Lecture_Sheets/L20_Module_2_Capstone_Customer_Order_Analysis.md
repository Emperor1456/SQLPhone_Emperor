# 📘 SQLPhone Emperor v3.0 · Module 2
# 📖 L20 – Module 2 Capstone: Customer Order Analysis

---

## 🎯 OBJECTIVE — What You Will Master

> Integrate every Module‑2 skill — filtering, logic, functions, and formatting — into a complete business intelligence report for customer orders. This capstone proves you can take raw data and turn it into actionable business insights.

- 🧱 **Schema design** – normalized tables for customers, products, and orders
- 🔍 **Filtering & logic** – `WHERE`, `AND/OR/NOT`, `BETWEEN`, `IN`, `LIKE`, `NULL`
- 🧮 **Computed columns & aliases** – derived fields with `AS`
- 📊 **Conditional logic** – `CASE` for categorization
- 🧹 **String & date functions** – cleaning and formatting output

---

## 🧱 THE BUSINESS SCENARIO

Imperial Commerce Inc. needs a complete customer order analysis from three tables: `customers`, `products`, and `orders`. The CEO wants to know who bought what, how much they spent, and what needs attention.

```sql
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT NOT NULL,
    joined_date TEXT DEFAULT (date('now'))
);

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    unit_price REAL NOT NULL CHECK(unit_price > 0)
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK(quantity > 0),
    order_date TEXT DEFAULT (date('now')),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

---

## 🧱 SEED DATA

```sql
INSERT INTO customers VALUES (1, 'Emperor', 'Dhaka', '2026-01-10');
INSERT INTO customers VALUES (2, 'Rahim', 'Chittagong', '2026-02-15');
INSERT INTO customers VALUES (3, 'Karim', 'Dhaka', '2026-03-20');

INSERT INTO products VALUES (1, 'Laptop', 'Electronics', 999.99);
INSERT INTO products VALUES (2, 'Desk', 'Furniture', 249.50);
INSERT INTO products VALUES (3, 'Mouse', 'Electronics', 24.99);

INSERT INTO orders VALUES (1, 1, 1, 2, '2026-06-20');
INSERT INTO orders VALUES (2, 2, 2, 1, '2026-07-01');
INSERT INTO orders VALUES (3, 1, 3, 5, '2026-07-10');
INSERT INTO orders VALUES (4, 3, 1, 1, '2026-07-11');
```

---

## 🧱 BUSINESS QUERIES

**① All orders with customer name and product name (join preview)**
```sql
SELECT c.name AS customer,
       p.name AS product,
       o.quantity,
       o.order_date
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id;
```

**② Total revenue per order line**
```sql
SELECT o.order_id,
       c.name AS customer,
       p.name AS product,
       o.quantity * p.unit_price AS total_revenue
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id;
```

**③ Order size classification with CASE**
```sql
SELECT o.order_id,
       c.name AS customer,
       CASE
           WHEN o.quantity * p.unit_price >= 1000 THEN 'Large Order'
           WHEN o.quantity * p.unit_price >= 500 THEN 'Medium Order'
           ELSE 'Small Order'
       END AS order_size
FROM orders o
JOIN products p ON o.product_id = p.product_id
JOIN customers c ON o.customer_id = c.customer_id;
```

**④ Customers who joined in 2026 (date filtering)**
```sql
SELECT name, city
FROM customers
WHERE strftime('%Y', joined_date) = '2026';
```

**⑤ Products never ordered (NOT IN subquery preview)**
```sql
SELECT name FROM products
WHERE product_id NOT IN (SELECT DISTINCT product_id FROM orders);
```

---

## 💡 Real‑world Usage

**Banking – customer account summary with transaction categorization**
**E‑commerce – monthly sales by category with growth comparison**
**Logistics – shipment status report with delivery performance**
**HR – employee tenure and salary band analysis**

---

## 🔍 Practice Preview
You will build the Imperial Commerce database and answer business questions.

| Level | Task |
|-------|------|
| Easy | Create the three tables and insert the provided seed data. |
| Medium | Write a query that shows each order with customer name, product name, and total line revenue. |
| Hard | Classify each order as Large/Medium/Small using `CASE`, and list only orders placed in the last 30 days using date functions. |

Run the coach:
```bash
python ii_Practice_Sheets/L20_Module_2_Capstone_Customer_Order_Analysis.py
```

---

## 📌 Key Takeaway
- Module‑2 skills combine to produce complete business reports.
- Filtering, logic, functions, and joins work together in real‑world queries.
- This capstone mirrors the daily work of a backend developer — transforming raw tables into executive summaries.

*For Emperor.*