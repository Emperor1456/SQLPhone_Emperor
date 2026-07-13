import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE test (id INTEGER, name TEXT);
INSERT INTO test (1, 'Emperor');
SELECT * FROM test;"""

EXPECTED = "[(1, 'Emperor')]"

HINTS = [
    "The INSERT statement is missing a keyword.",
    "You need the word VALUES before the list of values.",
    "INSERT INTO test VALUES (1, 'Emperor');"
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L04 – INSERT INTO – Single & Multi‑row, RETURNING",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )