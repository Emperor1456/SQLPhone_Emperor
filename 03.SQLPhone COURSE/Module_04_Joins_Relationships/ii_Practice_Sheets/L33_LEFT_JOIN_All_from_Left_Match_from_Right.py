import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "📋  All Soldiers – LEFT JOIN with Regiment\n\n"
        "The `soldiers` table has 4 rows, but one soldier\n"
        "(Spy) has a NULL regiment_id.\n"
        "Write a LEFT JOIN query that returns ALL soldiers\n"
        "with their regiment name. Soldiers with no regiment\n"
        "should still appear (regiment_name will be NULL).\n"
        "Sort by soldier name.\n\n"
        "Expected output:\n[('Ali','Red Guard'), ('Emperor','Imperial Guard'), ('Hasan','Red Guard'), ('Spy',None)]"
    ),
    setup_sql=(
        "CREATE TABLE regiments (regiment_id INTEGER PRIMARY KEY, regiment_name TEXT NOT NULL);"
        "INSERT INTO regiments VALUES (1, 'Imperial Guard'), (2, 'Red Guard');"
        "CREATE TABLE soldiers (soldier_id INTEGER PRIMARY KEY, name TEXT NOT NULL, regiment_id INTEGER);"
        "INSERT INTO soldiers VALUES (1, 'Emperor', 1), (2, 'Spy', NULL), (3, 'Ali', 2), (4, 'Hasan', 2);"
    ),
    expected_output="[('Ali', 'Red Guard'), ('Emperor', 'Imperial Guard'), ('Hasan', 'Red Guard'), ('Spy', None)]",
    level=Level.EASY,
    hints=[
        "SELECT s.name, r.regiment_name FROM soldiers s LEFT JOIN regiments r ON s.regiment_id = r.regiment_id ORDER BY s.name;"
    ]
)

easy2 = Task(
    description=(
        "🔍  Find Unassigned – LEFT JOIN + IS NULL\n\n"
        "The same tables exist.\n"
        "Use a LEFT JOIN and WHERE right_column IS NULL\n"
        "to find soldiers who have NO regiment.\n"
        "Return only their name.\n\n"
        "Expected output: [('Spy',)]"
    ),
    setup_sql=(
        "CREATE TABLE regiments (regiment_id INTEGER PRIMARY KEY, regiment_name TEXT NOT NULL);"
        "INSERT INTO regiments VALUES (1, 'Imperial Guard'), (2, 'Red Guard');"
        "CREATE TABLE soldiers (soldier_id INTEGER PRIMARY KEY, name TEXT NOT NULL, regiment_id INTEGER);"
        "INSERT INTO soldiers VALUES (1, 'Emperor', 1), (2, 'Spy', NULL), (3, 'Ali', 2), (4, 'Hasan', 2);"
    ),
    expected_output="[('Spy',)]",
    level=Level.EASY,
    hints=[
        "SELECT s.name FROM soldiers s LEFT JOIN regiments r ON s.regiment_id = r.regiment_id WHERE s.regiment_id IS NULL;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "📊  Regimental Strength – Count with LEFT JOIN\n\n"
        "The `regiments` and `soldiers` tables exist.\n"
        "Write a query that returns EVERY regiment with\n"
        "the count of soldiers in each. Include regiments\n"
        "with ZERO soldiers.\n"
        "Use LEFT JOIN and GROUP BY.\n"
        "Sort by regiment name.\n\n"
        "Expected output:\n[('Blue Shield',0), ('Imperial Guard',1), ('Red Guard',2)]"
    ),
    setup_sql=(
        "CREATE TABLE regiments (regiment_id INTEGER PRIMARY KEY, regiment_name TEXT NOT NULL);"
        "INSERT INTO regiments VALUES (1, 'Imperial Guard'), (2, 'Red Guard'), (3, 'Blue Shield');"
        "CREATE TABLE soldiers (soldier_id INTEGER PRIMARY KEY, name TEXT NOT NULL, regiment_id INTEGER);"
        "INSERT INTO soldiers VALUES (1, 'Emperor', 1), (2, 'Ali', 2), (3, 'Hasan', 2);"
    ),
    expected_output="[('Blue Shield', 0), ('Imperial Guard', 1), ('Red Guard', 2)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT r.regiment_name, COUNT(s.soldier_id) AS soldier_count FROM regiments r LEFT JOIN soldiers s ON r.regiment_id = s.regiment_id GROUP BY r.regiment_id ORDER BY r.regiment_name;"
    ]
)

medium2 = Task(
    description=(
        "📋  All Customers – Even Those Without Orders\n\n"
        "Three tables exist: `customers`, `products`, `orders`.\n"
        "Write a query that returns ALL customers with\n"
        "their order details (order_id, product name, quantity).\n"
        "Customers with no orders should still appear\n"
        "(order_id will be NULL).\n"
        "Use two LEFT JOINs.\n"
        "Sort by customer name, then order_id.\n\n"
        "Expected output:\n[('Ali','Monitor',3), ('Emperor','Laptop',2), ('Emperor','Keyboard',1), ('Karim',None,None), ('Rahim','Mouse',5)]"
    ),
    setup_sql=(
        "CREATE TABLE customers (customer_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO customers VALUES (1, 'Emperor'), (2, 'Rahim'), (3, 'Ali'), (4, 'Karim');"
        "CREATE TABLE products (product_id INTEGER PRIMARY KEY, name TEXT NOT NULL, price REAL);"
        "INSERT INTO products VALUES (1, 'Laptop', 1000), (2, 'Mouse', 50), (3, 'Keyboard', 80), (4, 'Monitor', 300);"
        "CREATE TABLE orders (order_id INTEGER PRIMARY KEY, customer_id INTEGER, product_id INTEGER, quantity INTEGER);"
        "INSERT INTO orders VALUES (1, 1, 1, 2), (2, 2, 2, 5), (3, 1, 3, 1), (4, 3, 4, 3);"
    ),
    expected_output="[('Ali', 'Monitor', 3), ('Emperor', 'Laptop', 2), ('Emperor', 'Keyboard', 1), ('Karim', None, None), ('Rahim', 'Mouse', 5)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT c.name, p.name, o.quantity FROM customers c LEFT JOIN orders o ON c.customer_id = o.customer_id LEFT JOIN products p ON o.product_id = p.product_id ORDER BY c.name, o.order_id;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🔍  Products Never Ordered – LEFT JOIN + IS NULL\n\n"
        "The three tables from Medium2 exist.\n"
        "Write a query that finds all products that have\n"
        "NEVER been ordered.\n"
        "Use LEFT JOIN and WHERE right_column IS NULL.\n"
        "Return product name and price.\n"
        "Sort by product name.\n\n"
        "Expected output:\n[('Chair',250.0), ('Desk',500.0)]"
    ),
    setup_sql=(
        "CREATE TABLE customers (customer_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO customers VALUES (1, 'Emperor'), (2, 'Rahim'), (3, 'Ali');"
        "CREATE TABLE products (product_id INTEGER PRIMARY KEY, name TEXT NOT NULL, price REAL);"
        "INSERT INTO products VALUES (1, 'Laptop', 1000), (2, 'Mouse', 50), (3, 'Keyboard', 80), (4, 'Monitor', 300), (5, 'Desk', 500), (6, 'Chair', 250);"
        "CREATE TABLE orders (order_id INTEGER PRIMARY KEY, customer_id INTEGER, product_id INTEGER, quantity INTEGER);"
        "INSERT INTO orders VALUES (1, 1, 1, 2), (2, 2, 2, 5), (3, 1, 3, 1), (4, 3, 4, 3);"
    ),
    expected_output="[('Chair', 250.0), ('Desk', 500.0)]",
    level=Level.HARD,
    hints=[
        "SELECT p.name, p.price FROM products p LEFT JOIN orders o ON p.product_id = o.product_id WHERE o.order_id IS NULL ORDER BY p.name;"
    ]
)

hard2 = Task(
    description=(
        "🧹  COALESCE with LEFT JOIN – Friendly Defaults\n\n"
        "The `soldiers` and `regiments` tables exist.\n"
        "Write a query that returns ALL soldiers with\n"
        "their regiment name. But if a soldier has no\n"
        "regiment, display 'Unassigned' instead of NULL.\n"
        "Use COALESCE.\n"
        "Also compute a `pay_grade` column using CASE:\n"
        "  • salary >= 4500 → 'High'\n"
        "  • salary >= 3000 → 'Medium'\n"
        "  • ELSE → 'Low'\n"
        "Return name, regiment (with default), salary, pay_grade.\n"
        "Sort by name.\n\n"
        "Expected output:\n[('Ali','Red Guard',3500,'Medium'), ('Emperor','Imperial Guard',5000,'High'), ('Hasan','Unassigned',2500,'Low'), ('Rahim','Red Guard',4000,'Medium')]"
    ),
    setup_sql=(
        "CREATE TABLE regiments (regiment_id INTEGER PRIMARY KEY, regiment_name TEXT NOT NULL);"
        "INSERT INTO regiments VALUES (1, 'Imperial Guard'), (2, 'Red Guard');"
        "CREATE TABLE soldiers (soldier_id INTEGER PRIMARY KEY, name TEXT NOT NULL, regiment_id INTEGER, salary REAL);"
        "INSERT INTO soldiers VALUES (1, 'Emperor', 1, 5000), (2, 'Rahim', 2, 4000), (3, 'Ali', 2, 3500), (4, 'Hasan', NULL, 2500);"
    ),
    expected_output="[('Ali', 'Red Guard', 3500.0, 'Medium'), ('Emperor', 'Imperial Guard', 5000.0, 'High'), ('Hasan', 'Unassigned', 2500.0, 'Low'), ('Rahim', 'Red Guard', 4000.0, 'Medium')]",
    level=Level.HARD,
    hints=[
        "SELECT s.name, COALESCE(r.regiment_name, 'Unassigned') AS regiment, s.salary, CASE WHEN s.salary >= 4500 THEN 'High' WHEN s.salary >= 3000 THEN 'Medium' ELSE 'Low' END AS pay_grade FROM soldiers s LEFT JOIN regiments r ON s.regiment_id = r.regiment_id ORDER BY s.name;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L33.json",
        module_name="Module_04_Joins_Relationships",
        lesson_name="L33_LEFT_JOIN"
    )
