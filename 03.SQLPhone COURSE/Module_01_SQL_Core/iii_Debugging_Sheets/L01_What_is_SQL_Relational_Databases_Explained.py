import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE empire (id INTEGER name TEXT);
INSERT INTO empire VALUES (1, 'Emperor');
SELECT * FROM empire;"""

EXPECTED = "[(1, 'Emperor')]"

HINTS = [
    "Look at the CREATE TABLE statement carefully.",
    "Each column definition must be separated by a comma.",
    "id INTEGER, name TEXT"
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L01 – What is SQL?",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
