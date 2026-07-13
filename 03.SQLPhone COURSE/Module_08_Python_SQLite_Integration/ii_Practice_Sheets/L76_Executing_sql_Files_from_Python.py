import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "📄  Execute a Single SQL File\n\n"
        "Write Python code that:\n"
        "  1. Connects to ':memory:'\n"
        "  2. Reads a SQL string containing:\n"
        "     CREATE TABLE test (id INTEGER);\n"
        "     INSERT INTO test VALUES (42);\n"
        "  3. Executes the SQL using executescript()\n"
        "  4. SELECTs * FROM test and prints the result.\n\n"
        "Expected output:\n[(42,)]"
    ),
    expected_output="[(42,)]",
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "sql = 'CREATE TABLE test (id INTEGER); INSERT INTO test VALUES (42);'",
        "conn.executescript(sql)",
        "cursor = conn.execute('SELECT * FROM test')",
        "print(cursor.fetchall())",
    ]
)

easy2 = Task(
    description=(
        "📋  Execute a Script with Multiple Statements\n\n"
        "Write Python code that:\n"
        "  1. Connects to ':memory:'\n"
        "  2. Creates two tables: `alpha` (id), `beta` (id)\n"
        "     using a single executescript() call.\n"
        "  3. Inserts (1) into alpha and (2) into beta\n"
        "     using a second executescript().\n"
        "  4. SELECTs COUNT(*) FROM alpha and\n"
        "     COUNT(*) FROM beta, prints both counts.\n\n"
        "Expected output:\n[(1,)]\n[(1,)]"
    ),
    expected_output="[(1,)]\n[(1,)]",
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.executescript('''",
        "CREATE TABLE alpha (id INTEGER);",
        "CREATE TABLE beta (id INTEGER);",
        "''')",
        "conn.executescript('''",
        "INSERT INTO alpha VALUES (1);",
        "INSERT INTO beta VALUES (2);",
        "''')",
        "print(conn.execute('SELECT COUNT(*) FROM alpha').fetchall())",
        "print(conn.execute('SELECT COUNT(*) FROM beta').fetchall())",
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🔄  Read SQL from a File – Simulated\n\n"
        "Write Python code that:\n"
        "  1. Defines a multi‑line string `schema_sql` containing:\n"
        "     CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT);\n"
        "     INSERT INTO soldiers VALUES (1,'Emperor'),(2,'Rahim');\n"
        "  2. Connects to ':memory:'\n"
        "  3. Executes the string with executescript()\n"
        "  4. SELECTs all rows from soldiers and prints.\n\n"
        "Expected output:\n[(1, 'Emperor'), (2, 'Rahim')]"
    ),
    expected_output="[(1, 'Emperor'), (2, 'Rahim')]",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "import sqlite3",
        "schema_sql = '''",
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO soldiers VALUES (1,'Emperor'),(2,'Rahim');",
        "'''",
        "conn = sqlite3.connect(':memory:')",
        "conn.executescript(schema_sql)",
        "cursor = conn.execute('SELECT * FROM soldiers')",
        "print(cursor.fetchall())",
    ]
)

medium2 = Task(
    description=(
        "⚠️  Error Handling – Catch Script Failure\n\n"
        "Write Python code that:\n"
        "  1. Defines a string `bad_sql` with a syntax error:\n"
        "     'CREATE TABLEX broken (id INTEGER);'\n"
        "  2. Tries to execute it using executescript()\n"
        "  3. Catches the sqlite3.Error and prints 'Script failed'.\n"
        "  4. Then connects again, creates a correct table,\n"
        "     inserts a row, and prints the result.\n\n"
        "Expected output:\nScript failed\n[(42,)]"
    ),
    expected_output="Script failed\n[(42,)]",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "import sqlite3",
        "bad_sql = 'CREATE TABLEX broken (id INTEGER);'",
        "try:",
        "    conn = sqlite3.connect(':memory:')",
        "    conn.executescript(bad_sql)",
        "except sqlite3.Error:",
        "    print('Script failed')",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('CREATE TABLE ok (id INTEGER)')",
        "conn.execute('INSERT INTO ok VALUES (42)')",
        "conn.commit()",
        "print(conn.execute('SELECT * FROM ok').fetchall())",
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  Migration Runner – Execute Multiple Files\n\n"
        "Write a function `run_migrations(conn, scripts)`\n"
        "that takes a connection and a list of SQL strings,\n"
        "and executes each one in order.\n"
        "Then use it to:\n"
        "  1. Create table `v1` with column `a`\n"
        "  2. Insert row (1) into v1\n"
        "  3. Create table `v2` with column `b`\n"
        "  4. Insert row (2) into v2\n"
        "After running, SELECT * FROM v1 and * FROM v2,\n"
        "printing both results.\n\n"
        "Expected output:\n[(1,)]\n[(2,)]"
    ),
    expected_output="[(1,)]\n[(2,)]",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3",
        "def run_migrations(conn, scripts):",
        "    for script in scripts:",
        "        conn.executescript(script)",
        "conn = sqlite3.connect(':memory:')",
        "scripts = [",
        "    'CREATE TABLE v1 (a INTEGER); INSERT INTO v1 VALUES (1);',",
        "    'CREATE TABLE v2 (b INTEGER); INSERT INTO v2 VALUES (2);'",
        "]",
        "run_migrations(conn, scripts)",
        "print(conn.execute('SELECT * FROM v1').fetchall())",
        "print(conn.execute('SELECT * FROM v2').fetchall())",
    ]
)

hard2 = Task(
    description=(
        "📊  Seed Database from a Script – Full Workflow\n\n"
        "Write Python code that:\n"
        "  1. Defines a `seed_sql` string containing:\n"
        "     • CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price REAL);\n"
        "     • INSERT INTO products VALUES (1,'Laptop',999.99);\n"
        "     • INSERT INTO products VALUES (2,'Mouse',24.99);\n"
        "     • INSERT INTO products VALUES (3,'Keyboard',79.99);\n"
        "  2. Connects to ':memory:'\n"
        "  3. Executes the script\n"
        "  4. SELECTs all products and prints.\n"
        "  5. Then SELECTs the COUNT of products and prints.\n\n"
        "Expected output:\n[(1, 'Laptop', 999.99), (2, 'Mouse', 24.99), (3, 'Keyboard', 79.99)]\n[(3,)]"
    ),
    expected_output="[(1, 'Laptop', 999.99), (2, 'Mouse', 24.99), (3, 'Keyboard', 79.99)]\n[(3,)]",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3",
        "seed_sql = '''",
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price REAL);",
        "INSERT INTO products VALUES (1,'Laptop',999.99);",
        "INSERT INTO products VALUES (2,'Mouse',24.99);",
        "INSERT INTO products VALUES (3,'Keyboard',79.99);",
        "'''",
        "conn = sqlite3.connect(':memory:')",
        "conn.executescript(seed_sql)",
        "print(conn.execute('SELECT * FROM products').fetchall())",
        "print(conn.execute('SELECT COUNT(*) FROM products').fetchall())",
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L76.json",
        module_name="Module_08_Python_SQLite_Integration",
        lesson_name="L76_Executing_sql_Files_from_Python"
    )