import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "📄  Basic CSV Export – All Rows\n\n"
        "The `soldiers` table has 4 rows.\n"
        "Write a SELECT query that returns all columns.\n"
        "The engine will simulate exporting the result\n"
        "to CSV by checking the output format.\n"
        "Return id, name, rank, salary for all soldiers\n"
        "sorted by id.\n\n"
        "Expected output:\n[(1,'Emperor','General',5000.0), (2,'Rahim','Colonel',4000.0), (3,'Ali','General',4500.0), (4,'Hasan','Private',3500.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Ali','General',4500), (4,'Hasan','Private',3500);"
    ),
    expected_output="[(1, 'Emperor', 'General', 5000.0), (2, 'Rahim', 'Colonel', 4000.0), (3, 'Ali', 'General', 4500.0), (4, 'Hasan', 'Private', 3500.0)]",
    level=Level.EASY,
    hints=[
        "SELECT * FROM soldiers ORDER BY id;"
    ]
)

easy2 = Task(
    description=(
        "📋  Filtered CSV Export – Active Soldiers Only\n\n"
        "The `soldiers` table has 4 rows with a `status` column.\n"
        "Write a SELECT that returns only the name and rank\n"
        "of soldiers whose status is 'active', sorted by name.\n"
        "This simulates exporting a filtered list to CSV.\n\n"
        "Expected output:\n[('Ali','General'), ('Emperor','General'), ('Hasan','Colonel')]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, status TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General','active',5000), (2,'Rahim','Colonel','reserve',4000), (3,'Ali','General','active',4500), (4,'Hasan','Colonel','active',3500);"
    ),
    expected_output="[('Ali', 'General'), ('Emperor', 'General'), ('Hasan', 'Colonel')]",
    level=Level.EASY,
    hints=[
        "SELECT name, rank FROM soldiers WHERE status = 'active' ORDER BY name;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "📊  Export with Aliases – Friendly Column Names\n\n"
        "The `soldiers` table has 4 rows.\n"
        "Write a SELECT that renames the output columns:\n"
        "  • name → Soldier\n"
        "  • rank → Position\n"
        "  • salary → Monthly_Pay\n"
        "This simulates preparing a CSV with human‑readable headers.\n"
        "Sort by Soldier.\n\n"
        "Expected output:\n[('Ali','General',4500.0), ('Emperor','General',5000.0), ('Hasan','Private',3500.0), ('Rahim','Colonel',4000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Ali','General',4500), (4,'Hasan','Private',3500);"
    ),
    expected_output="[('Ali', 'General', 4500.0), ('Emperor', 'General', 5000.0), ('Hasan', 'Private', 3500.0), ('Rahim', 'Colonel', 4000.0)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT name AS Soldier, rank AS Position, salary AS Monthly_Pay FROM soldiers ORDER BY Soldier;"
    ]
)

medium2 = Task(
    description=(
        "📅  Date‑Filtered Export – Monthly Report\n\n"
        "Create a table `missions` with columns:\n"
        "  • id INTEGER, name TEXT, mission_date TEXT, status TEXT.\n"
        "Insert 6 missions across different months.\n"
        "Write a SELECT that returns mission name, date, and status\n"
        "for missions that occurred in the current month (July 2026).\n"
        "Use strftime to filter.\n"
        "Sort by mission_date.\n\n"
        "Expected output:\n[('Patrol Alpha','2026-07-05','completed'), ('Recon Beta','2026-07-10','active'), ('Supply Drop','2026-07-15','pending')]"
    ),
    expected_output="[('Patrol Alpha', '2026-07-05', 'completed'), ('Recon Beta', '2026-07-10', 'active'), ('Supply Drop', '2026-07-15', 'pending')]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE missions (id INTEGER, name TEXT, mission_date TEXT, status TEXT);",
        "INSERT INTO missions VALUES (1,'Patrol Alpha','2026-07-05','completed'), (2,'Recon Beta','2026-07-10','active'), (3,'Supply Drop','2026-07-15','pending'), (4,'Guard Duty','2026-06-28','completed'), (5,'Training','2026-08-01','scheduled'), (6,'Raid','2026-07-20','active');",
        "SELECT name, mission_date, status FROM missions WHERE strftime('%Y-%m', mission_date) = '2026-07' ORDER BY mission_date;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  Export Joined Data – Multi‑Table CSV\n\n"
        "Create two tables: `regiments` and `soldiers`.\n"
        "Write a SELECT that JOINs soldiers with regiments\n"
        "and returns: soldier name, regiment name, salary.\n"
        "Include soldiers without a regiment (LEFT JOIN).\n"
        "Use aliases for the columns.\n"
        "Sort by regiment name, then soldier name.\n"
        "This simulates exporting a multi‑table report.\n\n"
        "Expected output:\n[('Hasan','Blue Shield',3500.0), ('Emperor','Imperial Guard',5000.0), ('Ali','Red Guard',4500.0), ('Rahim','Red Guard',4000.0), ('Spy',None,None)]"
    ),
    expected_output="[('Hasan', 'Blue Shield', 3500.0), ('Emperor', 'Imperial Guard', 5000.0), ('Ali', 'Red Guard', 4500.0), ('Rahim', 'Red Guard', 4000.0), ('Spy', None, None)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, regiment_name TEXT);",
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard'), (3,'Blue Shield');",
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER, salary REAL);",
        "INSERT INTO soldiers VALUES (1,'Emperor',1,5000), (2,'Rahim',2,4000), (3,'Ali',2,4500), (4,'Hasan',3,3500), (5,'Spy',NULL,NULL);",
        "SELECT s.name AS Soldier, r.regiment_name AS Regiment, s.salary AS Salary FROM soldiers s LEFT JOIN regiments r ON s.regiment_id = r.id ORDER BY r.regiment_name, s.name;"
    ]
)

hard2 = Task(
    description=(
        "📊  Export with Aggregation – Summary Report\n\n"
        "Create a table `sales` with columns:\n"
        "  • id INTEGER, product TEXT, amount REAL, sale_date TEXT.\n"
        "Insert 8 sales across multiple months and categories.\n"
        "Write a SELECT that groups by month (strftime '%Y-%m')\n"
        "and returns:\n"
        "  • month\n"
        "  • total_amount (SUM of amount)\n"
        "  • avg_amount (ROUND(AVG(amount), 2))\n"
        "  • order_count (COUNT(*))\n"
        "Sort by month.\n"
        "This simulates exporting an aggregated summary.\n\n"
        "Expected output:\n[('2026-01',800.0,400.0,2), ('2026-02',950.0,316.67,3), ('2026-03',1100.0,366.67,3)]"
    ),
    expected_output="[('2026-01', 800.0, 400.0, 2), ('2026-02', 950.0, 316.67, 3), ('2026-03', 1100.0, 366.67, 3)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE sales (id INTEGER, product TEXT, amount REAL, sale_date TEXT);",
        "INSERT INTO sales VALUES (1,'Laptop',500,'2026-01-15'), (2,'Mouse',300,'2026-01-25'), (3,'Desk',400,'2026-02-10'), (4,'Chair',250,'2026-02-20'), (5,'Monitor',300,'2026-02-28'), (6,'Keyboard',150,'2026-03-05'), (7,'Pen',50,'2026-03-15'), (8,'Paper',900,'2026-03-25');",
        "SELECT strftime('%Y-%m', sale_date) AS month, SUM(amount) AS total_amount, ROUND(AVG(amount), 2) AS avg_amount, COUNT(*) AS order_count FROM sales GROUP BY month ORDER BY month;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L67.json",
        module_name="Module_07_Views_Optimization_Security",
        lesson_name="L67_Export_to_CSV"
    )
