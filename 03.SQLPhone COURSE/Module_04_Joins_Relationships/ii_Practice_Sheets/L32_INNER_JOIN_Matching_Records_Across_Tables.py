import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🔗  First JOIN – Soldiers + Regiments\n\n"
        "The `soldiers` and `regiments` tables exist.\n"
        "Write a query that returns the soldier's name\n"
        "and their regiment's name using INNER JOIN.\n"
        "Sort by soldier name.\n\n"
        "Expected output:\n[('Ali','Red Guard'), ('Emperor','Imperial Guard'), ('Hasan','Red Guard')]"
    ),
    setup_sql=(
        "CREATE TABLE regiments (regiment_id INTEGER PRIMARY KEY, regiment_name TEXT NOT NULL);"
        "INSERT INTO regiments VALUES (1, 'Imperial Guard'), (2, 'Red Guard');"
        "CREATE TABLE soldiers (soldier_id INTEGER PRIMARY KEY, name TEXT NOT NULL, regiment_id INTEGER);"
        "INSERT INTO soldiers VALUES (1, 'Emperor', 1), (2, 'Rahim', 2), (3, 'Ali', 2), (4, 'Hasan', 2);"
    ),
    expected_output="[('Ali', 'Red Guard'), ('Emperor', 'Imperial Guard'), ('Hasan', 'Red Guard')]",
    level=Level.EASY,
    hints=[
        "SELECT s.name, r.regiment_name FROM soldiers s JOIN regiments r ON s.regiment_id = r.regiment_id ORDER BY s.name;"
    ]
)

easy2 = Task(
    description=(
        "📊  JOIN + WHERE – Filter After Join\n\n"
        "The same tables exist.\n"
        "Return the soldier's name and regiment name\n"
        "for soldiers who are in the 'Red Guard' regiment.\n"
        "Use JOIN and a WHERE clause.\n"
        "Sort by name.\n\n"
        "Expected output:\n[('Ali','Red Guard'), ('Hasan','Red Guard'), ('Rahim','Red Guard')]"
    ),
    setup_sql=(
        "CREATE TABLE regiments (regiment_id INTEGER PRIMARY KEY, regiment_name TEXT NOT NULL);"
        "INSERT INTO regiments VALUES (1, 'Imperial Guard'), (2, 'Red Guard');"
        "CREATE TABLE soldiers (soldier_id INTEGER PRIMARY KEY, name TEXT NOT NULL, regiment_id INTEGER);"
        "INSERT INTO soldiers VALUES (1, 'Emperor', 1), (2, 'Rahim', 2), (3, 'Ali', 2), (4, 'Hasan', 2);"
    ),
    expected_output="[('Ali', 'Red Guard'), ('Hasan', 'Red Guard'), ('Rahim', 'Red Guard')]",
    level=Level.EASY,
    hints=[
        "SELECT s.name, r.regiment_name FROM soldiers s JOIN regiments r ON s.regiment_id = r.regiment_id WHERE r.regiment_name = 'Red Guard' ORDER BY s.name;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "📋  Three‑Table JOIN – Orders with Customer & Product\n\n"
        "Three tables exist: `customers`, `products`, `orders`.\n"
        "Write a query that returns:\n"
        "  • order_id\n"
        "  • customer name\n"
        "  • product name\n"
        "  • quantity\n"
        "Join all three tables.\n"
        "Sort by order_id.\n\n"
        "Expected output:\n[(1,'Emperor','Laptop',2), (2,'Rahim','Mouse',5), (3,'Emperor','Keyboard',1), (4,'Ali','Monitor',3)]"
    ),
    setup_sql=(
        "CREATE TABLE customers (customer_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO customers VALUES (1, 'Emperor'), (2, 'Rahim'), (3, 'Ali');"
        "CREATE TABLE products (product_id INTEGER PRIMARY KEY, name TEXT NOT NULL, price REAL);"
        "INSERT INTO products VALUES (1, 'Laptop', 1000), (2, 'Mouse', 50), (3, 'Keyboard', 80), (4, 'Monitor', 300);"
        "CREATE TABLE orders (order_id INTEGER PRIMARY KEY, customer_id INTEGER, product_id INTEGER, quantity INTEGER);"
        "INSERT INTO orders VALUES (1, 1, 1, 2), (2, 2, 2, 5), (3, 1, 3, 1), (4, 3, 4, 3);"
    ),
    expected_output="[(1, 'Emperor', 'Laptop', 2), (2, 'Rahim', 'Mouse', 5), (3, 'Emperor', 'Keyboard', 1), (4, 'Ali', 'Monitor', 3)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT o.order_id, c.name, p.name, o.quantity FROM orders o JOIN customers c ON o.customer_id = c.customer_id JOIN products p ON o.product_id = p.product_id ORDER BY o.order_id;"
    ]
)

medium2 = Task(
    description=(
        "💰  JOIN + Computed Column – Line Total\n\n"
        "The three tables from Medium1 exist.\n"
        "Write a query that returns order_id, customer name,\n"
        "product name, quantity, price, and line total\n"
        "(quantity * price) for each order.\n"
        "Sort by line total descending.\n\n"
        "Expected output:\n[(1,'Emperor','Laptop',2,1000.0,2000.0), (4,'Ali','Monitor',3,300.0,900.0), (2,'Rahim','Mouse',5,50.0,250.0), (3,'Emperor','Keyboard',1,80.0,80.0)]"
    ),
    setup_sql=(
        "CREATE TABLE customers (customer_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO customers VALUES (1, 'Emperor'), (2, 'Rahim'), (3, 'Ali');"
        "CREATE TABLE products (product_id INTEGER PRIMARY KEY, name TEXT NOT NULL, price REAL);"
        "INSERT INTO products VALUES (1, 'Laptop', 1000), (2, 'Mouse', 50), (3, 'Keyboard', 80), (4, 'Monitor', 300);"
        "CREATE TABLE orders (order_id INTEGER PRIMARY KEY, customer_id INTEGER, product_id INTEGER, quantity INTEGER);"
        "INSERT INTO orders VALUES (1, 1, 1, 2), (2, 2, 2, 5), (3, 1, 3, 1), (4, 3, 4, 3);"
    ),
    expected_output="[(1, 'Emperor', 'Laptop', 2, 1000.0, 2000.0), (4, 'Ali', 'Monitor', 3, 300.0, 900.0), (2, 'Rahim', 'Mouse', 5, 50.0, 250.0), (3, 'Emperor', 'Keyboard', 1, 80.0, 80.0)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT o.order_id, c.name, p.name, o.quantity, p.price, o.quantity * p.price AS line_total FROM orders o JOIN customers c ON o.customer_id = c.customer_id JOIN products p ON o.product_id = p.product_id ORDER BY line_total DESC;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  JOIN + Aggregation – Revenue per Customer\n\n"
        "The three tables from Medium1 exist.\n"
        "Write a query that returns, for each customer:\n"
        "  • customer name\n"
        "  • order_count (number of orders)\n"
        "  • total_spent (SUM of line totals)\n"
        "Group by customer.\n"
        "Sort by total_spent descending.\n\n"
        "Expected output:\n[('Emperor',2,2080.0), ('Ali',1,900.0), ('Rahim',1,250.0)]"
    ),
    setup_sql=(
        "CREATE TABLE customers (customer_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO customers VALUES (1, 'Emperor'), (2, 'Rahim'), (3, 'Ali');"
        "CREATE TABLE products (product_id INTEGER PRIMARY KEY, name TEXT NOT NULL, price REAL);"
        "INSERT INTO products VALUES (1, 'Laptop', 1000), (2, 'Mouse', 50), (3, 'Keyboard', 80), (4, 'Monitor', 300);"
        "CREATE TABLE orders (order_id INTEGER PRIMARY KEY, customer_id INTEGER, product_id INTEGER, quantity INTEGER);"
        "INSERT INTO orders VALUES (1, 1, 1, 2), (2, 2, 2, 5), (3, 1, 3, 1), (4, 3, 4, 3);"
    ),
    expected_output="[('Emperor', 2, 2080.0), ('Ali', 1, 900.0), ('Rahim', 1, 250.0)]",
    level=Level.HARD,
    hints=[
        "SELECT c.name, COUNT(o.order_id) AS order_count, SUM(o.quantity * p.price) AS total_spent FROM customers c JOIN orders o ON c.customer_id = o.customer_id JOIN products p ON o.product_id = p.product_id GROUP BY c.customer_id ORDER BY total_spent DESC;"
    ]
)

hard2 = Task(
    description=(
        "🔍  Multi‑Table JOIN with Filter – Complex Report\n\n"
        "Four tables exist: `regiments`, `soldiers`, `missions`, `deployments`.\n"
        "Write a query that returns:\n"
        "  • soldier name\n"
        "  • regiment name\n"
        "  • mission task\n"
        "  • deployment location\n"
        "for soldiers who are in 'Imperial Guard' regiment\n"
        "AND have missions whose task contains 'Recon'.\n"
        "Join all four tables.\n"
        "Sort by soldier name.\n\n"
        "Expected output:\n[('Emperor','Imperial Guard','Recon Alpha','North Sector'), ('Emperor','Imperial Guard','Recon Beta','South Sector')]"
    ),
    setup_sql=(
        "CREATE TABLE regiments (regiment_id INTEGER PRIMARY KEY, regiment_name TEXT NOT NULL);"
        "INSERT INTO regiments VALUES (1, 'Imperial Guard'), (2, 'Red Guard');"
        "CREATE TABLE soldiers (soldier_id INTEGER PRIMARY KEY, name TEXT NOT NULL, regiment_id INTEGER);"
        "INSERT INTO soldiers VALUES (1, 'Emperor', 1), (2, 'Rahim', 2), (3, 'Ali', 1);"
        "CREATE TABLE missions (mission_id INTEGER PRIMARY KEY, soldier_id INTEGER, task TEXT, deployment_id INTEGER);"
        "INSERT INTO missions VALUES (1, 1, 'Recon Alpha', 1), (2, 1, 'Recon Beta', 2), (3, 2, 'Guard Duty', 1), (4, 3, 'Supply Run', 2);"
        "CREATE TABLE deployments (deployment_id INTEGER PRIMARY KEY, location TEXT);"
        "INSERT INTO deployments VALUES (1, 'North Sector'), (2, 'South Sector');"
    ),
    expected_output="[('Emperor', 'Imperial Guard', 'Recon Alpha', 'North Sector'), ('Emperor', 'Imperial Guard', 'Recon Beta', 'South Sector')]",
    level=Level.HARD,
    hints=[
        "SELECT s.name, r.regiment_name, m.task, d.location FROM soldiers s JOIN regiments r ON s.regiment_id = r.regiment_id JOIN missions m ON s.soldier_id = m.soldier_id JOIN deployments d ON m.deployment_id = d.deployment_id WHERE r.regiment_name = 'Imperial Guard' AND m.task LIKE '%Recon%' ORDER BY s.name;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L32.json",
        module_name="Module_04_Joins_Relationships",
        lesson_name="L32_INNER_JOIN"
    )
