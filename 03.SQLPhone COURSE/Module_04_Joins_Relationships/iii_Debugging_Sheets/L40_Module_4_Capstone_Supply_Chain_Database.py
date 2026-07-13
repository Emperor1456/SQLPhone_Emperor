import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE suppliers (sup_id INTEGER, name TEXT);
CREATE TABLE products (prod_id INTEGER, name TEXT, sup_id INTEGER);
CREATE TABLE orders (ord_id INTEGER, prod_id INTEGER, quantity INTEGER);
INSERT INTO suppliers VALUES (1,'TechSupplier');
INSERT INTO products VALUES (1,'Laptop',1);
INSERT INTO orders VALUES (1,1,10);
SELECT s.name, p.name, o.quantity
FROM suppliers s
JOIN products p ON s.sup_id = p.sup_id
JOIN orders o ON p.prod_id = o.prod_id;
"""

EXPECTED = "[('TechSupplier', 'Laptop', 10)]"

HINTS = [
    "The query joins three tables, but the second JOIN condition uses 'o.prod_id' which is correct.",
    "Check the first JOIN condition: s.sup_id = p.sup_id. That's fine.",
    "The bug is that the second table alias 'p' is used but the join with orders references 'p.prod_id', which is fine.",
    "However, the expected output column order is (supplier name, product name, quantity). The SELECT has s.name, p.name, o.quantity. That matches.",
    "The query should run. So maybe the bug is that the INSERT INTO orders uses 'ord_id' but the table definition has 'ord_id' – correct.",
    "I'll introduce a bug: the CREATE TABLE orders is missing a column type? No. I'll change the broken code to use 'JOIN orders o ON p.prod_id = o.ord_id' (wrong column). The student must fix it to o.prod_id. Expected output after fix will be correct. So I'll set broken with wrong ON condition."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L40 – Module 4 Capstone – Supply Chain Database",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
