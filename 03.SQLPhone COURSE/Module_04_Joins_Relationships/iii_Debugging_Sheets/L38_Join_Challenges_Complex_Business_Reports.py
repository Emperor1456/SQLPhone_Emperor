import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE customers (id INTEGER, name TEXT);
CREATE TABLE orders (id INTEGER, cust_id INTEGER, total REAL);
INSERT INTO customers VALUES (1,'Karim'),(2,'Fatima');
INSERT INTO orders VALUES (1,1,100.0),(2,1,200.0),(3,2,50.0);
SELECT c.name, SUM(o.total) FROM customers c JOIN orders o ON c.id = o.cust_id;
"""

EXPECTED = "[('Fatima', 50.0), ('Karim', 300.0)]"

HINTS = [
    "The query uses SUM() but has no GROUP BY.",
    "Aggregate with non‑aggregate column needs GROUP BY.",
    "Add GROUP BY c.name and ORDER BY c.name."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L38 – Join Challenges – Complex Business Reports",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
