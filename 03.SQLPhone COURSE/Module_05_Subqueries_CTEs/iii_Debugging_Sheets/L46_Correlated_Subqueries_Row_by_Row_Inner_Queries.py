import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE regiments (id INTEGER, name TEXT);
CREATE TABLE soldiers (id INTEGER, name TEXT, regiment_id INTEGER);
INSERT INTO regiments VALUES (1,'Red'),(2,'Blue');
INSERT INTO soldiers VALUES (1,'Emperor',1),(2,'Rahim',2),(3,'Ali',1);
SELECT name FROM regiments r
WHERE 2 <= (SELECT COUNT(*) FROM soldiers WHERE regiment_id = regiment_id);
"""

EXPECTED = "[('Red',)]"

HINTS = [
    "The correlated subquery uses the same column name on both sides of the equality.",
    "It should reference the outer table's id and the inner table's regiment_id.",
    "Change 'regiment_id = regiment_id' to 'regiment_id = r.id'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L46 – Correlated Subqueries – Row‑by‑Row Inner Queries",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
