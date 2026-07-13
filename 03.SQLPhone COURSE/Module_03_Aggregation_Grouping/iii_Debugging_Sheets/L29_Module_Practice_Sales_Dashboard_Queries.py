import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE products (prod_id INTEGER, name TEXT, price REAL);
CREATE TABLE orders (ord_id INTEGER, cust_id INTEGER);
CREATE TABLE order_items (ord_id INTEGER, prod_id INTEGER, quantity INTEGER);
INSERT INTO products VALUES (1,'Laptop',999.99),(2,'Mouse',24.50);
INSERT INTO orders VALUES (1,1);
INSERT INTO order_items VALUES (1,1,1),(1,2,2);
SELECT p.name, SUM(oi.quantity * p.price) AS revenue
FROM products p
JOIN order_items oi ON p.prod_id = oi.prod_id
JOIN orders o ON oi.ord_id = o.ord_id;
"""

EXPECTED = "[('Laptop', 999.99), ('Mouse', 49.0)]"

HINTS = [
    "The query uses SUM() but has no GROUP BY.",
    "Non‑aggregate columns need a GROUP BY clause.",
    "Add GROUP BY p.name at the end."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L29 – Module Practice: Sales Dashboard Queries",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
