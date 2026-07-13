import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🗑️  DELETE Single Row – Remove a Soldier\n\n"
        "The `soldiers` table has 4 rows.\n"
        "Write a DELETE that removes the soldier named 'Hasan'.\n"
        "Then SELECT all remaining rows, sorted by id.\n\n"
        "Expected output:\n[(1,'Emperor','General',5000.0), (2,'Rahim','Colonel',4000.0), (3,'Ali','General',4500.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Ali','General',4500), (4,'Hasan','Private',3500);"
    ),
    expected_output="[(1, 'Emperor', 'General', 5000.0), (2, 'Rahim', 'Colonel', 4000.0), (3, 'Ali', 'General', 4500.0)]",
    level=Level.EASY,
    hints=[
        "DELETE FROM soldiers WHERE name = 'Hasan';",
        "SELECT * FROM soldiers ORDER BY id;"
    ]
)

easy2 = Task(
    description=(
        "🧹  DELETE with Condition – Remove Low Salary\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Write a DELETE that removes all soldiers with\n"
        "salary less than 3000.\n"
        "Then SELECT all remaining rows, sorted by id.\n\n"
        "Expected output:\n[(1,'Emperor','General',5000.0), (2,'Rahim','Colonel',4000.0), (3,'Ali','General',4500.0), (4,'Hasan','Private',3500.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Ali','General',4500), (4,'Hasan','Private',3500), (5,'Karim','Private',2000);"
    ),
    expected_output="[(1, 'Emperor', 'General', 5000.0), (2, 'Rahim', 'Colonel', 4000.0), (3, 'Ali', 'General', 4500.0), (4, 'Hasan', 'Private', 3500.0)]",
    level=Level.EASY,
    hints=[
        "DELETE FROM soldiers WHERE salary < 3000;",
        "SELECT * FROM soldiers ORDER BY id;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🔍  DELETE with Subquery – Remove Disbanded Regiment\n\n"
        "Create `regiments` and `soldiers` tables.\n"
        "Write a DELETE that removes all soldiers whose\n"
        "regiment_id is IN (SELECT id FROM regiments\n"
        "WHERE status = 'disbanded').\n"
        "Then SELECT all remaining soldiers, sorted by id.\n\n"
        "Expected output:\n[(1,'Emperor',1), (3,'Ali',1)]"
    ),
    expected_output="[(1, 'Emperor', 1), (3, 'Ali', 1)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT, status TEXT);",
        "INSERT INTO regiments VALUES (1,'Imperial Guard','active'), (2,'Red Guard','disbanded');",
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER);",
        "INSERT INTO soldiers VALUES (1,'Emperor',1), (2,'Rahim',2), (3,'Ali',1), (4,'Hasan',2);",
        "DELETE FROM soldiers WHERE regiment_id IN (SELECT id FROM regiments WHERE status = 'disbanded');",
        "SELECT * FROM soldiers ORDER BY id;"
    ]
)

medium2 = Task(
    description=(
        "⚠️  Safe DELETE – Test with SELECT First\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Before deleting, write a SELECT to verify which\n"
        "rows would be affected: soldiers with salary < 3000\n"
        "AND rank = 'Private'.\n"
        "Then write the DELETE to remove those rows.\n"
        "Show the final table.\n\n"
        "Expected output:\n[(1,'Emperor','General',5000.0), (2,'Rahim','Colonel',4000.0), (3,'Ali','General',4500.0), (4,'Hasan','Private',3500.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Ali','General',4500), (4,'Hasan','Private',3500), (5,'Karim','Private',2000);"
    ),
    expected_output="[(1, 'Emperor', 'General', 5000.0), (2, 'Rahim', 'Colonel', 4000.0), (3, 'Ali', 'General', 4500.0), (4, 'Hasan', 'Private', 3500.0)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT * FROM soldiers WHERE salary < 3000 AND rank = 'Private';",
        "DELETE FROM soldiers WHERE salary < 3000 AND rank = 'Private';",
        "SELECT * FROM soldiers ORDER BY id;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🔄  DELETE with NOT EXISTS – Orphan Records\n\n"
        "Create `regiments` and `soldiers` tables.\n"
        "Write a DELETE that removes soldiers who are NOT\n"
        "assigned to any regiment (regiment_id IS NULL)\n"
        "OR whose regiment_id does NOT EXIST in regiments.\n"
        "Use NOT EXISTS for the orphan check.\n"
        "Then SELECT all remaining soldiers, sorted by id.\n\n"
        "Expected output:\n[(1,'Emperor',1), (3,'Ali',1)]"
    ),
    expected_output="[(1, 'Emperor', 1), (3, 'Ali', 1)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO regiments VALUES (1,'Imperial Guard');",
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER);",
        "INSERT INTO soldiers VALUES (1,'Emperor',1), (2,'Rahim',NULL), (3,'Ali',1), (4,'Hasan',99);",
        "DELETE FROM soldiers WHERE regiment_id IS NULL OR NOT EXISTS (SELECT 1 FROM regiments r WHERE r.id = soldiers.regiment_id);",
        "SELECT * FROM soldiers ORDER BY id;"
    ]
)

hard2 = Task(
    description=(
        "🧪  Soft Delete – Mark Instead of Remove\n\n"
        "The `soldiers` table has 4 rows.\n"
        "First, ALTER TABLE to add a `deleted_at` column.\n"
        "Then, instead of actually deleting Hasan,\n"
        "UPDATE his row to set deleted_at = datetime('now').\n"
        "Then SELECT only rows where deleted_at IS NULL\n"
        "(the active soldiers), sorted by id.\n\n"
        "Expected output:\n[(1,'Emperor','General',5000.0,None), (2,'Rahim','Colonel',4000.0,None), (3,'Ali','General',4500.0,None)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Ali','General',4500), (4,'Hasan','Private',3500);"
    ),
    expected_output="[(1, 'Emperor', 'General', 5000.0, None), (2, 'Rahim', 'Colonel', 4000.0, None), (3, 'Ali', 'General', 4500.0, None)]",
    level=Level.HARD,
    hints=[
        "ALTER TABLE soldiers ADD COLUMN deleted_at TEXT;",
        "UPDATE soldiers SET deleted_at = datetime('now') WHERE name = 'Hasan';",
        "SELECT * FROM soldiers WHERE deleted_at IS NULL ORDER BY id;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L52.json",
        module_name="Module_06_Modifying_Data_Schema",
        lesson_name="L52_DELETE"
    )
