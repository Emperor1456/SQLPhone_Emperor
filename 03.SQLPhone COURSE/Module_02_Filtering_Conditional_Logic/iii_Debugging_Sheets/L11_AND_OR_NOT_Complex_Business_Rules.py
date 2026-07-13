import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);
INSERT INTO soldiers VALUES (1,'Emperor','General',5000),(2,'Rahim','Colonel',4000),(3,'Ali','Private',3500);
SELECT * FROM soldiers WHERE rank = 'General' OR 'Colonel';
"""

EXPECTED = "[(1, 'Emperor', 'General', 5000.0), (2, 'Rahim', 'Colonel', 4000.0)]"

HINTS = [
    "The OR operator needs a complete condition on both sides.",
    "rank = 'Colonel' is missing on the right side of OR.",
    "Use: WHERE rank = 'General' OR rank = 'Colonel'"
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L11 – AND, OR, NOT – Complex Business Rules",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
