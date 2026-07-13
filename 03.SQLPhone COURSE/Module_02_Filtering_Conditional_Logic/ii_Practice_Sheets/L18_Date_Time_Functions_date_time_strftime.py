import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "📅  Today's Date – date('now')\n\n"
        "Return today's date using the date() function.\n"
        "The output will be in YYYY-MM-DD format.\n\n"
        "Expected output: [(current date)]"
    ),
    expected_output=None,  # dynamic date
    level=Level.EASY,
    hints=[
        "SELECT date('now');"
    ],
    verify_func=lambda conn: (
        len(conn.execute("SELECT date('now')").fetchone()[0]) == 10
    )
)

easy2 = Task(
    description=(
        "⏰  Current Time – time('now')\n\n"
        "Return the current time using the time() function.\n"
        "The output will be in HH:MM:SS format.\n\n"
        "Expected output: [(current time)]"
    ),
    expected_output=None,
    level=Level.EASY,
    hints=[
        "SELECT time('now');"
    ],
    verify_func=lambda conn: (
        len(conn.execute("SELECT time('now')").fetchone()[0]) == 8
    )
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "📆  Date Arithmetic – 7 Days from Now\n\n"
        "Return the date that is exactly 7 days from today.\n"
        "Use the modifier '+7 days'.\n\n"
        "Expected output: [(date 7 days from now)]"
    ),
    expected_output=None,
    level=Level.MEDIUM,
    hints=[
        "SELECT date('now', '+7 days');"
    ],
    verify_func=lambda conn: (
        conn.execute("SELECT date('now', '+7 days')").fetchone()[0] is not None
    )
)

medium2 = Task(
    description=(
        "🧙  strftime – Month Name\n\n"
        "Return the current month's full name\n"
        "(e.g., 'January', 'February') using strftime.\n"
        "Use the format '%B'.\n\n"
        "Expected output: [(current month name)]"
    ),
    expected_output=None,
    level=Level.MEDIUM,
    hints=[
        "SELECT strftime('%B', 'now');"
    ],
    verify_func=lambda conn: (
        len(conn.execute("SELECT strftime('%B', 'now')").fetchone()[0]) > 0
    )
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧮  Age Calculation – Years from Birth Date\n\n"
        "Create a table `soldiers` with columns:\n"
        "  • id INTEGER, name TEXT, birth_date TEXT.\n"
        "Insert 3 soldiers with different birth dates.\n"
        "Return name, birth_date, and age in years\n"
        "(current year minus birth year, adjusted if\n"
        "birthday hasn't occurred yet this year).\n"
        "Sort by age descending.\n\n"
        "Expected output (if today is 2026-07-12):\n[('Rahim',31), ('Karim',25), ('Emperor',17)]"
    ),
    expected_output="[('Rahim', 31), ('Karim', 25), ('Emperor', 17)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE soldiers (id INTEGER, name TEXT, birth_date TEXT);",
        "INSERT INTO soldiers VALUES (1,'Emperor','2008-07-10'), (2,'Rahim','1995-03-22'), (3,'Karim','2000-11-05');",
        "SELECT name, birth_date, (strftime('%Y','now') - strftime('%Y', birth_date)) - (strftime('%m-%d','now') < strftime('%m-%d', birth_date)) AS age FROM soldiers ORDER BY age DESC;"
    ]
)

hard2 = Task(
    description=(
        "📊  This Month's Records – strftime Filter\n\n"
        "Create a table `missions` with columns:\n"
        "  • id INTEGER, name TEXT, mission_date TEXT.\n"
        "Insert 5 missions with dates spanning several months.\n"
        "Return name and mission_date for missions\n"
        "that occurred in the current month.\n"
        "Use strftime to compare year‑month.\n\n"
        "Expected output (if today is 2026-07-12):\n[('Patrol Alpha','2026-07-05'), ('Recon Beta','2026-07-10')]"
    ),
    expected_output="[('Patrol Alpha', '2026-07-05'), ('Recon Beta', '2026-07-10')]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE missions (id INTEGER, name TEXT, mission_date TEXT);",
        "INSERT INTO missions VALUES (1,'Patrol Alpha','2026-07-05'), (2,'Recon Beta','2026-07-10'), (3,'Supply Drop','2026-06-28'), (4,'Guard Duty','2026-08-01'), (5,'Training','2026-07-15');",
        "SELECT name, mission_date FROM missions WHERE strftime('%Y-%m', mission_date) = strftime('%Y-%m', 'now') ORDER BY mission_date;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L18.json",
        module_name="Module_02_Filtering_Conditional_Logic",
        lesson_name="L18_Date_Time_Functions"
    )
