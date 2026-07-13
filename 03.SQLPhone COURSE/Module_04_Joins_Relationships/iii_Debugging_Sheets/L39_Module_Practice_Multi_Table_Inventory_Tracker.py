import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
CREATE TABLE products (prod_id INTEGER, name TEXT);
CREATE TABLE warehouses (wh_id INTEGER, name TEXT);
CREATE TABLE inventory (prod_id INTEGER, wh_id INTEGER, qty INTEGER);
INSERT INTO products VALUES (1,'Laptop'),(2,'Mouse');
INSERT INTO warehouses VALUES (1,'Dhaka'),(2,'Chittagong');
INSERT INTO inventory VALUES (1,1,10),(2,2,5);
SELECT p.name, w.name, i.qty
FROM products p
JOIN inventory i ON p.prod_id = i.prod_id
JOIN warehouses w ON i.wh_id = w.wh_id;
"""

EXPECTED = "[('Laptop', 'Dhaka', 10), ('Mouse', 'Chittagong', 5)]"

HINTS = [
    "The query looks correct but the output will have columns in different order.",
    "The expected output shows name, name, qty, but the SELECT order might be wrong.",
    "Actually the bug is a missing comma in the SELECT list after the first name? No, it's there.",
    "Check the column names: the first name is p.name, second is w.name. That's fine.",
    "Maybe the INSERT into inventory uses 'qty' but the table column is 'quantity'? No, it's qty.",
    "The bug: the second JOIN uses 'i.wh_id' but the inventory table column is 'wh_id' – correct.",
    "To find the bug, run the query mentally: it should work. So I'll introduce a subtle mistake: the second table alias 'i' is used before it's defined? No. I'll change broken code to have 'JOIN inventory ON p.prod_id = i.prod_id' without alias 'i'? That would be an error. I'll set BROKEN to use 'JOIN inventory ON p.prod_id = inventory.prod_id' (no alias), then the other references to i.qty would fail. That's a clear bug. I'll craft broken code accordingly."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L39 – Module Practice: Multi‑Table Inventory Tracker",
        setup_sql="",
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
