import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "📝  Single‑Line Comment\n\n"
        "Create a table `supplies` with columns\n"
        "  • id INTEGER\n"
        "  • item TEXT\n\n"
        "Include a single‑line comment (--)\n"
        "explaining what the table stores.\n"
        "Then insert one row (1, 'Rations')\n"
        "and SELECT all rows.\n\n"
        "Expected output: [(1, 'Rations')]"
    ),
    expected_output="[(1, 'Rations')]",
    level=Level.EASY,
    hints=[
        "-- Imperial supply depot table",
        "CREATE TABLE supplies (id INTEGER, item TEXT);",
        "INSERT INTO supplies VALUES (1, 'Rations');",
        "SELECT * FROM supplies;"
    ]
)

easy2 = Task(
    description=(
        "💬  Inline Comment\n\n"
        "The `supplies` table already has one row.\n"
        "Insert a second row with a different item,\n"
        "and add an inline comment explaining\n"
        "why this item is being added.\n"
        "Then SELECT all rows.\n\n"
        "Expected output: [(1, 'Rations'), (2, 'Medicine')]"
    ),
    setup_sql=(
        "CREATE TABLE supplies (id INTEGER, item TEXT);"
        "INSERT INTO supplies VALUES (1, 'Rations');"
    ),
    expected_output="[(1, 'Rations'), (2, 'Medicine')]",
    level=Level.EASY,
    hints=[
        "INSERT INTO supplies VALUES (2, 'Medicine'); -- medical supplies for field hospital",
        "SELECT * FROM supplies;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "📄  Block Comment Header\n\n"
        "Create a table `garrison` with columns\n"
        "  • id INTEGER, name TEXT, location TEXT.\n"
        "Include a multi‑line block comment (/* */)\n"
        "above the CREATE TABLE statement that\n"
        "describes the table's purpose and author.\n"
        "Insert two rows:\n"
        "  (1, 'Fort Dhaka', 'North')\n"
        "  (2, 'Fort Chittagong', 'South')\n"
        "SELECT all rows sorted by id.\n\n"
        "Expected output:\n[(1, 'Fort Dhaka', 'North'), (2, 'Fort Chittagong', 'South')]"
    ),
    expected_output="[(1, 'Fort Dhaka', 'North'), (2, 'Fort Chittagong', 'South')]",
    level=Level.MEDIUM,
    hints=[
        "/*",
        "  Table: garrison",
        "  Purpose: track imperial forts",
        "  Author: Emperor",
        "*/",
        "CREATE TABLE garrison (id INTEGER, name TEXT, location TEXT);",
        "INSERT INTO garrison VALUES (1, 'Fort Dhaka', 'North'), (2, 'Fort Chittagong', 'South');",
        "SELECT * FROM garrison ORDER BY id;"
    ]
)

medium2 = Task(
    description=(
        "📐  Professional Formatting – Uppercase Keywords\n\n"
        "Create a table `fleet` with columns\n"
        "  id INTEGER, ship_name TEXT, crew INTEGER.\n"
        "Write the CREATE TABLE statement with all\n"
        "SQL keywords in UPPERCASE and each clause\n"
        "on its own line.\n"
        "Insert one row: (1, 'Imperial Star', 500).\n"
        "Then SELECT all rows.\n\n"
        "Expected output: [(1, 'Imperial Star', 500)]"
    ),
    expected_output="[(1, 'Imperial Star', 500)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE fleet (",
        "    id INTEGER,",
        "    ship_name TEXT,",
        "    crew INTEGER",
        ");",
        "INSERT INTO fleet VALUES (1, 'Imperial Star', 500);",
        "SELECT * FROM fleet;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "📋  Documented Query – Full Report\n\n"
        "The `soldiers` table exists with 4 rows.\n"
        "Write a SELECT query that:\n"
        "  • Has a block comment header describing the report\n"
        "  • Uses UPPERCASE keywords\n"
        "  • Returns name and rank for active soldiers only\n"
        "  • Sorted by rank (custom order: General=1, Colonel=2, Private=3)\n\n"
        "Expected output:\n[('Emperor','General'), ('Ali','General'), ('Rahim','Colonel'), ('Karim','Private')]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL, status TEXT);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000,'active'), (2,'Rahim','Colonel',4000,'active'), (3,'Karim','Private',2000,'reserve'), (4,'Ali','General',4500,'active');"
    ),
    expected_output="[('Emperor', 'General'), ('Ali', 'General'), ('Rahim', 'Colonel'), ('Karim', 'Private')]",
    level=Level.HARD,
    hints=[
        "/*",
        "  Report: Active Duty Roster",
        "  Sorted by rank priority",
        "*/",
        "SELECT name, rank",
        "FROM soldiers",
        "WHERE status = 'active'",
        "ORDER BY CASE rank",
        "    WHEN 'General' THEN 1",
        "    WHEN 'Colonel' THEN 2",
        "    ELSE 3",
        "END;"
    ]
)

hard2 = Task(
    description=(
        "🧹  Formatting Audit – Fix the Mess\n\n"
        "A junior officer wrote this query in a single\n"
        "line with lowercase keywords. Rewrite it with:\n"
        "  • UPPERCASE keywords\n"
        "  • Each clause on a new line\n"
        "  • A single‑line comment explaining the filter\n"
        "The original query is:\n"
        "select name,salary from soldiers where salary>3000 order by salary desc\n\n"
        "Expected output:\n[('Emperor',5000.0), ('Ali',4500.0), ('Rahim',4000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500);"
    ),
    expected_output="[('Emperor', 5000.0), ('Ali', 4500.0), ('Rahim', 4000.0)]",
    level=Level.HARD,
    hints=[
        "-- Show high‑earning soldiers",
        "SELECT name, salary",
        "FROM soldiers",
        "WHERE salary > 3000",
        "ORDER BY salary DESC;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L08.json",
        module_name="Module_01_SQL_Core",
        lesson_name="L08_SQL_Comments_Formatting"
    )
