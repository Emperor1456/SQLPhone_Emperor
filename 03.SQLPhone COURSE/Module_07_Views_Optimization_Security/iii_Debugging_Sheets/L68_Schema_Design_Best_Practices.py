import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_name TEXT,
    product_name TEXT,
    quantity INTEGER
);
INSERT INTO orders VALUES (1,'Emperor','Laptop',1);
SELECT * FROM orders;
"""

EXPECTED = "[(1, 'Emperor', 'Laptop', 1)]"

HINTS = [
    "This table design violates normalization principles: it embeds customer and product names directly.",
    "The fix is to split into multiple tables (customers, products, orders) with foreign keys.",
    "Create separate tables: customers(id, name), products(id, name), orders(id, customer_id, product_id, quantity)."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L68 – Schema Design Best Practices",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
