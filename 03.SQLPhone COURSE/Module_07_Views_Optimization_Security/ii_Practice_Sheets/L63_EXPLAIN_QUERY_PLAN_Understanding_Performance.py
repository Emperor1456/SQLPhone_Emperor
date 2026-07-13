import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🔍  EXPLAIN QUERY PLAN – Simple Scan\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Run EXPLAIN QUERY PLAN on a SELECT that filters\n"
        "by name without an index.\n"
        "You should see 'SCAN TABLE soldiers'.\n\n"
        "Expected output:\n[('SCAN TABLE soldiers',)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[('SCAN TABLE soldiers',)]",
    level=Level.EASY,
    hints=[
        "EXPLAIN QUERY PLAN SELECT * FROM soldiers WHERE name = 'Emperor';"
    ]
)

easy2 = Task(
    description=(
        "📇  EXPLAIN with Index – See SEARCH\n\n"
        "Create the same `soldiers` table, then create\n"
        "an index on the `name` column.\n"
        "Run EXPLAIN QUERY PLAN on the same SELECT.\n"
        "Now you should see 'SEARCH TABLE soldiers USING\n"
        "INDEX idx_soldiers_name'.\n\n"
        "Expected output:\n[('SEARCH TABLE soldiers USING INDEX idx_soldiers_name',)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
        "CREATE INDEX idx_soldiers_name ON soldiers(name);"
    ),
    expected_output="[('SEARCH TABLE soldiers USING INDEX idx_soldiers_name',)]",
    level=Level.EASY,
    hints=[
        "EXPLAIN QUERY PLAN SELECT * FROM soldiers WHERE name = 'Emperor';"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🔗  EXPLAIN a JOIN – Two Tables\n\n"
        "Create `regiments` and `soldiers` tables with\n"
        "a foreign key relationship. Insert 2 regiments,\n"
        "4 soldiers. Create an index on soldiers.regiment_id.\n"
        "Run EXPLAIN QUERY PLAN on a JOIN query.\n"
        "The output should show SEARCH for the indexed\n"
        "column and SCAN or SEARCH for regiments.\n\n"
        "Expected output:\n[('SCAN TABLE regiments',), ('SEARCH TABLE soldiers USING INDEX idx_soldiers_regiment',)]"
    ),
    expected_output="[('SCAN TABLE regiments',), ('SEARCH TABLE soldiers USING INDEX idx_soldiers_regiment',)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard');",
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER);",
        "INSERT INTO soldiers VALUES (1,'Emperor',1), (2,'Rahim',2), (3,'Ali',2), (4,'Hasan',2);",
        "CREATE INDEX idx_soldiers_regiment ON soldiers(regiment_id);",
        "EXPLAIN QUERY PLAN SELECT s.name, r.name FROM soldiers s JOIN regiments r ON s.regiment_id = r.id;"
    ]
)

medium2 = Task(
    description=(
        "📊  Composite Index EXPLAIN – Two Columns\n\n"
        "Create a table `deployments` with columns\n"
        "id, soldier_id, location, status.\n"
        "Insert 6 rows.\n"
        "Create a composite index on (status, location).\n"
        "Run EXPLAIN QUERY PLAN on a query that filters\n"
        "on both columns.\n"
        "The output should show SEARCH using the composite index.\n\n"
        "Expected output:\n[('SEARCH TABLE deployments USING INDEX idx_deployments_status_location',)]"
    ),
    expected_output="[('SEARCH TABLE deployments USING INDEX idx_deployments_status_location',)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE deployments (id INTEGER, soldier_id INTEGER, location TEXT, status TEXT);",
        "INSERT INTO deployments VALUES (1,1,'North','active'), (2,2,'South','active'), (3,3,'North','completed'), (4,4,'South','completed'), (5,5,'North','active'), (6,6,'East','pending');",
        "CREATE INDEX idx_deployments_status_location ON deployments(status, location);",
        "EXPLAIN QUERY PLAN SELECT * FROM deployments WHERE status = 'active' AND location = 'North';"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  Before and After – Compare Plans\n\n"
        "Create a table `inventory` with columns\n"
        "id, item, qty. Insert 10 rows.\n"
        "Run EXPLAIN QUERY PLAN BEFORE creating an index\n"
        "on a filter query – you should see SCAN.\n"
        "Then CREATE INDEX on `item` and run the same\n"
        "EXPLAIN QUERY PLAN – you should see SEARCH.\n"
        "Return both plan outputs, the SCAN first, then\n"
        "the SEARCH.\n\n"
        "Expected output:\n[('SCAN TABLE inventory',), ('SEARCH TABLE inventory USING INDEX idx_inventory_item',)]"
    ),
    expected_output="[('SCAN TABLE inventory',), ('SEARCH TABLE inventory USING INDEX idx_inventory_item',)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE inventory (id INTEGER, item TEXT, qty INTEGER);",
        "INSERT INTO inventory VALUES (1,'Sword',10), (2,'Shield',5), (3,'Bow',8), (4,'Axe',12), (5,'Spear',7), (6,'Helm',3), (7,'Armor',2), (8,'Boots',15), (9,'Gloves',20), (10,'Ring',1);",
        "EXPLAIN QUERY PLAN SELECT * FROM inventory WHERE item = 'Sword';",
        "CREATE INDEX idx_inventory_item ON inventory(item);",
        "EXPLAIN QUERY PLAN SELECT * FROM inventory WHERE item = 'Sword';"
    ]
)

hard2 = Task(
    description=(
        "📊  Index on ORDER BY – Avoid Sort Step\n\n"
        "Create a table `missions` with columns\n"
        "id, name, priority INTEGER, status TEXT.\n"
        "Insert 8 rows with varied priorities.\n"
        "First, run EXPLAIN QUERY PLAN on a SELECT\n"
        "with ORDER BY priority BEFORE any index.\n"
        "Then CREATE INDEX on priority and run the same\n"
        "EXPLAIN QUERY PLAN again.\n"
        "Return both plan outputs.\n\n"
        "Expected output:\n[('SCAN TABLE missions',), ('SCAN TABLE missions USING INDEX idx_missions_priority',)]"
    ),
    expected_output="[('SCAN TABLE missions',), ('SCAN TABLE missions USING INDEX idx_missions_priority',)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE missions (id INTEGER, name TEXT, priority INTEGER, status TEXT);",
        "INSERT INTO missions VALUES (1,'Patrol',3,'active'), (2,'Recon',1,'active'), (3,'Supply',2,'completed'), (4,'Guard',4,'active'), (5,'Raid',1,'pending'), (6,'Train',5,'completed'), (7,'Escort',2,'active'), (8,'Scout',3,'pending');",
        "EXPLAIN QUERY PLAN SELECT * FROM missions ORDER BY priority;",
        "CREATE INDEX idx_missions_priority ON missions(priority);",
        "EXPLAIN QUERY PLAN SELECT * FROM missions ORDER BY priority;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L63.json",
        module_name="Module_07_Views_Optimization_Security",
        lesson_name="L63_EXPLAIN_QUERY_PLAN"
    )
