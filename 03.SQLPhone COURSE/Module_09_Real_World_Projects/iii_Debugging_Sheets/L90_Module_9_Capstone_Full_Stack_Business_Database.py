import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
SELECT strftime('%Y-%m', o.order_date) AS month,
       SUM(oi.quantity * p.price) AS revenue
FROM orders o
JOIN order_items oi ON o.ord_id = oi.ord_id
JOIN products p ON oi.prod_id = p.prod_id
GROUP BY month
ORDER BY month;"""

EXPECTED = "[('2026-07', 2249.48)]"

SETUP = """\
CREATE TABLE departments (dept_id INTEGER PRIMARY KEY, name TEXT NOT NULL); INSERT INTO departments VALUES (1,'Sales'), (2,'Logistics'), (3,'Finance');
CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT NOT NULL, dept_id INTEGER, salary REAL CHECK(salary > 0), hire_date TEXT DEFAULT (date('now')), FOREIGN KEY (dept_id) REFERENCES departments(dept_id)); INSERT INTO employees VALUES (1,'Emperor',1,5000,'2025-06-01'),(2,'Rahim',2,4000,'2025-08-15');
CREATE TABLE suppliers (sup_id INTEGER PRIMARY KEY, name TEXT NOT NULL); INSERT INTO suppliers VALUES (1,'TechSupplier Inc'), (2,'OfficeDepot');
CREATE TABLE products (prod_id INTEGER PRIMARY KEY, name TEXT NOT NULL, sup_id INTEGER, price REAL CHECK(price > 0), stock INTEGER DEFAULT 0 CHECK(stock >= 0), FOREIGN KEY (sup_id) REFERENCES suppliers(sup_id)); INSERT INTO products VALUES (1,'Laptop',1,999.99,50),(2,'Desk',2,249.50,30);
CREATE TABLE customers (cust_id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE, join_date TEXT DEFAULT (date('now'))); INSERT INTO customers VALUES (1,'Karim','karim@email.com','2026-01-10'),(2,'Fatima','fatima@email.com','2026-03-20');
CREATE TABLE orders (ord_id INTEGER PRIMARY KEY, cust_id INTEGER, emp_id INTEGER, order_date TEXT DEFAULT (datetime('now')), FOREIGN KEY (cust_id) REFERENCES customers(cust_id), FOREIGN KEY (emp_id) REFERENCES employees(emp_id)); INSERT INTO orders VALUES (1,1,1,'2026-07-01'),(2,2,1,'2026-07-02');
CREATE TABLE order_items (ord_id INTEGER, prod_id INTEGER, quantity INTEGER CHECK(quantity > 0), PRIMARY KEY (ord_id, prod_id), FOREIGN KEY (ord_id) REFERENCES orders(ord_id), FOREIGN KEY (prod_id) REFERENCES products(prod_id)); INSERT INTO order_items VALUES (1,1,2),(2,2,1);"""

HINTS = [
    "The query is almost perfect, but there is a typo in the table alias for order_items.",
    "Check the JOIN condition – you wrote 'oi.prod_id' but the alias is misspelled as 'oi'? Actually correct. The bug could be that the table 'order_items' is misspelled as 'order_item'.",
    "Change 'order_item' to 'order_items'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L90 – Module 9 Capstone – Full‑Stack Business Database",
        setup_sql=SETUP,
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
