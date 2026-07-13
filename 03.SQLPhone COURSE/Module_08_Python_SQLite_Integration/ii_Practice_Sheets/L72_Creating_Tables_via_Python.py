import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🏗️  Create Table from Python – Imperial Arsenal\n\n"
        "Write Python code that connects to ':memory:',\n"
        "creates a table `weapons` with columns:\n"
        "  • id INTEGER PRIMARY KEY\n"
        "  • name TEXT NOT NULL\n"
        "  • power_level INTEGER\n\n"
        "Then insert one row:\n"
        "  (1, 'Laser', 5)\n"
        "Commit, SELECT all rows, and print the result.\n\n"
        "Expected output:\n[(1, 'Laser', 5)]"
    ),
    expected_output="[(1, 'Laser', 5)]",
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('CREATE TABLE weapons (id INTEGER PRIMARY KEY, name TEXT NOT NULL, power_level INTEGER)')",
        "conn.execute(\"INSERT INTO weapons VALUES (1, 'Laser', 5)\")",
        "conn.commit()",
        "cursor = conn.execute('SELECT * FROM weapons')",
        "print(cursor.fetchall())",
    ]
)

easy2 = Task(
    description=(
        "📋  Create Table with Constraints – Soldiers DB\n\n"
        "Write Python code that:\n"
        "  1. Connects to ':memory:'\n"
        "  2. Creates a table `soldiers` with columns:\n"
        "     • id INTEGER PRIMARY KEY\n"
        "     • name TEXT NOT NULL\n"
        "     • rank TEXT DEFAULT 'Private'\n"
        "     • salary REAL CHECK(salary > 0)\n"
        "  3. Inserts two rows:\n"
        "     (1, 'Emperor', 'General', 5000)\n"
        "     (2, 'Rahim', NULL, 3000)  ← uses DEFAULT for rank\n"
        "  4. Commits, then SELECTs all rows sorted by id.\n"
        "Print the result.\n\n"
        "Expected output:\n[(1, 'Emperor', 'General', 5000.0), (2, 'Rahim', 'Private', 3000.0)]"
    ),
    expected_output="[(1, 'Emperor', 'General', 5000.0), (2, 'Rahim', 'Private', 3000.0)]",
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('''CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT NOT NULL, rank TEXT DEFAULT \\'Private\\', salary REAL CHECK(salary > 0))''')",
        "conn.execute(\"INSERT INTO soldiers VALUES (1, 'Emperor', 'General', 5000)\")",
        "conn.execute(\"INSERT INTO soldiers (id, name, salary) VALUES (2, 'Rahim', 3000)\")",
        "conn.commit()",
        "cursor = conn.execute('SELECT * FROM soldiers ORDER BY id')",
        "print(cursor.fetchall())",
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🔍  Check Table Existence Before Creating\n\n"
        "Write Python code that:\n"
        "  1. Connects to ':memory:'\n"
        "  2. Creates a table `regiments` if it doesn't exist\n"
        "     (use CREATE TABLE IF NOT EXISTS)\n"
        "  3. Queries sqlite_master to confirm the table exists\n"
        "  4. Prints only the table name.\n\n"
        "Expected output:\n[('regiments',)]"
    ),
    expected_output="[('regiments',)]",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('CREATE TABLE IF NOT EXISTS regiments (id INTEGER PRIMARY KEY, name TEXT)')",
        "cursor = conn.execute(\"SELECT name FROM sqlite_master WHERE type='table' AND name='regiments'\")",
        "print(cursor.fetchall())",
    ]
)

medium2 = Task(
    description=(
        "🔄  Safe Table Creation – Drop & Recreate\n\n"
        "Write Python code that:\n"
        "  1. Connects to ':memory:'\n"
        "  2. Creates a table `temp_data` and inserts a row\n"
        "  3. Drops the table (DROP TABLE IF EXISTS)\n"
        "  4. Recreates the table with an additional column\n"
        "  5. Inserts a new row that uses the new column\n"
        "  6. SELECTs all rows and prints the result.\n\n"
        "Expected output:\n[(1, 'Test', 'Extra')]"
    ),
    expected_output="[(1, 'Test', 'Extra')]",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('CREATE TABLE temp_data (id INTEGER PRIMARY KEY, value TEXT)')",
        "conn.execute(\"INSERT INTO temp_data VALUES (1, 'Old')\")",
        "conn.commit()",
        "conn.execute('DROP TABLE IF EXISTS temp_data')",
        "conn.execute('CREATE TABLE temp_data (id INTEGER PRIMARY KEY, value TEXT, extra TEXT)')",
        "conn.execute(\"INSERT INTO temp_data VALUES (1, 'Test', 'Extra')\")",
        "conn.commit()",
        "cursor = conn.execute('SELECT * FROM temp_data')",
        "print(cursor.fetchall())",
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  Dynamic Table Creation – From a Dictionary\n\n"
        "Write a Python function `create_table_from_dict(conn, table_name, columns)`\n"
        "that takes a connection, a table name, and a dictionary\n"
        "of column definitions (e.g., {'id': 'INTEGER PRIMARY KEY', 'name': 'TEXT NOT NULL'}).\n"
        "The function should build the CREATE TABLE statement and execute it.\n"
        "Then use it to create a table `inventory` with columns:\n"
        "  • item_id INTEGER PRIMARY KEY\n"
        "  • item_name TEXT NOT NULL\n"
        "  • quantity INTEGER CHECK(quantity >= 0)\n"
        "Insert one row, SELECT, and print the result.\n\n"
        "Expected output:\n[(1, 'Sword', 10)]"
    ),
    expected_output="[(1, 'Sword', 10)]",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3",
        "def create_table_from_dict(conn, table_name, columns):",
        "    col_defs = ', '.join(f'{name} {dtype}' for name, dtype in columns.items())",
        "    conn.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({col_defs})')",
        "conn = sqlite3.connect(':memory:')",
        "create_table_from_dict(conn, 'inventory', {'item_id': 'INTEGER PRIMARY KEY', 'item_name': 'TEXT NOT NULL', 'quantity': 'INTEGER CHECK(quantity >= 0)'})",
        "conn.execute(\"INSERT INTO inventory VALUES (1, 'Sword', 10)\")",
        "conn.commit()",
        "cursor = conn.execute('SELECT * FROM inventory')",
        "print(cursor.fetchall())",
    ]
)

hard2 = Task(
    description=(
        "📊  Table Schema Comparison – sqlite_master\n\n"
        "Write Python code that:\n"
        "  1. Connects to ':memory:'\n"
        "  2. Creates two tables: `employees` and `departments`\n"
        "  3. Queries sqlite_master to retrieve the CREATE statement\n"
        "     for the `employees` table.\n"
        "  4. Prints the `sql` column.\n\n"
        "Expected output:\n[('CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT NOT NULL)',)]"
    ),
    expected_output="[('CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT NOT NULL)',)]",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT NOT NULL)')",
        "conn.execute('CREATE TABLE departments (id INTEGER PRIMARY KEY, name TEXT)')",
        "cursor = conn.execute(\"SELECT sql FROM sqlite_master WHERE type='table' AND name='employees'\")",
        "print(cursor.fetchall())",
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L72.json",
        module_name="Module_08_Python_SQLite_Integration",
        lesson_name="L72_Creating_Tables_via_Python"
    )