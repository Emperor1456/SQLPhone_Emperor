import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE items (id INTEGER, category TEXT);
INSERT INTO items VALUES (1,'A'), (2,'B'), (3,'A');
SELECT * FROM items WHERE category = A;
"""

EXPECTED = "[(1, 'A'), (3, 'A')]"

HINTS = [
    "Look at the WHERE clause – how is the category value written?",
    "String values in SQL must be quoted.",
    "Use 'A' instead of A."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L06 – WHERE – Comparison Operators & Logical Precedence",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )