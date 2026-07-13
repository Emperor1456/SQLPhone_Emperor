import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);
INSERT INTO soldiers VALUES (1,'Emperor','General',5000),(2,'Rahim','Colonel',4000),(3,'Ali','Private',3500);
SELECT rank, AVG(salary) FROM soldiers GROUP BY rank WHERE salary > 3500;
"""

EXPECTED = "[('Colonel', 4000.0), ('General', 5000.0)]"

HINTS = [
    "The WHERE clause must come before GROUP BY.",
    "Filter rows with WHERE first, then group them.",
    "Move WHERE salary > 3500 before the GROUP BY clause."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L26 – Combining WHERE, GROUP BY & HAVING",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
