import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🧱  Simple CTE – High‑Paid Soldiers\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Write a query using a CTE named `high_paid` that\n"
        "selects soldiers with salary > 4000.\n"
        "Then SELECT all columns from that CTE.\n"
        "Sort by name.\n\n"
        "Expected output:\n[('Ali',4500.0), ('Emperor',5000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[('Ali', 4500.0), ('Emperor', 5000.0)]",
    level=Level.EASY,
    hints=[
        "WITH high_paid AS (SELECT name, salary FROM soldiers WHERE salary > 4000) SELECT * FROM high_paid ORDER BY name;"
    ]
)

easy2 = Task(
    description=(
        "📊  CTE with Aggregation – Average Salary per Rank\n\n"
        "The same `soldiers` table.\n"
        "Write a query using a CTE named `rank_avg` that\n"
        "computes the average salary for each rank.\n"
        "Then SELECT from the CTE, showing ranks with avg > 3000.\n"
        "Sort by avg_salary descending.\n\n"
        "Expected output:\n[('General',4750.0), ('Colonel',3750.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[('General', 4750.0), ('Colonel', 3750.0)]",
    level=Level.EASY,
    hints=[
        "WITH rank_avg AS (SELECT rank, AVG(salary) AS avg_salary FROM soldiers GROUP BY rank) SELECT * FROM rank_avg WHERE avg_salary > 3000 ORDER BY avg_salary DESC;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🧪  Two CTEs – Regiment Stats + Filter\n\n"
        "Create tables `regiments` and `soldiers` with salaries.\n"
        "Write a query using TWO CTEs:\n"
        "  1. `regiment_stats`: computes AVG(salary) per regiment_id\n"
        "  2. `high_avg`: selects regiments with avg_salary > 3500\n"
        "Then SELECT soldiers from regiments in `high_avg`.\n"
        "Return soldier name, regiment_id, and salary.\n"
        "Sort by name.\n\n"
        "Expected output:\n[('Emperor',1,5000.0), ('Hasan',1,3500.0)]"
    ),
    expected_output="[('Emperor', 1, 5000.0), ('Hasan', 1, 3500.0)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard');",
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER, salary REAL);",
        "INSERT INTO soldiers VALUES (1,'Emperor',1,5000), (2,'Rahim',2,4000), (3,'Ali',2,3500), (4,'Hasan',1,3500);",
        "WITH regiment_stats AS (SELECT regiment_id, AVG(salary) AS avg_sal FROM soldiers GROUP BY regiment_id), high_avg AS (SELECT regiment_id FROM regiment_stats WHERE avg_sal > 3500) SELECT name, regiment_id, salary FROM soldiers WHERE regiment_id IN (SELECT regiment_id FROM high_avg) ORDER BY name;"
    ]
)

medium2 = Task(
    description=(
        "📋  CTE for Readability – Customer Spending\n\n"
        "Create `customers`, `products`, `orders` tables.\n"
        "Use a CTE named `customer_spending` to compute\n"
        "each customer's total spending (SUM of qty*price).\n"
        "Then SELECT customers whose total_spent > 500,\n"
        "showing name and total_spent.\n"
        "Sort by total_spent descending.\n\n"
        "Expected output:\n[('Emperor',2080.0), ('Ali',900.0), ('Rahim',250.0)]"
    ),
    setup_sql=(
        "CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT);"
        "INSERT INTO customers VALUES (1,'Emperor'), (2,'Rahim'), (3,'Ali');"
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price REAL);"
        "INSERT INTO products VALUES (1,'Laptop',1000), (2,'Mouse',50), (3,'Keyboard',80), (4,'Monitor',300);"
        "CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER, product_id INTEGER, quantity INTEGER);"
        "INSERT INTO orders VALUES (1,1,1,2), (2,2,2,5), (3,1,3,1), (4,3,4,3);"
    ),
    expected_output="[('Emperor', 2080.0), ('Ali', 900.0), ('Rahim', 250.0)]",
    level=Level.MEDIUM,
    hints=[
        "WITH customer_spending AS (SELECT c.id, c.name, SUM(o.quantity * p.price) AS total_spent FROM customers c JOIN orders o ON c.id = o.customer_id JOIN products p ON o.product_id = p.id GROUP BY c.id) SELECT name, total_spent FROM customer_spending WHERE total_spent > 500 ORDER BY total_spent DESC;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧮  Multi‑Step CTE – Top Products by Revenue\n\n"
        "Create `products`, `orders`, `order_items` tables.\n"
        "Use a CTE named `product_revenue` to compute\n"
        "SUM(quantity * price) per product.\n"
        "Then SELECT the product name and revenue for the\n"
        "top 3 products by revenue.\n"
        "Use ORDER BY and LIMIT in the final SELECT.\n"
        "Sort by revenue descending.\n\n"
        "Expected output:\n[('Laptop',2000.0), ('Monitor',900.0), ('Mouse',250.0)]"
    ),
    setup_sql=(
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price REAL);"
        "INSERT INTO products VALUES (1,'Laptop',1000), (2,'Mouse',50), (3,'Keyboard',80), (4,'Monitor',300);"
        "CREATE TABLE orders (id INTEGER PRIMARY KEY, order_date TEXT);"
        "INSERT INTO orders VALUES (1,'2026-07-01'), (2,'2026-07-02');"
        "CREATE TABLE order_items (order_id INTEGER, product_id INTEGER, quantity INTEGER, PRIMARY KEY(order_id, product_id));"
        "INSERT INTO order_items VALUES (1,1,2), (1,2,5), (2,4,3);"
    ),
    expected_output="[('Laptop', 2000.0), ('Monitor', 900.0), ('Mouse', 250.0)]",
    level=Level.HARD,
    hints=[
        "WITH product_revenue AS (SELECT p.id, p.name, SUM(oi.quantity * p.price) AS revenue FROM products p JOIN order_items oi ON p.id = oi.product_id GROUP BY p.id) SELECT name, revenue FROM product_revenue ORDER BY revenue DESC LIMIT 3;"
    ]
)

hard2 = Task(
    description=(
        "📊  CTE with Multiple References – Compare to Average\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Write a query using a CTE that computes the overall\n"
        "average salary, then SELECT each soldier's name,\n"
        "salary, and whether they are 'Above' or 'Below' average.\n"
        "Reference the CTE twice (once in SELECT, once in CASE).\n"
        "Sort by name.\n\n"
        "Expected output:\n[('Ali','Above'), ('Emperor','Above'), ('Hasan','Below'), ('Karim','Below'), ('Rahim','Above')]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[('Ali', 'Above'), ('Emperor', 'Above'), ('Hasan', 'Below'), ('Karim', 'Below'), ('Rahim', 'Above')]",
    level=Level.HARD,
    hints=[
        "WITH overall_avg AS (SELECT AVG(salary) AS avg_sal FROM soldiers) SELECT name, CASE WHEN salary > (SELECT avg_sal FROM overall_avg) THEN 'Above' ELSE 'Below' END AS position FROM soldiers ORDER BY name;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L47.json",
        module_name="Module_05_Subqueries_CTEs",
        lesson_name="L47_WITH_Clause_CTEs"
    )
