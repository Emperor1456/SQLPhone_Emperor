import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);
INSERT INTO soldiers VALUES (1,'Emperor','General',5000),(2,'Rahim','Colonel',4000),(3,'Ali','Private',3500);
SELECT SUM(CASE WHEN rank = 'General' THEN salary ELSE 0) AS total_general_salary FROM soldiers;
"""

EXPECTED = "[(5000.0,)]"

HINTS = [
    "The CASE expression inside the SUM is not closed.",
    "Every CASE must end with END.",
    "Add END after ELSE 0, before the closing parenthesis of SUM."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L27 – Aggregation with CASE – Conditional Sums",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
