import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER REFERENCES regiments(id));
CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT);
INSERT INTO regiments VALUES (1,'Red');
INSERT INTO soldiers VALUES (1,'Emperor',1);
SELECT s.name, r.name FROM soldiers s JOIN regiments r ON s.regiment_id = r.id;
"""

EXPECTED = "[('Emperor', 'Red')]"

HINTS = [
    "A table that references another must be created after the referenced table.",
    "Create regiments first, then soldiers.",
    "Swap the order of the CREATE TABLE statements."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L10 – Module 1 Capstone – Imperial Registry Database",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )