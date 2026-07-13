import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE test (id INTEGER);
INSERT INTO test VALUES (42)
SELECT * FROM test;"""

EXPECTED = "[(42,)]"

HINTS = [
    "The script contains multiple statements. One statement is missing a terminator.",
    "Each SQL statement should end with a semicolon.",
    "Add a semicolon after the INSERT line."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L76 – Executing .sql Files from Python",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
