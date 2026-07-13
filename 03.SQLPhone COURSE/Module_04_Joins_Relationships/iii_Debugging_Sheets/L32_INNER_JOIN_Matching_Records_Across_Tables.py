import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE regiments (id INTEGER, name TEXT);
CREATE TABLE soldiers (id INTEGER, name TEXT, regiment_id INTEGER);
INSERT INTO regiments VALUES (1,'Red'),(2,'Blue');
INSERT INTO soldiers VALUES (1,'Emperor',1),(2,'Rahim',2);
SELECT s.name, r.name FROM soldiers s INNER JOIN regiments r;
"""

EXPECTED = "[('Emperor', 'Red'), ('Rahim', 'Blue')]"

HINTS = [
    "The INNER JOIN is missing its ON condition.",
    "Without the ON clause, all rows are joined (Cartesian product).",
    "Add ON s.regiment_id = r.id."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L32 – INNER JOIN – Matching Records Across Tables",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
