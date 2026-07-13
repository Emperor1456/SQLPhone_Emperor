import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🔍  fetchone() – Retrieve a Single Row\n\n"
        "The `soldiers` table already has 4 rows.\n"
        "Write Python code that:\n"
        "  1. Executes a SELECT to find the soldier with id = 2.\n"
        "  2. Uses fetchone() to get the single row.\n"
        "  3. Prints the row (as a tuple).\n\n"
        "Expected output:\n(2, 'Rahim', 'Colonel', 4000.0)"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000),(2,'Rahim','Colonel',4000),(3,'Ali','General',4500),(4,'Hasan','Private',3500);"
    ),
    expected_output="(2, 'Rahim', 'Colonel', 4000.0)",
    level=Level.EASY,
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('''CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, salary REAL)''')",
        "conn.execute(\"INSERT INTO soldiers VALUES (1,'Emperor','General',5000),(2,'Rahim','Colonel',4000),(3,'Ali','General',4500),(4,'Hasan','Private',3500)\")",
        "cursor = conn.execute('SELECT * FROM soldiers WHERE id = 2')",
        "row = cursor.fetchone()",
        "print(row)",
    ]
)

easy2 = Task(
    description=(
        "📊  fetchall() – Retrieve All Rows\n\n"
        "The `soldiers` table has 4 rows.\n"
        "Write Python code that:\n"
        "  1. Executes a SELECT * FROM soldiers ORDER BY id.\n"
        "  2. Uses fetchall() to get all rows as a list.\n"
        "  3. Prints the list.\n\n"
        "Expected output:\n[(1, 'Emperor', 'General', 5000.0), (2, 'Rahim', 'Colonel', 4000.0), (3, 'Ali', 'General', 4500.0), (4, 'Hasan', 'Private', 3500.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000),(2,'Rahim','Colonel',4000),(3,'Ali','General',4500),(4,'Hasan','Private',3500);"
    ),
    expected_output="[(1, 'Emperor', 'General', 5000.0), (2, 'Rahim', 'Colonel', 4000.0), (3, 'Ali', 'General', 4500.0), (4, 'Hasan', 'Private', 3500.0)]",
    level=Level.EASY,
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('''CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, salary REAL)''')",
        "conn.execute(\"INSERT INTO soldiers VALUES (1,'Emperor','General',5000),(2,'Rahim','Colonel',4000),(3,'Ali','General',4500),(4,'Hasan','Private',3500)\")",
        "cursor = conn.execute('SELECT * FROM soldiers ORDER BY id')",
        "rows = cursor.fetchall()",
        "print(rows)",
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "📦  fetchmany(size) – Retrieve in Batches\n\n"
        "The `soldiers` table has 4 rows.\n"
        "Write Python code that:\n"
        "  1. Executes a SELECT * FROM soldiers ORDER BY id.\n"
        "  2. Uses fetchmany(2) to get the first 2 rows.\n"
        "  3. Prints those 2 rows.\n"
        "  4. Calls fetchmany(2) again to get the next 2 rows.\n"
        "  5. Prints those 2 rows.\n\n"
        "Expected output:\n[(1, 'Emperor', 'General', 5000.0), (2, 'Rahim', 'Colonel', 4000.0)]\n[(3, 'Ali', 'General', 4500.0), (4, 'Hasan', 'Private', 3500.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000),(2,'Rahim','Colonel',4000),(3,'Ali','General',4500),(4,'Hasan','Private',3500);"
    ),
    expected_output="[(1, 'Emperor', 'General', 5000.0), (2, 'Rahim', 'Colonel', 4000.0)]\n[(3, 'Ali', 'General', 4500.0), (4, 'Hasan', 'Private', 3500.0)]",
    level=Level.MEDIUM,
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('''CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, salary REAL)''')",
        "conn.execute(\"INSERT INTO soldiers VALUES (1,'Emperor','General',5000),(2,'Rahim','Colonel',4000),(3,'Ali','General',4500),(4,'Hasan','Private',3500)\")",
        "cursor = conn.execute('SELECT * FROM soldiers ORDER BY id')",
        "batch1 = cursor.fetchmany(2)",
        "print(batch1)",
        "batch2 = cursor.fetchmany(2)",
        "print(batch2)",
    ]
)

medium2 = Task(
    description=(
        "🔄  Loop with fetchmany() – Process in Chunks\n\n"
        "The `soldiers` table has 4 rows.\n"
        "Write Python code that:\n"
        "  1. Executes a SELECT * FROM soldiers ORDER BY id.\n"
        "  2. Uses a while loop that calls fetchmany(3)\n"
        "     repeatedly until an empty list is returned.\n"
        "  3. Prints each batch as a list.\n\n"
        "Expected output:\n[(1, 'Emperor', 'General', 5000.0), (2, 'Rahim', 'Colonel', 4000.0), (3, 'Ali', 'General', 4500.0)]\n[(4, 'Hasan', 'Private', 3500.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000),(2,'Rahim','Colonel',4000),(3,'Ali','General',4500),(4,'Hasan','Private',3500);"
    ),
    expected_output="[(1, 'Emperor', 'General', 5000.0), (2, 'Rahim', 'Colonel', 4000.0), (3, 'Ali', 'General', 4500.0)]\n[(4, 'Hasan', 'Private', 3500.0)]",
    level=Level.MEDIUM,
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('''CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, salary REAL)''')",
        "conn.execute(\"INSERT INTO soldiers VALUES (1,'Emperor','General',5000),(2,'Rahim','Colonel',4000),(3,'Ali','General',4500),(4,'Hasan','Private',3500)\")",
        "cursor = conn.execute('SELECT * FROM soldiers ORDER BY id')",
        "while True:",
        "    batch = cursor.fetchmany(3)",
        "    if not batch:",
        "        break",
        "    print(batch)",
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  Row Factory – Dict‑Like Access\n\n"
        "Connect to ':memory:', set row_factory = sqlite3.Row.\n"
        "Create the `soldiers` table and insert the same 4 rows.\n"
        "Execute a SELECT for soldier with id = 1, use fetchone(),\n"
        "and print the soldier's name using row['name'].\n\n"
        "Expected output:\nEmperor"
    ),
    expected_output="Emperor",
    level=Level.HARD,
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.row_factory = sqlite3.Row",
        "conn.execute('''CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, salary REAL)''')",
        "conn.execute(\"INSERT INTO soldiers VALUES (1,'Emperor','General',5000),(2,'Rahim','Colonel',4000),(3,'Ali','General',4500),(4,'Hasan','Private',3500)\")",
        "cursor = conn.execute('SELECT * FROM soldiers WHERE id = 1')",
        "row = cursor.fetchone()",
        "print(row['name'])",
    ]
)

hard2 = Task(
    description=(
        "📊  Pagination – fetchmany() with OFFSET\n\n"
        "The `soldiers` table has 4 rows.\n"
        "Write a Python function `paginate(page_size, page_number)`\n"
        "that takes a page size and page number (1‑indexed),\n"
        "and returns the rows for that page using LIMIT/OFFSET.\n"
        "Use fetchall() to retrieve the page rows.\n"
        "Call paginate(2, 2) to get the second page\n"
        "(rows 3‑4) and print the result.\n\n"
        "Expected output:\n[(3, 'Ali', 'General', 4500.0), (4, 'Hasan', 'Private', 3500.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000),(2,'Rahim','Colonel',4000),(3,'Ali','General',4500),(4,'Hasan','Private',3500);"
    ),
    expected_output="[(3, 'Ali', 'General', 4500.0), (4, 'Hasan', 'Private', 3500.0)]",
    level=Level.HARD,
    hints=[
        "import sqlite3",
        "def paginate(page_size, page_number):",
        "    conn = sqlite3.connect(':memory:')",
        "    conn.row_factory = sqlite3.Row",
        "    conn.execute('''CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, salary REAL)''')",
        "    conn.execute(\"INSERT INTO soldiers VALUES (1,'Emperor','General',5000),(2,'Rahim','Colonel',4000),(3,'Ali','General',4500),(4,'Hasan','Private',3500)\")",
        "    offset = (page_number - 1) * page_size",
        "    cursor = conn.execute('SELECT * FROM soldiers ORDER BY id LIMIT ? OFFSET ?', (page_size, offset))",
        "    return cursor.fetchall()",
        "print(paginate(2, 2))",
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L74.json",
        module_name="Module_08_Python_SQLite_Integration",
        lesson_name="L74_fetchone_fetchall_fetchmany"
    )
