import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE soldiers (id INTEGER AUTOINCREMENT, name TEXT);
INSERT INTO soldiers (name) VALUES ('Emperor');
SELECT * FROM soldiers;"""

EXPECTED = "[(1, 'Emperor')]"

HINTS = [
    "AUTOINCREMENT is not a valid standalone keyword in SQLite table definitions.",
    "Use AUTOINCREMENT only after INTEGER PRIMARY KEY, or simply use INTEGER PRIMARY KEY for auto‑increment behaviour.",
    "Change 'INTEGER AUTOINCREMENT' to 'INTEGER PRIMARY KEY AUTOINCREMENT' or just 'INTEGER PRIMARY KEY'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L56 – AUTOINCREMENT vs INTEGER PRIMARY KEY",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
