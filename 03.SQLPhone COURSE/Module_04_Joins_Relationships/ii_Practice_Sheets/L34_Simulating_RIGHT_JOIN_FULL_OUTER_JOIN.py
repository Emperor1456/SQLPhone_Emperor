import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🔄  Simulate RIGHT JOIN – Swap Tables\n\n"
        "The `regiments` and `soldiers` tables exist.\n"
        "A RIGHT JOIN shows all regiments, even those\n"
        "without soldiers. SQLite has no RIGHT JOIN keyword.\n"
        "Simulate it by swapping the table order in a LEFT JOIN.\n"
        "Return regiment_name and soldier name for ALL regiments.\n"
        "Sort by regiment_name, then soldier name.\n\n"
        "Expected output:\n[('Blue Shield',None), ('Imperial Guard','Emperor'), ('Red Guard','Ali'), ('Red Guard','Hasan'), ('Red Guard','Rahim')]"
    ),
    setup_sql=(
        "CREATE TABLE regiments (regiment_id INTEGER PRIMARY KEY, regiment_name TEXT NOT NULL);"
        "INSERT INTO regiments VALUES (1, 'Imperial Guard'), (2, 'Red Guard'), (3, 'Blue Shield');"
        "CREATE TABLE soldiers (soldier_id INTEGER PRIMARY KEY, name TEXT NOT NULL, regiment_id INTEGER);"
        "INSERT INTO soldiers VALUES (1, 'Emperor', 1), (2, 'Rahim', 2), (3, 'Ali', 2), (4, 'Hasan', 2);"
    ),
    expected_output="[('Blue Shield', None), ('Imperial Guard', 'Emperor'), ('Red Guard', 'Ali'), ('Red Guard', 'Hasan'), ('Red Guard', 'Rahim')]",
    level=Level.EASY,
    hints=[
        "SELECT r.regiment_name, s.name FROM regiments r LEFT JOIN soldiers s ON r.regiment_id = s.regiment_id ORDER BY r.regiment_name, s.name;"
    ]
)

easy2 = Task(
    description=(
        "📋  Simulate RIGHT JOIN – All Products\n\n"
        "Create two tables: `suppliers` and `products`.\n"
        "Insert 3 suppliers, but only 2 have products.\n"
        "Simulate a RIGHT JOIN on products (show all products,\n"
        "even if their supplier info is missing).\n"
        "Use LEFT JOIN with swapped tables.\n"
        "Return product name and supplier name.\n"
        "Sort by product name.\n\n"
        "Expected output:\n[('Laptop','TechCorp'), ('Mouse','TechCorp'), ('Orphan Product',None)]"
    ),
    expected_output="[('Laptop', 'TechCorp'), ('Mouse', 'TechCorp'), ('Orphan Product', None)]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE suppliers (sup_id INTEGER PRIMARY KEY, sup_name TEXT);",
        "INSERT INTO suppliers VALUES (1, 'TechCorp'), (2, 'OfficeDepot'), (3, 'EmptySupplier');",
        "CREATE TABLE products (prod_id INTEGER PRIMARY KEY, name TEXT, sup_id INTEGER);",
        "INSERT INTO products VALUES (1, 'Laptop', 1), (2, 'Mouse', 1), (3, 'Orphan Product', 99);",
        "SELECT p.name, s.sup_name FROM products p LEFT JOIN suppliers s ON p.sup_id = s.sup_id ORDER BY p.name;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "📊  FULL OUTER JOIN – Soldiers + Regiments\n\n"
        "SQLite has no FULL OUTER JOIN. Simulate it with\n"
        "UNION ALL of two LEFT JOINs.\n"
        "The `regiments` and `soldiers` tables have:\n"
        "  • Soldiers with valid regiments\n"
        "  • One soldier with NULL regiment (Spy)\n"
        "  • One regiment with no soldiers (Blue Shield)\n"
        "Return all soldier‑regiment pairs, including\n"
        "unassigned soldiers AND empty regiments.\n"
        "Use UNION ALL with the second query filtering\n"
        "for NULL right-side keys.\n"
        "Sort by soldier name, then regiment name.\n\n"
        "Expected output:\n[('Ali','Red Guard'), ('Emperor','Imperial Guard'), ('Hasan','Red Guard'), ('Rahim','Red Guard'), ('Spy',None), (None,'Blue Shield')]"
    ),
    setup_sql=(
        "CREATE TABLE regiments (regiment_id INTEGER PRIMARY KEY, regiment_name TEXT NOT NULL);"
        "INSERT INTO regiments VALUES (1, 'Imperial Guard'), (2, 'Red Guard'), (3, 'Blue Shield');"
        "CREATE TABLE soldiers (soldier_id INTEGER PRIMARY KEY, name TEXT NOT NULL, regiment_id INTEGER);"
        "INSERT INTO soldiers VALUES (1, 'Emperor', 1), (2, 'Rahim', 2), (3, 'Ali', 2), (4, 'Hasan', 2), (5, 'Spy', NULL);"
    ),
    expected_output="[('Ali', 'Red Guard'), ('Emperor', 'Imperial Guard'), ('Hasan', 'Red Guard'), ('Rahim', 'Red Guard'), ('Spy', None), (None, 'Blue Shield')]",
    level=Level.MEDIUM,
    hints=[
        "SELECT s.name, r.regiment_name FROM soldiers s LEFT JOIN regiments r ON s.regiment_id = r.regiment_id UNION ALL SELECT s.name, r.regiment_name FROM regiments r LEFT JOIN soldiers s ON r.regiment_id = s.regiment_id WHERE s.soldier_id IS NULL;"
    ]
)

medium2 = Task(
    description=(
        "🧹  FULL OUTER JOIN – Products + Orders\n\n"
        "Create tables: `products` and `orders`.\n"
        "Some products have never been ordered;\n"
        "one order references a deleted product (orphan).\n"
        "Simulate FULL OUTER JOIN to show:\n"
        "  • All products with their orders\n"
        "  • Orphan orders (product_id not in products)\n"
        "Return product name, order_id, and quantity.\n"
        "Sort by product name, then order_id.\n\n"
        "Expected output:\n[('Desk',None,None), ('Keyboard',3,1), ('Laptop',1,2), ('Mouse',2,5), (None,4,3)]"
    ),
    expected_output="[('Desk', None, None), ('Keyboard', 3, 1), ('Laptop', 1, 2), ('Mouse', 2, 5), (None, 4, 3)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE products (prod_id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO products VALUES (1,'Laptop'), (2,'Mouse'), (3,'Keyboard'), (4,'Desk');",
        "CREATE TABLE orders (order_id INTEGER PRIMARY KEY, prod_id INTEGER, qty INTEGER);",
        "INSERT INTO orders VALUES (1,1,2), (2,2,5), (3,3,1), (4,99,3);",
        "SELECT p.name, o.order_id, o.qty FROM products p LEFT JOIN orders o ON p.prod_id = o.prod_id UNION ALL SELECT p.name, o.order_id, o.qty FROM orders o LEFT JOIN products p ON o.prod_id = p.prod_id WHERE p.prod_id IS NULL ORDER BY p.name, o.order_id;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  Complex FULL OUTER JOIN – Multi‑Table Simulation\n\n"
        "Three tables exist: `customers`, `orders`, and `shipments`.\n"
        "Some orders have no shipments; some customers have no orders.\n"
        "Simulate a full outer join between customers, orders,\n"
        "and shipments to produce a complete report.\n"
        "Return customer name, order_id, and shipment status.\n"
        "Include customers without orders and orders without shipments.\n"
        "Use a combination of LEFT JOINs and UNION ALL.\n"
        "Sort by customer name, then order_id.\n\n"
        "Expected output:\n[('Ali',4,'delivered'), ('Emperor',1,'in transit'), ('Emperor',3,None), ('Karim',None,None), ('Rahim',2,'delayed')]"
    ),
    setup_sql=(
        "CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT);"
        "INSERT INTO customers VALUES (1,'Emperor'), (2,'Rahim'), (3,'Ali'), (4,'Karim');"
        "CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER, product TEXT);"
        "INSERT INTO orders VALUES (1,1,'Laptop'), (2,2,'Mouse'), (3,1,'Keyboard'), (4,3,'Monitor');"
        "CREATE TABLE shipments (id INTEGER PRIMARY KEY, order_id INTEGER, status TEXT);"
        "INSERT INTO shipments VALUES (1,1,'in transit'), (2,2,'delayed'), (3,4,'delivered');"
    ),
    expected_output="[('Ali', 4, 'delivered'), ('Emperor', 1, 'in transit'), ('Emperor', 3, None), ('Karim', None, None), ('Rahim', 2, 'delayed')]",
    level=Level.HARD,
    hints=[
        "SELECT c.name, o.id, sh.status FROM customers c LEFT JOIN orders o ON c.id = o.customer_id LEFT JOIN shipments sh ON o.id = sh.order_id WHERE c.id IS NOT NULL UNION ALL SELECT NULL, o.id, sh.status FROM orders o LEFT JOIN shipments sh ON o.id = sh.order_id WHERE o.id NOT IN (SELECT order_id FROM shipments WHERE order_id IS NOT NULL) AND o.id IS NOT NULL ORDER BY 1, 2;"
    ]
)

hard2 = Task(
    description=(
        "📊  Full Audit Report – Complete Data Merge\n\n"
        "Create two tables: `employees` and `projects` with a\n"
        "join table `assignments`. Some employees are unassigned;\n"
        "some projects have no one assigned.\n"
        "Simulate a FULL OUTER JOIN to produce a complete\n"
        "staffing report.\n"
        "Return employee name, project name, and hours.\n"
        "Include all employees and all projects.\n"
        "Sort by employee name, then project name.\n\n"
        "Expected output:\n[('Ali','Project X',40), ('Emperor','Project Alpha',20), ('Emperor','Project Beta',15), ('Fatima',None,None), ('Rahim','Project Alpha',30), (None,'Project Gamma',None)]"
    ),
    expected_output="[('Ali', 'Project X', 40), ('Emperor', 'Project Alpha', 20), ('Emperor', 'Project Beta', 15), ('Fatima', None, None), ('Rahim', 'Project Alpha', 30), (None, 'Project Gamma', None)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO employees VALUES (1,'Emperor'), (2,'Rahim'), (3,'Ali'), (4,'Fatima');",
        "CREATE TABLE projects (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO projects VALUES (1,'Project Alpha'), (2,'Project Beta'), (3,'Project Gamma'), (4,'Project X');",
        "CREATE TABLE assignments (emp_id INTEGER, proj_id INTEGER, hours INTEGER, PRIMARY KEY(emp_id, proj_id));",
        "INSERT INTO assignments VALUES (1,1,20), (1,2,15), (2,1,30), (3,4,40);",
        "SELECT e.name, p.name, a.hours FROM employees e LEFT JOIN assignments a ON e.id = a.emp_id LEFT JOIN projects p ON a.proj_id = p.id UNION ALL SELECT NULL, p.name, NULL FROM projects p WHERE p.id NOT IN (SELECT proj_id FROM assignments) ORDER BY 1, 2;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L34.json",
        module_name="Module_04_Joins_Relationships",
        lesson_name="L34_Simulating_RIGHT_FULL_JOIN"
    )
