import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "📋  List All Tables – Inspect the Database\n\n"
        "The database has two tables: `soldiers` and `regiments`.\n"
        "Write a query using `sqlite_master` to list the names\n"
        "of all user‑created tables (type='table').\n"
        "Sort alphabetically.\n\n"
        "Expected output:\n[('regiments',), ('soldiers',)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT);"
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT);"
    ),
    expected_output="[('regiments',), ('soldiers',)]",
    level=Level.EASY,
    hints=[
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
    ]
)

easy2 = Task(
    description=(
        "🔍  Show CREATE Statement – .schema Alternative\n\n"
        "The `soldiers` table exists.\n"
        "Write a query that returns the exact CREATE TABLE\n"
        "statement for the 'soldiers' table, using the `sql`\n"
        "column from `sqlite_master`.\n\n"
        "Expected output:\n[('CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT)',)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT);"
    ),
    expected_output="[('CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT)',)]",
    level=Level.EASY,
    hints=[
        "SELECT sql FROM sqlite_master WHERE type='table' AND name='soldiers';"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "💾  Table Backup – Copy All Rows\n\n"
        "The `soldiers` table has 3 rows.\n"
        "Create a backup table named `soldiers_backup` with\n"
        "the same columns (id INTEGER, name TEXT, rank TEXT).\n"
        "Then insert all rows from `soldiers` into the backup.\n"
        "Finally, SELECT all rows from the backup table,\n"
        "sorted by id.\n\n"
        "Expected output:\n[(1,'Emperor','General'), (2,'Rahim','Colonel'), (3,'Ali','Major')]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General'), (2,'Rahim','Colonel'), (3,'Ali','Major');"
    ),
    expected_output="[(1, 'Emperor', 'General'), (2, 'Rahim', 'Colonel'), (3, 'Ali', 'Major')]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE soldiers_backup (id INTEGER, name TEXT, rank TEXT);",
        "INSERT INTO soldiers_backup SELECT * FROM soldiers;",
        "SELECT * FROM soldiers_backup ORDER BY id;"
    ]
)

medium2 = Task(
    description=(
        "📊  Check AUTOINCREMENT Status – sqlite_sequence\n\n"
        "Create a table `logs` with an AUTOINCREMENT primary key.\n"
        "Insert 3 rows, then query the `sqlite_sequence` table\n"
        "to see the current sequence number for this table.\n\n"
        "Expected output:\n[('logs', 3)]"
    ),
    setup_sql=(
        "CREATE TABLE logs (id INTEGER PRIMARY KEY AUTOINCREMENT, msg TEXT);"
        "INSERT INTO logs (msg) VALUES ('first'), ('second'), ('third');"
    ),
    expected_output="[('logs', 3)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT name, seq FROM sqlite_sequence WHERE name='logs';"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "📄  Export Entire Schema – Simulate .dump\n\n"
        "The database has two tables: `soldiers` and `regiments`.\n"
        "Write a query that returns the complete SQL needed to\n"
        "recreate both tables, concatenated into a single string.\n"
        "Use `GROUP_CONCAT(sql, '; ')` on `sqlite_master`.\n\n"
        "Expected output:\n[('CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT); CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT)',)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT);"
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT);"
    ),
    expected_output="[('CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT); CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT)',)]",
    level=Level.HARD,
    hints=[
        "SELECT GROUP_CONCAT(sql, '; ') FROM sqlite_master WHERE type='table';"
    ]
)

hard2 = Task(
    description=(
        "🔄  Simulate Restore – Delete and Re‑insert\n\n"
        "A backup table `soldiers_backup` already contains the\n"
        "original data. The `soldiers` table has been damaged.\n"
        "Write statements to:\n"
        "  1. DELETE all rows from `soldiers`\n"
        "  2. INSERT all rows from `soldiers_backup` into `soldiers`\n"
        "  3. SELECT from the restored `soldiers` table, sorted by id.\n\n"
        "Expected output:\n[(1,'Emperor','General'), (2,'Rahim','Colonel'), (3,'Ali','Major')]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General'), (2,'Rahim','Colonel'), (3,'Ali','Major');"
        "CREATE TABLE soldiers_backup (id INTEGER, name TEXT, rank TEXT);"
        "INSERT INTO soldiers_backup SELECT * FROM soldiers;"
        "DELETE FROM soldiers;"
    ),
    expected_output="[(1, 'Emperor', 'General'), (2, 'Rahim', 'Colonel'), (3, 'Ali', 'Major')]",
    level=Level.HARD,
    hints=[
        "DELETE FROM soldiers;",
        "INSERT INTO soldiers SELECT * FROM soldiers_backup;",
        "SELECT * FROM soldiers ORDER BY id;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L66.json",
        module_name="Module_07_Views_Optimization_Security",
        lesson_name="L66_Backup_Restore"
    )
