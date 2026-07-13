import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "✏️  UPDATE from Python – Promote a Soldier\n\n"
        "The `soldiers` table has 4 rows.\n"
        "Write Python code that:\n"
        "  1. Connects to the database\n"
        "  2. Uses a parameterized UPDATE to change\n"
        "     Rahim's rank from 'Colonel' to 'General'\n"
        "  3. Commits, then SELECTs the updated row.\n"
        "  4. Prints the row (fetchone).\n\n"
        "Expected output:\n(2, 'Rahim', 'General', 4000.0)"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000),(2,'Rahim','Colonel',4000),(3,'Ali','Colonel',4500),(4,'Hasan','Private',3500);"
    ),
    expected_output="(2, 'Rahim', 'General', 4000.0)",
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('''CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, salary REAL)''')",
        "conn.execute(\"INSERT INTO soldiers VALUES (1,'Emperor','General',5000),(2,'Rahim','Colonel',4000),(3,'Ali','Colonel',4500),(4,'Hasan','Private',3500)\")",
        "conn.execute('UPDATE soldiers SET rank = ? WHERE name = ?', ('General', 'Rahim'))",
        "conn.commit()",
        "cursor = conn.execute('SELECT * FROM soldiers WHERE id = 2')",
        "print(cursor.fetchone())",
    ]
)

easy2 = Task(
    description=(
        "🗑️  DELETE from Python – Remove a Soldier\n\n"
        "The `soldiers` table has 4 rows.\n"
        "Write Python code that:\n"
        "  1. Uses a parameterized DELETE to remove\n"
        "     the soldier with id = 4 (Hasan).\n"
        "  2. Commits, then SELECTs all remaining rows.\n"
        "  3. Prints the result.\n\n"
        "Expected output:\n[(1,'Emperor','General',5000.0), (2,'Rahim','Colonel',4000.0), (3,'Ali','Colonel',4500.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000),(2,'Rahim','Colonel',4000),(3,'Ali','Colonel',4500),(4,'Hasan','Private',3500);"
    ),
    expected_output="[(1, 'Emperor', 'General', 5000.0), (2, 'Rahim', 'Colonel', 4000.0), (3, 'Ali', 'Colonel', 4500.0)]",
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('''CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, salary REAL)''')",
        "conn.execute(\"INSERT INTO soldiers VALUES (1,'Emperor','General',5000),(2,'Rahim','Colonel',4000),(3,'Ali','Colonel',4500),(4,'Hasan','Private',3500)\")",
        "conn.execute('DELETE FROM soldiers WHERE id = ?', (4,))",
        "conn.commit()",
        "cursor = conn.execute('SELECT * FROM soldiers ORDER BY id')",
        "print(cursor.fetchall())",
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "📊  Batch UPDATE with Rowcount – Raise for All Colonels\n\n"
        "The `soldiers` table has 4 rows.\n"
        "Write Python code that:\n"
        "  1. Updates ALL soldiers with rank 'Colonel'\n"
        "     to have rank 'Major'.\n"
        "  2. Prints the number of rows affected (cursor.rowcount).\n"
        "  3. Commits, then SELECTs only the updated rows.\n\n"
        "Expected output:\n2\n[(2, 'Rahim', 'Major', 4000.0), (3, 'Ali', 'Major', 4500.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000),(2,'Rahim','Colonel',4000),(3,'Ali','Colonel',4500),(4,'Hasan','Private',3500);"
    ),
    expected_output="2\n[(2, 'Rahim', 'Major', 4000.0), (3, 'Ali', 'Major', 4500.0)]",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('''CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, salary REAL)''')",
        "conn.execute(\"INSERT INTO soldiers VALUES (1,'Emperor','General',5000),(2,'Rahim','Colonel',4000),(3,'Ali','Colonel',4500),(4,'Hasan','Private',3500)\")",
        "cursor = conn.execute('UPDATE soldiers SET rank = ? WHERE rank = ?', ('Major', 'Colonel'))",
        "print(cursor.rowcount)",
        "conn.commit()",
        "cursor = conn.execute('SELECT * FROM soldiers WHERE rank = ?', ('Major',))",
        "print(cursor.fetchall())",
    ]
)

medium2 = Task(
    description=(
        "⚠️  Safe DELETE – Test with SELECT First\n\n"
        "The `soldiers` table has 4 rows.\n"
        "Write Python code that:\n"
        "  1. First SELECTs soldiers with salary < 3000\n"
        "     and prints the count of such soldiers.\n"
        "  2. Then DELETEs those soldiers.\n"
        "  3. Prints the number of deleted rows.\n"
        "  4. Commits, then prints all remaining rows.\n\n"
        "Expected output:\n0\n0\n[(1,'Emperor','General',5000.0), (2,'Rahim','Colonel',4000.0), (3,'Ali','Colonel',4500.0), (4,'Hasan','Private',3500.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000),(2,'Rahim','Colonel',4000),(3,'Ali','Colonel',4500),(4,'Hasan','Private',3500);"
    ),
    expected_output="0\n0\n[(1, 'Emperor', 'General', 5000.0), (2, 'Rahim', 'Colonel', 4000.0), (3, 'Ali', 'Colonel', 4500.0), (4, 'Hasan', 'Private', 3500.0)]",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('''CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, salary REAL)''')",
        "conn.execute(\"INSERT INTO soldiers VALUES (1,'Emperor','General',5000),(2,'Rahim','Colonel',4000),(3,'Ali','Colonel',4500),(4,'Hasan','Private',3500)\")",
        "count = conn.execute('SELECT COUNT(*) FROM soldiers WHERE salary < 3000').fetchone()[0]",
        "print(count)",
        "cursor = conn.execute('DELETE FROM soldiers WHERE salary < 3000')",
        "print(cursor.rowcount)",
        "conn.commit()",
        "cursor = conn.execute('SELECT * FROM soldiers ORDER BY id')",
        "print(cursor.fetchall())",
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  UPDATE with Subquery – Set to Regimental Average\n\n"
        "The `soldiers` table now has a `regiment_id` column.\n"
        "Insert 5 soldiers across 2 regiments.\n"
        "Write Python code that:\n"
        "  1. Executes an UPDATE that sets each soldier's salary\n"
        "     to the average salary of their regiment using a\n"
        "     correlated subquery in the SET clause.\n"
        "  2. Commits, then SELECTs all rows sorted by id.\n"
        "  3. Prints the result.\n\n"
        "Expected output:\n[(1,'Emperor',4750.0,1), (2,'Rahim',3166.67,2), (3,'Ali',4750.0,1), (4,'Hasan',3166.67,2), (5,'Karim',3166.67,2)]"
    ),
    expected_output="[(1, 'Emperor', 4750.0, 1), (2, 'Rahim', 3166.66666666667, 2), (3, 'Ali', 4750.0, 1), (4, 'Hasan', 3166.66666666667, 2), (5, 'Karim', 3166.66666666667, 2)]",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('''CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, salary REAL, regiment_id INTEGER)''')",
        "conn.execute(\"INSERT INTO soldiers VALUES (1,'Emperor',5000,1),(2,'Rahim',4000,2),(3,'Ali',4500,1),(4,'Hasan',3500,2),(5,'Karim',2000,2)\")",
        "conn.execute('UPDATE soldiers SET salary = (SELECT AVG(salary) FROM soldiers s2 WHERE s2.regiment_id = soldiers.regiment_id)')",
        "conn.commit()",
        "cursor = conn.execute('SELECT * FROM soldiers ORDER BY id')",
        "print(cursor.fetchall())",
    ]
)

hard2 = Task(
    description=(
        "🔄  Soft DELETE – Mark Instead of Remove\n\n"
        "The `soldiers` table has 4 rows.\n"
        "Write Python code that:\n"
        "  1. ALTER TABLE to add a `deleted_at` column (TEXT).\n"
        "  2. Instead of actually deleting Hasan (id=4),\n"
        "     UPDATE his row to set deleted_at = datetime('now').\n"
        "  3. Commits.\n"
        "  4. SELECT only rows where deleted_at IS NULL\n"
        "     (the active soldiers), ordered by id.\n"
        "  5. Prints the result.\n\n"
        "Expected output:\n[(1,'Emperor','General',5000.0,None), (2,'Rahim','Colonel',4000.0,None), (3,'Ali','General',4500.0,None)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000),(2,'Rahim','Colonel',4000),(3,'Ali','General',4500),(4,'Hasan','Private',3500);"
    ),
    expected_output="[(1, 'Emperor', 'General', 5000.0, None), (2, 'Rahim', 'Colonel', 4000.0, None), (3, 'Ali', 'General', 4500.0, None)]",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('''CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, salary REAL)''')",
        "conn.execute(\"INSERT INTO soldiers VALUES (1,'Emperor','General',5000),(2,'Rahim','Colonel',4000),(3,'Ali','General',4500),(4,'Hasan','Private',3500)\")",
        "conn.execute('ALTER TABLE soldiers ADD COLUMN deleted_at TEXT')",
        "conn.execute(\"UPDATE soldiers SET deleted_at = datetime('now') WHERE name = 'Hasan'\")",
        "conn.commit()",
        "cursor = conn.execute('SELECT * FROM soldiers WHERE deleted_at IS NULL ORDER BY id')",
        "print(cursor.fetchall())",
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L75.json",
        module_name="Module_08_Python_SQLite_Integration",
        lesson_name="L75_UPDATE_DELETE_with_Python"
    )