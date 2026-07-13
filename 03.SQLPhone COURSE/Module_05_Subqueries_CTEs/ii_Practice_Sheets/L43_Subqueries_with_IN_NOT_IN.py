import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "📋  IN with Subquery – Soldiers in Deployed Regiments\n\n"
        "The `regiments` and `soldiers` tables exist.\n"
        "The `deployments` table lists which regiments have\n"
        "been deployed.\n"
        "Write a query that returns the names of soldiers\n"
        "whose regiment_id appears in the deployments table.\n"
        "Use IN with a subquery.\n"
        "Sort by name.\n\n"
        "Expected output:\n[('Ali',), ('Emperor',), ('Hasan',)]"
    ),
    setup_sql=(
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT);"
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard'), (3,'Blue Shield');"
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER);"
        "INSERT INTO soldiers VALUES (1,'Emperor',1), (2,'Rahim',3), (3,'Ali',1), (4,'Hasan',2);"
        "CREATE TABLE deployments (id INTEGER PRIMARY KEY, regiment_id INTEGER, location TEXT);"
        "INSERT INTO deployments VALUES (1,1,'North'), (2,2,'South');"
    ),
    expected_output="[('Ali',), ('Emperor',), ('Hasan',)]",
    level=Level.EASY,
    hints=[
        "SELECT name FROM soldiers WHERE regiment_id IN (SELECT regiment_id FROM deployments) ORDER BY name;"
    ]
)

easy2 = Task(
    description=(
        "🔍  NOT IN with Subquery – Soldiers Not Deployed\n\n"
        "The same tables exist.\n"
        "Write a query that returns the names of soldiers\n"
        "whose regiment has NEVER been deployed.\n"
        "Use NOT IN with a subquery.\n"
        "Sort by name.\n\n"
        "Expected output: [('Rahim',)]"
    ),
    setup_sql=(
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT);"
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard'), (3,'Blue Shield');"
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER);"
        "INSERT INTO soldiers VALUES (1,'Emperor',1), (2,'Rahim',3), (3,'Ali',1), (4,'Hasan',2);"
        "CREATE TABLE deployments (id INTEGER PRIMARY KEY, regiment_id INTEGER, location TEXT);"
        "INSERT INTO deployments VALUES (1,1,'North'), (2,2,'South');"
    ),
    expected_output="[('Rahim',)]",
    level=Level.EASY,
    hints=[
        "SELECT name FROM soldiers WHERE regiment_id NOT IN (SELECT regiment_id FROM deployments) ORDER BY name;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🧪  IN with Multiple Conditions – Active Generals\n\n"
        "The `soldiers` table has 6 rows with rank and status.\n"
        "Write a query that returns the name and rank of soldiers\n"
        "whose rank is IN the list of ranks held by 'active' soldiers.\n"
        "Use a subquery with IN that first finds ranks of active soldiers.\n"
        "Only show soldiers who are themselves active.\n"
        "Sort by name.\n\n"
        "Expected output:\n[('Ali','General'), ('Emperor','General'), ('Hasan','Colonel')]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, status TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General','active',5000), (2,'Rahim','Colonel','reserve',4000), (3,'Karim','Private','active',2000), (4,'Ali','General','active',4500), (5,'Hasan','Colonel','active',3500), (6,'Fatima','Private','reserve',1800);"
    ),
    expected_output="[('Ali', 'General'), ('Emperor', 'General'), ('Hasan', 'Colonel')]",
    level=Level.MEDIUM,
    hints=[
        "SELECT name, rank FROM soldiers WHERE status = 'active' AND rank IN (SELECT DISTINCT rank FROM soldiers WHERE status = 'active') ORDER BY name;"
    ]
)

medium2 = Task(
    description=(
        "📊  NOT IN – Customers Without Orders\n\n"
        "Create tables `customers` and `orders`.\n"
        "Write a query that returns the names of customers\n"
        "who have never placed an order.\n"
        "Use NOT IN with a subquery.\n"
        "Sort by name.\n\n"
        "Expected output:\n[('Karim',), ('Rana',)]"
    ),
    expected_output="[('Karim',), ('Rana',)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO customers VALUES (1,'Emperor'), (2,'Rahim'), (3,'Karim'), (4,'Ali'), (5,'Rana');",
        "CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER);",
        "INSERT INTO orders VALUES (1,1), (2,2), (3,1), (4,4);",
        "SELECT name FROM customers WHERE id NOT IN (SELECT DISTINCT customer_id FROM orders) ORDER BY name;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "⚠️  NOT IN with NULL – The Trap\n\n"
        "Create a table `missions` with a column `soldier_id` that\n"
        "contains NULL values.\n"
        "Write a query that returns the names of soldiers\n"
        "who are NOT assigned to any mission.\n"
        "First try NOT IN and observe the result (it will be empty).\n"
        "Then write the CORRECT query using NOT EXISTS instead.\n"
        "Return soldier names.\n"
        "Sort by name.\n\n"
        "Expected output (using NOT EXISTS):\n[('Fatima',), ('Hasan',)]"
    ),
    expected_output="[('Fatima',), ('Hasan',)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO soldiers VALUES (1,'Emperor'), (2,'Rahim'), (3,'Ali'), (4,'Hasan'), (5,'Fatima');",
        "CREATE TABLE missions (id INTEGER PRIMARY KEY, soldier_id INTEGER, task TEXT);",
        "INSERT INTO missions VALUES (1,1,'Patrol'), (2,2,'Recon'), (3,3,'Guard'), (4,NULL,'Supply');",
        "SELECT name FROM soldiers s WHERE NOT EXISTS (SELECT 1 FROM missions m WHERE m.soldier_id = s.id) ORDER BY name;"
    ]
)

hard2 = Task(
    description=(
        "🧮  Nested NOT IN – Multi‑Level Exclusion\n\n"
        "Create three tables: `regiments`, `soldiers`, `deployments`.\n"
        "Write a query that returns the names of soldiers whose\n"
        "regiment is NOT IN the list of regiments that have been\n"
        "deployed to the 'North' region.\n"
        "Use nested subqueries: the inner finds regiments deployed\n"
        "to North, the outer uses NOT IN.\n"
        "Sort by name.\n\n"
        "Expected output:\n[('Hasan',), ('Rahim',)]"
    ),
    expected_output="[('Hasan',), ('Rahim',)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard'), (3,'Blue Shield');",
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER);",
        "INSERT INTO soldiers VALUES (1,'Emperor',1), (2,'Rahim',3), (3,'Ali',1), (4,'Hasan',2);",
        "CREATE TABLE deployments (id INTEGER PRIMARY KEY, regiment_id INTEGER, location TEXT);",
        "INSERT INTO deployments VALUES (1,1,'North'), (2,2,'South'), (3,1,'East');",
        "SELECT name FROM soldiers WHERE regiment_id NOT IN (SELECT regiment_id FROM deployments WHERE location = 'North') ORDER BY name;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L43.json",
        module_name="Module_05_Subqueries_CTEs",
        lesson_name="L43_Subqueries_IN_NOT_IN"
    )
