import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE soldiers (id INTEGER, name TEXT, salary REAL);
INSERT INTO soldiers VALUES (1,'Emperor',5000),(2,'Rahim',4000),(3,'Ali',3500);
SELECT COUNT(salary), SUM(salary), AVG(salary) FROM soldiers;
"""

EXPECTED = "[(3, 12500.0, 4166.66666666667)]"

HINTS = [
    "Aggregate functions are fine, but the output has no column names — that's not the bug.",
    "Look at the COUNT function. It counts non‑NULL values. Is salary NULL anywhere? No.",
    "The bug is elsewhere: the query is correct. So what's wrong? Actually, the query is fine. So the real bug must be that AVG is misspelled? Check spelling of AVG."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L21 – COUNT, SUM, AVG – Basic Aggregates",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
