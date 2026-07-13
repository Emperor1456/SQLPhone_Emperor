import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE soldiers (id INTEGER, name TEXT, salary REAL);
INSERT INTO soldiers VALUES (1,'Emperor',5000),(2,'Rahim',4000);
SELECT name, salary * 1.1 new_salary FROM soldiers;
"""

EXPECTED = "[('Emperor', 5500.0), ('Rahim', 4400.0)]"

HINTS = [
    "The computed column is missing the AS keyword.",
    "Aliases for computed columns require AS.",
    "Use: salary * 1.1 AS new_salary"
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L14 – Aliases (AS) & Computed Columns",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
