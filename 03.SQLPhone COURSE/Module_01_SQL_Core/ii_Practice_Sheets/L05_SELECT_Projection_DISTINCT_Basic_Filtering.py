import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "📋  Projection – Pick Columns\n\n"
        "The `soldiers` table has columns:\n"
        "  id, name, rank, salary.\n"
        "Select only `name` and `rank` for all rows.\n\n"
        "Expected output:\n[('Emperor','General'), ('Rahim','Colonel'), ('Karim','Private')]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000);"
    ),
    expected_output="[('Emperor', 'General'), ('Rahim', 'Colonel'), ('Karim', 'Private')]",
    level=Level.EASY,
    hints=[
        "SELECT name, rank FROM soldiers;"
    ]
)

easy2 = Task(
    description=(
        "🌟  All Columns – Quick Scan\n\n"
        "The `soldiers` table has 3 rows.\n"
        "Use SELECT * to return all columns\n"
        "for every row.\n\n"
        "Expected output:\n[(1,'Emperor','General',5000.0), (2,'Rahim','Colonel',4000.0), (3,'Karim','Private',2000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000);"
    ),
    expected_output="[(1, 'Emperor', 'General', 5000.0), (2, 'Rahim', 'Colonel', 4000.0), (3, 'Karim', 'Private', 2000.0)]",
    level=Level.EASY,
    hints=[
        "SELECT * FROM soldiers;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🧹  DISTINCT – Unique Ranks\n\n"
        "The `soldiers` table contains multiple ranks.\n"
        "Some ranks appear more than once.\n"
        "Write a query that returns each rank only once.\n\n"
        "Expected output:\n[('Colonel',), ('General',), ('Private',)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500);"
    ),
    expected_output="[('Colonel',), ('General',), ('Private',)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT DISTINCT rank FROM soldiers ORDER BY rank;"
    ]
)

medium2 = Task(
    description=(
        "🔍  Basic WHERE – Filter by Rank\n\n"
        "The `soldiers` table has 4 rows.\n"
        "Return the name and salary of all soldiers\n"
        "whose rank is 'General'.\n\n"
        "Expected output:\n[('Emperor',5000.0), ('Ali',4500.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500);"
    ),
    expected_output="[('Emperor', 5000.0), ('Ali', 4500.0)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT name, salary FROM soldiers WHERE rank = 'General';"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "💰  WHERE with Numbers – High Earners\n\n"
        "The `soldiers` table has 4 rows.\n"
        "Return name and salary for soldiers\n"
        "with salary greater than 3000,\n"
        "sorted by salary descending.\n\n"
        "Expected output:\n[('Emperor',5000.0), ('Ali',4500.0), ('Rahim',4000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500);"
    ),
    expected_output="[('Emperor', 5000.0), ('Ali', 4500.0), ('Rahim', 4000.0)]",
    level=Level.HARD,
    hints=[
        "SELECT name, salary FROM soldiers WHERE salary > 3000 ORDER BY salary DESC;"
    ]
)

hard2 = Task(
    description=(
        "🧪  DISTINCT + WHERE – Active Categories\n\n"
        "Create a table `inventory` with columns:\n"
        "  id INTEGER, item TEXT, category TEXT, stock INTEGER.\n"
        "Insert 6 rows (some categories repeat).\n"
        "Then SELECT DISTINCT category for items\n"
        "where stock > 0, sorted alphabetically.\n\n"
        "Expected output:\n[('Electronics',), ('Furniture',), ('Office',)]"
    ),
    expected_output="[('Electronics',), ('Furniture',), ('Office',)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE inventory (id INTEGER, item TEXT, category TEXT, stock INTEGER);",
        "INSERT INTO inventory VALUES (1,'Laptop','Electronics',10), (2,'Mouse','Electronics',0), (3,'Desk','Furniture',5), (4,'Chair','Furniture',0), (5,'Pen','Office',50), (6,'Notebook','Office',30);",
        "SELECT DISTINCT category FROM inventory WHERE stock > 0 ORDER BY category;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L05.json",
        module_name="Module_01_SQL_Core",
        lesson_name="L05_SELECT_Projection_DISTINCT"
    )
