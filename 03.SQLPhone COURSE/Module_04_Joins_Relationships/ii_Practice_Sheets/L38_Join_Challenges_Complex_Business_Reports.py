import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "📊  Regimental Strength Report\n\n"
        "Create tables `regiments` and `soldiers`.\n"
        "Insert 3 regiments (one empty) and 5 soldiers.\n"
        "Write a query that returns regiment_name and\n"
        "the COUNT of soldiers in each, including regiments\n"
        "with zero soldiers (use LEFT JOIN).\n"
        "Sort by soldier_count descending.\n\n"
        "Expected output:\n[('Red Guard',2), ('Imperial Guard',2), ('Blue Shield',0)]"
    ),
    expected_output="[('Red Guard', 2), ('Imperial Guard', 2), ('Blue Shield', 0)]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, regiment_name TEXT);",
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard'), (3,'Blue Shield');",
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER);",
        "INSERT INTO soldiers VALUES (1,'Emperor',1), (2,'Rahim',2), (3,'Ali',2), (4,'Hasan',1), (5,'Spy',NULL);",
        "SELECT r.regiment_name, COUNT(s.id) AS soldier_count FROM regiments r LEFT JOIN soldiers s ON r.id = s.regiment_id GROUP BY r.id ORDER BY soldier_count DESC;"
    ]
)

easy2 = Task(
    description=(
        "🔍  Products Never Ordered\n\n"
        "Create tables `products` and `orders`.\n"
        "Insert 4 products, but only 2 have ever been ordered.\n"
        "Write a query that returns the names of products that\n"
        "have NEVER been ordered (use LEFT JOIN + IS NULL).\n"
        "Sort by product name.\n\n"
        "Expected output:\n[('Chair',), ('Desk',)]"
    ),
    expected_output="[('Chair',), ('Desk',)]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO products VALUES (1,'Laptop'), (2,'Mouse'), (3,'Chair'), (4,'Desk');",
        "CREATE TABLE orders (id INTEGER PRIMARY KEY, product_id INTEGER, qty INTEGER);",
        "INSERT INTO orders VALUES (1,1,2), (2,2,5);",
        "SELECT p.name FROM products p LEFT JOIN orders o ON p.id = o.product_id WHERE o.id IS NULL ORDER BY p.name;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🧮  Employee Team Size – Self‑Join + Count\n\n"
        "Create an `employees` table with self‑referencing manager_id.\n"
        "Insert 5 employees (Emperor CEO, Rahim & Ali report to Emperor,\n"
        "Hasan reports to Rahim, Fatima reports to Ali).\n"
        "Write a self‑join query that returns each manager's name\n"
        "and the number of direct reports they have.\n"
        "Include managers with zero direct reports.\n"
        "Sort by direct_reports descending.\n\n"
        "Expected output:\n[('Emperor',2), ('Ali',1), ('Rahim',1), ('Fatima',0), ('Hasan',0)]"
    ),
    expected_output="[('Emperor', 2), ('Ali', 1), ('Rahim', 1), ('Fatima', 0), ('Hasan', 0)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT, manager_id INTEGER REFERENCES employees(emp_id));",
        "INSERT INTO employees VALUES (1,'Emperor',NULL), (2,'Rahim',1), (3,'Ali',1), (4,'Hasan',2), (5,'Fatima',3);",
        "SELECT m.name, COUNT(e.emp_id) AS direct_reports FROM employees m LEFT JOIN employees e ON m.emp_id = e.manager_id GROUP BY m.emp_id ORDER BY direct_reports DESC;"
    ]
)

medium2 = Task(
    description=(
        "💰  Customer Spend Report – JOIN + SUM\n\n"
        "Create `customers`, `products`, and `orders` tables.\n"
        "Insert 3 customers, 3 products, and 5 orders.\n"
        "Write a query that returns each customer's name,\n"
        "the number of orders they placed, and their total spent\n"
        "(SUM of qty * price). Include customers with zero orders\n"
        "using LEFT JOIN, showing 0 for both.\n"
        "Sort by total_spent descending.\n\n"
        "Expected output:\n[('Emperor',3,2580.0), ('Rahim',2,1250.0), ('Ali',0,0.0)]"
    ),
    expected_output="[('Emperor', 3, 2580.0), ('Rahim', 2, 1250.0), ('Ali', 0, 0.0)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO customers VALUES (1,'Emperor'), (2,'Rahim'), (3,'Ali');",
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price REAL);",
        "INSERT INTO products VALUES (1,'Laptop',1000), (2,'Mouse',50), (3,'Keyboard',80);",
        "CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER, product_id INTEGER, quantity INTEGER);",
        "INSERT INTO orders VALUES (1,1,1,2), (2,2,2,5), (3,1,3,1), (4,1,2,3), (5,2,1,1);",
        "SELECT c.name, COUNT(o.id) AS order_count, COALESCE(SUM(o.quantity * p.price), 0) AS total_spent FROM customers c LEFT JOIN orders o ON c.id = o.customer_id LEFT JOIN products p ON o.product_id = p.id GROUP BY c.id ORDER BY total_spent DESC;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  Full Order Fulfillment Report – 5‑Table Join\n\n"
        "Create five tables: customers, products, orders, shipments, carriers.\n"
        "Write a query that returns: order_id, customer name, product name,\n"
        "quantity, order_date, shipment status, and carrier name.\n"
        "Orders without shipments should still appear (use LEFT JOIN).\n"
        "Sort by order_date, then order_id.\n\n"
        "Expected output:\n[(1,'Emperor','Laptop',2,'2026-06-20','delivered','FastShip'), (2,'Rahim','Desk',1,'2026-07-01','in transit','SwiftLog'), (3,'Emperor','Mouse',5,'2026-07-10',NULL,NULL)]"
    ),
    expected_output="[(1, 'Emperor', 'Laptop', 2, '2026-06-20', 'delivered', 'FastShip'), (2, 'Rahim', 'Desk', 1, '2026-07-01', 'in transit', 'SwiftLog'), (3, 'Emperor', 'Mouse', 5, '2026-07-10', None, None)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO customers VALUES (1,'Emperor'), (2,'Rahim');",
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO products VALUES (1,'Laptop'), (2,'Desk'), (3,'Mouse');",
        "CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER, product_id INTEGER, quantity INTEGER, order_date TEXT);",
        "INSERT INTO orders VALUES (1,1,1,2,'2026-06-20'), (2,2,2,1,'2026-07-01'), (3,1,3,5,'2026-07-10');",
        "CREATE TABLE carriers (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO carriers VALUES (1,'FastShip'), (2,'SwiftLog');",
        "CREATE TABLE shipments (id INTEGER PRIMARY KEY, order_id INTEGER, carrier_id INTEGER, status TEXT);",
        "INSERT INTO shipments VALUES (1,1,1,'delivered'), (2,2,2,'in transit');",
        "SELECT o.id, c.name, p.name, o.quantity, o.order_date, sh.status, cr.name FROM orders o JOIN customers c ON o.customer_id = c.id JOIN products p ON o.product_id = p.id LEFT JOIN shipments sh ON o.id = sh.order_id LEFT JOIN carriers cr ON sh.carrier_id = cr.id ORDER BY o.order_date, o.id;"
    ]
)

hard2 = Task(
    description=(
        "📊  Executive Dashboard – Multi‑Metric Report\n\n"
        "Create four tables: departments, employees, projects, assignments.\n"
        "Insert 3 departments, 6 employees, 3 projects, and varied assignments.\n"
        "Write ONE query that returns, for each department:\n"
        "  • department name\n"
        "  • headcount (total employees)\n"
        "  • avg_salary (rounded)\n"
        "  • project_count (distinct projects assigned)\n"
        "  • total_project_hours (SUM of hours worked)\n"
        "Include departments with zero projects (use LEFT JOIN).\n"
        "Sort by headcount descending.\n\n"
        "Expected output:\n[('Engineering',2,5500.0,2,35), ('Sales',2,4000.0,2,55), ('HR',2,3400.0,0,None)]"
    ),
    expected_output="[('Engineering', 2, 5500.0, 2, 35), ('Sales', 2, 4000.0, 2, 55), ('HR', 2, 3400.0, 0, None)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE departments (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO departments VALUES (1,'Engineering'), (2,'Sales'), (3,'HR');",
        "CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, dept_id INTEGER, salary REAL);",
        "INSERT INTO employees VALUES (1,'Emperor',1,5000), (2,'Rahim',2,4000), (3,'Ali',2,4000), (4,'Hasan',1,6000), (5,'Fatima',3,3000), (6,'Karim',3,3800);",
        "CREATE TABLE projects (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO projects VALUES (1,'Project Alpha'), (2,'Project Beta'), (3,'Project Gamma');",
        "CREATE TABLE assignments (emp_id INTEGER, proj_id INTEGER, hours INTEGER, PRIMARY KEY(emp_id, proj_id));",
        "INSERT INTO assignments VALUES (1,1,20), (1,2,15), (2,1,30), (3,2,25), (4,1,10), (4,2,25);",
        "SELECT d.name, COUNT(DISTINCT e.id) AS headcount, ROUND(AVG(e.salary)) AS avg_salary, COUNT(DISTINCT a.proj_id) AS project_count, SUM(a.hours) AS total_hours FROM departments d LEFT JOIN employees e ON d.id = e.dept_id LEFT JOIN assignments a ON e.id = a.emp_id GROUP BY d.id ORDER BY headcount DESC;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L38.json",
        module_name="Module_04_Joins_Relationships",
        lesson_name="L38_Join_Challenges"
    )
