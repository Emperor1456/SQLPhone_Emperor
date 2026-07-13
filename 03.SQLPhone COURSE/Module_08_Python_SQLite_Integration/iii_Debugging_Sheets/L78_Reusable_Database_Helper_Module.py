import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT DEFAULT Private);
INSERT INTO soldiers (name, rank) VALUES ('Emperor', 'General');
SELECT * FROM soldiers;"""

EXPECTED = "[(1, 'Emperor', 'General')]"

HINTS = [
    "The DEFAULT value for the rank column is not a string literal.",
    "String defaults must be enclosed in single quotes.",
    "Change `DEFAULT Private` to `DEFAULT 'Private'`."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L78 – Reusable Database Helper Module",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
