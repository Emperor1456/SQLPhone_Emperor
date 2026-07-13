import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE weapons (id INTEGER, name, power_level INTEGER);
INSERT INTO weapons VALUES (1, 'Laser', 5);
SELECT * FROM weapons;"""

EXPECTED = "[(1, 'Laser', 5)]"

HINTS = [
    "The `name` column is missing a data type.",
    "Every column must have a declared type.",
    "Add `TEXT` after `name`."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L72 – Creating Tables via Python",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
