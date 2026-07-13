import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "📊  GROUP BY – Count by Rank\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Write a query that groups soldiers by rank\n"
        "and returns the rank and the count of\n"
        "soldiers in each rank.\n"
        "Sort by count descending.\n\n"
        "Expected output:\n[('General',2), ('Colonel',2), ('Private',1)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[('General', 2), ('Colonel', 2), ('Private', 1)]",
    level=Level.EASY,
    hints=[
        "SELECT rank, COUNT(*) AS count FROM soldiers GROUP BY rank ORDER BY count DESC;"
    ]
)

easy2 = Task(
    description=(
        "📈  GROUP BY – Average Salary per Rank\n\n"
        "The same `soldiers` table.\n"
        "Write a query that returns the rank and\n"
        "the average salary for each rank.\n"
        "Round the average to 2 decimal places.\n"
        "Sort by rank alphabetically.\n\n"
        "Expected output:\n[('Colonel',3750.0), ('General',4750.0), ('Private',2000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[('Colonel', 3750.0), ('General', 4750.0), ('Private', 2000.0)]",
    level=Level.EASY,
    hints=[
        "SELECT rank, ROUND(AVG(salary), 2) AS avg_salary FROM soldiers GROUP BY rank ORDER BY rank;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🧮  GROUP BY – Multiple Aggregates\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Write a query that returns, for each rank:\n"
        "  • rank\n"
        "  • soldiers: COUNT(*)\n"
        "  • avg_salary: ROUND(AVG(salary), 2)\n"
        "  • max_salary: MAX(salary)\n"
        "  • min_salary: MIN(salary)\n"
        "Sort by soldiers descending.\n\n"
        "Expected output:\n[('General',2,4750.0,5000.0,4500.0), ('Colonel',2,3750.0,4000.0,3500.0), ('Private',1,2000.0,2000.0,2000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[('General', 2, 4750.0, 5000.0, 4500.0), ('Colonel', 2, 3750.0, 4000.0, 3500.0), ('Private', 1, 2000.0, 2000.0, 2000.0)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT rank, COUNT(*) AS soldiers, ROUND(AVG(salary), 2) AS avg_salary, MAX(salary) AS max_salary, MIN(salary) AS min_salary FROM soldiers GROUP BY rank ORDER BY soldiers DESC;"
    ]
)

medium2 = Task(
    description=(
        "📋  GROUP BY Expression – First Letter\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Write a query that groups soldiers by the\n"
        "first letter of their name (use SUBSTR).\n"
        "Return the first letter and the count\n"
        "of soldiers whose name starts with that letter.\n"
        "Sort by first letter.\n\n"
        "Expected output:\n[('A',1), ('E',1), ('H',1), ('K',1), ('R',1)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[('A', 1), ('E', 1), ('H', 1), ('K', 1), ('R', 1)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT SUBSTR(name, 1, 1) AS first_letter, COUNT(*) AS count FROM soldiers GROUP BY first_letter ORDER BY first_letter;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🏭  GROUP BY on Calculated Column – Pay Bands\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Create a query that groups soldiers into\n"
        "pay bands based on salary:\n"
        "  • salary >= 4500 → 'Top'\n"
        "  • salary >= 3500 → 'Mid'\n"
        "  • ELSE → 'Entry'\n"
        "Return the band name and count of soldiers\n"
        "in each band, sorted by count descending.\n\n"
        "Expected output:\n[('Top',2), ('Mid',2), ('Entry',1)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[('Top', 2), ('Mid', 2), ('Entry', 1)]",
    level=Level.HARD,
    hints=[
        "SELECT CASE WHEN salary >= 4500 THEN 'Top' WHEN salary >= 3500 THEN 'Mid' ELSE 'Entry' END AS band, COUNT(*) AS count FROM soldiers GROUP BY band ORDER BY count DESC;"
    ]
)

hard2 = Task(
    description=(
        "📊  GROUP BY with WHERE – Active Counts\n\n"
        "Create a table `roster` with columns:\n"
        "  • id INTEGER, name TEXT, regiment TEXT, status TEXT.\n"
        "Insert 6 rows with varied regiments and statuses.\n"
        "Write a query that counts soldiers per regiment,\n"
        "but only includes soldiers with status='active'.\n"
        "Return regiment and count, sorted by count desc.\n\n"
        "Expected output:\n[('Red',2), ('Blue',1), ('Green',1)]"
    ),
    expected_output="[('Red', 2), ('Blue', 1), ('Green', 1)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE roster (id INTEGER, name TEXT, regiment TEXT, status TEXT);",
        "INSERT INTO roster VALUES (1,'Emperor','Red','active'), (2,'Rahim','Blue','active'), (3,'Karim','Red','reserve'), (4,'Ali','Red','active'), (5,'Hasan','Green','active'), (6,'Fatima','Blue','reserve');",
        "SELECT regiment, COUNT(*) AS count FROM roster WHERE status = 'active' GROUP BY regiment ORDER BY count DESC;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L23.json",
        module_name="Module_03_Aggregation_Grouping",
        lesson_name="L23_GROUP_BY_Single_Column"
    )
