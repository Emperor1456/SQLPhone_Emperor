import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "⚠️  Catch IntegrityError – Duplicate Key\n\n"
        "Write Python code that:\n"
        "  1. Connects to ':memory:'\n"
        "  2. Creates a table `users` (id INTEGER PRIMARY KEY,\n"
        "     username TEXT UNIQUE).\n"
        "  3. Inserts ('Emperor') successfully.\n"
        "  4. Tries to insert ('Emperor') again – this should fail.\n"
        "  5. Catches sqlite3.IntegrityError and prints 'Duplicate'.\n"
        "  6. Finally SELECTs all rows and prints.\n\n"
        "Expected output:\nDuplicate\n[(1, 'Emperor')]"
    ),
    expected_output="Duplicate\n[(1, 'Emperor')]",
    level=Level.EASY,
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT UNIQUE)')",
        "conn.execute(\"INSERT INTO users (username) VALUES ('Emperor')\")",
        "conn.commit()",
        "try:",
        "    conn.execute(\"INSERT INTO users (username) VALUES ('Emperor')\")",
        "except sqlite3.IntegrityError:",
        "    print('Duplicate')",
        "cursor = conn.execute('SELECT * FROM users')",
        "print(cursor.fetchall())",
    ]
)

easy2 = Task(
    description=(
        "🛡️  Catch OperationalError – Bad SQL\n\n"
        "Write Python code that:\n"
        "  1. Connects to ':memory:'\n"
        "  2. Tries to execute 'SELECTT * FROM nothing' (typo).\n"
        "  3. Catches sqlite3.OperationalError and prints 'Bad SQL'.\n"
        "  4. Then executes correct SQL: SELECT 1 and prints result.\n\n"
        "Expected output:\nBad SQL\n[(1,)]"
    ),
    expected_output="Bad SQL\n[(1,)]",
    level=Level.EASY,
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "try:",
        "    conn.execute('SELECTT * FROM nothing')",
        "except sqlite3.OperationalError:",
        "    print('Bad SQL')",
        "cursor = conn.execute('SELECT 1')",
        "print(cursor.fetchall())",
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🔄  try/except/finally – Always Close Connection\n\n"
        "Write Python code that:\n"
        "  1. Connects to ':memory:'\n"
        "  2. Creates a table `test` (id INTEGER).\n"
        "  3. Uses try/except/finally to ensure the connection\n"
        "     is closed even if an error occurs.\n"
        "  4. Inside try: inserts (1), commits, prints 'OK'.\n"
        "  5. Inside finally: closes connection, prints 'Closed'.\n"
        "  6. After the finally block, print 'Done'.\n\n"
        "Expected output:\nOK\nClosed\nDone"
    ),
    expected_output="OK\nClosed\nDone",
    level=Level.MEDIUM,
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('CREATE TABLE test (id INTEGER)')",
        "try:",
        "    conn.execute('INSERT INTO test VALUES (1)')",
        "    conn.commit()",
        "    print('OK')",
        "except sqlite3.Error as e:",
        "    print(f'Error: {e}')",
        "finally:",
        "    conn.close()",
        "    print('Closed')",
        "print('Done')",
    ]
)

medium2 = Task(
    description=(
        "🧪  Retry on Database Locked – Exponential Backoff\n\n"
        "Write a function `execute_with_retry(conn, sql, params)`\n"
        "that tries to execute a SQL statement up to 3 times\n"
        "if the database is locked, sleeping 0.1, 0.2, 0.4 seconds\n"
        "between attempts.\n"
        "Test it on a simple INSERT. Print 'Success' after execution.\n\n"
        "Expected output:\nSuccess"
    ),
    expected_output="Success",
    level=Level.MEDIUM,
    hints=[
        "import sqlite3, time",
        "def execute_with_retry(conn, sql, params, max_retries=3):",
        "    for attempt in range(max_retries):",
        "        try:",
        "            conn.execute(sql, params)",
        "            conn.commit()",
        "            return",
        "        except sqlite3.OperationalError as e:",
        "            if 'locked' in str(e) and attempt < max_retries - 1:",
        "                time.sleep(0.1 * (2 ** attempt))",
        "            else:",
        "                raise",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('CREATE TABLE retry_test (id INTEGER PRIMARY KEY, value TEXT)')",
        "execute_with_retry(conn, 'INSERT INTO retry_test (value) VALUES (?)', ('test',))",
        "print('Success')",
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🔐  Transaction with Rollback – Safe Fund Transfer\n\n"
        "Write Python code that:\n"
        "  1. Creates `accounts` table and seeds Emperor (1000), Rahim (500).\n"
        "  2. Uses try/except to attempt a transfer of 2000 from\n"
        "     Emperor to Rahim (insufficient funds simulation).\n"
        "  3. If any error occurs (including manual check), ROLLBACK.\n"
        "  4. After rollback, prints 'Rolled back'.\n"
        "  5. Finally SELECT both accounts and print.\n\n"
        "Expected output:\nRolled back\n[(1, 'Emperor', 1000.0), (2, 'Rahim', 500.0)]"
    ),
    expected_output="Rolled back\n[(1, 'Emperor', 1000.0), (2, 'Rahim', 500.0)]",
    level=Level.HARD,
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('CREATE TABLE accounts (id INTEGER PRIMARY KEY, holder TEXT, balance REAL)')",
        "conn.execute(\"INSERT INTO accounts VALUES (1,'Emperor',1000),(2,'Rahim',500)\")",
        "conn.commit()",
        "try:",
        "    conn.execute('BEGIN')",
        "    cursor = conn.execute('UPDATE accounts SET balance = balance - 2000 WHERE id = 1')",
        "    if conn.execute('SELECT balance FROM accounts WHERE id = 1').fetchone()[0] < 0:",
        "        raise ValueError('Insufficient funds')",
        "    conn.execute('UPDATE accounts SET balance = balance + 2000 WHERE id = 2')",
        "    conn.commit()",
        "except:",
        "    conn.rollback()",
        "    print('Rolled back')",
        "cursor = conn.execute('SELECT * FROM accounts ORDER BY id')",
        "print(cursor.fetchall())",
    ]
)

hard2 = Task(
    description=(
        "📊  Error Logging – Save Failures to a Table\n\n"
        "Write Python code that:\n"
        "  1. Creates a `error_log` table (id, message, timestamp).\n"
        "  2. Creates a `users` table with UNIQUE constraint on email.\n"
        "  3. Tries to insert two users with the SAME email.\n"
        "  4. Catches IntegrityError, logs the error to `error_log`\n"
        "     with datetime('now'), and prints 'Error logged'.\n"
        "  5. Finally SELECT * FROM error_log and print.\n\n"
        "Expected output:\nError logged\n[(1, 'UNIQUE constraint failed: users.email', (timestamp))]"
    ),
    expected_output="Error logged\n[(1, 'UNIQUE constraint failed: users.email', '2026-07-12')]",
    level=Level.HARD,
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute('CREATE TABLE error_log (id INTEGER PRIMARY KEY, message TEXT, timestamp TEXT)')",
        "conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, email TEXT UNIQUE)')",
        "conn.execute(\"INSERT INTO users (email) VALUES ('emperor@empire.com')\")",
        "conn.commit()",
        "try:",
        "    conn.execute(\"INSERT INTO users (email) VALUES ('emperor@empire.com')\")",
        "except sqlite3.IntegrityError as e:",
        "    conn.execute(\"INSERT INTO error_log (message, timestamp) VALUES (?, datetime('now'))\", (str(e),))",
        "    conn.commit()",
        "    print('Error logged')",
        "cursor = conn.execute('SELECT * FROM error_log')",
        "print(cursor.fetchall())",
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L77.json",
        module_name="Module_08_Python_SQLite_Integration",
        lesson_name="L77_Database_Error_Handling"
    )
