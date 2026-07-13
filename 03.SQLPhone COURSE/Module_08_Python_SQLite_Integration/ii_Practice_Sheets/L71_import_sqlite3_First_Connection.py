import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🔗  First Connection – sqlite3.connect()\n\n"
        "Import the sqlite3 module and connect to an\n"
        "in‑memory database (':memory:').\n"
        "Create a cursor, execute a query that returns\n"
        "the SQLite version, fetch the result, and print it.\n\n"
        "Expected output:\n[(sqlite_version_string,)]"
    ),
    expected_output=None,  # dynamic version string
    level=Level.EASY,
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.cursor()",
        "cursor.execute('SELECT sqlite_version()')",
        "print(cursor.fetchone())",
    ],
    verify_func=lambda conn: (
        conn.execute("SELECT 1").fetchone() is not None
    )
)

easy2 = Task(
    description=(
        "📦  Create Table & Insert – In‑Memory DB\n\n"
        "Connect to ':memory:', create a table `test`\n"
        "with a single column `value TEXT`.\n"
        "Insert the row ('Emperor'), then SELECT all rows.\n"
        "Fetch and print the result.\n\n"
        "Expected output:\n[('Emperor',)]"
    ),
    expected_output="[('Emperor',)]",
    level=Level.EASY,
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.cursor()",
        "cursor.execute('CREATE TABLE test (value TEXT)')",
        "cursor.execute(\"INSERT INTO test VALUES ('Emperor')\")",
        "conn.commit()",
        "cursor.execute('SELECT * FROM test')",
        "print(cursor.fetchall())",
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🔍  Check Table Existence – sqlite_master\n\n"
        "Connect to ':memory:'. Create a table `soldiers`.\n"
        "Then write a SELECT against `sqlite_master` to\n"
        "verify that the table exists.\n"
        "Return the table name.\n\n"
        "Expected output:\n[('soldiers',)]"
    ),
    expected_output="[('soldiers',)]",
    level=Level.MEDIUM,
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('CREATE TABLE soldiers (id INTEGER)')",
        "cursor = conn.cursor()",
        "cursor.execute(\"SELECT name FROM sqlite_master WHERE type='table' AND name='soldiers'\")",
        "print(cursor.fetchall())",
    ]
)

medium2 = Task(
    description=(
        "🔄  Context Manager – Auto‑Close Connection\n\n"
        "Use the connection as a context manager (`with`)\n"
        "to ensure the connection is closed automatically.\n"
        "Inside the `with` block, create a table `weapons`,\n"
        "insert one row, and SELECT it.\n"
        "Print the result.\n\n"
        "Expected output:\n[('Laser',)]"
    ),
    expected_output="[('Laser',)]",
    level=Level.MEDIUM,
    hints=[
        "import sqlite3",
        "with sqlite3.connect(':memory:') as conn:",
        "    conn.execute('CREATE TABLE weapons (name TEXT)')",
        "    conn.execute(\"INSERT INTO weapons VALUES ('Laser')\")",
        "    conn.commit()",
        "    cursor = conn.execute('SELECT * FROM weapons')",
        "    print(cursor.fetchall())",
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  Connection Helper Function – Reusable\n\n"
        "Define a function `get_connection(path=':memory:')`\n"
        "that returns a connection with `row_factory`\n"
        "set to `sqlite3.Row` (enables dict‑like access).\n"
        "Use the function to connect, create a table `heroes`\n"
        "(id INTEGER PRIMARY KEY, name TEXT).\n"
        "Insert ('Emperor'), commit, SELECT, and print the\n"
        "result using row['name'].\n\n"
        "Expected output:\nEmperor"
    ),
    expected_output="Emperor",
    level=Level.HARD,
    hints=[
        "import sqlite3",
        "def get_connection(path=':memory:'):",
        "    conn = sqlite3.connect(path)",
        "    conn.row_factory = sqlite3.Row",
        "    return conn",
        "conn = get_connection()",
        "conn.execute('CREATE TABLE heroes (id INTEGER PRIMARY KEY, name TEXT)')",
        "conn.execute(\"INSERT INTO heroes (name) VALUES ('Emperor')\")",
        "conn.commit()",
        "row = conn.execute('SELECT * FROM heroes').fetchone()",
        "print(row['name'])",
    ]
)

hard2 = Task(
    description=(
        "📊  Count Tables in a Database – sqlite_master\n\n"
        "Connect to ':memory:'. Create three tables:\n"
        "  • `alpha` (id INTEGER)\n"
        "  • `beta` (id INTEGER)\n"
        "  • `gamma` (id INTEGER)\n\n"
        "Write a query that returns the total number\n"
        "of user‑created tables.\n\n"
        "Expected output:\n[(3,)]"
    ),
    expected_output="[(3,)]",
    level=Level.HARD,
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('CREATE TABLE alpha (id INTEGER)')",
        "conn.execute('CREATE TABLE beta (id INTEGER)')",
        "conn.execute('CREATE TABLE gamma (id INTEGER)')",
        "cursor = conn.execute(\"SELECT COUNT(*) FROM sqlite_master WHERE type='table'\")",
        "print(cursor.fetchall())",
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L71.json",
        module_name="Module_08_Python_SQLite_Integration",
        lesson_name="L71_import_sqlite3_First_Connection"
    )
