import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);
INSERT INTO soldiers VALUES (1,'Emperor','General',5000),(2,'Rahim','Colonel',4000),(3,'Ali','Private',3500);
SELECT rank, AVG(salary) AS avg_sal FROM soldiers GROUP BY rank WHERE AVG(salary) > 4000;
"""

EXPECTED = "[('General', 5000.0)]"

HINTS = [
    "WHERE clause cannot be used with aggregate functions.",
    "Use HAVING instead of WHERE when filtering groups.",
    "Replace WHERE with HAVING."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L25 – HAVING – Filtering Groups",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
