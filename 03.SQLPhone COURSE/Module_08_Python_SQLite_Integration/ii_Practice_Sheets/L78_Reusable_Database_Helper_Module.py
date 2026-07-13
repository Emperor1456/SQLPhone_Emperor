import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🧰  Connection Factory – get_connection()\n\n"
        "Write a Python function `get_connection(path=':memory:')`\n"
        "that returns a connection with:\n"
        "  • row_factory = sqlite3.Row\n"
        "  • PRAGMA foreign_keys = ON\n\n"
        "Use it to connect, create a table `test` (id INTEGER),\n"
        "insert (42), SELECT *, and print the result.\n\n"
        "Expected output:\n[(42,)]"
    ),
    expected_output="[(42,)]",
    level=Level.EASY,
    hints=[
        "import sqlite3",
        "def get_connection(path=':memory:'):",
        "    conn = sqlite3.connect(path)",
        "    conn.row_factory = sqlite3.Row",
        "    conn.execute('PRAGMA foreign_keys = ON')",
        "    return conn",
        "conn = get_connection()",
        "conn.execute('CREATE TABLE test (id INTEGER)')",
        "conn.execute('INSERT INTO test VALUES (42)')",
        "conn.commit()",
        "cursor = conn.execute('SELECT * FROM test')",
        "print(cursor.fetchall())",
    ]
)

easy2 = Task(
    description=(
        "📦  Context Manager – with connect()\n\n"
        "Write a Python context manager `connect()` using\n"
        "`contextmanager` from `contextlib` that:\n"
        "  • Yields a connection from `get_connection()`\n"
        "  • Commits on success\n"
        "  • Rolls back on exception\n"
        "  • Closes in finally\n\n"
        "Use it to create a table `heroes` (id, name),\n"
        "insert ('Emperor'), and SELECT *. Print the result.\n\n"
        "Expected output:\n[(1, 'Emperor')]"
    ),
    expected_output="[(1, 'Emperor')]",
    level=Level.EASY,
    hints=[
        "import sqlite3",
        "from contextlib import contextmanager",
        "def get_connection(path=':memory:'):",
        "    conn = sqlite3.connect(path)",
        "    conn.row_factory = sqlite3.Row",
        "    conn.execute('PRAGMA foreign_keys = ON')",
        "    return conn",
        "@contextmanager",
        "def connect(path=':memory:'):",
        "    conn = get_connection(path)",
        "    try:",
        "        yield conn",
        "        conn.commit()",
        "    except:",
        "        conn.rollback()",
        "        raise",
        "    finally:",
        "        conn.close()",
        "with connect() as conn:",
        "    conn.execute('CREATE TABLE heroes (id INTEGER PRIMARY KEY, name TEXT)')",
        "    conn.execute(\"INSERT INTO heroes (name) VALUES ('Emperor')\")",
        "    cursor = conn.execute('SELECT * FROM heroes')",
        "    print(cursor.fetchall())",
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🔍  Helper Functions – fetch_all() & execute()\n\n"
        "Add two functions to your `db.py` module:\n"
        "  • fetch_all(conn, sql, params) → returns list of dicts\n"
        "  • execute(conn, sql, params) → returns rowcount\n\n"
        "Use them to:\n"
        "  1. Create table `soldiers` (id, name, rank)\n"
        "  2. Insert two soldiers\n"
        "  3. fetch_all() to get all rows, print them\n"
        "  4. execute() an UPDATE, print rowcount.\n\n"
        "Expected output:\n[(1, 'Emperor', 'General'), (2, 'Rahim', 'Colonel')]\n1"
    ),
    expected_output="[(1, 'Emperor', 'General'), (2, 'Rahim', 'Colonel')]\n1",
    level=Level.MEDIUM,
    hints=[
        "import sqlite3",
        "def get_connection():",
        "    conn = sqlite3.connect(':memory:')",
        "    conn.row_factory = sqlite3.Row",
        "    return conn",
        "def fetch_all(conn, sql, params=()):",
        "    return [dict(row) for row in conn.execute(sql, params).fetchall()]",
        "def execute(conn, sql, params=()):",
        "    return conn.execute(sql, params).rowcount",
        "conn = get_connection()",
        "conn.execute('CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT)')",
        "conn.execute(\"INSERT INTO soldiers (name, rank) VALUES ('Emperor','General'),('Rahim','Colonel')\")",
        "conn.commit()",
        "print(fetch_all(conn, 'SELECT * FROM soldiers ORDER BY id'))",
        "rc = execute(conn, 'UPDATE soldiers SET rank = ? WHERE name = ?', ('General', 'Rahim'))",
        "print(rc)",
    ]
)

medium2 = Task(
    description=(
        "🔄  Execute .sql File – Script Runner\n\n"
        "Write a function `execute_sql_file(conn, filepath)`\n"
        "that reads a SQL file and executes it with\n"
        "`executescript()`. Simulate the file content with\n"
        "a multi‑line string (no actual file I/O).\n"
        "The script should:\n"
        "  • CREATE TABLE weapons (id, name)\n"
        "  • INSERT INTO weapons VALUES (1,'Laser')\n"
        "After execution, SELECT * and print.\n\n"
        "Expected output:\n[(1, 'Laser')]"
    ),
    expected_output="[(1, 'Laser')]",
    level=Level.MEDIUM,
    hints=[
        "import sqlite3",
        "def execute_sql_file(conn, sql_text):",
        "    conn.executescript(sql_text)",
        "    conn.commit()",
        "conn = sqlite3.connect(':memory:')",
        "sql = '''",
        "CREATE TABLE weapons (id INTEGER, name TEXT);",
        "INSERT INTO weapons VALUES (1, 'Laser');",
        "'''",
        "execute_sql_file(conn, sql)",
        "cursor = conn.execute('SELECT * FROM weapons')",
        "print(cursor.fetchall())",
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  Full DB Helper Module – db.py\n\n"
        "Build a complete `db.py` module with:\n"
        "  1. get_connection(path=':memory:') – with row_factory\n"
        "     and PRAGMA foreign_keys = ON\n"
        "  2. connect() – context manager with commit/rollback/close\n"
        "  3. fetch_all(conn, sql, params) → list of dicts\n"
        "  4. execute(conn, sql, params) → rowcount\n"
        "  5. execute_script(conn, sql_text) – executescript wrapper\n\n"
        "Use it to:\n"
        "  • Create `regiments` (id, name) and `soldiers`\n"
        "    (id, name, regiment_id REFERENCES regiments)\n"
        "  • Insert 2 regiments, 3 soldiers\n"
        "  • Fetch all soldiers with their regiment name (JOIN)\n"
        "  • Print the result.\n\n"
        "Expected output:\n[{'name': 'Emperor', 'regiment_name': 'Imperial Guard'}, {'name': 'Rahim', 'regiment_name': 'Red Guard'}, {'name': 'Ali', 'regiment_name': 'Red Guard'}]"
    ),
    expected_output="[{'name': 'Emperor', 'regiment_name': 'Imperial Guard'}, {'name': 'Rahim', 'regiment_name': 'Red Guard'}, {'name': 'Ali', 'regiment_name': 'Red Guard'}]",
    level=Level.HARD,
    hints=[
        "import sqlite3",
        "from contextlib import contextmanager",
        "def get_connection(path=':memory:'):",
        "    conn = sqlite3.connect(path)",
        "    conn.row_factory = sqlite3.Row",
        "    conn.execute('PRAGMA foreign_keys = ON')",
        "    return conn",
        "@contextmanager",
        "def connect(path=':memory:'):",
        "    conn = get_connection(path)",
        "    try:",
        "        yield conn",
        "        conn.commit()",
        "    except:",
        "        conn.rollback()",
        "        raise",
        "    finally:",
        "        conn.close()",
        "def fetch_all(conn, sql, params=()):",
        "    return [dict(row) for row in conn.execute(sql, params).fetchall()]",
        "def execute(conn, sql, params=()):",
        "    return conn.execute(sql, params).rowcount",
        "def execute_script(conn, sql_text):",
        "    conn.executescript(sql_text)",
        "    conn.commit()",
        "with connect() as conn:",
        "    execute_script(conn, '''",
        "        CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT);",
        "        INSERT INTO regiments VALUES (1,'Imperial Guard'),(2,'Red Guard');",
        "        CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER REFERENCES regiments);",
        "        INSERT INTO soldiers VALUES (1,'Emperor',1),(2,'Rahim',2),(3,'Ali',2);",
        "    ''')",
        "    rows = fetch_all(conn, '''",
        "        SELECT s.name, r.name AS regiment_name",
        "        FROM soldiers s JOIN regiments r ON s.regiment_id = r.id",
        "        ORDER BY s.id",
        "    ''')",
        "    print(rows)",
    ]
)

hard2 = Task(
    description=(
        "📊  Migration Helper – Schema Versioning\n\n"
        "Write a function `migrate(conn, migrations)` that takes\n"
        "a list of SQL strings and executes each one. If any\n"
        "migration fails, the entire batch should rollback.\n"
        "Use it to run a batch of 3 migrations:\n"
        "  1. CREATE TABLE v1 (a INTEGER)\n"
        "  2. INSERT INTO v1 VALUES (1)\n"
        "  3. CREATE TABLE v2 (b INTEGER)\n"
        "After success, SELECT COUNT(*) FROM v1 and v2,\n"
        "printing both counts.\n\n"
        "Expected output:\n[(1,)]\n[(1,)]"
    ),
    expected_output="[(1,)]\n[(1,)]",
    level=Level.HARD,
    hints=[
        "import sqlite3",
        "def migrate(conn, migrations):",
        "    try:",
        "        conn.execute('BEGIN')",
        "        for m in migrations:",
        "            conn.executescript(m)",
        "        conn.commit()",
        "    except:",
        "        conn.rollback()",
        "        raise",
        "conn = sqlite3.connect(':memory:')",
        "migrations = [",
        "    'CREATE TABLE v1 (a INTEGER);',",
        "    'INSERT INTO v1 VALUES (1);',",
        "    'CREATE TABLE v2 (b INTEGER); INSERT INTO v2 VALUES (2);',",
        "]",
        "migrate(conn, migrations)",
        "print(conn.execute('SELECT COUNT(*) FROM v1').fetchall())",
        "print(conn.execute('SELECT COUNT(*) FROM v2').fetchall())",
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L78.json",
        module_name="Module_08_Python_SQLite_Integration",
        lesson_name="L78_Reusable_Database_Helper_Module"
    )
