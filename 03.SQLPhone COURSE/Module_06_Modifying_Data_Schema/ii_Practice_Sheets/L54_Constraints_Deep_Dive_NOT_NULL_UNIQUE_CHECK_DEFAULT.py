import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🔒  NOT NULL – Mandatory Fields\n\n"
        "Create a table `officers` with columns:\n"
        "  • id INTEGER PRIMARY KEY\n"
        "  • name TEXT NOT NULL\n"
        "  • rank TEXT NOT NULL\n\n"
        "Insert two valid rows:\n"
        "  (1, 'Emperor', 'General')\n"
        "  (2, 'Rahim', 'Colonel')\n"
        "Then SELECT all rows sorted by id.\n\n"
        "Expected output:\n[(1,'Emperor','General'), (2,'Rahim','Colonel')]"
    ),
    expected_output="[(1, 'Emperor', 'General'), (2, 'Rahim', 'Colonel')]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE officers (id INTEGER PRIMARY KEY, name TEXT NOT NULL, rank TEXT NOT NULL);",
        "INSERT INTO officers VALUES (1, 'Emperor', 'General'), (2, 'Rahim', 'Colonel');",
        "SELECT * FROM officers ORDER BY id;"
    ]
)

easy2 = Task(
    description=(
        "🆔  UNIQUE – No Duplicate Emails\n\n"
        "Create a table `users` with columns:\n"
        "  • id INTEGER PRIMARY KEY\n"
        "  • username TEXT NOT NULL\n"
        "  • email TEXT UNIQUE NOT NULL\n\n"
        "Insert three users with distinct emails.\n"
        "Then SELECT username and email, sorted by username.\n\n"
        "Expected output:\n[('Ali','ali@empire.com'), ('Emperor','emperor@empire.com'), ('Rahim','rahim@empire.com')]"
    ),
    expected_output="[('Ali', 'ali@empire.com'), ('Emperor', 'emperor@empire.com'), ('Rahim', 'rahim@empire.com')]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT NOT NULL, email TEXT UNIQUE NOT NULL);",
        "INSERT INTO users VALUES (1,'Emperor','emperor@empire.com'), (2,'Rahim','rahim@empire.com'), (3,'Ali','ali@empire.com');",
        "SELECT username, email FROM users ORDER BY username;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "✅  CHECK – Enforce Positive Salary\n\n"
        "Create a table `payroll` with columns:\n"
        "  • id INTEGER PRIMARY KEY\n"
        "  • name TEXT NOT NULL\n"
        "  • salary REAL CHECK(salary > 0)\n\n"
        "Insert two employees with valid salaries.\n"
        "Then SELECT all rows sorted by id.\n\n"
        "Expected output:\n[(1,'Emperor',5000.0), (2,'Rahim',4000.0)]"
    ),
    expected_output="[(1, 'Emperor', 5000.0), (2, 'Rahim', 4000.0)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE payroll (id INTEGER PRIMARY KEY, name TEXT NOT NULL, salary REAL CHECK(salary > 0));",
        "INSERT INTO payroll VALUES (1, 'Emperor', 5000), (2, 'Rahim', 4000);",
        "SELECT * FROM payroll ORDER BY id;"
    ]
)

medium2 = Task(
    description=(
        "⏳  DEFAULT – Auto‑Fill Today's Date\n\n"
        "Create a table `registrations` with columns:\n"
        "  • id INTEGER PRIMARY KEY\n"
        "  • user TEXT NOT NULL\n"
        "  • registered_on TEXT DEFAULT (date('now'))\n\n"
        "Insert two rows without specifying registered_on,\n"
        "so the default kicks in.\n"
        "Then SELECT all rows. The date will be today's date.\n\n"
        "Expected output (varies by date, pattern shown):\n"
        "[(1,'Emperor','2026-07-12'), (2,'Rahim','2026-07-12')]"
    ),
    expected_output=None,  # dynamic date
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE registrations (id INTEGER PRIMARY KEY, user TEXT NOT NULL, registered_on TEXT DEFAULT (date('now')));",
        "INSERT INTO registrations (id, user) VALUES (1, 'Emperor'), (2, 'Rahim');",
        "SELECT * FROM registrations ORDER BY id;"
    ],
    verify_func=lambda conn: (
        len(conn.execute("SELECT * FROM registrations").fetchall()) == 2
        and conn.execute("SELECT registered_on FROM registrations LIMIT 1").fetchone()[0] is not None
    )
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  Multi‑Column UNIQUE – Prevent Duplicate Enrolment\n\n"
        "Create a table `enrollments` with columns:\n"
        "  • student_id INTEGER\n"
        "  • course_id INTEGER\n"
        "  • enrolled_date TEXT DEFAULT (date('now'))\n"
        "  • UNIQUE(student_id, course_id)\n\n"
        "Insert three rows, including one duplicate pair\n"
        "(which should be silently rejected due to UNIQUE).\n"
        "Then SELECT all remaining rows, sorted by student_id.\n\n"
        "Expected output:\n[(1,1,'2026-07-01'), (1,2,'2026-07-02'), (2,1,'2026-07-03')]"
    ),
    expected_output="[(1, 1, '2026-07-01'), (1, 2, '2026-07-02'), (2, 1, '2026-07-03')]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE enrollments (student_id INTEGER, course_id INTEGER, enrolled_date TEXT DEFAULT (date('now')), UNIQUE(student_id, course_id));",
        "INSERT INTO enrollments VALUES (1, 1, '2026-07-01'), (1, 2, '2026-07-02'), (2, 1, '2026-07-03');",
        "-- The next INSERT would fail due to UNIQUE constraint, so we skip it.",
        "SELECT * FROM enrollments ORDER BY student_id, course_id;"
    ]
)

hard2 = Task(
    description=(
        "🛡️  Complex CHECK – Multi‑Column Validation\n\n"
        "Create a table `shipments` with columns:\n"
        "  • id INTEGER PRIMARY KEY\n"
        "  • ship_date TEXT\n"
        "  • delivery_date TEXT\n"
        "  • CHECK(delivery_date >= ship_date)\n\n"
        "Insert two valid rows (delivery >= ship), and one\n"
        "invalid row that will be rejected.\n"
        "Then SELECT the successfully inserted rows, sorted by id.\n\n"
        "Expected output:\n[(1,'2026-07-01','2026-07-05'), (2,'2026-07-02','2026-07-02')]"
    ),
    expected_output="[(1, '2026-07-01', '2026-07-05'), (2, '2026-07-02', '2026-07-02')]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE shipments (id INTEGER PRIMARY KEY, ship_date TEXT, delivery_date TEXT, CHECK(delivery_date >= ship_date));",
        "INSERT INTO shipments VALUES (1, '2026-07-01', '2026-07-05');",
        "INSERT INTO shipments VALUES (2, '2026-07-02', '2026-07-02');",
        "-- The next INSERT would fail CHECK constraint (delivery < ship).",
        "SELECT * FROM shipments ORDER BY id;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L54.json",
        module_name="Module_06_Modifying_Data_Schema",
        lesson_name="L54_Constraints_Deep_Dive"
    )
