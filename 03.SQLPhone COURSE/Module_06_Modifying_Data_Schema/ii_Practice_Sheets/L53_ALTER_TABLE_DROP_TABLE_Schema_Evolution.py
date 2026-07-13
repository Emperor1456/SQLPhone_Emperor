import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "➕  ALTER TABLE – Add a Column\n\n"
        "The `soldiers` table has 4 rows with columns\n"
        "id, name, rank, and salary.\n"
        "Write an ALTER TABLE statement to add a\n"
        "new column `email` of type TEXT.\n"
        "Then SELECT all columns to confirm the new\n"
        "column appears (it will be NULL for existing rows).\n\n"
        "Expected output:\n[(1,'Emperor','General',5000.0,None), (2,'Rahim','Colonel',4000.0,None), (3,'Ali','General',4500.0,None), (4,'Hasan','Private',3500.0,None)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Ali','General',4500), (4,'Hasan','Private',3500);"
    ),
    expected_output="[(1, 'Emperor', 'General', 5000.0, None), (2, 'Rahim', 'Colonel', 4000.0, None), (3, 'Ali', 'General', 4500.0, None), (4, 'Hasan', 'Private', 3500.0, None)]",
    level=Level.EASY,
    hints=[
        "ALTER TABLE soldiers ADD COLUMN email TEXT;",
        "SELECT * FROM soldiers ORDER BY id;"
    ]
)

easy2 = Task(
    description=(
        "✏️  ALTER TABLE – Rename a Column\n\n"
        "The `soldiers` table has columns id, name, rank, salary.\n"
        "Write an ALTER TABLE statement to rename the\n"
        "column `name` to `full_name`.\n"
        "Then SELECT the renamed column.\n"
        "Sort by id.\n\n"
        "Expected output:\n[('Emperor',), ('Rahim',), ('Ali',), ('Hasan',)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Ali','General',4500), (4,'Hasan','Private',3500);"
    ),
    expected_output="[('Emperor',), ('Rahim',), ('Ali',), ('Hasan',)]",
    level=Level.EASY,
    hints=[
        "ALTER TABLE soldiers RENAME COLUMN name TO full_name;",
        "SELECT full_name FROM soldiers ORDER BY id;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🔄  ALTER TABLE – Rename Entire Table\n\n"
        "The `soldiers` table exists.\n"
        "Write an ALTER TABLE to rename it to `imperial_army`.\n"
        "Then SELECT all rows from the new table name.\n"
        "Sort by id.\n\n"
        "Expected output:\n[(1,'Emperor','General',5000.0), (2,'Rahim','Colonel',4000.0), (3,'Ali','General',4500.0), (4,'Hasan','Private',3500.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Ali','General',4500), (4,'Hasan','Private',3500);"
    ),
    expected_output="[(1, 'Emperor', 'General', 5000.0), (2, 'Rahim', 'Colonel', 4000.0), (3, 'Ali', 'General', 4500.0), (4, 'Hasan', 'Private', 3500.0)]",
    level=Level.MEDIUM,
    hints=[
        "ALTER TABLE soldiers RENAME TO imperial_army;",
        "SELECT * FROM imperial_army ORDER BY id;"
    ]
)

medium2 = Task(
    description=(
        "🗑️  DROP TABLE – Remove Entire Table\n\n"
        "Create a temporary table `temp_logs`.\n"
        "Write a DROP TABLE statement to remove it.\n"
        "Then query sqlite_master to confirm it no longer exists.\n\n"
        "Expected output: [] (empty result, temp_logs is gone)"
    ),
    expected_output="[]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE temp_logs (id INTEGER, msg TEXT);",
        "INSERT INTO temp_logs VALUES (1,'test');",
        "DROP TABLE IF EXISTS temp_logs;",
        "SELECT name FROM sqlite_master WHERE type='table' AND name='temp_logs';"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  Simulate DROP COLUMN – Table Recreation\n\n"
        "The `soldiers` table has columns id, name, rank, salary.\n"
        "You want to remove the `salary` column.\n"
        "Since SQLite does not support ALTER TABLE DROP COLUMN,\n"
        "simulate it by:\n"
        "  1. Create a new table `soldiers_new` without salary.\n"
        "  2. Copy data from soldiers to soldiers_new.\n"
        "  3. DROP soldiers.\n"
        "  4. Rename soldiers_new to soldiers.\n"
        "Then SELECT from the new soldiers table.\n\n"
        "Expected output:\n[(1,'Emperor','General'), (2,'Rahim','Colonel'), (3,'Ali','General'), (4,'Hasan','Private')]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Ali','General',4500), (4,'Hasan','Private',3500);"
    ),
    expected_output="[(1, 'Emperor', 'General'), (2, 'Rahim', 'Colonel'), (3, 'Ali', 'General'), (4, 'Hasan', 'Private')]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE soldiers_new (id INTEGER, name TEXT, rank TEXT);",
        "INSERT INTO soldiers_new SELECT id, name, rank FROM soldiers;",
        "DROP TABLE soldiers;",
        "ALTER TABLE soldiers_new RENAME TO soldiers;",
        "SELECT * FROM soldiers ORDER BY id;"
    ]
)

hard2 = Task(
    description=(
        "📊  Schema Migration – Add Constraint via Recreation\n\n"
        "The `soldiers` table has columns id, name, rank, salary.\n"
        "You need to add a NOT NULL constraint to the `rank` column.\n"
        "Simulate this by creating a new table with the constraint,\n"
        "copying data, and replacing the old table.\n"
        "Then verify by checking the schema from sqlite_master.\n\n"
        "Expected output:\n[('CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT NOT NULL, salary REAL)',)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000);"
    ),
    expected_output="[('CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT NOT NULL, salary REAL)',)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE soldiers_new (id INTEGER, name TEXT, rank TEXT NOT NULL, salary REAL);",
        "INSERT INTO soldiers_new SELECT * FROM soldiers;",
        "DROP TABLE soldiers;",
        "ALTER TABLE soldiers_new RENAME TO soldiers;",
        "SELECT sql FROM sqlite_master WHERE type='table' AND name='soldiers';"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L53.json",
        module_name="Module_06_Modifying_Data_Schema",
        lesson_name="L53_ALTER_TABLE_DROP_TABLE"
    )
