import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🔍  Trace the Engine – Verify a Query\n\n"
        "A simplified engine connects to :memory:,\n"
        "creates a table `test` with one row (1, 'Emperor'),\n"
        "runs a hardcoded query `SELECT * FROM test`,\n"
        "and compares the result.\n\n"
        "Write the Python code that does this and prints\n"
        "✅ Correct! if the output matches `[(1, 'Emperor')]`.\n\n"
        "Expected output:\n✅ Correct!"
    ),
    expected_output="✅ Correct!",
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('CREATE TABLE test (id INTEGER, name TEXT)')",
        "conn.execute(\"INSERT INTO test VALUES (1, 'Emperor')\")",
        "cur = conn.execute('SELECT * FROM test')",
        "if cur.fetchall() == [(1, 'Emperor')]:",
        "    print('✅ Correct!')",
    ]
)

easy2 = Task(
    description=(
        "🧪  Basic Engine – Run setup_sql & Print Output\n\n"
        "The engine receives a `setup_sql` string that\n"
        "creates a table `heroes` (id, name) and inserts\n"
        "(1, 'Emperor'). Write code that:\n"
        "  1. Executes that setup.\n"
        "  2. Executes `SELECT * FROM heroes`.\n"
        "  3. Prints the fetched rows.\n\n"
        "Expected output:\n[(1, 'Emperor')]"
    ),
    setup_sql=(
        "CREATE TABLE heroes (id INTEGER, name TEXT);"
        "INSERT INTO heroes VALUES (1, 'Emperor');"
    ),
    expected_output="[(1, 'Emperor')]",
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.executescript('''CREATE TABLE heroes (id INTEGER, name TEXT);''')",
        "conn.executescript('''INSERT INTO heroes VALUES (1, 'Emperor');''')",
        "cur = conn.execute('SELECT * FROM heroes')",
        "print(cur.fetchall())",
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "➕  Add a Task Definition\n\n"
        "Create a `Task` object (import Task, Level from\n"
        "practice_engine) with these attributes:\n"
        "  description = 'Create table soldiers'\n"
        "  setup_sql = 'CREATE TABLE soldiers (id, name);'\n"
        "  expected_output = \"[(1, 'Emperor')]\"\n"
        "  level = Level.EASY\n"
        "  hints = ['Use CREATE TABLE',\n"
        "           'INSERT INTO soldiers VALUES (1,\"Emperor\");',\n"
        "           'SELECT * FROM soldiers']\n"
        "Print the task's description attribute.\n\n"
        "Expected output:\nCreate table soldiers"
    ),
    expected_output="Create table soldiers",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "from practice_engine import Task, Level",
        "task = Task(description='Create table soldiers',",
        "            setup_sql='CREATE TABLE soldiers (id INTEGER, name TEXT);',",
        "            expected_output=\"[(1, 'Emperor')]\",",
        "            level=Level.EASY,",
        "            hints=['Use CREATE TABLE',",
        "                   \"INSERT INTO soldiers VALUES (1,'Emperor');\",",
        "                   'SELECT * FROM soldiers'])",
        "print(task.description)",
    ]
)

medium2 = Task(
    description=(
        "🔄  Verify Against a Task's expected_output\n\n"
        "Given a Task `t` with:\n"
        "  setup_sql = 'CREATE TABLE weapons (id, name);\n"
        "               INSERT INTO weapons VALUES (1,\"Laser\");'\n"
        "  expected_output = \"[(1, 'Laser')]\"\n\n"
        "Write code that:\n"
        "  1. Executes t.setup_sql.\n"
        "  2. Runs a query to match the expected_output.\n"
        "  3. Prints ✅ Correct! if they match,\n"
        "     else prints ❌ Mismatch.\n\n"
        "Expected output:\n✅ Correct!"
    ),
    expected_output="✅ Correct!",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "t = Task(",
        "    description='',",
        "    setup_sql=\"CREATE TABLE weapons (id INTEGER, name TEXT); INSERT INTO weapons VALUES (1,'Laser');\",",
        "    expected_output=\"[(1, 'Laser')]\",",
        "    level=Level.EASY,",
        "    hints=[]",
        ")",
        "conn = sqlite3.connect(':memory:')",
        "conn.executescript(t.setup_sql)",
        "cur = conn.execute('SELECT * FROM weapons')",
        "if str(cur.fetchall()) == t.expected_output:",
        "    print('✅ Correct!')",
        "else:",
        "    print('❌ Mismatch')",
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧩  Build a Mini Engine for a JOIN Challenge\n\n"
        "Design a mini practice engine that:\n"
        "  1. Connects to :memory:\n"
        "  2. Runs a hardcoded setup_sql creating\n"
        "     `regiments` (id, name) and `soldiers`\n"
        "     (id, name, regiment_id) with 2 soldiers in\n"
        "     regiment 1 ('Red').\n"
        "  3. Executes a JOIN query:\n"
        "     SELECT s.id, s.name, r.name FROM soldiers s\n"
        "     JOIN regiments r ON s.regiment_id = r.id\n"
        "     ORDER BY s.id\n"
        "  4. Compares output to\n"
        "     [(1,'Emperor','Red'),(2,'Rahim','Red')]\n"
        "  5. Prints ✅ Correct! if matches.\n\n"
        "Expected output:\n✅ Correct!"
    ),
    expected_output="✅ Correct!",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3; conn = sqlite3.connect(':memory:')",
        "setup = '''",
        "CREATE TABLE regiments (id INTEGER, name TEXT);",
        "INSERT INTO regiments VALUES (1,'Red');",
        "CREATE TABLE soldiers (id INTEGER, name TEXT, regiment_id INTEGER);",
        "INSERT INTO soldiers VALUES (1,'Emperor',1),(2,'Rahim',1);",
        "'''",
        "conn.executescript(setup)",
        "cur = conn.execute('SELECT s.id, s.name, r.name FROM soldiers s JOIN regiments r ON s.regiment_id = r.id ORDER BY s.id')",
        "if cur.fetchall() == [(1,'Emperor','Red'),(2,'Rahim','Red')]:",
        "    print('✅ Correct!')",
    ]
)

hard2 = Task(
    description=(
        "📦  Generate a Practice Sheet Structure\n\n"
        "Write a Python program that prints the first three\n"
        "lines of a valid practice sheet file (like L78):\n"
        "  1. import sys, os\n"
        "  2. sys.path.append(\"../..\")\n"
        "  3. from practice_engine import Task, Level, run_sequence\n\n"
        "Expected output (exactly these three lines):\n"
        "import sys, os\nsys.path.append(\"../..\")\nfrom practice_engine import Task, Level, run_sequence"
    ),
    expected_output="import sys, os\nsys.path.append(\"../..\")\nfrom practice_engine import Task, Level, run_sequence",
    level=Level.HARD,
    mode="python",
    hints=[
        "Use print() for each line.",
        "print('import sys, os')",
        "print('sys.path.append(\"../..\")')",
        "print('from practice_engine import Task, Level, run_sequence')",
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L79.json",
        module_name="Module_08_Python_SQLite_Integration",
        lesson_name="L79_Interactive_Practice_Coach_Engine"
    )