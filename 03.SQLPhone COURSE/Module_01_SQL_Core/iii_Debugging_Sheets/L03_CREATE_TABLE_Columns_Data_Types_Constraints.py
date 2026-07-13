import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE soldiers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    rank TEXT DEFAULT Private,
    salary REAL CHECK(salary > 0)
);"""

EXPECTED = "[]"

HINTS = [
    "Check the DEFAULT value for the rank column.",
    "String literals need single quotes in SQL.",
    "DEFAULT 'Private'"
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L03 – CREATE TABLE Columns, Data Types & Constraints",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )