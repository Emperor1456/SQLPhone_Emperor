import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER REFERENCES regiment(id));
INSERT INTO regiments VALUES (1,'Red');
INSERT INTO soldiers VALUES (1,'Emperor',1);
SELECT * FROM soldiers;
"""

EXPECTED = "[(1, 'Emperor', 1)]"

HINTS = [
    "The foreign key references a table name that doesn't match.",
    "The table is named 'regiments', not 'regiment'.",
    "Change REFERENCES regiment(id) to REFERENCES regiments(id)."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L31 – Foreign Keys & Referential Integrity",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
