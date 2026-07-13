import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE test (id INTEGER, name TEXT);
INSERT INTO test VALUES (1 'Emperor');
SELECT * FROM test;"""

EXPECTED = "[(1, 'Emperor')]"

HINTS = [
    "Check the INSERT statement syntax.",
    "In SQL, values must be separated by commas.",
    "INSERT INTO test VALUES (1, 'Emperor');"
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L02 – Installing SQLite & Your First Database",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )