import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "✅  When to Index – Column in WHERE\n\n"
        "Create a table `products` with columns:\n"
        "  • id INTEGER, name TEXT, category TEXT, price REAL.\n"
        "Insert 6 rows.\n"
        "Create an index on the `category` column (often used\n"
        "in WHERE clause).\n"
        "Run EXPLAIN QUERY PLAN on a SELECT that filters\n"
        "by category. You should see SEARCH using the index.\n\n"
        "Expected output:\n[('SEARCH TABLE products USING INDEX idx_products_category',)]"
    ),
    expected_output="[('SEARCH TABLE products USING INDEX idx_products_category',)]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE products (id INTEGER, name TEXT, category TEXT, price REAL);",
        "INSERT INTO products VALUES (1,'Laptop','Electronics',1000), (2,'Mouse','Electronics',50), (3,'Desk','Furniture',500), (4,'Chair','Furniture',250), (5,'Monitor','Electronics',300), (6,'Pen','Office',5);",
        "CREATE INDEX idx_products_category ON products(category);",
        "EXPLAIN QUERY PLAN SELECT * FROM products WHERE category = 'Electronics';"
    ]
)

easy2 = Task(
    description=(
        "❌  When NOT to Index – Low Cardinality\n\n"
        "Create a table `employees` with columns:\n"
        "  • id INTEGER, name TEXT, gender TEXT (only 'M' or 'F').\n"
        "Insert 10 rows (all 'M' or 'F').\n"
        "Do NOT create an index on gender.\n"
        "Run EXPLAIN QUERY PLAN on a SELECT filtering\n"
        "by gender. Even without an index, a SCAN may be\n"
        "chosen because low cardinality doesn't benefit\n"
        "from an index. Show the plan.\n\n"
        "Expected output:\n[('SCAN TABLE employees',)]"
    ),
    expected_output="[('SCAN TABLE employees',)]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE employees (id INTEGER, name TEXT, gender TEXT);",
        "INSERT INTO employees VALUES (1,'A','M'), (2,'B','F'), (3,'C','M'), (4,'D','F'), (5,'E','M'), (6,'F','M'), (7,'G','F'), (8,'H','M'), (9,'I','F'), (10,'J','M');",
        "EXPLAIN QUERY PLAN SELECT * FROM employees WHERE gender = 'M';"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🧱  Composite Index Strategy – Column Order\n\n"
        "Create a table `shipments` with columns:\n"
        "  id, destination TEXT, status TEXT, weight REAL.\n"
        "Insert 8 rows with varied data.\n"
        "Create a composite index on (status, destination).\n"
        "Explain a query that filters on both columns.\n"
        "Then explain a query that filters ONLY on destination\n"
        "(the second column in the index).\n"
        "Show both plan outputs: the first should use the index,\n"
        "the second may not (because destination is not the\n"
        "first column in the index).\n\n"
        "Expected output:\n[('SEARCH TABLE shipments USING INDEX idx_shipments_status_dest',), ('SCAN TABLE shipments',)]"
    ),
    expected_output="[('SEARCH TABLE shipments USING INDEX idx_shipments_status_dest',), ('SCAN TABLE shipments',)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE shipments (id INTEGER, destination TEXT, status TEXT, weight REAL);",
        "INSERT INTO shipments VALUES (1,'Dhaka','delivered',12), (2,'Chittagong','in transit',8), (3,'Dhaka','pending',5), (4,'Sylhet','delivered',10), (5,'Khulna','in transit',7), (6,'Dhaka','delivered',15), (7,'Chittagong','pending',9), (8,'Sylhet','in transit',11);",
        "CREATE INDEX idx_shipments_status_dest ON shipments(status, destination);",
        "EXPLAIN QUERY PLAN SELECT * FROM shipments WHERE status = 'delivered' AND destination = 'Dhaka';",
        "EXPLAIN QUERY PLAN SELECT * FROM shipments WHERE destination = 'Dhaka';"
    ]
)

medium2 = Task(
    description=(
        "⚖️  Index Trade‑off – Write Performance\n\n"
        "Create a table `logs` with columns:\n"
        "  • id INTEGER PRIMARY KEY, msg TEXT.\n"
        "Create an index on `msg`.\n"
        "Insert 10 rows (writes are slower because index\n"
        "must be updated). Then count the rows.\n"
        "Explain that each INSERT also updates the index.\n\n"
        "Expected output: [(10,)]"
    ),
    expected_output="[(10,)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE logs (id INTEGER PRIMARY KEY, msg TEXT);",
        "CREATE INDEX idx_logs_msg ON logs(msg);",
        "INSERT INTO logs (msg) VALUES ('a'),('b'),('c'),('d'),('e'),('f'),('g'),('h'),('i'),('j');",
        "SELECT COUNT(*) FROM logs;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  Design Index Strategy – Given Queries\n\n"
        "You are given a table `orders` with columns:\n"
        "  order_id, customer_id, product_id, order_date, amount.\n"
        "The following queries run frequently:\n"
        "  1. SELECT * FROM orders WHERE customer_id = ?\n"
        "  2. SELECT * FROM orders WHERE order_date BETWEEN ? AND ?\n"
        "  3. SELECT * FROM orders WHERE customer_id = ? AND order_date >= ?\n"
        "Create the MINIMUM set of indexes to optimize all three.\n"
        "(Hint: A composite index on (customer_id, order_date) covers\n"
        "all three.)\n"
        "Create the table, insert sample data, create the composite\n"
        "index, then EXPLAIN each of the three queries.\n"
        "Return all three plan outputs.\n\n"
        "Expected output:\n[('SEARCH TABLE orders USING INDEX idx_orders_cust_date',), ('SEARCH TABLE orders USING INDEX idx_orders_cust_date',), ('SEARCH TABLE orders USING INDEX idx_orders_cust_date',)]"
    ),
    expected_output="[('SEARCH TABLE orders USING INDEX idx_orders_cust_date',), ('SEARCH TABLE orders USING INDEX idx_orders_cust_date',), ('SEARCH TABLE orders USING INDEX idx_orders_cust_date',)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE orders (order_id INTEGER PRIMARY KEY, customer_id INTEGER, product_id INTEGER, order_date TEXT, amount REAL);",
        "INSERT INTO orders VALUES (1,1,1,'2026-01-15',100), (2,2,2,'2026-02-20',200), (3,1,3,'2026-03-10',300);",
        "CREATE INDEX idx_orders_cust_date ON orders(customer_id, order_date);",
        "EXPLAIN QUERY PLAN SELECT * FROM orders WHERE customer_id = 1;",
        "EXPLAIN QUERY PLAN SELECT * FROM orders WHERE order_date BETWEEN '2026-01-01' AND '2026-03-31';",
        "EXPLAIN QUERY PLAN SELECT * FROM orders WHERE customer_id = 1 AND order_date >= '2026-02-01';"
    ]
)

hard2 = Task(
    description=(
        "📊  Analyze a Workload – Index Recommendations\n\n"
        "Create a table `analytics` with columns:\n"
        "  id, user_id, event_type, event_date, value.\n"
        "The following queries are run 1000x/day:\n"
        "  A: SELECT * FROM analytics WHERE user_id = ?\n"
        "  B: SELECT * FROM analytics WHERE event_type = ? AND event_date >= ?\n"
        "  C: SELECT * FROM analytics ORDER BY event_date DESC LIMIT 100\n"
        "Create indexes to optimize A, B, and C with as few\n"
        "indexes as possible.\n"
        "Create the table, insert 5 rows, create the indexes,\n"
        "then EXPLAIN each query.\n\n"
        "Expected output:\n[('SEARCH TABLE analytics USING INDEX idx_analytics_user',), ('SEARCH TABLE analytics USING INDEX idx_analytics_type_date',), ('SCAN TABLE analytics USING INDEX idx_analytics_date',)]"
    ),
    expected_output="[('SEARCH TABLE analytics USING INDEX idx_analytics_user',), ('SEARCH TABLE analytics USING INDEX idx_analytics_type_date',), ('SCAN TABLE analytics USING INDEX idx_analytics_date',)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE analytics (id INTEGER PRIMARY KEY, user_id INTEGER, event_type TEXT, event_date TEXT, value REAL);",
        "INSERT INTO analytics VALUES (1,1,'click','2026-07-01',10), (2,2,'view','2026-07-02',20), (3,1,'click','2026-07-03',30), (4,3,'purchase','2026-07-04',40), (5,2,'click','2026-07-05',50);",
        "CREATE INDEX idx_analytics_user ON analytics(user_id);",
        "CREATE INDEX idx_analytics_type_date ON analytics(event_type, event_date);",
        "CREATE INDEX idx_analytics_date ON analytics(event_date);",
        "EXPLAIN QUERY PLAN SELECT * FROM analytics WHERE user_id = 1;",
        "EXPLAIN QUERY PLAN SELECT * FROM analytics WHERE event_type = 'click' AND event_date >= '2026-07-01';",
        "EXPLAIN QUERY PLAN SELECT * FROM analytics ORDER BY event_date DESC LIMIT 100;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L64.json",
        module_name="Module_07_Views_Optimization_Security",
        lesson_name="L64_Index_Usage_Strategy"
    )
