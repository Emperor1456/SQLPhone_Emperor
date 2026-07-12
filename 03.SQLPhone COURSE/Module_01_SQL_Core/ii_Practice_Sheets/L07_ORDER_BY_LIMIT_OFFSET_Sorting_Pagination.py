import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "📊  Sort by Salary – Ascending\n\n"
        "The `soldiers` table has 4 rows.\n"
        "Return name and salary, sorted by salary\n"
        "from lowest to highest.\n\n"
        "Expected output:\n[('Karim',2000.0), ('Rahim',4000.0), ('Ali',4500.0), ('Emperor',5000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500);"
    ),
    expected_output="[('Karim', 2000.0), ('Rahim', 4000.0), ('Ali', 4500.0), ('Emperor', 5000.0)]",
    level=Level.EASY,
    hints=[
        "SELECT name, salary FROM soldiers ORDER BY salary ASC;"
    ]
)

easy2 = Task(
    description=(
        "📉  Sort by Salary – Descending\n\n"
        "The same `soldiers` table.\n"
        "Return name and salary, sorted by salary\n"
        "from highest to lowest.\n\n"
        "Expected output:\n[('Emperor',5000.0), ('Ali',4500.0), ('Rahim',4000.0), ('Karim',2000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500);"
    ),
    expected_output="[('Emperor', 5000.0), ('Ali', 4500.0), ('Rahim', 4000.0), ('Karim', 2000.0)]",
    level=Level.EASY,
    hints=[
        "SELECT name, salary FROM soldiers ORDER BY salary DESC;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🔝  Top 3 Earners – LIMIT\n\n"
        "The `soldiers` table has 4 rows.\n"
        "Return the name and salary of the 3 soldiers\n"
        "with the highest salary.\n\n"
        "Expected output:\n[('Emperor',5000.0), ('Ali',4500.0), ('Rahim',4000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500);"
    ),
    expected_output="[('Emperor', 5000.0), ('Ali', 4500.0), ('Rahim', 4000.0)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT name, salary FROM soldiers ORDER BY salary DESC LIMIT 3;"
    ]
)

medium2 = Task(
    description=(
        "📄  Pagination – Page 2\n\n"
        "The `soldiers` table has 4 rows.\n"
        "Return the name and salary of soldiers,\n"
        "skipping the top 2 (OFFSET 2) and showing\n"
        "the next 2 rows (LIMIT 2), sorted by salary desc.\n\n"
        "Expected output:\n[('Rahim',4000.0), ('Karim',2000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500);"
    ),
    expected_output="[('Rahim', 4000.0), ('Karim', 2000.0)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT name, salary FROM soldiers ORDER BY salary DESC LIMIT 2 OFFSET 2;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧱  Multi‑Column Sort – Rank then Name\n\n"
        "Create a table `regiment` with columns:\n"
        "  id INTEGER, name TEXT, rank TEXT, regiment_id INTEGER.\n"
        "Insert 6 rows with varied data.\n"
        "Return name, rank, and regiment_id,\n"
        "sorted first by regiment_id ASC,\n"
        "then by rank (using a custom order where\n"
        "'General' = 1, 'Colonel' = 2, 'Major' = 3, 'Private' = 4).\n"
        "Use a CASE expression in ORDER BY.\n\n"
        "Expected output:\n[('Ali','General',1), ('Emperor','General',1), ('Hasan','Colonel',1), ('Rahim','Major',2), ('Karim','Private',2), ('Fatima','Private',3)]"
    ),
    expected_output="[('Ali', 'General', 1), ('Emperor', 'General', 1), ('Hasan', 'Colonel', 1), ('Rahim', 'Major', 2), ('Karim', 'Private', 2), ('Fatima', 'Private', 3)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE regiment (id INTEGER, name TEXT, rank TEXT, regiment_id INTEGER);",
        "INSERT INTO regiment VALUES (1,'Emperor','General',1), (2,'Rahim','Major',2), (3,'Karim','Private',2), (4,'Ali','General',1), (5,'Hasan','Colonel',1), (6,'Fatima','Private',3);",
        "SELECT name, rank, regiment_id FROM regiment ORDER BY regiment_id ASC, CASE rank WHEN 'General' THEN 1 WHEN 'Colonel' THEN 2 WHEN 'Major' THEN 3 WHEN 'Private' THEN 4 ELSE 5 END;"
    ]
)

hard2 = Task(
    description=(
        "🔍  Nth Highest – Skip & Limit\n\n"
        "The `soldiers` table has 4 rows.\n"
        "Find the soldier with the 3rd highest salary\n"
        "(i.e., skip the top 2, take the next 1).\n"
        "Return name and salary.\n\n"
        "Expected output:\n[('Rahim',4000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500);"
    ),
    expected_output="[('Rahim', 4000.0)]",
    level=Level.HARD,
    hints=[
        "SELECT name, salary FROM soldiers ORDER BY salary DESC LIMIT 1 OFFSET 2;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L07.json",
        module_name="Module_01_SQL_Core",
        lesson_name="L07_ORDER_BY_LIMIT_OFFSET"
    )
