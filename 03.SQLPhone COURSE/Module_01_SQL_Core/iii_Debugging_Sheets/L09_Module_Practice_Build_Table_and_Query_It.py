import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE inventory (id INTEGER PRIMARY KEY name TEXT, quantity INTEGER);
INSERT INTO inventory VALUES (1,'Sword',10);
SELECT * FROM inventory;"""

EXPECTED = "[(1, 'Sword', 10)]"

HINTS = [
    "Check the column definitions in CREATE TABLE.",
    "Each column definition must be separated by a comma.",
    "Add a comma after PRIMARY KEY."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L09 – Module Practice: Build a Table and Query It",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )