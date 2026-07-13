import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🏗️  Create & Seed – Imperial Commerce\n\n"
        "Create two tables with full constraints:\n\n"
        "1. `customers`:\n"
        "  • id INTEGER PRIMARY KEY\n"
        "  • name TEXT NOT NULL\n"
        "  • city TEXT NOT NULL\n"
        "  • joined TEXT DEFAULT (date('now'))\n\n"
        "2. `products`:\n"
        "  • id INTEGER PRIMARY KEY\n"
        "  • name TEXT NOT NULL\n"
        "  • category TEXT NOT NULL\n"
        "  • price REAL CHECK(price > 0)\n\n"
        "Insert 3 customers and 3 products.\n"
        "Then SELECT all customers sorted by name.\n\n"
        "Expected output:\n[('Emperor','Dhaka'), ('Karim','Khulna'), ('Rahim','Chittagong')]"
    ),
    expected_output="[('Emperor', 'Dhaka'), ('Karim', 'Khulna'), ('Rahim', 'Chittagong')]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT NOT NULL, city TEXT NOT NULL, joined TEXT DEFAULT (date('now')));",
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, category TEXT NOT NULL, price REAL CHECK(price > 0));",
        "INSERT INTO customers (name, city) VALUES ('Emperor','Dhaka'), ('Rahim','Chittagong'), ('Karim','Khulna');",
        "INSERT INTO products (name, category, price) VALUES ('Laptop','Electronics',999.99), ('Desk','Furniture',249.50), ('Mouse','Electronics',24.99);",
        "SELECT name, city FROM customers ORDER BY name;"
    ]
)

easy2 = Task(
    description=(
        "🔗  Order Lookup – JOIN Query\n\n"
        "The `customers` and `products` tables exist.\n"
        "Create an `orders` table:\n"
        "  • id INTEGER PRIMARY KEY\n"
        "  • customer_id INTEGER REFERENCES customers(id)\n"
        "  • product_id INTEGER REFERENCES products(id)\n"
        "  • qty INTEGER CHECK(qty > 0)\n"
        "  • order_date TEXT DEFAULT (date('now'))\n\n"
        "Insert 3 orders linking customers to products.\n"
        "Then SELECT order_id, customer name, product name,\n"
        "and qty for all orders, sorted by order_id.\n\n"
        "Expected output:\n[(1,'Emperor','Laptop',2), (2,'Rahim','Desk',1), (3,'Emperor','Mouse',5)]"
    ),
    expected_output="[(1, 'Emperor', 'Laptop', 2), (2, 'Rahim', 'Desk', 1), (3, 'Emperor', 'Mouse', 5)]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT NOT NULL, city TEXT NOT NULL);",
        "INSERT INTO customers VALUES (1,'Emperor','Dhaka'), (2,'Rahim','Chittagong'), (3,'Karim','Khulna');",
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, category TEXT NOT NULL, price REAL CHECK(price > 0));",
        "INSERT INTO products VALUES (1,'Laptop','Electronics',999.99), (2,'Desk','Furniture',249.50), (3,'Mouse','Electronics',24.99);",
        "CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER REFERENCES customers(id), product_id INTEGER REFERENCES products(id), qty INTEGER CHECK(qty > 0), order_date TEXT DEFAULT (date('now')));",
        "INSERT INTO orders (customer_id, product_id, qty) VALUES (1,1,2), (2,2,1), (1,3,5);",
        "SELECT o.id, c.name, p.name, o.qty FROM orders o JOIN customers c ON o.customer_id = c.id JOIN products p ON o.product_id = p.id ORDER BY o.id;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "💰  Revenue Report – Computed Columns\n\n"
        "The three tables exist with 3 orders.\n"
        "Write a query that returns:\n"
        "  • order_id\n"
        "  • customer name\n"
        "  • product name\n"
        "  • line_total (qty * price)\n"
        "  • order_date\n"
        "Sort by line_total descending.\n\n"
        "Expected output:\n[(1,'Emperor','Laptop',1999.98,'2026-07-01'), (3,'Emperor','Mouse',124.95,'2026-07-10'), (2,'Rahim','Desk',249.50,'2026-07-05')]"
    ),
    setup_sql=(
        "CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT NOT NULL, city TEXT NOT NULL);"
        "INSERT INTO customers VALUES (1,'Emperor','Dhaka'), (2,'Rahim','Chittagong'), (3,'Karim','Khulna');"
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, category TEXT NOT NULL, price REAL CHECK(price > 0));"
        "INSERT INTO products VALUES (1,'Laptop','Electronics',999.99), (2,'Desk','Furniture',249.50), (3,'Mouse','Electronics',24.99);"
        "CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER REFERENCES customers(id), product_id INTEGER REFERENCES products(id), qty INTEGER CHECK(qty > 0), order_date TEXT DEFAULT (date('now')));"
        "INSERT INTO orders (customer_id, product_id, qty, order_date) VALUES (1,1,2,'2026-07-01'), (2,2,1,'2026-07-05'), (1,3,5,'2026-07-10');"
    ),
    expected_output="[(1, 'Emperor', 'Laptop', 1999.98, '2026-07-01'), (3, 'Emperor', 'Mouse', 124.95, '2026-07-10'), (2, 'Rahim', 'Desk', 249.5, '2026-07-05')]",
    level=Level.MEDIUM,
    hints=[
        "SELECT o.id, c.name, p.name, o.qty * p.price AS line_total, o.order_date FROM orders o JOIN customers c ON o.customer_id = c.id JOIN products p ON o.product_id = p.id ORDER BY line_total DESC;"
    ]
)

medium2 = Task(
    description=(
        "📊  Order Classification – CASE\n\n"
        "The three tables exist with 3 orders.\n"
        "Write a query that returns:\n"
        "  • order_id\n"
        "  • customer name\n"
        "  • line_total (qty * price)\n"
        "  • size – use CASE:\n"
        "      • line_total >= 1000 → 'Large'\n"
        "      • line_total >= 200 → 'Medium'\n"
        "      • ELSE → 'Small'\n"
        "Sort by order_id.\n\n"
        "Expected output:\n[(1,'Emperor',1999.98,'Large'), (2,'Rahim',249.5,'Medium'), (3,'Emperor',124.95,'Small')]"
    ),
    setup_sql=(
        "CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT NOT NULL, city TEXT NOT NULL);"
        "INSERT INTO customers VALUES (1,'Emperor','Dhaka'), (2,'Rahim','Chittagong'), (3,'Karim','Khulna');"
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, category TEXT NOT NULL, price REAL CHECK(price > 0));"
        "INSERT INTO products VALUES (1,'Laptop','Electronics',999.99), (2,'Desk','Furniture',249.50), (3,'Mouse','Electronics',24.99);"
        "CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER REFERENCES customers(id), product_id INTEGER REFERENCES products(id), qty INTEGER CHECK(qty > 0), order_date TEXT DEFAULT (date('now')));"
        "INSERT INTO orders (customer_id, product_id, qty, order_date) VALUES (1,1,2,'2026-07-01'), (2,2,1,'2026-07-05'), (1,3,5,'2026-07-10');"
    ),
    expected_output="[(1, 'Emperor', 1999.98, 'Large'), (2, 'Rahim', 249.5, 'Medium'), (3, 'Emperor', 124.95, 'Small')]",
    level=Level.MEDIUM,
    hints=[
        "SELECT o.id, c.name, o.qty * p.price AS line_total, CASE WHEN o.qty * p.price >= 1000 THEN 'Large' WHEN o.qty * p.price >= 200 THEN 'Medium' ELSE 'Small' END AS size FROM orders o JOIN customers c ON o.customer_id = c.id JOIN products p ON o.product_id = p.id ORDER BY o.id;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🔍  Customer Filter – Recent High‑Value\n\n"
        "The three tables exist with orders.\n"
        "Add one more order:\n"
        "  (4, 2, 3, 3, '2026-07-12')\n"
        "Write a query that returns customer name,\n"
        "product name, line_total, and order_date\n"
        "for orders that:\n"
        "  • Were placed in the last 30 days (use date arithmetic)\n"
        "  • Have a line_total > 100\n"
        "  • Customer is from 'Dhaka' OR 'Chittagong' (use IN)\n"
        "Sort by order_date descending.\n\n"
        "Expected output:\n[('Rahim','Mouse',74.97,'2026-07-12'), ('Emperor','Mouse',124.95,'2026-07-10'), ('Rahim','Desk',249.5,'2026-07-05'), ('Emperor','Laptop',1999.98,'2026-07-01')]"
    ),
    setup_sql=(
        "CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT NOT NULL, city TEXT NOT NULL);"
        "INSERT INTO customers VALUES (1,'Emperor','Dhaka'), (2,'Rahim','Chittagong'), (3,'Karim','Khulna');"
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, category TEXT NOT NULL, price REAL CHECK(price > 0));"
        "INSERT INTO products VALUES (1,'Laptop','Electronics',999.99), (2,'Desk','Furniture',249.50), (3,'Mouse','Electronics',24.99);"
        "CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER REFERENCES customers(id), product_id INTEGER REFERENCES products(id), qty INTEGER CHECK(qty > 0), order_date TEXT DEFAULT (date('now')));"
        "INSERT INTO orders (customer_id, product_id, qty, order_date) VALUES (1,1,2,'2026-07-01'), (2,2,1,'2026-07-05'), (1,3,5,'2026-07-10'), (2,3,3,'2026-07-12');"
    ),
    expected_output="[('Rahim', 'Mouse', 74.97, '2026-07-12'), ('Emperor', 'Mouse', 124.95, '2026-07-10'), ('Rahim', 'Desk', 249.5, '2026-07-05'), ('Emperor', 'Laptop', 1999.98, '2026-07-01')]",
    level=Level.HARD,
    hints=[
        "SELECT c.name, p.name, o.qty * p.price AS line_total, o.order_date FROM orders o JOIN customers c ON o.customer_id = c.id JOIN products p ON o.product_id = p.id WHERE o.order_date >= date('now', '-30 days') AND o.qty * p.price > 50 AND c.city IN ('Dhaka','Chittagong') ORDER BY o.order_date DESC;"
    ]
)

hard2 = Task(
    description=(
        "📊  Customer Spend Summary – Multi‑Function\n\n"
        "The three tables exist with 4 orders.\n"
        "Write a query that returns, for each customer:\n"
        "  • name\n"
        "  • city\n"
        "  • order_count (number of orders)\n"
        "  • total_spent (SUM of line totals)\n"
        "  • avg_order_value (ROUNDed to 2 decimals)\n"
        "  • status – CASE:\n"
        "      • total_spent >= 1000 → 'VIP'\n"
        "      • total_spent >= 200 → 'Regular'\n"
        "      • ELSE → 'New'\n"
        "Sort by total_spent descending.\n\n"
        "Expected output:\n[('Emperor','Dhaka',2,2124.93,1062.46,'VIP'), ('Rahim','Chittagong',2,324.47,162.24,'Regular')]"
    ),
    setup_sql=(
        "CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT NOT NULL, city TEXT NOT NULL);"
        "INSERT INTO customers VALUES (1,'Emperor','Dhaka'), (2,'Rahim','Chittagong'), (3,'Karim','Khulna');"
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, category TEXT NOT NULL, price REAL CHECK(price > 0));"
        "INSERT INTO products VALUES (1,'Laptop','Electronics',999.99), (2,'Desk','Furniture',249.50), (3,'Mouse','Electronics',24.99);"
        "CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER REFERENCES customers(id), product_id INTEGER REFERENCES products(id), qty INTEGER CHECK(qty > 0), order_date TEXT DEFAULT (date('now')));"
        "INSERT INTO orders (customer_id, product_id, qty, order_date) VALUES (1,1,2,'2026-07-01'), (2,2,1,'2026-07-05'), (1,3,5,'2026-07-10'), (2,3,3,'2026-07-12');"
    ),
    expected_output="[('Emperor', 'Dhaka', 2, 2124.93, 1062.46, 'VIP'), ('Rahim', 'Chittagong', 2, 324.47, 162.24, 'Regular')]",
    level=Level.HARD,
    hints=[
        "SELECT c.name, c.city, COUNT(o.id) AS order_count, SUM(o.qty * p.price) AS total_spent, ROUND(AVG(o.qty * p.price), 2) AS avg_order_value, CASE WHEN SUM(o.qty * p.price) >= 1000 THEN 'VIP' WHEN SUM(o.qty * p.price) >= 200 THEN 'Regular' ELSE 'New' END AS status FROM customers c JOIN orders o ON c.id = o.customer_id JOIN products p ON o.product_id = p.id GROUP BY c.id ORDER BY total_spent DESC;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L20.json",
        module_name="Module_02_Filtering_Conditional_Logic",
        lesson_name="L20_Module_2_Capstone"
    )
