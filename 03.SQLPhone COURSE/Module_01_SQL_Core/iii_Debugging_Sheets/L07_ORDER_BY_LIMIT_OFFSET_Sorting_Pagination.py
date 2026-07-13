import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE nums (val INTEGER);
INSERT INTO nums VALUES (3), (1), (2);
SELECT val FROM nums LIMIT 2 ORDER BY val;
"""

EXPECTED = "[(1,), (2,)]"

HINTS = [
    "The order of clauses matters in a SELECT statement.",
    "ORDER BY must come before LIMIT.",
    "Correct: SELECT val FROM nums ORDER BY val LIMIT 2;"
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L07 – ORDER BY, LIMIT & OFFSET – Sorting & Pagination",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )