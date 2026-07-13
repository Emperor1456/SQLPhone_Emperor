import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE products (id INTEGER, name TEXT, price TEXT);
INSERT INTO products VALUES (1,'Laptop','999.99'),(2,'Mouse','24.50');
SELECT name, CAST(price INT) AS price_int FROM products;
"""

EXPECTED = "[('Laptop', 999), ('Mouse', 24)]"

HINTS = [
    "Check the CAST syntax – you need a keyword between the value and the target type.",
    "CAST(price AS INT)",
    "Add the word AS."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L19 – Mathematical Functions & CAST",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
