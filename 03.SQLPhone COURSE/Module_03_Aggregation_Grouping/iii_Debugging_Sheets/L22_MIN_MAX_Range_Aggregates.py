import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE products (id INTEGER, name TEXT, price REAL);
INSERT INTO products VALUES (1,'Laptop',999.99),(2,'Mouse',24.99),(3,'Keyboard',79.99);
SELECT MIN(price), MAX(price) FROM products;
"""

EXPECTED = "[(24.99, 999.99)]"

HINTS = [
    "The query looks correct, but one function is spelled wrong.",
    "MAX is correct, but MIN is often confused with a similar word.",
    "Check the spelling of MIN — it's M‑I‑N, not MINIMUM."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L22 – MIN, MAX – Range Aggregates",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
