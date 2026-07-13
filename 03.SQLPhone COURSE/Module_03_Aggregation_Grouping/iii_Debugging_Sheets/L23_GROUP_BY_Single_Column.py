import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);
INSERT INTO soldiers VALUES (1,'Emperor','General',5000),(2,'Rahim','Colonel',4000),(3,'Ali','Private',3500);
SELECT rank, AVG(salary) FROM soldiers;
"""

EXPECTED = "[('Colonel', 4000.0), ('General', 5000.0), ('Private', 3500.0)]"

HINTS = [
    "You're selecting rank and an aggregate function without GROUP BY.",
    "Aggregate functions with non‑aggregate columns require GROUP BY.",
    "Add GROUP BY rank at the end."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L23 – GROUP BY – Single Column",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
