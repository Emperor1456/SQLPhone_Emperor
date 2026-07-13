import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE regiments (id INTEGER, name TEXT);
CREATE TABLE soldiers (id INTEGER, name TEXT, regiment_id INTEGER);
INSERT INTO regiments VALUES (1,'Red'),(2,'Blue');
INSERT INTO soldiers VALUES (1,'Emperor',1);
SELECT r.name, s.name FROM regiments r INNER JOIN soldiers s ON r.id = s.regiment_id;
"""

EXPECTED = "[('Red', 'Emperor'), ('Blue', None)]"

HINTS = [
    "You need ALL regiments, even those without soldiers.",
    "INNER JOIN excludes regiments with no matching soldier.",
    "Use LEFT JOIN instead of INNER JOIN."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L33 – LEFT JOIN – All from Left, Match from Right",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
