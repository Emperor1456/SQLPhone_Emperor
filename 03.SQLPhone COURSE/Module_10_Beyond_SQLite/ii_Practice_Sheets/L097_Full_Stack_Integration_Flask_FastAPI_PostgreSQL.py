import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🚀  Flask App Initialization\n\n"
        "Write Python code that prints the exact line\n"
        "of code from the lecture that creates a Flask\n"
        "application instance named `app`.\n\n"
        "Expected output:\napp = Flask(__name__)"
    ),
    expected_output="app = Flask(__name__)",
    level=Level.EASY,
    mode="python",
    hints=[
        "The line uses the Flask class, passing __name__.",
        "print('app = Flask(__name__)')",
    ]
)

easy2 = Task(
    description=(
        "🏊  Connection Pool Import\n\n"
        "Print the import statement that brings in\n"
        "`SimpleConnectionPool` from `psycopg2.pool`.\n"
        "Exactly as shown in the lecture.\n\n"
        "Expected output:\nfrom psycopg2.pool import SimpleConnectionPool"
    ),
    expected_output="from psycopg2.pool import SimpleConnectionPool",
    level=Level.EASY,
    mode="python",
    hints=[
        "It's a from … import statement.",
        "Module: psycopg2.pool, class: SimpleConnectionPool.",
        "print('from psycopg2.pool import SimpleConnectionPool')",
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🔗  Create a Connection Pool\n\n"
        "Print the line of code that instantiates a\n"
        "`SimpleConnectionPool` with min 1, max 10,\n"
        "and the connection string shown in the lecture.\n\n"
        "Expected output:\npool = SimpleConnectionPool(1, 10, \"postgresql://user:pass@localhost/empire\")"
    ),
    expected_output='pool = SimpleConnectionPool(1, 10, "postgresql://user:pass@localhost/empire")',
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "The constructor takes (minconn, maxconn, dsn).",
        "The connection string is the same as in earlier examples.",
        "print('pool = SimpleConnectionPool(1, 10, \"postgresql://user:pass@localhost/empire\")')",
    ]
)

medium2 = Task(
    description=(
        "⚡  FastAPI App Skeleton\n\n"
        "Print the two lines that import FastAPI and\n"
        "create an `app` instance, as shown in the lecture.\n\n"
        "Expected output:\nfrom fastapi import FastAPI\napp = FastAPI()"
    ),
    expected_output="from fastapi import FastAPI\napp = FastAPI()",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "First: from fastapi import FastAPI",
        "Second: app = FastAPI()",
        "Print them with a newline.",
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🔁  Acquire & Release a Pool Connection\n\n"
        "Inside an endpoint, you need to get a connection\n"
        "from the pool and later return it. Print the two\n"
        "lines that do this (one to get, one to put back),\n"
        "each on its own line, as shown in the lecture.\n\n"
        "Expected output:\nconn = pool.getconn()\npool.putconn(conn)"
    ),
    expected_output="conn = pool.getconn()\npool.putconn(conn)",
    level=Level.HARD,
    mode="python",
    hints=[
        "The method to obtain is .getconn()",
        "The method to release is .putconn(conn)",
        "Print both lines with a newline.",
    ]
)

hard2 = Task(
    description=(
        "🧪  Complete Flask Endpoint with Pool\n\n"
        "Print the exact body of the `list_soldiers`\n"
        "function (without the decorator) that uses the\n"
        "connection pool. Include all five lines of code\n"
        "(acquire, cursor, execute, build rows, release).\n"
        "Indent the body with 4 spaces.\n\n"
        "Expected output:\n"
        "def list_soldiers():\n"
        "    conn = pool.getconn()\n"
        "    cur = conn.cursor()\n"
        "    cur.execute(\"SELECT id, name, rank FROM soldiers\")\n"
        "    rows = [{\"id\": r[0], \"name\": r[1], \"rank\": r[2]} for r in cur.fetchall()]\n"
        "    cur.close()\n"
        "    pool.putconn(conn)\n"
        "    return rows"
    ),
    expected_output=(
        "def list_soldiers():\n"
        "    conn = pool.getconn()\n"
        "    cur = conn.cursor()\n"
        '    cur.execute("SELECT id, name, rank FROM soldiers")\n'
        '    rows = [{"id": r[0], "name": r[1], "rank": r[2]} for r in cur.fetchall()]\n'
        "    cur.close()\n"
        "    pool.putconn(conn)\n"
        "    return rows"
    ),
    level=Level.HARD,
    mode="python",
    hints=[
        "The function definition line is 'def list_soldiers():'",
        "Then 4-space indentation.",
        "Steps: pool.getconn, cursor, execute, build rows dict, cur.close, pool.putconn, return.",
        "Print exactly the block using triple quotes.",
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L97.json",
        module_name="Module_10_Beyond_SQLite",
        lesson_name="L97_Full_Stack_Integration_Flask_FastAPI_PostgreSQL"
    )