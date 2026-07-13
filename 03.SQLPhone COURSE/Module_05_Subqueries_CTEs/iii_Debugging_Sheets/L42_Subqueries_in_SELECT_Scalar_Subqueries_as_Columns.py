import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE regiments (id INTEGER, name TEXT);
CREATE TABLE soldiers (id INTEGER, name TEXT, regiment_id INTEGER);
INSERT INTO regiments VALUES (1,'Red'),(2,'Blue');
INSERT INTO soldiers VALUES (1,'Emperor',1),(2,'Rahim',2),(3,'Ali',1);
SELECT r.name,
       (SELECT COUNT(*) FROM soldiers WHERE regiment_id = r.id) AS soldier_count
FROM regiments r;
"""

EXPECTED = "[('Blue', 1), ('Red', 2)]"

HINTS = [
    "The scalar subquery uses 'r.id' correctly correlated, but the outer query is missing an ORDER BY to match expected alphabetical order.",
    "The expected output is sorted by regiment name. Add ORDER BY r.name.",
    "Add ORDER BY r.name at the end of the outer query."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L42 – Subqueries in SELECT – Scalar Subqueries as Columns",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
