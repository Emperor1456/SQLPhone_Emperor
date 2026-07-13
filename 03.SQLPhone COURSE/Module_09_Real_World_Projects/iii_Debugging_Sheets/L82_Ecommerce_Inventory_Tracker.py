import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
UPDATE products
SET stock = stock - 3
WHERE product_id = 1;

SELECT name, stock FROM products WHERE product_id = 1;"""

EXPECTED = "[(147,)]"

SETUP = """\
CREATE TABLE suppliers (supplier_id INTEGER PRIMARY KEY, name TEXT NOT NULL);
INSERT INTO suppliers VALUES (1,'TechSupplier Inc.');
CREATE TABLE products (product_id INTEGER PRIMARY KEY, name TEXT NOT NULL, supplier_id INTEGER, price REAL CHECK(price > 0), stock INTEGER DEFAULT 0 CHECK(stock >= 0), FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id));
INSERT INTO products VALUES (1,'Wireless Mouse',1,24.99,150);"""

HINTS = [
    "The expected output shows only the stock value, but the SELECT returns two columns (name, stock).",
    "Remove the name column from the SELECT clause to match the expected output.",
    "Change 'SELECT name, stock' to 'SELECT stock'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L82 – E‑commerce Inventory Tracker",
        setup_sql=SETUP,
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
