import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "📇  Create Index – Speed Up Name Search\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Create an index named `idx_soldiers_name`\n"
        "on the `name` column.\n"
        "Then run EXPLAIN QUERY PLAN on a SELECT\n"
        "that filters by name.\n"
        "The output should show SEARCH TABLE USING INDEX\n"
        "instead of SCAN TABLE.\n\n"
        "Expected output:\n[('SEARCH TABLE soldiers USING INDEX idx_soldiers_name',)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[('SEARCH TABLE soldiers USING INDEX idx_soldiers_name',)]",
    level=Level.EASY,
    hints=[
        "CREATE INDEX idx_soldiers_name ON soldiers(name);",
        "EXPLAIN QUERY PLAN SELECT * FROM soldiers WHERE name = 'Emperor';"
    ]
)

easy2 = Task(
    description=(
        "🔍  Index on Foreign Key – Speed Up JOIN\n\n"
        "Create two tables: `regiments` (id PK, name)\n"
        "and `soldiers` (id PK, name, regiment_id).\n"
        "Insert data. Create an index on soldiers.regiment_id.\n"
        "Then EXPLAIN QUERY PLAN a JOIN query.\n"
        "The output should show SEARCH for the indexed column.\n\n"
        "Expected output:\n[('SEARCH TABLE soldiers USING INDEX idx_soldiers_regiment',)]"
    ),
    expected_output="[('SEARCH TABLE soldiers USING INDEX idx_soldiers_regiment',)]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard');",
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER);",
        "INSERT INTO soldiers VALUES (1,'Emperor',1), (2,'Rahim',2), (3,'Ali',2);",
        "CREATE INDEX idx_soldiers_regiment ON soldiers(regiment_id);",
        "EXPLAIN QUERY PLAN SELECT s.name, r.name FROM soldiers s JOIN regiments r ON s.regiment_id = r.id;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🧱  Composite Index – Two Columns\n\n"
        "Create a table `deployments` with columns\n"
        "id, soldier_id, location, status.\n"
        "Insert 6 rows.\n"
        "Create a composite index on (status, location).\n"
        "Then EXPLAIN QUERY PLAN a query that filters\n"
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

medium2 = Task(
    description=(
        "🆔  UNIQUE Index – Prevent Duplicate Emails\n\n"
        "Create a table `users` with columns\n"
        "id INTEGER PRIMARY KEY, username TEXT, email TEXT.\n"
        "Create a UNIQUE index on email.\n"
        "Insert two users with distinct emails.\n"
        "Then try inserting a duplicate email – it should fail.\n"
        "After the error, SELECT all successfully inserted rows.\n\n"
        "Expected output:\n[(1,'Emperor','emperor@empire.com'), (2,'Rahim','rahim@empire.com')]"
    ),
    expected_output="[(1, 'Emperor', 'emperor@empire.com'), (2, 'Rahim', 'rahim@empire.com')]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, email TEXT);",
        "CREATE UNIQUE INDEX idx_users_email ON users(email);",
        "INSERT INTO users VALUES (1,'Emperor','emperor@empire.com'), (2,'Rahim','rahim@empire.com');",
        "-- The next INSERT would fail: INSERT INTO users VALUES (3,'Ali','emperor@empire.com');",
        "SELECT * FROM users ORDER BY id;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  Before & After – SCAN vs SEARCH\n\n"
        "Create a table `inventory` with columns\n"
        "id INTEGER, item TEXT, qty INTEGER.\n"
        "Insert 10 rows.\n"
        "First, run EXPLAIN QUERY PLAN on a filter\n"
        "query BEFORE creating any index – you should\n"
        "see SCAN TABLE.\n"
        "Then CREATE INDEX on `item` and run the same\n"
        "EXPLAIN QUERY PLAN – you should see SEARCH.\n"
        "Return both plan outputs.\n\n"
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
        "id INTEGER, name TEXT, priority INTEGER, status TEXT.\n"
        "Insert 8 rows with varied priorities.\n"
        "First, run EXPLAIN QUERY PLAN on a SELECT\n"
        "with ORDER BY priority BEFORE any index.\n"
        "Then CREATE INDEX on priority and run the\n"
        "same EXPLAIN QUERY PLAN again.\n"
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
        progress_name=".progress_L57.json",
        module_name="Module_06_Modifying_Data_Schema",
        lesson_name="L57_CREATE_INDEX"
    )
