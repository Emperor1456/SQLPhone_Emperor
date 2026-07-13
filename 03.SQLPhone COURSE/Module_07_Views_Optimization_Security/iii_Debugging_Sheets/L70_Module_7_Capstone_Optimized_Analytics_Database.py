import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE sales (id INTEGER PRIMARY KEY, product TEXT, amount REAL, sale_date TEXT);
INSERT INTO sales VALUES (1,'Laptop',999.99,'2026-07-01'),(2,'Mouse',24.99,'2026-07-02');
CREATE INDEX idx_sales_product ON sales (product);
SELECT product, SUM(amount) FROM sales GROUP BY product;
"""

EXPECTED = "[('Laptop', 999.99), ('Mouse', 24.99)]"

HINTS = [
    "The SUM(amount) column has no alias, but that's not an error. The bug is that the index creation syntax is wrong.",
    "The CREATE INDEX statement misses the table name after ON.",
    "Should be: CREATE INDEX idx_sales_product ON sales(product);"
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L70 – Module 7 Capstone – Optimized Analytics Database",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
