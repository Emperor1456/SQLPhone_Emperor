import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🔗  Three‑Table JOIN – Soldiers + Regiments + Deployments\n\n"
        "Create three tables:\n"
        "  • regiments (id, name)\n"
        "  • soldiers (id, name, regiment_id, deployment_id)\n"
        "  • deployments (id, location)\n\n"
        "Insert 2 regiments, 4 soldiers, 2 deployments.\n"
        "One soldier has NULL deployment.\n"
        "Write a query using INNER JOIN on all three tables\n"
        "to return soldier name, regiment name, and deployment location.\n"
        "Sort by soldier name.\n\n"
        "Expected output:\n[('Ali','Red Guard','South'), ('Emperor','Imperial Guard','North'), ('Hasan','Red Guard','South')]"
    ),
    expected_output="[('Ali', 'Red Guard', 'South'), ('Emperor', 'Imperial Guard', 'North'), ('Hasan', 'Red Guard', 'South')]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard');",
        "CREATE TABLE deployments (id INTEGER PRIMARY KEY, location TEXT);",
        "INSERT INTO deployments VALUES (1,'North'), (2,'South');",
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER, deployment_id INTEGER);",
        "INSERT INTO soldiers VALUES (1,'Emperor',1,1), (2,'Rahim',2,2), (3,'Ali',2,2), (4,'Hasan',2,2);",
        "SELECT s.name, r.name, d.location FROM soldiers s JOIN regiments r ON s.regiment_id = r.id JOIN deployments d ON s.deployment_id = d.id ORDER BY s.name;"
    ]
)

easy2 = Task(
    description=(
        "📋  Mixed JOINs – INNER + LEFT\n\n"
        "The same three tables exist.\n"
        "Write a query that returns ALL soldiers with their\n"
        "regiment name and deployment location. Use INNER JOIN\n"
        "to regiments (every soldier has one) and LEFT JOIN to\n"
        "deployments (some soldiers are unassigned).\n"
        "Sort by soldier name.\n\n"
        "Expected output:\n[('Ali','Red Guard','South'), ('Emperor','Imperial Guard','North'), ('Hasan','Red Guard','South'), ('Rahim','Red Guard','South'), ('Spy','Red Guard',None)]"
    ),
    setup_sql=(
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT);"
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard');"
        "CREATE TABLE deployments (id INTEGER PRIMARY KEY, location TEXT);"
        "INSERT INTO deployments VALUES (1,'North'), (2,'South');"
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER, deployment_id INTEGER);"
        "INSERT INTO soldiers VALUES (1,'Emperor',1,1), (2,'Rahim',2,2), (3,'Ali',2,2), (4,'Hasan',2,2), (5,'Spy',2,NULL);"
    ),
    expected_output="[('Ali', 'Red Guard', 'South'), ('Emperor', 'Imperial Guard', 'North'), ('Hasan', 'Red Guard', 'South'), ('Rahim', 'Red Guard', 'South'), ('Spy', 'Red Guard', None)]",
    level=Level.EASY,
    hints=[
        "SELECT s.name, r.name, d.location FROM soldiers s JOIN regiments r ON s.regiment_id = r.id LEFT JOIN deployments d ON s.deployment_id = d.id ORDER BY s.name;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "💰  Four‑Table JOIN – Orders + Customers + Products + Shipments\n\n"
        "Create four tables: customers, products, orders, shipments.\n"
        "Insert varied data.\n"
        "Write a query that returns order_id, customer name,\n"
        "product name, quantity, and shipment status.\n"
        "Join all four tables. Use LEFT JOIN for shipments\n"
        "since not all orders have shipped yet.\n"
        "Sort by order_id.\n\n"
        "Expected output:\n[(1,'Emperor','Laptop',2,'delivered'), (2,'Rahim','Mouse',5,'in transit'), (3,'Emperor','Keyboard',1,None)]"
    ),
    setup_sql=(
        "CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT);"
        "INSERT INTO customers VALUES (1,'Emperor'), (2,'Rahim');"
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price REAL);"
        "INSERT INTO products VALUES (1,'Laptop',1000), (2,'Mouse',50), (3,'Keyboard',80);"
        "CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER, product_id INTEGER, quantity INTEGER);"
        "INSERT INTO orders VALUES (1,1,1,2), (2,2,2,5), (3,1,3,1);"
        "CREATE TABLE shipments (id INTEGER PRIMARY KEY, order_id INTEGER, status TEXT);"
        "INSERT INTO shipments VALUES (1,1,'delivered'), (2,2,'in transit');"
    ),
    expected_output="[(1, 'Emperor', 'Laptop', 2, 'delivered'), (2, 'Rahim', 'Mouse', 5, 'in transit'), (3, 'Emperor', 'Keyboard', 1, None)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT o.id, c.name, p.name, o.quantity, sh.status FROM orders o JOIN customers c ON o.customer_id = c.id JOIN products p ON o.product_id = p.id LEFT JOIN shipments sh ON o.id = sh.order_id ORDER BY o.id;"
    ]
)

medium2 = Task(
    description=(
        "📊  Five‑Table JOIN – Full Supply Chain\n\n"
        "Create five tables: suppliers, products, orders, customers, shipments.\n"
        "Insert minimal data connecting all.\n"
        "Write a query that returns: product name, supplier name,\n"
        "order_id, customer name, and shipment status.\n"
        "Use appropriate JOINs (INNER for required, LEFT for optional).\n"
        "Sort by product name, then order_id.\n\n"
        "Expected output:\n[('Keyboard','OfficeDepot',3,'Emperor',None), ('Laptop','TechCorp',1,'Emperor','delivered'), ('Mouse','TechCorp',2,'Rahim','in transit')]"
    ),
    setup_sql=(
        "CREATE TABLE suppliers (id INTEGER PRIMARY KEY, name TEXT);"
        "INSERT INTO suppliers VALUES (1,'TechCorp'), (2,'OfficeDepot');"
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, supplier_id INTEGER);"
        "INSERT INTO products VALUES (1,'Laptop',1), (2,'Mouse',1), (3,'Keyboard',2);"
        "CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT);"
        "INSERT INTO customers VALUES (1,'Emperor'), (2,'Rahim');"
        "CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER, product_id INTEGER, quantity INTEGER);"
        "INSERT INTO orders VALUES (1,1,1,2), (2,2,2,5), (3,1,3,1);"
        "CREATE TABLE shipments (id INTEGER PRIMARY KEY, order_id INTEGER, status TEXT);"
        "INSERT INTO shipments VALUES (1,1,'delivered'), (2,2,'in transit');"
    ),
    expected_output="[('Keyboard', 'OfficeDepot', 3, 'Emperor', None), ('Laptop', 'TechCorp', 1, 'Emperor', 'delivered'), ('Mouse', 'TechCorp', 2, 'Rahim', 'in transit')]",
    level=Level.MEDIUM,
    hints=[
        "SELECT p.name, sup.name, o.id, c.name, sh.status FROM products p JOIN suppliers sup ON p.supplier_id = sup.id JOIN orders o ON p.id = o.product_id JOIN customers c ON o.customer_id = c.id LEFT JOIN shipments sh ON o.id = sh.order_id ORDER BY p.name, o.id;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  Complex Report – Revenue per Supplier per Region\n\n"
        "Create five tables: suppliers, products, orders, customers, shipments.\n"
        "Insert data with varied regions and suppliers.\n"
        "Write a query that returns:\n"
        "  • supplier name\n"
        "  • customer region\n"
        "  • total_revenue (SUM of quantity * price)\n"
        "  • order_count\n"
        "Join all relevant tables.\n"
        "Group by supplier and region.\n"
        "Sort by total_revenue descending.\n\n"
        "Expected output:\n[('TechCorp','North',2000.0,1), ('TechCorp','South',250.0,1), ('OfficeDepot','North',80.0,1)]"
    ),
    expected_output="[('TechCorp', 'North', 2000.0, 1), ('TechCorp', 'South', 250.0, 1), ('OfficeDepot', 'North', 80.0, 1)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE suppliers (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO suppliers VALUES (1,'TechCorp'), (2,'OfficeDepot');",
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, supplier_id INTEGER, price REAL);",
        "INSERT INTO products VALUES (1,'Laptop',1,1000), (2,'Mouse',1,50), (3,'Keyboard',2,80);",
        "CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT, region TEXT);",
        "INSERT INTO customers VALUES (1,'Emperor','North'), (2,'Rahim','South');",
        "CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER, product_id INTEGER, quantity INTEGER);",
        "INSERT INTO orders VALUES (1,1,1,2), (2,2,2,5), (3,1,3,1);",
        "SELECT sup.name, c.region, SUM(o.quantity * p.price) AS total_revenue, COUNT(o.id) AS order_count FROM suppliers sup JOIN products p ON sup.id = p.supplier_id JOIN orders o ON p.id = o.product_id JOIN customers c ON o.customer_id = c.id GROUP BY sup.id, c.region ORDER BY total_revenue DESC;"
    ]
)

hard2 = Task(
    description=(
        "📊  Full‑Stack Dashboard – Multi‑KPI Query\n\n"
        "Create six tables: regiments, soldiers, deployments, missions,\n"
        "supplies, and mission_supplies (join table).\n"
        "Insert data connecting soldiers → regiments → deployments,\n"
        "and missions → mission_supplies → supplies.\n"
        "Write ONE query that returns, for each soldier:\n"
        "  • soldier name\n"
        "  • regiment name\n"
        "  • deployment location\n"
        "  • mission_count (number of missions assigned)\n"
        "  • total_supply_weight (SUM of quantity * weight from supplies)\n"
        "Use multiple JOINs and GROUP BY.\n"
        "Sort by soldier name.\n\n"
        "Expected output:\n[('Ali','Red Guard','South',1,15.0), ('Emperor','Imperial Guard','North',2,55.0), ('Rahim','Red Guard','South',0,None)]"
    ),
    expected_output="[('Ali', 'Red Guard', 'South', 1, 15.0), ('Emperor', 'Imperial Guard', 'North', 2, 55.0), ('Rahim', 'Red Guard', 'South', 0, None)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard');",
        "CREATE TABLE deployments (id INTEGER PRIMARY KEY, location TEXT);",
        "INSERT INTO deployments VALUES (1,'North'), (2,'South');",
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER, deployment_id INTEGER);",
        "INSERT INTO soldiers VALUES (1,'Emperor',1,1), (2,'Rahim',2,2), (3,'Ali',2,2);",
        "CREATE TABLE missions (id INTEGER PRIMARY KEY, soldier_id INTEGER, task TEXT);",
        "INSERT INTO missions VALUES (1,1,'Patrol'), (2,1,'Recon'), (3,3,'Guard');",
        "CREATE TABLE supplies (id INTEGER PRIMARY KEY, name TEXT, weight REAL);",
        "INSERT INTO supplies VALUES (1,'Ammo',10), (2,'Rations',5);",
        "CREATE TABLE mission_supplies (mission_id INTEGER, supply_id INTEGER, quantity INTEGER, PRIMARY KEY(mission_id, supply_id));",
        "INSERT INTO mission_supplies VALUES (1,1,2), (1,2,3), (2,1,1), (3,1,1), (3,2,1);",
        "SELECT s.name, r.name, d.location, COUNT(DISTINCT m.id) AS mission_count, SUM(ms.quantity * sup.weight) AS total_supply_weight FROM soldiers s JOIN regiments r ON s.regiment_id = r.id JOIN deployments d ON s.deployment_id = d.id LEFT JOIN missions m ON s.id = m.soldier_id LEFT JOIN mission_supplies ms ON m.id = ms.mission_id LEFT JOIN supplies sup ON ms.supply_id = sup.id GROUP BY s.id ORDER BY s.name;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L36.json",
        module_name="Module_04_Joins_Relationships",
        lesson_name="L36_Joining_More_Than_Two_Tables"
    )
