import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE products (id INTEGER, name TEXT, price REAL);
INSERT INTO products VALUES (1,'Laptop',999.99),(2,'Mouse',24.99),(3,'Keyboard',79.99);
SELECT * FROM products WHERE price BETWEEN 25 AND 100;
"""

EXPECTED = "[(2, 'Mouse', 24.99), (3, 'Keyboard', 79.99)]"

HINTS = [
    "BETWEEN is inclusive, but 24.99 is not between 25 and 100.",
    "The lower bound should include 24.99.",
    "Change the lower bound to 24 or a value less than 24.99."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L12 – BETWEEN, IN, LIKE – Range, Membership, Patterns",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
