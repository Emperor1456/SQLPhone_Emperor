import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT);
INSERT INTO products VALUES (1,'Laptop'), (2,'Mouse');
CREATE INDEX idx_product_nme ON products (nme);
SELECT * FROM products WHERE name = 'Laptop';
"""

EXPECTED = "[(1, 'Laptop')]"

HINTS = [
    "The index creation references a non‑existent column.",
    "The column name in the ON clause is misspelled.",
    "Change 'nme' to 'name'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L64 – Index Usage Strategy – When to Index, When Not",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
