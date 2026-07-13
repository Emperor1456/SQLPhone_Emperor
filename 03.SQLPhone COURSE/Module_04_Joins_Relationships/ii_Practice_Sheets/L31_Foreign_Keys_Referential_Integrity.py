import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🔗  Create Related Tables – FK Setup\n\n"
        "Create two tables with a foreign key relationship:\n\n"
        "1. `regiments`:\n"
        "  • regiment_id INTEGER PRIMARY KEY\n"
        "  • regiment_name TEXT NOT NULL\n\n"
        "2. `soldiers`:\n"
        "  • soldier_id INTEGER PRIMARY KEY\n"
        "  • name TEXT NOT NULL\n"
        "  • regiment_id INTEGER\n"
        "  • FOREIGN KEY (regiment_id) REFERENCES regiments(regiment_id)\n\n"
        "Enable foreign keys with PRAGMA foreign_keys = ON.\n"
        "Insert one regiment and one soldier.\n"
        "Then SELECT soldier name with their regiment name.\n\n"
        "Expected output: [('Emperor', 'Imperial Guard')]"
    ),
    expected_output="[('Emperor', 'Imperial Guard')]",
    level=Level.EASY,
    hints=[
        "PRAGMA foreign_keys = ON;",
        "CREATE TABLE regiments (regiment_id INTEGER PRIMARY KEY, regiment_name TEXT NOT NULL);",
        "CREATE TABLE soldiers (soldier_id INTEGER PRIMARY KEY, name TEXT NOT NULL, regiment_id INTEGER, FOREIGN KEY (regiment_id) REFERENCES regiments(regiment_id));",
        "INSERT INTO regiments VALUES (1, 'Imperial Guard');",
        "INSERT INTO soldiers VALUES (1, 'Emperor', 1);",
        "SELECT s.name, r.regiment_name FROM soldiers s JOIN regiments r ON s.regiment_id = r.regiment_id;"
    ]
)

easy2 = Task(
    description=(
        "⚠️  FK Violation – Try Invalid Reference\n\n"
        "The `regiments` and `soldiers` tables exist.\n"
        "Try to insert a soldier with a regiment_id\n"
        "that does NOT exist (e.g., 99).\n"
        "This should fail with an error.\n\n"
        "After the error, SELECT all soldiers to\n"
        "confirm the invalid row was NOT inserted.\n\n"
        "Expected output: [(1, 'Emperor', 1)]"
    ),
    setup_sql=(
        "PRAGMA foreign_keys = ON;"
        "CREATE TABLE regiments (regiment_id INTEGER PRIMARY KEY, regiment_name TEXT NOT NULL);"
        "INSERT INTO regiments VALUES (1, 'Imperial Guard');"
        "CREATE TABLE soldiers (soldier_id INTEGER PRIMARY KEY, name TEXT NOT NULL, regiment_id INTEGER, FOREIGN KEY (regiment_id) REFERENCES regiments(regiment_id));"
        "INSERT INTO soldiers VALUES (1, 'Emperor', 1);"
    ),
    expected_output="[(1, 'Emperor', 1)]",
    level=Level.EASY,
    hints=[
        "The invalid INSERT will be rejected by the FK constraint.",
        "INSERT INTO soldiers VALUES (2, 'Spy', 99); -- this fails",
        "SELECT * FROM soldiers; -- shows only the valid row"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🛡️  ON DELETE CASCADE – Auto‑Remove\n\n"
        "Create two tables:\n"
        "  1. `departments` (dept_id PK, name)\n"
        "  2. `employees` (emp_id PK, name, dept_id FK\n"
        "     REFERENCES departments ON DELETE CASCADE)\n\n"
        "Insert 2 departments and 4 employees.\n"
        "Then DELETE a department and verify that\n"
        "all its employees are automatically removed.\n"
        "SELECT the remaining employees.\n\n"
        "Expected output:\n[(3, 'Ali', 2), (4, 'Fatima', 2)]"
    ),
    expected_output="[(3, 'Ali', 2), (4, 'Fatima', 2)]",
    level=Level.MEDIUM,
    hints=[
        "PRAGMA foreign_keys = ON;",
        "CREATE TABLE departments (dept_id INTEGER PRIMARY KEY, name TEXT NOT NULL);",
        "INSERT INTO departments VALUES (1, 'Engineering'), (2, 'Sales');",
        "CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT NOT NULL, dept_id INTEGER, FOREIGN KEY (dept_id) REFERENCES departments(dept_id) ON DELETE CASCADE);",
        "INSERT INTO employees VALUES (1,'Emperor',1), (2,'Rahim',1), (3,'Ali',2), (4,'Fatima',2);",
        "DELETE FROM departments WHERE dept_id = 1;",
        "SELECT * FROM employees;"
    ]
)

medium2 = Task(
    description=(
        "🔍  Find Orphans – LEFT JOIN + IS NULL\n\n"
        "The `regiments` and `soldiers` tables exist.\n"
        "Insert a soldier with a NULL regiment_id\n"
        "(unassigned). Write a query that returns\n"
        "ALL soldiers with their regiment name,\n"
        "including unassigned soldiers.\n"
        "Then write a query that finds ONLY soldiers\n"
        "with no regiment (regiment_id IS NULL).\n\n"
        "Expected output:\n[('Spy', None)]"
    ),
    setup_sql=(
        "PRAGMA foreign_keys = ON;"
        "CREATE TABLE regiments (regiment_id INTEGER PRIMARY KEY, regiment_name TEXT NOT NULL);"
        "INSERT INTO regiments VALUES (1, 'Imperial Guard');"
        "CREATE TABLE soldiers (soldier_id INTEGER PRIMARY KEY, name TEXT NOT NULL, regiment_id INTEGER, FOREIGN KEY (regiment_id) REFERENCES regiments(regiment_id));"
        "INSERT INTO soldiers VALUES (1, 'Emperor', 1), (2, 'Spy', NULL);"
    ),
    expected_output="[('Spy', None)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT s.name, r.regiment_name FROM soldiers s LEFT JOIN regiments r ON s.regiment_id = r.regiment_id;  -- all soldiers",
        "SELECT s.name, r.regiment_name FROM soldiers s LEFT JOIN regiments r ON s.regiment_id = r.regiment_id WHERE s.regiment_id IS NULL;  -- only unassigned"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧱  Composite FK – Order Items\n\n"
        "Create three tables:\n"
        "  1. `orders` (order_id PK, customer TEXT)\n"
        "  2. `products` (product_id PK, name TEXT, price REAL)\n"
        "  3. `order_items` (order_id, product_id,\n"
        "     quantity, PRIMARY KEY(order_id, product_id),\n"
        "     FK(order_id) REFERENCES orders,\n"
        "     FK(product_id) REFERENCES products)\n\n"
        "Insert 2 orders, 3 products, and 4 order items.\n"
        "Then SELECT a summary: order_id, customer,\n"
        "product name, quantity, and line total (qty*price).\n"
        "Sort by order_id, then product name.\n\n"
        "Expected output:\n[(1,'Emperor','Laptop',2,2000.0), (1,'Emperor','Mouse',5,250.0), (2,'Rahim','Desk',1,500.0), (2,'Rahim','Laptop',1,1000.0)]"
    ),
    expected_output="[(1, 'Emperor', 'Laptop', 2, 2000.0), (1, 'Emperor', 'Mouse', 5, 250.0), (2, 'Rahim', 'Desk', 1, 500.0), (2, 'Rahim', 'Laptop', 1, 1000.0)]",
    level=Level.HARD,
    hints=[
        "PRAGMA foreign_keys = ON;",
        "CREATE TABLE orders (order_id INTEGER PRIMARY KEY, customer TEXT NOT NULL);",
        "INSERT INTO orders VALUES (1, 'Emperor'), (2, 'Rahim');",
        "CREATE TABLE products (product_id INTEGER PRIMARY KEY, name TEXT NOT NULL, price REAL NOT NULL);",
        "INSERT INTO products VALUES (1, 'Laptop', 1000.0), (2, 'Mouse', 50.0), (3, 'Desk', 500.0);",
        "CREATE TABLE order_items (order_id INTEGER, product_id INTEGER, quantity INTEGER, PRIMARY KEY(order_id, product_id), FOREIGN KEY(order_id) REFERENCES orders(order_id), FOREIGN KEY(product_id) REFERENCES products(product_id));",
        "INSERT INTO order_items VALUES (1, 1, 2), (1, 2, 5), (2, 3, 1), (2, 1, 1);",
        "SELECT o.order_id, o.customer, p.name, oi.quantity, oi.quantity * p.price AS line_total FROM orders o JOIN order_items oi ON o.order_id = oi.order_id JOIN products p ON oi.product_id = p.product_id ORDER BY o.order_id, p.name;"
    ]
)

hard2 = Task(
    description=(
        "🔗  FK Chain – Regiments → Soldiers → Missions\n\n"
        "Create three tables with cascading foreign keys:\n"
        "  1. `regiments` (regiment_id PK, name)\n"
        "  2. `soldiers` (soldier_id PK, name, regiment_id FK\n"
        "     REFERENCES regiments ON DELETE CASCADE)\n"
        "  3. `missions` (mission_id PK, soldier_id FK\n"
        "     REFERENCES soldiers ON DELETE CASCADE, task TEXT)\n\n"
        "Insert 1 regiment, 2 soldiers, and 3 missions.\n"
        "Then DELETE the regiment and verify that\n"
        "ALL soldiers AND their missions are removed.\n"
        "Show the remaining count from each table\n"
        "(should all be 0).\n\n"
        "Expected output: [(0, 0, 0)]"
    ),
    expected_output="[(0, 0, 0)]",
    level=Level.HARD,
    hints=[
        "PRAGMA foreign_keys = ON;",
        "CREATE TABLE regiments (regiment_id INTEGER PRIMARY KEY, name TEXT NOT NULL);",
        "INSERT INTO regiments VALUES (1, 'Imperial Guard');",
        "CREATE TABLE soldiers (soldier_id INTEGER PRIMARY KEY, name TEXT NOT NULL, regiment_id INTEGER, FOREIGN KEY (regiment_id) REFERENCES regiments(regiment_id) ON DELETE CASCADE);",
        "INSERT INTO soldiers VALUES (1, 'Emperor', 1), (2, 'Rahim', 1);",
        "CREATE TABLE missions (mission_id INTEGER PRIMARY KEY, soldier_id INTEGER, task TEXT, FOREIGN KEY (soldier_id) REFERENCES soldiers(soldier_id) ON DELETE CASCADE);",
        "INSERT INTO missions VALUES (1, 1, 'Patrol'), (2, 1, 'Recon'), (3, 2, 'Guard');",
        "DELETE FROM regiments WHERE regiment_id = 1;",
        "SELECT (SELECT COUNT(*) FROM regiments), (SELECT COUNT(*) FROM soldiers), (SELECT COUNT(*) FROM missions);"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L31.json",
        module_name="Module_04_Joins_Relationships",
        lesson_name="L31_Foreign_Keys"
    )
