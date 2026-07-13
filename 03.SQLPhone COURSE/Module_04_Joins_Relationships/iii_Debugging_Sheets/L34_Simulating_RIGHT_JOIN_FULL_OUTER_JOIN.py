import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE regiments (id INTEGER, name TEXT);
CREATE TABLE soldiers (id INTEGER, name TEXT, regiment_id INTEGER);
INSERT INTO regiments VALUES (1,'Red'),(2,'Blue');
INSERT INTO soldiers VALUES (1,'Emperor',1);
SELECT r.name, s.name FROM regiments r RIGHT JOIN soldiers s ON r.id = s.regiment_id;
"""

EXPECTED = "[('Red', 'Emperor')]"

HINTS = [
    "SQLite does not support RIGHT JOIN directly.",
    "To simulate a RIGHT JOIN, swap the tables and use LEFT JOIN.",
    "Change RIGHT JOIN to LEFT JOIN and swap the table order: FROM soldiers s LEFT JOIN regiments r ON ..."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L34 – Simulating RIGHT JOIN & FULL OUTER JOIN",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
