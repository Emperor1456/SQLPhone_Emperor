import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE test (id INTEGER); /* this comment is not closed
INSERT INTO test VALUES (1);
SELECT * FROM test;"""

EXPECTED = "[(1,)]"

HINTS = [
    "Look at the comment syntax – something is missing.",
    "Multi‑line comments must be closed with */.",
    "Add */ after the comment text."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L08 – SQL Comments & Professional Formatting",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )