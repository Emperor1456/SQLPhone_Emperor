import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "📦  Install psycopg2 – Command Recall\n\n"
        "Write Python code that prints the exact command\n"
        "to install the PostgreSQL adapter for Python,\n"
        "as shown in the lecture.\n\n"
        "Expected output:\npip install psycopg2-binary"
    ),
    expected_output="pip install psycopg2-binary",
    level=Level.EASY,
    mode="python",
    hints=[
        "The lecture shows: pip install psycopg2-binary",
        "Just print that string.",
        "print('pip install psycopg2-binary')",
    ]
)

easy2 = Task(
    description=(
        "🔌  First Connection Snippet\n\n"
        "Write Python code that prints the two lines of\n"
        "code that import psycopg2 and create a connection\n"
        "to the 'empire' database on localhost with user\n"
        "'postgres' and password 'your_password'.\n"
        "Print them exactly as shown in the lecture\n"
        "(all lowercase host, database, etc. inside\n"
        "single quotes).\n\n"
        "Expected output:\nimport psycopg2\nconn = psycopg2.connect(host='localhost', database='empire', user='postgres', password='your_password')"
    ),
    expected_output="import psycopg2\nconn = psycopg2.connect(host='localhost', database='empire', user='postgres', password='your_password')",
    level=Level.EASY,
    mode="python",
    hints=[
        "First line: import psycopg2",
        "Second line: conn = psycopg2.connect(...)",
        "Use single quotes for strings.",
        "print('import psycopg2\\nconn = psycopg2.connect(host='localhost', database='empire', user='postgres', password='your_password')')",
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "💉  Parameterized INSERT – The Correct Way\n\n"
        "Write Python code that prints the exact line\n"
        "from the lecture that inserts a soldier using\n"
        "parameterized query (%s placeholders) and then\n"
        "prints the commit call.\n"
        "The output must be these two statements on\n"
        "separate lines.\n\n"
        "Expected output:\ncursor.execute(\"INSERT INTO soldiers (name, rank, salary) VALUES (%s, %s, %s)\", ('Emperor', 'General', 5000.00))\nconn.commit()"
    ),
    expected_output="cursor.execute(\"INSERT INTO soldiers (name, rank, salary) VALUES (%s, %s, %s)\", ('Emperor', 'General', 5000.00))\nconn.commit()",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "Use cursor.execute with %s placeholders.",
        "Values are a tuple ('Emperor', 'General', 5000.00).",
        "Second line is conn.commit().",
        "Print the multi‑line string.",
    ]
)

medium2 = Task(
    description=(
        "🧰  Reusable get_connection() Function\n\n"
        "Write Python code that prints the exact\n"
        "definition of the `get_connection()` function\n"
        "from the lecture (including the return statement\n"
        "with psycopg2.connect(...) and the same keyword\n"
        "arguments). Keep the indentation (4 spaces).\n\n"
        "Expected output:\ndef get_connection():\n    return psycopg2.connect(\n        host=\"localhost\",\n        database=\"empire\",\n        user=\"postgres\",\n        password=\"your_password\"\n    )"
    ),
    expected_output="def get_connection():\n    return psycopg2.connect(\n        host=\"localhost\",\n        database=\"empire\",\n        user=\"postgres\",\n        password=\"your_password\"\n    )",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "Use triple quotes to keep the indentation.",
        "The function name is get_connection, no parameters.",
        "Inside the return, use keyword arguments.",
        "Print exactly that block.",
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🏦  Transactional Fund Transfer – Code Snippet\n\n"
        "Write Python code that prints the complete\n"
        "transactional block from the lecture (the one\n"
        "that uses `with connect() as conn:` to transfer\n"
        "500 from account 1 to account 2). Print the\n"
        "exact four lines (with context manager and two\n"
        "UPDATE statements).\n\n"
        "Expected output:\nwith connect() as conn:\n    cur = conn.cursor()\n    cur.execute(\"UPDATE accounts SET balance = balance - 500 WHERE id = 1\")\n    cur.execute(\"UPDATE accounts SET balance = balance + 500 WHERE id = 2\")"
    ),
    expected_output="with connect() as conn:\n    cur = conn.cursor()\n    cur.execute(\"UPDATE accounts SET balance = balance - 500 WHERE id = 1\")\n    cur.execute(\"UPDATE accounts SET balance = balance + 500 WHERE id = 2\")",
    level=Level.HARD,
    mode="python",
    hints=[
        "Use with connect() as conn:",
        "Create a cursor.",
        "Two update statements, each with cur.execute.",
        "Print exactly these four lines with proper indentation.",
    ]
)

hard2 = Task(
    description=(
        "🛡️  Error Handling Snippet – Integrity & Operational\n\n"
        "Write Python code that prints the complete\n"
        "try/except block from the lecture that catches\n"
        "IntegrityError and OperationalError when\n"
        "inserting a duplicate. Print it exactly.\n\n"
        "Expected output:\ntry:\n    with connect() as conn:\n        cur = conn.cursor()\n        cur.execute(\"INSERT INTO soldiers (id, name) VALUES (1, 'Duplicate')\")\nexcept IntegrityError as e:\n    print(f\"Integrity violation: {e}\")\nexcept OperationalError as e:\n    print(f\"Connection failed: {e}\")"
    ),
    expected_output="try:\n    with connect() as conn:\n        cur = conn.cursor()\n        cur.execute(\"INSERT INTO soldiers (id, name) VALUES (1, 'Duplicate')\")\nexcept IntegrityError as e:\n    print(f\"Integrity violation: {e}\")\nexcept OperationalError as e:\n    print(f\"Connection failed: {e}\")",
    level=Level.HARD,
    mode="python",
    hints=[
        "Starts with try:",
        "Inside, with connect() as conn: and cursor.",
        "Two except clauses, one for IntegrityError, one for OperationalError.",
        "Each prints an f‑string with the error.",
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L93.json",
        module_name="Module_10_Beyond_SQLite",
        lesson_name="L93_Connecting_Python_to_PostgreSQL_psycopg2"
    )