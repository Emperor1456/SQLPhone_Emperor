import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE soldiers (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    rank TEXT
);
INSERT INTO soldiers (name, rank) VALUES ('Emperor', 'General');
SELECT * FROM soldiers;"""

EXPECTED = "[(1, 'Emperor', 'General')]"

SETUP = ""

HINTS = [
    "SERIAL is a PostgreSQL‑specific auto‑increment type and is not valid in SQLite.",
    "Use INTEGER PRIMARY KEY instead, which auto‑increments in SQLite.",
    "Replace 'SERIAL PRIMARY KEY' with 'INTEGER PRIMARY KEY'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L91 – SQLite vs PostgreSQL vs MySQL – Choosing Your Engine",
        setup_sql=SETUP,
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
