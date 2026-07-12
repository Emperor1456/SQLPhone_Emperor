import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "➕  Single Recruit – Basic INSERT\n\n"
        "Create a table `recruits` with columns\n"
        "  • id INTEGER PRIMARY KEY\n"
        "  • name TEXT NOT NULL\n\n"
        "Insert one row with id=NULL (auto‑assign)\n"
        "and name='Emperor'.\n"
        "Then SELECT all rows.\n\n"
        "Expected output: [(1, 'Emperor')]"
    ),
    expected_output="[(1, 'Emperor')]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE recruits (id INTEGER PRIMARY KEY, name TEXT NOT NULL);",
        "INSERT INTO recruits VALUES (NULL, 'Emperor');",
        "SELECT * FROM recruits;"
    ]
)

easy2 = Task(
    description=(
        "✍️  Explicit Columns – Safer INSERT\n\n"
        "Create a table `soldiers` with columns\n"
        "  • id INTEGER PRIMARY KEY\n"
        "  • name TEXT NOT NULL\n"
        "  • rank TEXT\n\n"
        "Insert one row specifying only name and rank:\n"
        "  name='Rahim', rank='Colonel'\n"
        "Then SELECT all rows.\n\n"
        "Expected output: [(1, 'Rahim', 'Colonel')]"
    ),
    expected_output="[(1, 'Rahim', 'Colonel')]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT NOT NULL, rank TEXT);",
        "INSERT INTO soldiers (name, rank) VALUES ('Rahim', 'Colonel');",
        "SELECT * FROM soldiers;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "📋  Multi‑row Insert – Batch Enlistment\n\n"
        "Create a table `soldiers` (id INTEGER PRIMARY KEY,\n"
        "name TEXT NOT NULL, rank TEXT).\n"
        "Insert three soldiers in ONE statement:\n"
        "  ('Emperor','General')\n"
        "  ('Rahim','Colonel')\n"
        "  ('Karim','Private')\n"
        "Then SELECT all rows sorted by id.\n\n"
        "Expected output:\n[(1, 'Emperor', 'General'), (2, 'Rahim', 'Colonel'), (3, 'Karim', 'Private')]"
    ),
    expected_output="[(1, 'Emperor', 'General'), (2, 'Rahim', 'Colonel'), (3, 'Karim', 'Private')]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT NOT NULL, rank TEXT);",
        "INSERT INTO soldiers (name, rank) VALUES ('Emperor','General'), ('Rahim','Colonel'), ('Karim','Private');",
        "SELECT * FROM soldiers ORDER BY id;"
    ]
)

medium2 = Task(
    description=(
        "🔄  Mixed INSERT – Some Columns Omitted\n\n"
        "The `soldiers` table exists with three rows.\n"
        "Insert a fourth soldier:\n"
        "  name='Ali'\n"
        "  (no rank provided — use NULL)\n"
        "Then SELECT name and rank for all rows.\n\n"
        "Expected output:\n[('Emperor','General'), ('Rahim','Colonel'), ('Karim','Private'), ('Ali',None)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT NOT NULL, rank TEXT);"
        "INSERT INTO soldiers (name, rank) VALUES ('Emperor','General'), ('Rahim','Colonel'), ('Karim','Private');"
    ),
    expected_output="[('Emperor', 'General'), ('Rahim', 'Colonel'), ('Karim', 'Private'), ('Ali', None)]",
    level=Level.MEDIUM,
    hints=[
        "INSERT INTO soldiers (name) VALUES ('Ali');",
        "SELECT name, rank FROM soldiers ORDER BY id;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🆔  RETURNING – Capture Auto‑ID\n\n"
        "Create a table `officers` with columns\n"
        "  • id INTEGER PRIMARY KEY\n"
        "  • name TEXT NOT NULL\n\n"
        "Insert a row with name='Emperor' and\n"
        "use the RETURNING clause to get the\n"
        "generated id.\n\n"
        "Expected output: [(1,)]"
    ),
    expected_output="[(1,)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE officers (id INTEGER PRIMARY KEY, name TEXT NOT NULL);",
        "INSERT INTO officers (name) VALUES ('Emperor') RETURNING id;"
    ],
    note="RETURNING clause is available in SQLite 3.35+. Use it to capture auto‑generated IDs without a separate SELECT."
)

hard2 = Task(
    description=(
        "📊  Batch RETURNING – All New IDs\n\n"
        "The `officers` table already has one row.\n"
        "Insert three more officers in one statement\n"
        "and capture ALL generated IDs using RETURNING.\n"
        "Names: 'Rahim', 'Karim', 'Ali'\n\n"
        "Expected output: [(2,), (3,), (4,)]"
    ),
    setup_sql=(
        "CREATE TABLE officers (id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO officers (name) VALUES ('Emperor');"
    ),
    expected_output="[(2,), (3,), (4,)]",
    level=Level.HARD,
    hints=[
        "INSERT INTO officers (name) VALUES ('Rahim'), ('Karim'), ('Ali') RETURNING id;"
    ],
    note="RETURNING works with multi‑row inserts too. Every generated ID is returned as a separate row."
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L04.json",
        module_name="Module_01_SQL_Core",
        lesson_name="L04_INSERT_INTO"
    )
