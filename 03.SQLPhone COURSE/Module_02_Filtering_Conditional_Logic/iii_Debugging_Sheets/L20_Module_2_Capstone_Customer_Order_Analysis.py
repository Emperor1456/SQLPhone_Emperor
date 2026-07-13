import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE customers (cust_id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE orders (ord_id INTEGER PRIMARY KEY, cust_id INTEGER);
CREATE TABLE products (prod_id INTEGER PRIMARY KEY, name TEXT, price REAL);
CREATE TABLE order_items (ord_id INTEGER, prod_id INTEGER, quantity INTEGER);
INSERT INTO customers VALUES (1,'Karim'),(2,'Fatima');
INSERT INTO orders VALUES (1,1),(2,2);
INSERT INTO products VALUES (1,'Laptop',999.99),(2,'Mouse',24.50);
INSERT INTO order_items VALUES (1,1,1),(2,2,2);
SELECT c.name, SUM(oi.quantity * p.price) total_spent
FROM customers c
JOIN orders o ON c.cust_id = o.cust_id
JOIN order_items oi ON o.ord_id = oi.ord_id
JOIN products p ON oi.prod_id = p.prod_id
GROUP BY c.name
ORDER BY total_spent;
"""

EXPECTED = "[('Karim', 999.99), ('Fatima', 49.0)]"

HINTS = [
    "The bug is in the ORDER BY clause.",
    "The alias 'total_spent' is not recognised – SQLite needs the exact expression.",
    "Replace ORDER BY total_spent with ORDER BY SUM(oi.quantity * p.price)."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L20 – Module 2 Capstone – Customer Order Analysis",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
