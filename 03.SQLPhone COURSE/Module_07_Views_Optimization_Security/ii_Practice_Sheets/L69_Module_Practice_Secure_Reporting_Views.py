import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🛡️  Secure View – Hide Salary\n\n"
        "The `employees` table contains name, department,\n"
        "salary, and email.\n"
        "Create a view named `v_public_employees` that shows\n"
        "only name, department, and email — NO salary.\n"
        "Then SELECT all columns from the view, sorted by name.\n\n"
        "Expected output:\n[('Ali','Sales','ali@empire.com'), ('Emperor','Engineering','emperor@empire.com'), ('Hasan','Engineering','hasan@empire.com'), ('Rahim','Sales','rahim@empire.com')]"
    ),
    setup_sql=(
        "CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, department TEXT, salary REAL, email TEXT);"
        "INSERT INTO employees VALUES (1,'Emperor','Engineering',5000,'emperor@empire.com'), (2,'Rahim','Sales',4000,'rahim@empire.com'), (3,'Ali','Sales',3500,'ali@empire.com'), (4,'Hasan','Engineering',3000,'hasan@empire.com');"
    ),
    expected_output="[('Ali', 'Sales', 'ali@empire.com'), ('Emperor', 'Engineering', 'emperor@empire.com'), ('Hasan', 'Engineering', 'hasan@empire.com'), ('Rahim', 'Sales', 'rahim@empire.com')]",
    level=Level.EASY,
    hints=[
        "CREATE VIEW v_public_employees AS SELECT name, department, email FROM employees;",
        "SELECT * FROM v_public_employees ORDER BY name;"
    ]
)

easy2 = Task(
    description=(
        "📊  Aggregate View – Department Summary\n\n"
        "The `employees` table exists.\n"
        "Create a view named `v_dept_summary` that shows:\n"
        "  • department\n"
        "  • headcount (COUNT)\n"
        "  • avg_salary (ROUND to 0 decimals)\n"
        "Then SELECT from the view, sorted by department.\n\n"
        "Expected output:\n[('Engineering',2,4000.0), ('Sales',2,3750.0)]"
    ),
    setup_sql=(
        "CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, department TEXT, salary REAL, email TEXT);"
        "INSERT INTO employees VALUES (1,'Emperor','Engineering',5000,'emperor@empire.com'), (2,'Rahim','Sales',4000,'rahim@empire.com'), (3,'Ali','Sales',3500,'ali@empire.com'), (4,'Hasan','Engineering',3000,'hasan@empire.com');"
    ),
    expected_output="[('Engineering', 2, 4000.0), ('Sales', 2, 3750.0)]",
    level=Level.EASY,
    hints=[
        "CREATE VIEW v_dept_summary AS SELECT department, COUNT(*) AS headcount, ROUND(AVG(salary), 0) AS avg_salary FROM employees GROUP BY department;",
        "SELECT * FROM v_dept_summary ORDER BY department;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🔗  View with JOIN – Soldier Regiments\n\n"
        "Create `regiments` and `soldiers` tables.\n"
        "Create a view `v_soldier_regiment` that JOINs them\n"
        "showing soldier name, regiment name, and soldier rank.\n"
        "Then SELECT from the view where regiment name is\n"
        "'Red Guard', sorted by soldier name.\n\n"
        "Expected output:\n[('Ali','Red Guard','General'), ('Rahim','Red Guard','Colonel')]"
    ),
    expected_output="[('Ali', 'Red Guard', 'General'), ('Rahim', 'Red Guard', 'Colonel')]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, regiment_name TEXT);",
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard');",
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER, rank TEXT);",
        "INSERT INTO soldiers VALUES (1,'Emperor',1,'General'), (2,'Rahim',2,'Colonel'), (3,'Ali',2,'General');",
        "CREATE VIEW v_soldier_regiment AS SELECT s.name, r.regiment_name, s.rank FROM soldiers s JOIN regiments r ON s.regiment_id = r.id;",
        "SELECT * FROM v_soldier_regiment WHERE regiment_name = 'Red Guard' ORDER BY name;"
    ]
)

medium2 = Task(
    description=(
        "⚡  Index for View Performance\n\n"
        "Create a table `shipments` with columns:\n"
        "  id, tracking_code, status, ship_date, weight.\n"
        "Insert 8 rows. Create a view `v_pending` that shows\n"
        "only shipments with status = 'pending'.\n"
        "Create an index on `status` to speed up the view.\n"
        "Then EXPLAIN QUERY PLAN on selecting from the view.\n"
        "The output should show SEARCH using the index.\n\n"
        "Expected output:\n[('SEARCH TABLE shipments USING INDEX idx_shipments_status',)]"
    ),
    expected_output="[('SEARCH TABLE shipments USING INDEX idx_shipments_status',)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE shipments (id INTEGER, tracking_code TEXT, status TEXT, ship_date TEXT, weight REAL);",
        "INSERT INTO shipments VALUES (1,'TRK1','pending','2026-07-01',12.5), (2,'TRK2','delivered','2026-07-02',8.0), (3,'TRK3','pending','2026-07-03',5.2), (4,'TRK4','in transit','2026-07-04',10.0), (5,'TRK5','pending','2026-07-05',7.3), (6,'TRK6','delivered','2026-07-06',9.1), (7,'TRK7','in transit','2026-07-07',11.0), (8,'TRK8','pending','2026-07-08',6.8);",
        "CREATE VIEW v_pending AS SELECT * FROM shipments WHERE status = 'pending';",
        "CREATE INDEX idx_shipments_status ON shipments(status);",
        "EXPLAIN QUERY PLAN SELECT * FROM v_pending;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  Role‑Based Views – Junior vs Senior\n\n"
        "Create an `employees` table with columns:\n"
        "  id, name, department, salary, email, performance_score.\n"
        "Create TWO views:\n"
        "  1. `v_junior_report` – shows only name, department,\n"
        "     email (hides salary and performance_score)\n"
        "  2. `v_senior_report` – shows ALL columns\n\n"
        "Then SELECT from both views. Return the number of\n"
        "columns in each view using a query on sqlite_master\n"
        "or pragma (simplified: just show both views exist by\n"
        "selecting their names from sqlite_master).\n\n"
        "Expected output:\n[('v_junior_report',), ('v_senior_report',)]"
    ),
    expected_output="[('v_junior_report',), ('v_senior_report',)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, department TEXT, salary REAL, email TEXT, performance_score INTEGER);",
        "INSERT INTO employees VALUES (1,'Emperor','Engineering',5000,'emperor@empire.com',9);",
        "CREATE VIEW v_junior_report AS SELECT name, department, email FROM employees;",
        "CREATE VIEW v_senior_report AS SELECT * FROM employees;",
        "SELECT name FROM sqlite_master WHERE type='view' ORDER BY name;"
    ]
)

hard2 = Task(
    description=(
        "🔐  Parameterized Access Control – Safe Querying\n\n"
        "The `v_senior_report` view shows all employee data.\n"
        "Write a parameterized SELECT query against this view\n"
        "that:\n"
        "  • Filters by department using a ? placeholder\n"
        "  • Filters by minimum performance_score using a ?\n"
        "Return name, salary, performance_score, sorted by\n"
        "performance_score descending.\n\n"
        "Expected output:\n[(1,'Emperor','Engineering',5000,9)]"
    ),
    setup_sql=(
        "CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, department TEXT, salary REAL, email TEXT, performance_score INTEGER);"
        "INSERT INTO employees VALUES (1,'Emperor','Engineering',5000,'emperor@empire.com',9), (2,'Rahim','Sales',4000,'rahim@empire.com',7), (3,'Ali','Sales',3500,'ali@empire.com',6), (4,'Hasan','Engineering',3000,'hasan@empire.com',8);"
        "CREATE VIEW v_senior_report AS SELECT * FROM employees;"
    ),
    expected_output="[(1, 'Emperor', 'Engineering', 5000.0, 9)]",
    level=Level.HARD,
    hints=[
        "SELECT * FROM v_senior_report WHERE department = ? AND performance_score >= ? ORDER BY performance_score DESC;",
        "-- Engine supplies: 'Engineering', 8"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L69.json",
        module_name="Module_07_Views_Optimization_Security",
        lesson_name="L69_Module_Practice_Secure_Reporting"
    )
