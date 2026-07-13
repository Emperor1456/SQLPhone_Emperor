import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🏢  Imperial Enterprise – Build the Full Schema\n\n"
        "Write Python code that:\n"
        "  1. Connects to ':memory:'\n"
        "  2. Creates all 10 tables (departments, employees,\n"
        "     suppliers, products, stock_movements, customers,\n"
        "     orders, order_items, carriers, shipments)\n"
        "     with exact schemas from the lecture.\n"
        "  3. Inserts the core seed data:\n"
        "     • departments: (1,'Sales'), (2,'Logistics'), (3,'Finance')\n"
        "     • employees: (1,'Emperor',1,5000,'2025-06-01'),\n"
        "       (2,'Rahim',2,4000,'2025-08-15')\n"
        "     • suppliers: (1,'TechSupplier Inc'), (2,'OfficeDepot')\n"
        "     • products: (1,'Laptop',1,999.99,50),\n"
        "       (2,'Desk',2,249.50,30)\n"
        "     • customers: (1,'Karim','karim@email.com','2026-01-10'),\n"
        "       (2,'Fatima','fatima@email.com','2026-03-20')\n"
        "     • orders: (1,1,1,'2026-07-01'), (2,2,1,'2026-07-02')\n"
        "     • order_items: (1,1,2), (2,2,1)\n"
        "     • carriers: (1,'FastShip'), (2,'CourierX')\n"
        "     • shipments: (1,1,1,'in transit','2026-07-02',NULL)\n"
        "     • stock_movements: leave empty\n"
        "  4. Commits, then SELECTs all department names\n"
        "     sorted alphabetically and prints them.\n\n"
        "Expected output:\n[('Finance',), ('Logistics',), ('Sales',)]"
    ),
    expected_output="[('Finance',), ('Logistics',), ('Sales',)]",
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.executescript('''",
        "CREATE TABLE departments (dept_id INTEGER PRIMARY KEY, name TEXT NOT NULL);",
        "CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT NOT NULL, dept_id INTEGER, salary REAL CHECK(salary > 0), hire_date TEXT DEFAULT (date('now')), FOREIGN KEY (dept_id) REFERENCES departments(dept_id));",
        "CREATE TABLE suppliers (sup_id INTEGER PRIMARY KEY, name TEXT NOT NULL);",
        "CREATE TABLE products (prod_id INTEGER PRIMARY KEY, name TEXT NOT NULL, sup_id INTEGER, price REAL CHECK(price > 0), stock INTEGER DEFAULT 0 CHECK(stock >= 0), FOREIGN KEY (sup_id) REFERENCES suppliers(sup_id));",
        "CREATE TABLE stock_movements (mov_id INTEGER PRIMARY KEY, prod_id INTEGER, quantity INTEGER, movement_type TEXT CHECK(movement_type IN ('in','out')), movement_date TEXT DEFAULT (datetime('now')), FOREIGN KEY (prod_id) REFERENCES products(prod_id));",
        "CREATE TABLE customers (cust_id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE, join_date TEXT DEFAULT (date('now')));",
        "CREATE TABLE orders (ord_id INTEGER PRIMARY KEY, cust_id INTEGER, emp_id INTEGER, order_date TEXT DEFAULT (datetime('now')), FOREIGN KEY (cust_id) REFERENCES customers(cust_id), FOREIGN KEY (emp_id) REFERENCES employees(emp_id));",
        "CREATE TABLE order_items (ord_id INTEGER, prod_id INTEGER, quantity INTEGER CHECK(quantity > 0), PRIMARY KEY (ord_id, prod_id), FOREIGN KEY (ord_id) REFERENCES orders(ord_id), FOREIGN KEY (prod_id) REFERENCES products(prod_id));",
        "CREATE TABLE carriers (carrier_id INTEGER PRIMARY KEY, name TEXT NOT NULL);",
        "CREATE TABLE shipments (ship_id INTEGER PRIMARY KEY, ord_id INTEGER UNIQUE, carrier_id INTEGER, status TEXT DEFAULT 'pending' CHECK(status IN ('pending','in transit','delivered','cancelled')), ship_date TEXT, delivery_date TEXT, FOREIGN KEY (ord_id) REFERENCES orders(ord_id), FOREIGN KEY (carrier_id) REFERENCES carriers(carrier_id));",
        "''')",
        "conn.executescript('''",
        "INSERT INTO departments VALUES (1,'Sales'), (2,'Logistics'), (3,'Finance');",
        "INSERT INTO employees VALUES (1,'Emperor',1,5000,'2025-06-01');",
        "INSERT INTO employees VALUES (2,'Rahim',2,4000,'2025-08-15');",
        "INSERT INTO suppliers VALUES (1,'TechSupplier Inc'), (2,'OfficeDepot');",
        "INSERT INTO products VALUES (1,'Laptop',1,999.99,50);",
        "INSERT INTO products VALUES (2,'Desk',2,249.50,30);",
        "INSERT INTO customers VALUES (1,'Karim','karim@email.com','2026-01-10');",
        "INSERT INTO customers VALUES (2,'Fatima','fatima@email.com','2026-03-20');",
        "INSERT INTO orders VALUES (1,1,1,'2026-07-01');",
        "INSERT INTO orders VALUES (2,2,1,'2026-07-02');",
        "INSERT INTO order_items VALUES (1,1,2);",
        "INSERT INTO order_items VALUES (2,2,1);",
        "INSERT INTO carriers VALUES (1,'FastShip'), (2,'CourierX');",
        "INSERT INTO shipments VALUES (1,1,1,'in transit','2026-07-02',NULL);",
        "''')",
        "conn.commit()",
        "cursor = conn.execute('SELECT name FROM departments ORDER BY name')",
        "print(cursor.fetchall())",
    ]
)

easy2 = Task(
    description=(
        "📊  Monthly Revenue Report\n\n"
        "The enterprise database is fully seeded.\n"
        "Write Python code that computes total revenue\n"
        "per month (YYYY‑MM) using the formula:\n"
        "  SUM(order_items.quantity * products.price)\n"
        "Join orders, order_items, and products.\n"
        "Group by month, sort chronologically.\n\n"
        "Expected output:\n[('2026-07', 2249.48)]"
    ),
    setup_sql=(
        "CREATE TABLE departments (dept_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO departments VALUES (1,'Sales'), (2,'Logistics'), (3,'Finance');"
        "CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT NOT NULL, dept_id INTEGER, salary REAL CHECK(salary > 0), hire_date TEXT DEFAULT (date('now')), FOREIGN KEY (dept_id) REFERENCES departments(dept_id));"
        "INSERT INTO employees VALUES (1,'Emperor',1,5000,'2025-06-01');"
        "INSERT INTO employees VALUES (2,'Rahim',2,4000,'2025-08-15');"
        "CREATE TABLE suppliers (sup_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO suppliers VALUES (1,'TechSupplier Inc'), (2,'OfficeDepot');"
        "CREATE TABLE products (prod_id INTEGER PRIMARY KEY, name TEXT NOT NULL, sup_id INTEGER, price REAL CHECK(price > 0), stock INTEGER DEFAULT 0 CHECK(stock >= 0), FOREIGN KEY (sup_id) REFERENCES suppliers(sup_id));"
        "INSERT INTO products VALUES (1,'Laptop',1,999.99,50);"
        "INSERT INTO products VALUES (2,'Desk',2,249.50,30);"
        "CREATE TABLE stock_movements (mov_id INTEGER PRIMARY KEY, prod_id INTEGER, quantity INTEGER, movement_type TEXT CHECK(movement_type IN ('in','out')), movement_date TEXT DEFAULT (datetime('now')), FOREIGN KEY (prod_id) REFERENCES products(prod_id));"
        "CREATE TABLE customers (cust_id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE, join_date TEXT DEFAULT (date('now')));"
        "INSERT INTO customers VALUES (1,'Karim','karim@email.com','2026-01-10');"
        "INSERT INTO customers VALUES (2,'Fatima','fatima@email.com','2026-03-20');"
        "CREATE TABLE orders (ord_id INTEGER PRIMARY KEY, cust_id INTEGER, emp_id INTEGER, order_date TEXT DEFAULT (datetime('now')), FOREIGN KEY (cust_id) REFERENCES customers(cust_id), FOREIGN KEY (emp_id) REFERENCES employees(emp_id));"
        "INSERT INTO orders VALUES (1,1,1,'2026-07-01');"
        "INSERT INTO orders VALUES (2,2,1,'2026-07-02');"
        "CREATE TABLE order_items (ord_id INTEGER, prod_id INTEGER, quantity INTEGER CHECK(quantity > 0), PRIMARY KEY (ord_id, prod_id), FOREIGN KEY (ord_id) REFERENCES orders(ord_id), FOREIGN KEY (prod_id) REFERENCES products(prod_id));"
        "INSERT INTO order_items VALUES (1,1,2);"
        "INSERT INTO order_items VALUES (2,2,1);"
        "CREATE TABLE carriers (carrier_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO carriers VALUES (1,'FastShip'), (2,'CourierX');"
        "CREATE TABLE shipments (ship_id INTEGER PRIMARY KEY, ord_id INTEGER UNIQUE, carrier_id INTEGER, status TEXT DEFAULT 'pending' CHECK(status IN ('pending','in transit','delivered','cancelled')), ship_date TEXT, delivery_date TEXT, FOREIGN KEY (ord_id) REFERENCES orders(ord_id), FOREIGN KEY (carrier_id) REFERENCES carriers(carrier_id));"
        "INSERT INTO shipments VALUES (1,1,1,'in transit','2026-07-02',NULL);"
    ),
    expected_output="[('2026-07', 2249.48)]",
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT strftime('%Y-%m', o.order_date) AS month,",
        "       SUM(oi.quantity * p.price) AS revenue",
        "FROM orders o JOIN order_items oi ON o.ord_id = oi.ord_id",
        "JOIN products p ON oi.prod_id = p.prod_id",
        "GROUP BY month ORDER BY month",
        "''')",
        "print(cursor.fetchall())",
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🏅  Top Customers by Total Spend\n\n"
        "The enterprise database is seeded.\n"
        "Write Python code that lists the top 5 customers\n"
        "by total money spent (quantity * price).\n"
        "Show customer name and total_spent.\n"
        "Sort by total_spent descending.\n\n"
        "Expected output:\n[('Karim',1999.98), ('Fatima',249.5)]"
    ),
    setup_sql=(
        "CREATE TABLE departments (dept_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO departments VALUES (1,'Sales'), (2,'Logistics'), (3,'Finance');"
        "CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT NOT NULL, dept_id INTEGER, salary REAL CHECK(salary > 0), hire_date TEXT DEFAULT (date('now')), FOREIGN KEY (dept_id) REFERENCES departments(dept_id));"
        "INSERT INTO employees VALUES (1,'Emperor',1,5000,'2025-06-01');"
        "INSERT INTO employees VALUES (2,'Rahim',2,4000,'2025-08-15');"
        "CREATE TABLE suppliers (sup_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO suppliers VALUES (1,'TechSupplier Inc'), (2,'OfficeDepot');"
        "CREATE TABLE products (prod_id INTEGER PRIMARY KEY, name TEXT NOT NULL, sup_id INTEGER, price REAL CHECK(price > 0), stock INTEGER DEFAULT 0 CHECK(stock >= 0), FOREIGN KEY (sup_id) REFERENCES suppliers(sup_id));"
        "INSERT INTO products VALUES (1,'Laptop',1,999.99,50);"
        "INSERT INTO products VALUES (2,'Desk',2,249.50,30);"
        "CREATE TABLE customers (cust_id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE, join_date TEXT DEFAULT (date('now')));"
        "INSERT INTO customers VALUES (1,'Karim','karim@email.com','2026-01-10');"
        "INSERT INTO customers VALUES (2,'Fatima','fatima@email.com','2026-03-20');"
        "CREATE TABLE orders (ord_id INTEGER PRIMARY KEY, cust_id INTEGER, emp_id INTEGER, order_date TEXT DEFAULT (datetime('now')), FOREIGN KEY (cust_id) REFERENCES customers(cust_id), FOREIGN KEY (emp_id) REFERENCES employees(emp_id));"
        "INSERT INTO orders VALUES (1,1,1,'2026-07-01');"
        "INSERT INTO orders VALUES (2,2,1,'2026-07-02');"
        "CREATE TABLE order_items (ord_id INTEGER, prod_id INTEGER, quantity INTEGER CHECK(quantity > 0), PRIMARY KEY (ord_id, prod_id), FOREIGN KEY (ord_id) REFERENCES orders(ord_id), FOREIGN KEY (prod_id) REFERENCES products(prod_id));"
        "INSERT INTO order_items VALUES (1,1,2);"
        "INSERT INTO order_items VALUES (2,2,1);"
        "CREATE TABLE carriers (carrier_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO carriers VALUES (1,'FastShip'), (2,'CourierX');"
        "CREATE TABLE shipments (ship_id INTEGER PRIMARY KEY, ord_id INTEGER UNIQUE, carrier_id INTEGER, status TEXT DEFAULT 'pending' CHECK(status IN ('pending','in transit','delivered','cancelled')), ship_date TEXT, delivery_date TEXT, FOREIGN KEY (ord_id) REFERENCES orders(ord_id), FOREIGN KEY (carrier_id) REFERENCES carriers(carrier_id));"
        "INSERT INTO shipments VALUES (1,1,1,'in transit','2026-07-02',NULL);"
    ),
    expected_output="[('Karim', 1999.98), ('Fatima', 249.5)]",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT c.name, SUM(oi.quantity * p.price) AS total_spent",
        "FROM customers c JOIN orders o ON c.cust_id = o.cust_id",
        "JOIN order_items oi ON o.ord_id = oi.ord_id",
        "JOIN products p ON oi.prod_id = p.prod_id",
        "GROUP BY c.cust_id ORDER BY total_spent DESC LIMIT 5",
        "''')",
        "print(cursor.fetchall())",
    ]
)

medium2 = Task(
    description=(
        "🚫  Products Never Ordered\n\n"
        "The enterprise database includes a third product\n"
        "'Mouse' that has never been ordered.\n"
        "Write Python code that finds the names of all\n"
        "products that do NOT appear in any order_items.\n"
        "Sort by name.\n\n"
        "Expected output:\n[('Mouse',)]"
    ),
    setup_sql=(
        "CREATE TABLE departments (dept_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO departments VALUES (1,'Sales'), (2,'Logistics'), (3,'Finance');"
        "CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT NOT NULL, dept_id INTEGER, salary REAL CHECK(salary > 0), hire_date TEXT DEFAULT (date('now')), FOREIGN KEY (dept_id) REFERENCES departments(dept_id));"
        "INSERT INTO employees VALUES (1,'Emperor',1,5000,'2025-06-01');"
        "INSERT INTO employees VALUES (2,'Rahim',2,4000,'2025-08-15');"
        "CREATE TABLE suppliers (sup_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO suppliers VALUES (1,'TechSupplier Inc'), (2,'OfficeDepot');"
        "CREATE TABLE products (prod_id INTEGER PRIMARY KEY, name TEXT NOT NULL, sup_id INTEGER, price REAL CHECK(price > 0), stock INTEGER DEFAULT 0 CHECK(stock >= 0), FOREIGN KEY (sup_id) REFERENCES suppliers(sup_id));"
        "INSERT INTO products VALUES (1,'Laptop',1,999.99,50);"
        "INSERT INTO products VALUES (2,'Desk',2,249.50,30);"
        "INSERT INTO products VALUES (3,'Mouse',1,19.99,100);"
        "CREATE TABLE customers (cust_id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE, join_date TEXT DEFAULT (date('now')));"
        "INSERT INTO customers VALUES (1,'Karim','karim@email.com','2026-01-10');"
        "INSERT INTO customers VALUES (2,'Fatima','fatima@email.com','2026-03-20');"
        "CREATE TABLE orders (ord_id INTEGER PRIMARY KEY, cust_id INTEGER, emp_id INTEGER, order_date TEXT DEFAULT (datetime('now')), FOREIGN KEY (cust_id) REFERENCES customers(cust_id), FOREIGN KEY (emp_id) REFERENCES employees(emp_id));"
        "INSERT INTO orders VALUES (1,1,1,'2026-07-01');"
        "INSERT INTO orders VALUES (2,2,1,'2026-07-02');"
        "CREATE TABLE order_items (ord_id INTEGER, prod_id INTEGER, quantity INTEGER CHECK(quantity > 0), PRIMARY KEY (ord_id, prod_id), FOREIGN KEY (ord_id) REFERENCES orders(ord_id), FOREIGN KEY (prod_id) REFERENCES products(prod_id));"
        "INSERT INTO order_items VALUES (1,1,2);"
        "INSERT INTO order_items VALUES (2,2,1);"
        "CREATE TABLE carriers (carrier_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO carriers VALUES (1,'FastShip'), (2,'CourierX');"
        "CREATE TABLE shipments (ship_id INTEGER PRIMARY KEY, ord_id INTEGER UNIQUE, carrier_id INTEGER, status TEXT DEFAULT 'pending' CHECK(status IN ('pending','in transit','delivered','cancelled')), ship_date TEXT, delivery_date TEXT, FOREIGN KEY (ord_id) REFERENCES orders(ord_id), FOREIGN KEY (carrier_id) REFERENCES carriers(carrier_id));"
        "INSERT INTO shipments VALUES (1,1,1,'in transit','2026-07-02',NULL);"
    ),
    expected_output="[('Mouse',)]",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''SELECT name FROM products WHERE prod_id NOT IN (SELECT DISTINCT prod_id FROM order_items) ORDER BY name''')",
        "print(cursor.fetchall())",
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "📈  Executive Dashboard View\n\n"
        "The enterprise database is seeded.\n"
        "Write Python code that:\n"
        "  1. Creates the `executive_summary` view exactly\n"
        "     as defined in the lecture (KPIs: total customers,\n"
        "     total products, total employees, monthly revenue\n"
        "     for current month (use '2026-07'), active shipments).\n"
        "  2. SELECTs all columns from the view and prints them.\n\n"
        "Expected output:\n[(2, 2, 2, 2249.48, 1)]"
    ),
    setup_sql=(
        "CREATE TABLE departments (dept_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO departments VALUES (1,'Sales'), (2,'Logistics'), (3,'Finance');"
        "CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT NOT NULL, dept_id INTEGER, salary REAL CHECK(salary > 0), hire_date TEXT DEFAULT (date('now')), FOREIGN KEY (dept_id) REFERENCES departments(dept_id));"
        "INSERT INTO employees VALUES (1,'Emperor',1,5000,'2025-06-01');"
        "INSERT INTO employees VALUES (2,'Rahim',2,4000,'2025-08-15');"
        "CREATE TABLE suppliers (sup_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO suppliers VALUES (1,'TechSupplier Inc'), (2,'OfficeDepot');"
        "CREATE TABLE products (prod_id INTEGER PRIMARY KEY, name TEXT NOT NULL, sup_id INTEGER, price REAL CHECK(price > 0), stock INTEGER DEFAULT 0 CHECK(stock >= 0), FOREIGN KEY (sup_id) REFERENCES suppliers(sup_id));"
        "INSERT INTO products VALUES (1,'Laptop',1,999.99,50);"
        "INSERT INTO products VALUES (2,'Desk',2,249.50,30);"
        "CREATE TABLE customers (cust_id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE, join_date TEXT DEFAULT (date('now')));"
        "INSERT INTO customers VALUES (1,'Karim','karim@email.com','2026-01-10');"
        "INSERT INTO customers VALUES (2,'Fatima','fatima@email.com','2026-03-20');"
        "CREATE TABLE orders (ord_id INTEGER PRIMARY KEY, cust_id INTEGER, emp_id INTEGER, order_date TEXT DEFAULT (datetime('now')), FOREIGN KEY (cust_id) REFERENCES customers(cust_id), FOREIGN KEY (emp_id) REFERENCES employees(emp_id));"
        "INSERT INTO orders VALUES (1,1,1,'2026-07-01');"
        "INSERT INTO orders VALUES (2,2,1,'2026-07-02');"
        "CREATE TABLE order_items (ord_id INTEGER, prod_id INTEGER, quantity INTEGER CHECK(quantity > 0), PRIMARY KEY (ord_id, prod_id), FOREIGN KEY (ord_id) REFERENCES orders(ord_id), FOREIGN KEY (prod_id) REFERENCES products(prod_id));"
        "INSERT INTO order_items VALUES (1,1,2);"
        "INSERT INTO order_items VALUES (2,2,1);"
        "CREATE TABLE carriers (carrier_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO carriers VALUES (1,'FastShip'), (2,'CourierX');"
        "CREATE TABLE shipments (ship_id INTEGER PRIMARY KEY, ord_id INTEGER UNIQUE, carrier_id INTEGER, status TEXT DEFAULT 'pending' CHECK(status IN ('pending','in transit','delivered','cancelled')), ship_date TEXT, delivery_date TEXT, FOREIGN KEY (ord_id) REFERENCES orders(ord_id), FOREIGN KEY (carrier_id) REFERENCES carriers(carrier_id));"
        "INSERT INTO shipments VALUES (1,1,1,'in transit','2026-07-02',NULL);"
    ),
    expected_output="[(2, 2, 2, 2249.48, 1)]",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('''CREATE VIEW executive_summary AS",
        "SELECT",
        "    (SELECT COUNT(*) FROM customers) AS total_customers,",
        "    (SELECT COUNT(*) FROM products) AS total_products,",
        "    (SELECT COUNT(*) FROM employees) AS total_employees,",
        "    (SELECT SUM(oi.quantity * p.price)",
        "     FROM orders o",
        "     JOIN order_items oi ON o.ord_id = oi.ord_id",
        "     JOIN products p ON oi.prod_id = p.prod_id",
        "     WHERE strftime('%Y-%m', o.order_date) = '2026-07'",
        "    ) AS monthly_revenue,",
        "    (SELECT COUNT(*) FROM shipments WHERE status = 'in transit') AS active_shipments",
        "''')",
        "cursor = conn.execute('SELECT * FROM executive_summary')",
        "print(cursor.fetchall())",
    ]
)

hard2 = Task(
    description=(
        "🔍  Index Verification with EXPLAIN QUERY PLAN\n\n"
        "The enterprise database is seeded.\n"
        "Write Python code that:\n"
        "  1. Creates an index `idx_orders_customer` on\n"
        "     `orders(cust_id)`.\n"
        "  2. Runs EXPLAIN QUERY PLAN on the top‑customer\n"
        "     spend query (without LIMIT) to verify it uses\n"
        "     the index.\n"
        "  3. Prints only the `detail` column for the first\n"
        "     plan row (the one mentioning the index).\n\n"
        "Expected output:\n[('SEARCH TABLE orders USING INDEX idx_orders_customer',)]"
    ),
    setup_sql=(
        "CREATE TABLE departments (dept_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO departments VALUES (1,'Sales'), (2,'Logistics'), (3,'Finance');"
        "CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT NOT NULL, dept_id INTEGER, salary REAL CHECK(salary > 0), hire_date TEXT DEFAULT (date('now')), FOREIGN KEY (dept_id) REFERENCES departments(dept_id));"
        "INSERT INTO employees VALUES (1,'Emperor',1,5000,'2025-06-01');"
        "INSERT INTO employees VALUES (2,'Rahim',2,4000,'2025-08-15');"
        "CREATE TABLE suppliers (sup_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO suppliers VALUES (1,'TechSupplier Inc'), (2,'OfficeDepot');"
        "CREATE TABLE products (prod_id INTEGER PRIMARY KEY, name TEXT NOT NULL, sup_id INTEGER, price REAL CHECK(price > 0), stock INTEGER DEFAULT 0 CHECK(stock >= 0), FOREIGN KEY (sup_id) REFERENCES suppliers(sup_id));"
        "INSERT INTO products VALUES (1,'Laptop',1,999.99,50);"
        "INSERT INTO products VALUES (2,'Desk',2,249.50,30);"
        "CREATE TABLE customers (cust_id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE, join_date TEXT DEFAULT (date('now')));"
        "INSERT INTO customers VALUES (1,'Karim','karim@email.com','2026-01-10');"
        "INSERT INTO customers VALUES (2,'Fatima','fatima@email.com','2026-03-20');"
        "CREATE TABLE orders (ord_id INTEGER PRIMARY KEY, cust_id INTEGER, emp_id INTEGER, order_date TEXT DEFAULT (datetime('now')), FOREIGN KEY (cust_id) REFERENCES customers(cust_id), FOREIGN KEY (emp_id) REFERENCES employees(emp_id));"
        "INSERT INTO orders VALUES (1,1,1,'2026-07-01');"
        "INSERT INTO orders VALUES (2,2,1,'2026-07-02');"
        "CREATE TABLE order_items (ord_id INTEGER, prod_id INTEGER, quantity INTEGER CHECK(quantity > 0), PRIMARY KEY (ord_id, prod_id), FOREIGN KEY (ord_id) REFERENCES orders(ord_id), FOREIGN KEY (prod_id) REFERENCES products(prod_id));"
        "INSERT INTO order_items VALUES (1,1,2);"
        "INSERT INTO order_items VALUES (2,2,1);"
        "CREATE TABLE carriers (carrier_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO carriers VALUES (1,'FastShip'), (2,'CourierX');"
        "CREATE TABLE shipments (ship_id INTEGER PRIMARY KEY, ord_id INTEGER UNIQUE, carrier_id INTEGER, status TEXT DEFAULT 'pending' CHECK(status IN ('pending','in transit','delivered','cancelled')), ship_date TEXT, delivery_date TEXT, FOREIGN KEY (ord_id) REFERENCES orders(ord_id), FOREIGN KEY (carrier_id) REFERENCES carriers(carrier_id));"
        "INSERT INTO shipments VALUES (1,1,1,'in transit','2026-07-02',NULL);"
    ),
    expected_output="[('SEARCH TABLE orders USING INDEX idx_orders_customer',)]",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('CREATE INDEX idx_orders_customer ON orders(cust_id)')",
        "cursor = conn.execute('''EXPLAIN QUERY PLAN",
        "SELECT c.name, SUM(oi.quantity * p.price) AS total_spent",
        "FROM customers c JOIN orders o ON c.cust_id = o.cust_id",
        "JOIN order_items oi ON o.ord_id = oi.ord_id",
        "JOIN products p ON oi.prod_id = p.prod_id",
        "GROUP BY c.cust_id ORDER BY total_spent DESC",
        "''')",
        "row = cursor.fetchone()",
        "print([(row[3],)])  # the detail column is index 3 in EXPLAIN QUERY PLAN output",
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L90.json",
        module_name="Module_09_Real_World_Projects",
        lesson_name="L90_Module_9_Capstone_Full_Stack_Business_Database"
    )