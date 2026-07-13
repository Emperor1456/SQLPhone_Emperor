import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE soldiers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    rank TEXT DEFAULT 'Private'
);
INSERT INTO soldiers (id, name) VALUES (1, 'Emperor');
SELECT * FROM soldiers;"""

EXPECTED = "[(1, 'Emperor', 'Private')]"

HINTS = [
    "The INSERT provides only two columns, but the table has three. That is allowed if the missing column has a DEFAULT value, which rank does. So the SQL is actually correct. To create a bug, I'll make the default value missing: remove the DEFAULT clause, then the INSERT will fail due to NOT NULL constraint (rank has no default and is not nullable). Fix: add DEFAULT 'Private' to the rank column, but it's already there. Instead, I'll change the INSERT to omit the column list altogether: INSERT INTO soldiers VALUES (1, 'Emperor'); That will fail because two values are provided but three columns exist. The fix is to include the rank value. Let's adjust BROKEN.",
    "The broken code will be: INSERT INTO soldiers VALUES (1, 'Emperor'); (only two values). Correct by adding the third value, e.g., (1, 'Emperor', 'General') or keep the rank default if the table has it. I'll have the table without DEFAULT, so the INSERT must include all columns.",
    "Modify the INSERT to: INSERT INTO soldiers VALUES (1, 'Emperor', 'General');"
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L94 – ORMs – SQLAlchemy & Django ORM Introduction",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
