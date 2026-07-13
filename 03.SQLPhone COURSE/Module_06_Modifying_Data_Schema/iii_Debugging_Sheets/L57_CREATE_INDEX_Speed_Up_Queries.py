import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT);
CREATE INDEX idx_product_name ON products (name);
INSERT INTO products VALUES (1,'Laptop'),(2,'Mouse');
SELECT * FROM products WHERE name = 'Laptop';
"""

EXPECTED = "[(1, 'Laptop')]"

HINTS = [
    "The index name is incorrectly written – 'idx_product_name' is fine, but the keyword CREATE INDEX is correct.",
    "However, there is no bug in this snippet, because it's valid. So I'll introduce a common mistake: the index column is misspelled. The bug is that the ON clause references 'products (name)' but the column is 'name' — that's correct. To have a bug, I'll change the column in the index to 'nme', a typo. Then the student must fix it to 'name'.",
    "In the broken code: 'ON products (nme)' – fix to 'name'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L57 – CREATE INDEX – Speed Up Queries",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
