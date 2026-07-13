import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🗂️  The Big Three – Engine Names\n\n"
        "Write Python code that prints the names of the\n"
        "three major database engines discussed in this\n"
        "lesson — one per line, in alphabetical order.\n\n"
        "Expected output:\nMySQL\nPostgreSQL\nSQLite"
    ),
    expected_output="MySQL\nPostgreSQL\nSQLite",
    level=Level.EASY,
    mode="python",
    hints=[
        "Use print() three times.",
        "print('MySQL')\nprint('PostgreSQL')\nprint('SQLite')",
    ]
)

easy2 = Task(
    description=(
        "📱  SQLite's Sweet Spot – Primary Use Case\n\n"
        "Write Python code that prints the primary\n"
        "use case for SQLite as described in the lecture:\n"
        "\"Mobile apps and embedded systems\" (no quotes).\n\n"
        "Expected output:\nMobile apps and embedded systems"
    ),
    expected_output="Mobile apps and embedded systems",
    level=Level.EASY,
    mode="python",
    hints=[
        "print('Mobile apps and embedded systems')",
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "📊  Comparison Table – Create a Simple Text Table\n\n"
        "Write Python code that prints a fixed‑width\n"
        "comparison of the three engines. The output\n"
        "must exactly match the following 4 lines:\n\n"
        "Engine      | Concurrency | Best For\n"
        "------------+-------------+----------------------\n"
        "SQLite      | Single-writer| Mobile & embedded\n"
        "PostgreSQL  | Full MVCC   | Enterprise web apps\n"
        "MySQL       | Row-level   | Web & shared hosting\n\n"
        "Expected output (as above, exactly)."
    ),
    expected_output=(
        "Engine      | Concurrency | Best For\n"
        "------------+-------------+----------------------\n"
        "SQLite      | Single-writer| Mobile & embedded\n"
        "PostgreSQL  | Full MVCC   | Enterprise web apps\n"
        "MySQL       | Row-level   | Web & shared hosting"
    ),
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "Use multi‑line string with triple quotes.",
        "table = '''Engine      | Concurrency | Best For",
        "------------+-------------+----------------------",
        "SQLite      | Single-writer| Mobile & embedded",
        "PostgreSQL  | Full MVCC   | Enterprise web apps",
        "MySQL       | Row-level   | Web & shared hosting'''",
        "print(table)",
    ]
)

medium2 = Task(
    description=(
        "🔢  Serverless Count – Count Serverless Engines\n\n"
        "Among the three engines (SQLite, PostgreSQL, MySQL),\n"
        "only one is serverless (zero‑configuration, no\n"
        "separate process). Write Python code that prints\n"
        "the number of serverless engines as a single digit.\n\n"
        "Expected output:\n1"
    ),
    expected_output="1",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "The serverless engine is SQLite.",
        "print(1)",
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧠  Scenario Engine Choice – Real‑time Chat\n\n"
        "Read the following project description:\n\n"
        "  \"A real‑time chat application with 100k\n"
        "   concurrent users, requiring strict typing,\n"
        "   advanced indexing, and role‑based access.\"\n\n"
        "Write Python code that prints the name of the\n"
        "database engine best suited for this project\n"
        "(as recommended in the lecture decision table).\n\n"
        "Expected output:\nPostgreSQL"
    ),
    expected_output="PostgreSQL",
    level=Level.HARD,
    mode="python",
    hints=[
        "The decision table: real‑time analytics → PostgreSQL.",
        "PostgreSQL supports full MVCC, advanced indexes, roles.",
        "print('PostgreSQL')",
    ]
)

hard2 = Task(
    description=(
        "📝  PostgreSQL CREATE TABLE – SERIAL & NUMERIC\n\n"
        "Write Python code that prints the exact SQL\n"
        "statement from the lecture that creates a\n"
        "`soldiers` table in PostgreSQL using `SERIAL`\n"
        "and `NUMERIC(10,2)`.\n\n"
        "Expected output (one line):\nCREATE TABLE soldiers (id SERIAL PRIMARY KEY, name TEXT NOT NULL, salary NUMERIC(10,2) CHECK(salary > 0));"
    ),
    expected_output="CREATE TABLE soldiers (id SERIAL PRIMARY KEY, name TEXT NOT NULL, salary NUMERIC(10,2) CHECK(salary > 0));",
    level=Level.HARD,
    mode="python",
    hints=[
        "print('CREATE TABLE soldiers (id SERIAL PRIMARY KEY, name TEXT NOT NULL, salary NUMERIC(10,2) CHECK(salary > 0));')",
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L91.json",
        module_name="Module_10_Beyond_SQLite",
        lesson_name="L91_SQLite_vs_PostgreSQL_vs_MySQL_Choosing_Your_Engine"
    )