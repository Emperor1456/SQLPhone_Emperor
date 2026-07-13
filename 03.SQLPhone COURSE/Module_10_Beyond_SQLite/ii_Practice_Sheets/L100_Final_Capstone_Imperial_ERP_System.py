import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🏢  HR Domain – Departments & Employees\n\n"
        "Write Python code that:\n"
        "  1. Connects to the seeded in‑memory database.\n"
        "     The engine already created `departments` and\n"
        "     `employees` and inserted:\n"
        "       departments: (1,'Engineering'), (2,'Sales')\n"
        "       employees: (1,'Emperor',1,5000),\n"
        "                  (2,'Rahim',2,4000),\n"
        "                  (3,'Ali',2,3500)\n"
        "  2. Executes a SELECT that returns all department\n"
        "     names, sorted alphabetically.\n"
        "  3. Prints the result.\n\n"
        "Expected output:\n[('Engineering',), ('Sales',)]"
    ),
    setup_sql=(
        "CREATE TABLE departments (dept_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO departments VALUES (1,'Engineering'), (2,'Sales');"
        "CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT NOT NULL, dept_id INTEGER REFERENCES departments, salary REAL CHECK(salary > 0));"
        "INSERT INTO employees VALUES (1,'Emperor',1,5000), (2,'Rahim',2,4000), (3,'Ali',2,3500);"
    ),
    expected_output="[('Engineering',), ('Sales',)]",
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "# The engine has already run the setup_sql, so just execute the query.",
        "cursor = conn.execute('SELECT name FROM departments ORDER BY name')",
        "print(cursor.fetchall())",
    ]
)

easy2 = Task(
    description=(
        "🛒  Sales Domain – Customers & Orders\n\n"
        "The database now also has `customers` and `orders`\n"
        "tables (already created and seeded):\n"
        "  customers: (1,'Karim'), (2,'Fatima')\n"
        "  orders: (1,1,'2026-07-01'), (2,2,'2026-07-02')\n"
        "Write Python code that lists all customer names\n"
        "sorted alphabetically.\n\n"
        "Expected output:\n[('Fatima',), ('Karim',)]"
    ),
    setup_sql=(
        "CREATE TABLE customers (cust_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO customers VALUES (1,'Karim'), (2,'Fatima');"
        "CREATE TABLE orders (ord_id INTEGER PRIMARY KEY, cust_id INTEGER REFERENCES customers, order_date TEXT DEFAULT (date('now')));"
        "INSERT INTO orders VALUES (1,1,'2026-07-01'), (2,2,'2026-07-02');"
    ),
    expected_output="[('Fatima',), ('Karim',)]",
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('SELECT name FROM customers ORDER BY name')",
        "print(cursor.fetchall())",
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "📊  HR Report – Employees per Department\n\n"
        "The database contains `departments` and `employees`\n"
        "as seeded in Easy1. Write Python code that produces\n"
        "a report showing each department name and the\n"
        "number of employees in that department.\n"
        "Sort by department name.\n\n"
        "Expected output:\n[('Engineering',1), ('Sales',2)]"
    ),
    setup_sql=(
        "CREATE TABLE departments (dept_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO departments VALUES (1,'Engineering'), (2,'Sales');"
        "CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT NOT NULL, dept_id INTEGER REFERENCES departments, salary REAL CHECK(salary > 0));"
        "INSERT INTO employees VALUES (1,'Emperor',1,5000), (2,'Rahim',2,4000), (3,'Ali',2,3500);"
    ),
    expected_output="[('Engineering', 1), ('Sales', 2)]",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT d.name, COUNT(e.emp_id) AS employees",
        "FROM departments d LEFT JOIN employees e ON d.dept_id = e.dept_id",
        "GROUP BY d.dept_id ORDER BY d.name",
        "''')",
        "print(cursor.fetchall())",
    ]
)

medium2 = Task(
    description=(
        "🏅  Sales Report – Top 2 Customers by Spend\n\n"
        "The full sales module is now seeded: customers,\n"
        "orders, products, and order_items. Write Python\n"
        "code that lists the top 2 customers by total\n"
        "spending (SUM(quantity * price)). Show name and\n"
        "total_spent, sorted by total_spent descending.\n\n"
        "Expected output:\n[('Karim',999.98), ('Fatima',249.5)]"
    ),
    setup_sql=(
        "CREATE TABLE customers (cust_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO customers VALUES (1,'Karim'), (2,'Fatima');"
        "CREATE TABLE products (prod_id INTEGER PRIMARY KEY, name TEXT NOT NULL, price REAL CHECK(price > 0));"
        "INSERT INTO products VALUES (1,'Laptop',499.99), (2,'Mouse',249.50);"
        "CREATE TABLE orders (ord_id INTEGER PRIMARY KEY, cust_id INTEGER REFERENCES customers, order_date TEXT DEFAULT (date('now')));"
        "INSERT INTO orders VALUES (1,1,'2026-07-01'), (2,2,'2026-07-02');"
        "CREATE TABLE order_items (ord_id INTEGER REFERENCES orders, prod_id INTEGER REFERENCES products, quantity INTEGER CHECK(quantity > 0), PRIMARY KEY(ord_id, prod_id));"
        "INSERT INTO order_items VALUES (1,1,2), (2,2,1);"
    ),
    expected_output="[('Karim', 999.98), ('Fatima', 249.5)]",
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
        "GROUP BY c.cust_id ORDER BY total_spent DESC LIMIT 2",
        "''')",
        "print(cursor.fetchall())",
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "📦  Inventory – Low‑Stock Alert\n\n"
        "The database now includes `warehouses`, `products`,\n"
        "and `inventory`. Write Python code that lists every\n"
        "product name, warehouse name, and current quantity\n"
        "for items where stock is below 10 units.\n"
        "Sort by product name.\n\n"
        "Expected output:\n[('Desk','Dhaka',5), ('Laptop','Chittagong',8)]"
    ),
    setup_sql=(
        "CREATE TABLE warehouses (wh_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO warehouses VALUES (1,'Dhaka'), (2,'Chittagong');"
        "CREATE TABLE products (prod_id INTEGER PRIMARY KEY, name TEXT NOT NULL, price REAL CHECK(price > 0));"
        "INSERT INTO products VALUES (1,'Laptop',499.99), (2,'Desk',249.50), (3,'Monitor',299.99);"
        "CREATE TABLE inventory (prod_id INTEGER REFERENCES products, wh_id INTEGER REFERENCES warehouses, quantity INTEGER DEFAULT 0, PRIMARY KEY(prod_id, wh_id));"
        "INSERT INTO inventory VALUES (1,1,12), (1,2,8), (2,1,5), (2,2,15), (3,1,20), (3,2,30);"
    ),
    expected_output="[('Desk', 'Dhaka', 5), ('Laptop', 'Chittagong', 8)]",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT p.name, w.name, i.quantity",
        "FROM inventory i JOIN products p ON i.prod_id = p.prod_id",
        "JOIN warehouses w ON i.wh_id = w.wh_id",
        "WHERE i.quantity < 10 ORDER BY p.name",
        "''')",
        "print(cursor.fetchall())",
    ]
)

hard2 = Task(
    description=(
        "👑  Executive View – Employee Sales Performance\n\n"
        "Combine HR and Sales: the database has employees,\n"
        "customers, orders, and order_items (no products\n"
        "table). Write Python code that shows each employee\n"
        "name, the number of orders they handled, and the\n"
        "total quantity sold, sorted by total quantity\n"
        "descending.\n\n"
        "Expected output:\n[('Emperor',2,3), ('Rahim',1,1)]"
    ),
    setup_sql=(
        "CREATE TABLE departments (dept_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO departments VALUES (1,'Sales');"
        "CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT NOT NULL, dept_id INTEGER REFERENCES departments, salary REAL CHECK(salary > 0));"
        "INSERT INTO employees VALUES (1,'Emperor',1,5000), (2,'Rahim',1,4000);"
        "CREATE TABLE customers (cust_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO customers VALUES (1,'Karim'), (2,'Fatima');"
        "CREATE TABLE orders (ord_id INTEGER PRIMARY KEY, cust_id INTEGER REFERENCES customers, emp_id INTEGER REFERENCES employees, order_date TEXT DEFAULT (date('now')));"
        "INSERT INTO orders VALUES (1,1,1,'2026-07-01'), (2,2,1,'2026-07-02'), (3,1,2,'2026-07-03');"
        "CREATE TABLE order_items (ord_id INTEGER REFERENCES orders, prod_id INTEGER, quantity INTEGER CHECK(quantity > 0), PRIMARY KEY(ord_id, prod_id));"
        "INSERT INTO order_items VALUES (1,1,2), (2,2,1), (3,1,1);"
    ),
    expected_output="[('Emperor', 2, 3), ('Rahim', 1, 1)]",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT e.name, COUNT(o.ord_id) AS orders_handled, COALESCE(SUM(oi.quantity),0) AS total_quantity",
        "FROM employees e LEFT JOIN orders o ON e.emp_id = o.emp_id",
        "LEFT JOIN order_items oi ON o.ord_id = oi.ord_id",
        "GROUP BY e.emp_id ORDER BY total_quantity DESC",
        "''')",
        "print(cursor.fetchall())",
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L100.json",
        module_name="Module_10_Beyond_SQLite",
        lesson_name="L100_Final_Capstone_Imperial_ERP_System"
    )