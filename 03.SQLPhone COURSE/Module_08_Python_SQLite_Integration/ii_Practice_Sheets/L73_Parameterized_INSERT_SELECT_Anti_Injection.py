import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🔒  Parameterized INSERT – Safe Data Entry\n\n"
        "Write Python code that:\n"
        "  1. Connects to ':memory:'\n"
        "  2. Creates a table `agents` with columns:\n"
        "     • id INTEGER PRIMARY KEY\n"
        "     • code_name TEXT NOT NULL\n"
        "     • clearance_level INTEGER\n"
        "  3. Inserts one row using parameterized query\n"
        "     with ? placeholders.\n"
        "     Values: code_name='Emperor', clearance_level=5\n"
        "  4. Commits, then SELECTs and prints all rows.\n\n"
        "Expected output:\n[(1, 'Emperor', 5)]"
    ),
    expected_output="[(1, 'Emperor', 5)]",
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('CREATE TABLE agents (id INTEGER PRIMARY KEY, code_name TEXT NOT NULL, clearance_level INTEGER)')",
        "conn.execute('INSERT INTO agents (code_name, clearance_level) VALUES (?, ?)', ('Emperor', 5))",
        "conn.commit()",
        "cursor = conn.execute('SELECT * FROM agents')",
        "print(cursor.fetchall())",
    ]
)

easy2 = Task(
    description=(
        "🔍  Parameterized SELECT – Safe Lookup\n\n"
        "The `soldiers` table is already created and seeded\n"
        "with 4 rows.\n"
        "Write Python code that executes a parameterized\n"
        "SELECT query to find a soldier by name.\n"
        "Use a ? placeholder for the name 'Ali'.\n"
        "Print the fetched row.\n\n"
        "Expected output:\n[(3, 'Ali', 'General', 4500.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Ali','General',4500), (4,'Hasan','Private',3500);"
    ),
    expected_output="[(3, 'Ali', 'General', 4500.0)]",
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('''CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, salary REAL)''')",
        "conn.execute(\"INSERT INTO soldiers VALUES (1,'Emperor','General',5000),(2,'Rahim','Colonel',4000),(3,'Ali','General',4500),(4,'Hasan','Private',3500)\")",
        "cursor = conn.execute('SELECT * FROM soldiers WHERE name = ?', ('Ali',))",
        "print(cursor.fetchall())",
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🧪  Parameterized UPDATE – Safe Modification\n\n"
        "The `soldiers` table has 4 rows.\n"
        "Write Python code that uses a parameterized UPDATE\n"
        "to give a raise to a specific soldier by name.\n"
        "Increase Ali's salary by 500.\n"
        "Use two ? placeholders: one for the new salary,\n"
        "one for the name.\n"
        "Commit, then SELECT the updated row and print it.\n\n"
        "Expected output:\n[(3, 'Ali', 'General', 5000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Ali','General',4500), (4,'Hasan','Private',3500);"
    ),
    expected_output="[(3, 'Ali', 'General', 5000.0)]",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('''CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, salary REAL)''')",
        "conn.execute(\"INSERT INTO soldiers VALUES (1,'Emperor','General',5000),(2,'Rahim','Colonel',4000),(3,'Ali','General',4500),(4,'Hasan','Private',3500)\")",
        "conn.execute('UPDATE soldiers SET salary = ? WHERE name = ?', (5000.0, 'Ali'))",
        "conn.commit()",
        "cursor = conn.execute('SELECT * FROM soldiers WHERE name = ?', ('Ali',))",
        "print(cursor.fetchall())",
    ]
)

medium2 = Task(
    description=(
        "📊  Parameterized DELETE – Remove Safely\n\n"
        "The `soldiers` table has 4 rows.\n"
        "Write Python code that uses a parameterized DELETE\n"
        "to remove a soldier by their id.\n"
        "Delete the soldier with id = 4 (Hasan).\n"
        "Use a ? placeholder.\n"
        "Commit, then SELECT all remaining rows and print them.\n\n"
        "Expected output:\n[(1,'Emperor','General',5000.0), (2,'Rahim','Colonel',4000.0), (3,'Ali','General',4500.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Ali','General',4500), (4,'Hasan','Private',3500);"
    ),
    expected_output="[(1, 'Emperor', 'General', 5000.0), (2, 'Rahim', 'Colonel', 4000.0), (3, 'Ali', 'General', 4500.0)]",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('''CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, salary REAL)''')",
        "conn.execute(\"INSERT INTO soldiers VALUES (1,'Emperor','General',5000),(2,'Rahim','Colonel',4000),(3,'Ali','General',4500),(4,'Hasan','Private',3500)\")",
        "conn.execute('DELETE FROM soldiers WHERE id = ?', (4,))",
        "conn.commit()",
        "cursor = conn.execute('SELECT * FROM soldiers ORDER BY id')",
        "print(cursor.fetchall())",
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "⚠️  Unsafe vs Safe – Injection Demonstration\n\n"
        "Write Python code that shows the danger of SQL injection\n"
        "and the safety of parameterized queries.\n\n"
        "1. Create a table `users` with columns:\n"
        "   • id INTEGER PRIMARY KEY\n"
        "   • username TEXT\n"
        "   • password TEXT\n"
        "   Insert: (1, 'admin', 'secret'), (2, 'user', 'pass').\n\n"
        "2. Use an UNSAFE string‑formatted query with a malicious\n"
        "   input: username = \"admin' OR '1'='1\"\n"
        "   Show that this returns ALL rows (unsafe).\n\n"
        "3. Then use a PARAMETERIZED query with the SAME input.\n"
        "   Show that this returns ZERO rows (safe, correct).\n"
        "Print the result of the parameterized query.\n\n"
        "Expected output: []  (empty, because 'admin'' OR ''1''=''1' is not a real username)"
    ),
    expected_output="[]",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')",
        "conn.execute(\"INSERT INTO users VALUES (1,'admin','secret'), (2,'user','pass')\")",
        "conn.commit()",
        "# Unsafe: cursor = conn.execute(f\"SELECT * FROM users WHERE username = '{malicious}')\")",
        "# Safe: cursor = conn.execute('SELECT * FROM users WHERE username = ?', (malicious,))",
        "malicious = \"admin' OR '1'='1\"",
        "cursor = conn.execute('SELECT * FROM users WHERE username = ?', (malicious,))",
        "print(cursor.fetchall())",
    ]
)

hard2 = Task(
    description=(
        "📦  Bulk Parameterized INSERT – executemany()\n\n"
        "Write Python code that:\n"
        "  1. Connects to ':memory:'\n"
        "  2. Creates a table `recruits` with columns:\n"
        "     • id INTEGER PRIMARY KEY\n"
        "     • name TEXT NOT NULL\n"
        "     • regiment_id INTEGER\n"
        "  3. Uses `executemany()` to insert 3 rows at once\n"
        "     using parameterized placeholders.\n"
        "     Data: ('Emperor',1), ('Rahim',2), ('Karim',1)\n"
        "  4. Commits, then SELECTs all rows and prints them.\n\n"
        "Expected output:\n[(1,'Emperor',1), (2,'Rahim',2), (3,'Karim',1)]"
    ),
    expected_output="[(1, 'Emperor', 1), (2, 'Rahim', 2), (3, 'Karim', 1)]",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('CREATE TABLE recruits (id INTEGER PRIMARY KEY, name TEXT NOT NULL, regiment_id INTEGER)')",
        "data = [('Emperor', 1), ('Rahim', 2), ('Karim', 1)]",
        "conn.executemany('INSERT INTO recruits (name, regiment_id) VALUES (?, ?)', data)",
        "conn.commit()",
        "cursor = conn.execute('SELECT * FROM recruits ORDER BY id')",
        "print(cursor.fetchall())",
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L73.json",
        module_name="Module_08_Python_SQLite_Integration",
        lesson_name="L73_Parameterized_INSERT_SELECT"
    )