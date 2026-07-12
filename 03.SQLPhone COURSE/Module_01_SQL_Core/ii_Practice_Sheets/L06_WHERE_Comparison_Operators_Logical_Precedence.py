import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "⚖️  Equal To – Find the General\n\n"
        "The `soldiers` table has 4 rows.\n"
        "Return the name and salary of all soldiers\n"
        "whose rank equals 'General'.\n\n"
        "Expected output:\n[('Emperor',5000.0), ('Ali',4500.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500);"
    ),
    expected_output="[('Emperor', 5000.0), ('Ali', 4500.0)]",
    level=Level.EASY,
    hints=[
        "SELECT name, salary FROM soldiers WHERE rank = 'General';"
    ]
)

easy2 = Task(
    description=(
        "📏  Greater Than – High Salaries\n\n"
        "The `soldiers` table has 4 rows.\n"
        "Return the name and salary of soldiers\n"
        "whose salary is greater than 3000,\n"
        "sorted by salary descending.\n\n"
        "Expected output:\n[('Emperor',5000.0), ('Ali',4500.0), ('Rahim',4000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500);"
    ),
    expected_output="[('Emperor', 5000.0), ('Ali', 4500.0), ('Rahim', 4000.0)]",
    level=Level.EASY,
    hints=[
        "SELECT name, salary FROM soldiers WHERE salary > 3000 ORDER BY salary DESC;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🔗  AND – Generals with High Salary\n\n"
        "The `soldiers` table has 4 rows.\n"
        "Return the name and salary of soldiers\n"
        "who are BOTH Generals AND earn more than 4000.\n\n"
        "Expected output:\n[('Emperor',5000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500);"
    ),
    expected_output="[('Emperor', 5000.0)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT name, salary FROM soldiers WHERE rank = 'General' AND salary > 4000;"
    ]
)

medium2 = Task(
    description=(
        "🔀  OR – Generals or High Earners\n\n"
        "The `soldiers` table has 4 rows.\n"
        "Return the name, rank, and salary of soldiers\n"
        "who are Generals OR earn more than 4000.\n"
        "Sort by salary descending.\n\n"
        "Expected output:\n[('Emperor','General',5000.0), ('Ali','General',4500.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500);"
    ),
    expected_output="[('Emperor', 'General', 5000.0), ('Ali', 'General', 4500.0)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT name, rank, salary FROM soldiers WHERE rank = 'General' OR salary > 4000 ORDER BY salary DESC;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🚫  NOT – Exclude Privates\n\n"
        "The `soldiers` table has 4 rows.\n"
        "Return the name and rank of soldiers\n"
        "who are NOT Privates.\n\n"
        "Expected output:\n[('Emperor','General'), ('Rahim','Colonel'), ('Ali','General')]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500);"
    ),
    expected_output="[('Emperor', 'General'), ('Rahim', 'Colonel'), ('Ali', 'General')]",
    level=Level.HARD,
    hints=[
        "SELECT name, rank FROM soldiers WHERE NOT rank = 'Private';"
    ]
)

hard2 = Task(
    description=(
        "🧠  Precedence – Generals or High-Paid Non-Privates\n\n"
        "The `soldiers` table has 4 rows.\n"
        "Return name, rank, and salary for soldiers\n"
        "who are Generals OR (not Privates AND salary > 3000).\n"
        "Use parentheses to make the logic clear.\n"
        "Sort by salary descending.\n\n"
        "Expected output:\n[('Emperor','General',5000.0), ('Ali','General',4500.0), ('Rahim','Colonel',4000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500);"
    ),
    expected_output="[('Emperor', 'General', 5000.0), ('Ali', 'General', 4500.0), ('Rahim', 'Colonel', 4000.0)]",
    level=Level.HARD,
    hints=[
        "SELECT name, rank, salary FROM soldiers WHERE rank = 'General' OR (NOT rank = 'Private' AND salary > 3000) ORDER BY salary DESC;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L06.json",
        module_name="Module_01_SQL_Core",
        lesson_name="L06_WHERE_Comparison_Operators"
    )
