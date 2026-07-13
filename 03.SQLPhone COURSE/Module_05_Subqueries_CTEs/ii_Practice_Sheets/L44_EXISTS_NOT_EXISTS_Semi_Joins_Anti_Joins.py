import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "✅  EXISTS – Regiments with Soldiers\n\n"
        "The `regiments` and `soldiers` tables exist.\n"
        "Write a query that returns the regiment_name of\n"
        "regiments that have at least one soldier.\n"
        "Use EXISTS with a correlated subquery.\n"
        "Sort by regiment_name.\n\n"
        "Expected output:\n[('Imperial Guard',), ('Red Guard',)]"
    ),
    setup_sql=(
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, regiment_name TEXT);"
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard'), (3,'Blue Shield');"
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER);"
        "INSERT INTO soldiers VALUES (1,'Emperor',1), (2,'Rahim',2), (3,'Ali',2), (4,'Hasan',1);"
    ),
    expected_output="[('Imperial Guard',), ('Red Guard',)]",
    level=Level.EASY,
    hints=[
        "SELECT r.regiment_name FROM regiments r WHERE EXISTS (SELECT 1 FROM soldiers s WHERE s.regiment_id = r.id) ORDER BY r.regiment_name;"
    ]
)

easy2 = Task(
    description=(
        "❌  NOT EXISTS – Regiments with No Soldiers\n\n"
        "The same tables exist.\n"
        "Write a query that returns the regiment_name of\n"
        "regiments that have NO soldiers.\n"
        "Use NOT EXISTS with a correlated subquery.\n"
        "Sort by regiment_name.\n\n"
        "Expected output: [('Blue Shield',)]"
    ),
    setup_sql=(
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, regiment_name TEXT);"
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard'), (3,'Blue Shield');"
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER);"
        "INSERT INTO soldiers VALUES (1,'Emperor',1), (2,'Rahim',2), (3,'Ali',2), (4,'Hasan',1);"
    ),
    expected_output="[('Blue Shield',)]",
    level=Level.EASY,
    hints=[
        "SELECT r.regiment_name FROM regiments r WHERE NOT EXISTS (SELECT 1 FROM soldiers s WHERE s.regiment_id = r.id) ORDER BY r.regiment_name;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🔍  EXISTS with Additional Filter – Active Soldiers\n\n"
        "The `regiments` and `soldiers` tables exist.\n"
        "Write a query that returns the regiment_name of\n"
        "regiments that have at least one ACTIVE soldier.\n"
        "Use EXISTS with a correlated subquery that checks\n"
        "both regiment_id AND status = 'active'.\n"
        "Sort by regiment_name.\n\n"
        "Expected output:\n[('Imperial Guard',), ('Red Guard',)]"
    ),
    setup_sql=(
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, regiment_name TEXT);"
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard'), (3,'Blue Shield');"
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER, status TEXT);"
        "INSERT INTO soldiers VALUES (1,'Emperor',1,'active'), (2,'Rahim',2,'reserve'), (3,'Ali',2,'active'), (4,'Hasan',1,'active'), (5,'Spy',3,'reserve');"
    ),
    expected_output="[('Imperial Guard',), ('Red Guard',)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT r.regiment_name FROM regiments r WHERE EXISTS (SELECT 1 FROM soldiers s WHERE s.regiment_id = r.id AND s.status = 'active') ORDER BY r.regiment_name;"
    ]
)

medium2 = Task(
    description=(
        "📊  NOT EXISTS – Products Never Ordered\n\n"
        "Create tables `products` and `orders`.\n"
        "Write a query that returns product names that\n"
        "have never been ordered.\n"
        "Use NOT EXISTS with a correlated subquery.\n"
        "Sort by product name.\n\n"
        "Expected output:\n[('Chair',), ('Desk',)]"
    ),
    expected_output="[('Chair',), ('Desk',)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO products VALUES (1,'Laptop'), (2,'Mouse'), (3,'Chair'), (4,'Desk');",
        "CREATE TABLE orders (id INTEGER PRIMARY KEY, product_id INTEGER);",
        "INSERT INTO orders VALUES (1,1), (2,2), (3,1);",
        "SELECT p.name FROM products p WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.product_id = p.id) ORDER BY p.name;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  EXISTS with Two‑Level Correlation – Deployed Soldiers\n\n"
        "Create tables: `regiments`, `soldiers`, `deployments`.\n"
        "Write a query that returns the names of soldiers\n"
        "whose regiment has been deployed at least once.\n"
        "Use EXISTS with a subquery that checks deployments\n"
        "via the soldier's regiment_id.\n"
        "Sort by name.\n\n"
        "Expected output:\n[('Ali',), ('Emperor',), ('Hasan',)]"
    ),
    expected_output="[('Ali',), ('Emperor',), ('Hasan',)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard'), (3,'Blue Shield');",
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER);",
        "INSERT INTO soldiers VALUES (1,'Emperor',1), (2,'Rahim',3), (3,'Ali',1), (4,'Hasan',2);",
        "CREATE TABLE deployments (id INTEGER PRIMARY KEY, regiment_id INTEGER, location TEXT);",
        "INSERT INTO deployments VALUES (1,1,'North'), (2,2,'South');",
        "SELECT name FROM soldiers s WHERE EXISTS (SELECT 1 FROM deployments d WHERE d.regiment_id = s.regiment_id) ORDER BY name;"
    ]
)

hard2 = Task(
    description=(
        "📊  NOT EXISTS – Customers Without Recent Orders\n\n"
        "Create tables `customers` and `orders` with order_date.\n"
        "Write a query that returns the names of customers\n"
        "who have NOT placed any order in 2026.\n"
        "Use NOT EXISTS with a correlated subquery that checks\n"
        "both customer_id AND order_date >= '2026-01-01'.\n"
        "Sort by name.\n\n"
        "Expected output:\n[('Karim',), ('Rana',)]"
    ),
    expected_output="[('Karim',), ('Rana',)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO customers VALUES (1,'Emperor'), (2,'Rahim'), (3,'Karim'), (4,'Ali'), (5,'Rana');",
        "CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER, order_date TEXT);",
        "INSERT INTO orders VALUES (1,1,'2026-01-15'), (2,2,'2025-12-20'), (3,1,'2026-03-10'), (4,4,'2025-11-05');",
        "SELECT c.name FROM customers c WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id AND o.order_date >= '2026-01-01') ORDER BY c.name;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L44.json",
        module_name="Module_05_Subqueries_CTEs",
        lesson_name="L44_EXISTS_NOT_EXISTS"
    )
