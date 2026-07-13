import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT);
INSERT INTO soldiers VALUES (1,'Emperor','General'), (2,'Rahim','Colonel');
SELECT name, rank FROM soldiers WHERE rank = 'General;
"""

EXPECTED = "[('Emperor', 'General')]"

HINTS = [
    "Check the WHERE clause carefully.",
    "String literals must be enclosed in matching single quotes.",
    "The closing quote on 'General' is missing."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L05 – SELECT – Projection, DISTINCT, Basic Filtering",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )