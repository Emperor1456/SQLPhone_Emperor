import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "👁️  Create a Simple View – Active Soldiers\n\n"
        "The `soldiers` table has 5 rows with a `status` column.\n"
        "Create a view named `v_active_soldiers` that selects\n"
        "only soldiers whose status is 'active'.\n"
        "Then SELECT all columns from the view.\n"
        "Sort by name.\n\n"
        "Expected output:\n[('Ali', 'General', 'active'), ('Emperor', 'General', 'active'), ('Hasan', 'Colonel', 'active')]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, status TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General','active',5000), (2,'Rahim','Colonel','reserve',4000), (3,'Ali','General','active',4500), (4,'Hasan','Colonel','active',3500), (5,'Karim','Private','reserve',2000);"
    ),
    expected_output="[('Ali', 'General', 'active'), ('Emperor', 'General', 'active'), ('Hasan', 'Colonel', 'active')]",
    level=Level.EASY,
    hints=[
        "CREATE VIEW v_active_soldiers AS SELECT name, rank, status FROM soldiers WHERE status = 'active';",
        "SELECT * FROM v_active_soldiers ORDER BY name;"
    ]
)

easy2 = Task(
    description=(
        "🔍  Query a View – Count Active Soldiers\n\n"
        "The `v_active_soldiers` view already exists.\n"
        "Write a query that returns the total number\n"
        "of rows in that view.\n\n"
        "Expected output: [(3,)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, status TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General','active',5000), (2,'Rahim','Colonel','reserve',4000), (3,'Ali','General','active',4500), (4,'Hasan','Colonel','active',3500), (5,'Karim','Private','reserve',2000);"
        "CREATE VIEW v_active_soldiers AS SELECT name, rank, status FROM soldiers WHERE status = 'active';"
    ),
    expected_output="[(3,)]",
    level=Level.EASY,
    hints=[
        "SELECT COUNT(*) FROM v_active_soldiers;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "📊  View with JOIN – Soldier Regiments\n\n"
        "Create two tables: `regiments` and `soldiers`.\n"
        "Create a view named `v_soldier_regiment` that JOINs\n"
        "soldiers with regiments and shows:\n"
        "  • soldier name\n"
        "  • regiment name\n"
        "  • salary\n"
        "Then SELECT from the view where salary > 3000,\n"
        "sorted by salary descending.\n\n"
        "Expected output:\n[('Emperor','Imperial Guard',5000.0), ('Ali','Red Guard',4500.0), ('Rahim','Red Guard',4000.0)]"
    ),
    expected_output="[('Emperor', 'Imperial Guard', 5000.0), ('Ali', 'Red Guard', 4500.0), ('Rahim', 'Red Guard', 4000.0)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, regiment_name TEXT);",
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard');",
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER, salary REAL);",
        "INSERT INTO soldiers VALUES (1,'Emperor',1,5000), (2,'Rahim',2,4000), (3,'Ali',2,4500), (4,'Hasan',2,3500);",
        "CREATE VIEW v_soldier_regiment AS SELECT s.name, r.regiment_name, s.salary FROM soldiers s JOIN regiments r ON s.regiment_id = r.id;",
        "SELECT * FROM v_soldier_regiment WHERE salary > 3000 ORDER BY salary DESC;"
    ]
)

medium2 = Task(
    description=(
        "🔄  Replace a View – DROP & CREATE\n\n"
        "The `v_active_soldiers` view already exists.\n"
        "Modify it to also include the `salary` column.\n"
        "Drop the old view and create a new one with\n"
        "the additional column.\n"
        "Then SELECT from the new view, sorted by name.\n\n"
        "Expected output:\n[('Ali','General','active',4500.0), ('Emperor','General','active',5000.0), ('Hasan','Colonel','active',3500.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, status TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General','active',5000), (2,'Rahim','Colonel','reserve',4000), (3,'Ali','General','active',4500), (4,'Hasan','Colonel','active',3500), (5,'Karim','Private','reserve',2000);"
        "CREATE VIEW v_active_soldiers AS SELECT name, rank, status FROM soldiers WHERE status = 'active';"
    ),
    expected_output="[('Ali', 'General', 'active', 4500.0), ('Emperor', 'General', 'active', 5000.0), ('Hasan', 'Colonel', 'active', 3500.0)]",
    level=Level.MEDIUM,
    hints=[
        "DROP VIEW IF EXISTS v_active_soldiers;",
        "CREATE VIEW v_active_soldiers AS SELECT name, rank, status, salary FROM soldiers WHERE status = 'active';",
        "SELECT * FROM v_active_soldiers ORDER BY name;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🛡️  Security View – Hide Salaries\n\n"
        "Create a view named `v_public_soldiers` that shows\n"
        "soldier name, rank, and regiment name (by JOINing\n"
        "with regiments), but does NOT expose salary.\n"
        "Then SELECT from the view, sorted by name.\n\n"
        "Expected output:\n[('Ali','General','Red Guard'), ('Emperor','General','Imperial Guard'), ('Hasan','Colonel','Red Guard'), ('Rahim','Colonel','Red Guard')]"
    ),
    expected_output="[('Ali', 'General', 'Red Guard'), ('Emperor', 'General', 'Imperial Guard'), ('Hasan', 'Colonel', 'Red Guard'), ('Rahim', 'Colonel', 'Red Guard')]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, regiment_name TEXT);",
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard');",
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, regiment_id INTEGER, salary REAL);",
        "INSERT INTO soldiers VALUES (1,'Emperor','General',1,5000), (2,'Rahim','Colonel',2,4000), (3,'Ali','General',2,4500), (4,'Hasan','Colonel',2,3500);",
        "CREATE VIEW v_public_soldiers AS SELECT s.name, s.rank, r.regiment_name FROM soldiers s JOIN regiments r ON s.regiment_id = r.id;",
        "SELECT * FROM v_public_soldiers ORDER BY name;"
    ]
)

hard2 = Task(
    description=(
        "📊  Aggregate View – Regimental Strength\n\n"
        "Create a view named `v_regiment_summary` that shows:\n"
        "  • regiment_name\n"
        "  • soldier_count (COUNT of soldiers)\n"
        "  • avg_salary (AVG of salary, rounded to 2 decimals)\n"
        "Use JOIN and GROUP BY. Include regiments with zero\n"
        "soldiers (LEFT JOIN).\n"
        "Then SELECT from the view, sorted by soldier_count desc.\n\n"
        "Expected output:\n[('Red Guard',3,4000.0), ('Imperial Guard',1,5000.0), ('Blue Shield',0,None)]"
    ),
    expected_output="[('Red Guard', 3, 4000.0), ('Imperial Guard', 1, 5000.0), ('Blue Shield', 0, None)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, regiment_name TEXT);",
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard'), (3,'Blue Shield');",
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER, salary REAL);",
        "INSERT INTO soldiers VALUES (1,'Emperor',1,5000), (2,'Rahim',2,4000), (3,'Ali',2,4500), (4,'Hasan',2,3500);",
        "CREATE VIEW v_regiment_summary AS SELECT r.regiment_name, COUNT(s.id) AS soldier_count, ROUND(AVG(s.salary), 2) AS avg_salary FROM regiments r LEFT JOIN soldiers s ON r.id = s.regiment_id GROUP BY r.id;",
        "SELECT * FROM v_regiment_summary ORDER BY soldier_count DESC;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L61.json",
        module_name="Module_07_Views_Optimization_Security",
        lesson_name="L61_Views_Create_Query_Drop"
    )
