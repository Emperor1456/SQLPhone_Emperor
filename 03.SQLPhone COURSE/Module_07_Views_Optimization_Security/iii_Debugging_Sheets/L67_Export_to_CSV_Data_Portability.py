import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price REAL);
INSERT INTO products VALUES (1,'Laptop',999.99),(2,'Mouse',24.99);
.mode csv
SELECT * FROM products;
"""

EXPECTED = "[(1, 'Laptop', 999.99), (2, 'Mouse', 24.99)]"

HINTS = [
    "The .mode csv command is a dot‑command that only works in the SQLite shell, not in standard SQL.",
    "Remove the .mode csv line to make the script executable.",
    "Just delete the .mode csv line."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L67 – Export to CSV – Data Portability",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
