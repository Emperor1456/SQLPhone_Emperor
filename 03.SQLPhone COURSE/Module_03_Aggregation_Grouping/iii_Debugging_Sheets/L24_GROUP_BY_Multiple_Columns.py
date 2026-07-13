import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE orders (id INTEGER, region TEXT, product TEXT, amount REAL);
INSERT INTO orders VALUES (1,'North','Laptop',999.99),(2,'North','Mouse',24.99),(3,'South','Laptop',899.99);
SELECT region, product, SUM(amount) FROM orders GROUP BY region;
"""

EXPECTED = "[('North', 'Laptop', 1024.98), ('South', 'Laptop', 899.99)]"

HINTS = [
    "The GROUP BY clause is missing a column.",
    "You're selecting product but only grouping by region.",
    "Add product to GROUP BY: GROUP BY region, product."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L24 – GROUP BY – Multiple Columns",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
