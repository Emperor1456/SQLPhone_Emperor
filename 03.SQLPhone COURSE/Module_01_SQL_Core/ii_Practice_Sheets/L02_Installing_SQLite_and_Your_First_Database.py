import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "📦  Your First Table – Arsenal Test\n\n"
        "Create a table named `test` with a single\n"
        "column `id` of type INTEGER.\n\n"
        "Then insert one row with the value 42.\n"
        "Finally, SELECT all rows to confirm.\n\n"
        "Expected output: [(42,)]"
    ),
    expected_output="[(42,)]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE test (id INTEGER);",
        "INSERT INTO test VALUES (42);",
        "SELECT * FROM test;"
    ]
)

easy2 = Task(
    description=(
        "🔍  Inspect the Schema – sqlite_master\n\n"
        "After creating the `test` table, query the\n"
        "sqlite_master table to display the CREATE\n"
        "statement that was used.\n\n"
        "Use `SELECT sql FROM sqlite_master WHERE name='test';`\n\n"
        "Expected output: [('CREATE TABLE test (id INTEGER)',)]"
    ),
    setup_sql="CREATE TABLE test (id INTEGER);",
    expected_output="[('CREATE TABLE test (id INTEGER)',)]",
    level=Level.EASY,
    hints=[
        "SELECT sql FROM sqlite_master WHERE type='table' AND name='test';"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "📋  Multi‑row Insert – Weapon Log\n\n"
        "Create a table `arsenal` with columns\n"
        "`weapon_id` INTEGER and `weapon_name` TEXT.\n"
        "Insert three rows in a single statement:\n"
        "  (1, 'Laser'), (2, 'Plasma'), (3, 'Railgun').\n"
        "Then SELECT all rows sorted by weapon_id.\n\n"
        "Expected output:\n[(1, 'Laser'), (2, 'Plasma'), (3, 'Railgun')]"
    ),
    expected_output="[(1, 'Laser'), (2, 'Plasma'), (3, 'Railgun')]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE arsenal (weapon_id INTEGER, weapon_name TEXT);",
        "INSERT INTO arsenal VALUES (1,'Laser'), (2,'Plasma'), (3,'Railgun');",
        "SELECT * FROM arsenal ORDER BY weapon_id;"
    ]
)

medium2 = Task(
    description=(
        "🛠️  Schema Inspection – List All Tables\n\n"
        "The database has several tables.\n"
        "Query sqlite_master to list the names of all\n"
        "user‑created tables (type='table').\n"
        "Sort them alphabetically.\n\n"
        "Expected output: [('arsenal',), ('test',)]"
    ),
    setup_sql=(
        "CREATE TABLE test (id INTEGER);"
        "CREATE TABLE arsenal (weapon_id INTEGER, weapon_name TEXT);"
    ),
    expected_output="[('arsenal',), ('test',)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🏭  Build a Full Arsenal – Table & Data\n\n"
        "Create a table `inventory` with columns:\n"
        "  • item_id INTEGER\n"
        "  • item_name TEXT\n"
        "  • quantity INTEGER\n\n"
        "Insert three rows:\n"
        "  (1, 'Shield', 10)\n"
        "  (2, 'Sword', 25)\n"
        "  (3, 'Bow', 15)\n\n"
        "Then SELECT item_name and quantity for items\n"
        "where quantity > 10, sorted by quantity descending.\n\n"
        "Expected output:\n[('Sword', 25), ('Bow', 15)]"
    ),
    expected_output="[('Sword', 25), ('Bow', 15)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE inventory (item_id INTEGER, item_name TEXT, quantity INTEGER);",
        "INSERT INTO inventory VALUES (1,'Shield',10), (2,'Sword',25), (3,'Bow',15);",
        "SELECT item_name, quantity FROM inventory WHERE quantity > 10 ORDER BY quantity DESC;"
    ]
)

hard2 = Task(
    description=(
        "📊  Table Size Check – Count Rows\n\n"
        "The `inventory` table from the previous task\n"
        "has three rows. Write a query that returns the\n"
        "total number of rows in the table.\n\n"
        "Expected output: [(3,)]"
    ),
    setup_sql=(
        "CREATE TABLE inventory (item_id INTEGER, item_name TEXT, quantity INTEGER);"
        "INSERT INTO inventory VALUES (1,'Shield',10), (2,'Sword',25), (3,'Bow',15);"
    ),
    expected_output="[(3,)]",
    level=Level.HARD,
    hints=[
        "SELECT COUNT(*) FROM inventory;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L02.json",
        module_name="Module_01_SQL_Core",
        lesson_name="L02_Installing_SQLite"
    )
