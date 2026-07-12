import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🏗️  Soldiers Table – Basic Columns\n\n"
        "Create a table `soldiers` with two columns:\n"
        "  • soldier_id INTEGER\n"
        "  • name TEXT\n\n"
        "Insert one row: (1, 'Emperor').\n"
        "SELECT all rows.\n\n"
        "Expected output: [(1, 'Emperor')]"
    ),
    expected_output="[(1, 'Emperor')]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE soldiers (soldier_id INTEGER, name TEXT);",
        "INSERT INTO soldiers VALUES (1, 'Emperor');",
        "SELECT * FROM soldiers;"
    ]
)

easy2 = Task(
    description=(
        "🔒  Required Name – NOT NULL\n\n"
        "Create a table `officers` with columns:\n"
        "  • id INTEGER\n"
        "  • name TEXT NOT NULL\n"
        "  • rank TEXT\n\n"
        "Insert two rows:\n"
        "  (1, 'Emperor', 'General')\n"
        "  (2, 'Rahim', NULL)\n"
        "SELECT name, rank for all rows.\n\n"
        "Expected output:\n[('Emperor', 'General'), ('Rahim', None)]"
    ),
    expected_output="[('Emperor', 'General'), ('Rahim', None)]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE officers (id INTEGER, name TEXT NOT NULL, rank TEXT);",
        "INSERT INTO officers VALUES (1, 'Emperor', 'General'), (2, 'Rahim', NULL);",
        "SELECT name, rank FROM officers;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "💰  Positive Salary – CHECK Constraint\n\n"
        "Create a table `payroll` with columns:\n"
        "  • emp_id INTEGER PRIMARY KEY\n"
        "  • name TEXT NOT NULL\n"
        "  • salary REAL CHECK(salary > 0)\n\n"
        "Insert two rows:\n"
        "  (1, 'Emperor', 5000)\n"
        "  (2, 'Rahim', 3000)\n"
        "SELECT name and salary sorted by salary descending.\n\n"
        "Expected output:\n[('Emperor', 5000.0), ('Rahim', 3000.0)]"
    ),
    expected_output="[('Emperor', 5000.0), ('Rahim', 3000.0)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE payroll (emp_id INTEGER PRIMARY KEY, name TEXT NOT NULL, salary REAL CHECK(salary > 0));",
        "INSERT INTO payroll VALUES (1, 'Emperor', 5000), (2, 'Rahim', 3000);",
        "SELECT name, salary FROM payroll ORDER BY salary DESC;"
    ]
)

medium2 = Task(
    description=(
        "📅  Default Join Date – DEFAULT Value\n\n"
        "Create a table `recruits` with columns:\n"
        "  • id INTEGER PRIMARY KEY\n"
        "  • name TEXT NOT NULL\n"
        "  • joined TEXT DEFAULT (date('now'))\n\n"
        "Insert two rows:\n"
        "  (1, 'Ali')\n"
        "  (2, 'Hasan')\n"
        "Then SELECT name and joined.\n"
        "The joined column should show today's date.\n\n"
        "Expected output:\n[('Ali', (date)), ('Hasan', (date))]"
    ),
    setup_sql="",  # No setup, user creates table
    expected_output=None,  # Use verify_func due to dynamic date
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE recruits (id INTEGER PRIMARY KEY, name TEXT NOT NULL, joined TEXT DEFAULT (date('now')));",
        "INSERT INTO recruits (id, name) VALUES (1, 'Ali'), (2, 'Hasan');",
        "SELECT name, joined FROM recruits;"
    ],
    verify_func=lambda conn: (
        len(conn.execute("SELECT * FROM recruits").fetchall()) == 2
        and conn.execute("SELECT joined FROM recruits LIMIT 1").fetchone()[0] is not None
    )
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🛡️  Full Arsenal – UNIQUE & CHECK\n\n"
        "Create a table `weapons` with columns:\n"
        "  • weapon_id INTEGER PRIMARY KEY\n"
        "  • weapon_name TEXT NOT NULL UNIQUE\n"
        "  • power_level INTEGER CHECK(power_level > 0)\n\n"
        "Insert three rows:\n"
        "  (1, 'Laser', 5)\n"
        "  (2, 'Plasma', 8)\n"
        "  (3, 'Railgun', 10)\n"
        "SELECT weapon_name and power_level\n"
        "for weapons with power_level >= 8,\n"
        "sorted by power_level descending.\n\n"
        "Expected output:\n[('Railgun', 10), ('Plasma', 8)]"
    ),
    expected_output="[('Railgun', 10), ('Plasma', 8)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE weapons (weapon_id INTEGER PRIMARY KEY, weapon_name TEXT NOT NULL UNIQUE, power_level INTEGER CHECK(power_level > 0));",
        "INSERT INTO weapons VALUES (1,'Laser',5), (2,'Plasma',8), (3,'Railgun',10);",
        "SELECT weapon_name, power_level FROM weapons WHERE power_level >= 8 ORDER BY power_level DESC;"
    ]
)

hard2 = Task(
    description=(
        "🧱  Composite Constraints – Supply Depot\n\n"
        "Create a table `supplies` with columns:\n"
        "  • depot_id INTEGER\n"
        "  • item_name TEXT\n"
        "  • quantity INTEGER CHECK(quantity >= 0)\n"
        "  • PRIMARY KEY (depot_id, item_name)\n\n"
        "Insert three rows:\n"
        "  (1, 'Shield', 10)\n"
        "  (1, 'Sword', 25)\n"
        "  (2, 'Shield', 15)\n"
        "SELECT * ordered by depot_id, item_name.\n\n"
        "Expected output:\n[(1, 'Shield', 10), (1, 'Sword', 25), (2, 'Shield', 15)]"
    ),
    expected_output="[(1, 'Shield', 10), (1, 'Sword', 25), (2, 'Shield', 15)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE supplies (depot_id INTEGER, item_name TEXT, quantity INTEGER CHECK(quantity >= 0), PRIMARY KEY(depot_id, item_name));",
        "INSERT INTO supplies VALUES (1,'Shield',10), (1,'Sword',25), (2,'Shield',15);",
        "SELECT * FROM supplies ORDER BY depot_id, item_name;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L03.json",
        module_name="Module_01_SQL_Core",
        lesson_name="L03_CREATE_TABLE"
    )
