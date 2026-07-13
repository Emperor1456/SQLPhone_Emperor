import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, price REAL CHECK(price > 0));
INSERT INTO products VALUES (1, 'Laptop', -100);
SELECT * FROM products;"""

EXPECTED = "[(1, 'Laptop', 999.99)]"

SETUP = ""

HINTS = [
    "The INSERT violates the CHECK constraint (price must be positive).",
    "Change the price to a positive value, e.g., 999.99.",
    "Modify the INSERT VALUES to (1, 'Laptop', 999.99)."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L54 – Constraints Deep Dive – NOT NULL, UNIQUE, CHECK, DEFAULT",
        setup_sql=SETUP,
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
