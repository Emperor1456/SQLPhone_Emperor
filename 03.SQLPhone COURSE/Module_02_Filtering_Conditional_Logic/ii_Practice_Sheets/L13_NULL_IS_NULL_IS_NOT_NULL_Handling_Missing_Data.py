import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🕳️  Find Missing Ranks – IS NULL\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Some soldiers have no rank assigned (NULL).\n"
        "Return the name of all soldiers\n"
        "whose rank IS NULL.\n\n"
        "Expected output: [('Karim',)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim',NULL,2000), (4,'Ali','General',4500), (5,'Hasan',NULL,3500);"
    ),
    expected_output="[('Karim',)]",
    level=Level.EASY,
    hints=[
        "SELECT name FROM soldiers WHERE rank IS NULL;"
    ]
)

easy2 = Task(
    description=(
        "✅  Find Assigned Ranks – IS NOT NULL\n\n"
        "The same `soldiers` table.\n"
        "Return the name and rank of soldiers\n"
        "whose rank IS NOT NULL.\n"
        "Sort by name alphabetically.\n\n"
        "Expected output:\n[('Ali','General'), ('Emperor','General'), ('Hasan',NULL), ('Rahim','Colonel')]\n\nWait – Hasan has NULL rank, so should be excluded.\nLet's recheck: Hasan has NULL, so not included.\nExpected: [('Ali','General'), ('Emperor','General'), ('Rahim','Colonel')]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim',NULL,2000), (4,'Ali','General',4500), (5,'Hasan',NULL,3500);"
    ),
    expected_output="[('Ali', 'General'), ('Emperor', 'General'), ('Rahim', 'Colonel')]",
    level=Level.EASY,
    hints=[
        "SELECT name, rank FROM soldiers WHERE rank IS NOT NULL ORDER BY name;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🧹  Replace NULL – COALESCE in Action\n\n"
        "The `soldiers` table has soldiers with NULL ranks.\n"
        "Return the name and rank of ALL soldiers,\n"
        "but replace any NULL rank with 'Unassigned'.\n"
        "Use COALESCE(rank, 'Unassigned').\n"
        "Sort by name.\n\n"
        "Expected output:\n[('Ali','General'), ('Emperor','General'), ('Hasan','Unassigned'), ('Karim','Unassigned'), ('Rahim','Colonel')]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim',NULL,2000), (4,'Ali','General',4500), (5,'Hasan',NULL,3500);"
    ),
    expected_output="[('Ali', 'General'), ('Emperor', 'General'), ('Hasan', 'Unassigned'), ('Karim', 'Unassigned'), ('Rahim', 'Colonel')]",
    level=Level.MEDIUM,
    hints=[
        "SELECT name, COALESCE(rank, 'Unassigned') AS rank FROM soldiers ORDER BY name;"
    ]
)

medium2 = Task(
    description=(
        "📊  COUNT with NULL – Know the Difference\n\n"
        "The `soldiers` table has 5 rows, 2 with NULL rank.\n"
        "Write a query that returns:\n"
        "  • total: COUNT(*)\n"
        "  • with_rank: COUNT(rank)\n"
        "  • missing_rank: COUNT(*) - COUNT(rank)\n\n"
        "Expected output: [(5, 3, 2)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim',NULL,2000), (4,'Ali','General',4500), (5,'Hasan',NULL,3500);"
    ),
    expected_output="[(5, 3, 2)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT COUNT(*), COUNT(rank), COUNT(*) - COUNT(rank) FROM soldiers;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "⚠️  NULL in Comparisons – The Trap\n\n"
        "The `soldiers` table has soldiers with NULL rank.\n"
        "Write a query that returns the name of soldiers\n"
        "where rank != 'General'.\n"
        "Observe whether NULLs appear.\n"
        "Then write the CORRECT query to get soldiers\n"
        "who are not Generals, including those with NULL rank.\n"
        "Use: WHERE rank != 'General' OR rank IS NULL\n\n"
        "Expected output:\n[('Rahim','Colonel'), ('Karim',NULL), ('Hasan',NULL)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim',NULL,2000), (4,'Ali','General',4500), (5,'Hasan',NULL,3500);"
    ),
    expected_output="[('Rahim', 'Colonel'), ('Karim', None), ('Hasan', None)]",
    level=Level.HARD,
    hints=[
        "SELECT name, rank FROM soldiers WHERE rank != 'General' OR rank IS NULL;"
    ]
)

hard2 = Task(
    description=(
        "🧮  NULL in Arithmetic – Safety Net\n\n"
        "Create a table `bonus` with columns:\n"
        "  id INTEGER, name TEXT, base_salary REAL, bonus_pct REAL.\n"
        "Insert rows where some bonus_pct are NULL.\n"
        "Return name, base_salary, bonus_pct, and\n"
        "the total compensation (base_salary + base_salary * bonus_pct),\n"
        "but if bonus_pct is NULL, treat it as 0.\n"
        "Use COALESCE or IFNULL.\n"
        "Sort by total descending.\n\n"
        "Expected output:\n[('Emperor',5000.0,0.2,6000.0), ('Ali',4500.0,None,4500.0), ('Rahim',4000.0,0.15,4600.0)]"
    ),
    setup_sql=(
        "CREATE TABLE bonus (id INTEGER, name TEXT, base_salary REAL, bonus_pct REAL);"
        "INSERT INTO bonus VALUES (1,'Emperor',5000.0,0.2), (2,'Rahim',4000.0,0.15), (3,'Ali',4500.0,NULL);"
    ),
    expected_output="[('Emperor', 5000.0, 0.2, 6000.0), ('Rahim', 4000.0, 0.15, 4600.0), ('Ali', 4500.0, None, 4500.0)]",
    level=Level.HARD,
    hints=[
        "SELECT name, base_salary, bonus_pct, base_salary + base_salary * COALESCE(bonus_pct, 0) AS total FROM bonus ORDER BY total DESC;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L13.json",
        module_name="Module_02_Filtering_Conditional_Logic",
        lesson_name="L13_NULL"
    )
