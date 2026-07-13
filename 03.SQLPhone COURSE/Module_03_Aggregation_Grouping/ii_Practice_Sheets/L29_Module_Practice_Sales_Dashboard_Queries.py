import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "📊  Monthly Revenue – GROUP BY Month\n\n"
        "Create a table `sales` with columns:\n"
        "  • id INTEGER, product TEXT, amount REAL, sale_date TEXT.\n"
        "Insert 8 rows across different months.\n"
        "Write a query that groups by month (strftime '%Y-%m')\n"
        "and returns month and SUM(amount) as revenue.\n"
        "Sort by month.\n\n"
        "Expected output:\n[('2026-01',800.0), ('2026-02',650.0), ('2026-03',900.0)]"
    ),
    expected_output="[('2026-01', 800.0), ('2026-02', 650.0), ('2026-03', 900.0)]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE sales (id INTEGER, product TEXT, amount REAL, sale_date TEXT);",
        "INSERT INTO sales VALUES (1,'Laptop',500,'2026-01-15'), (2,'Mouse',300,'2026-01-25'), (3,'Desk',400,'2026-02-10'), (4,'Chair',250,'2026-02-20'), (5,'Monitor',600,'2026-03-05'), (6,'Keyboard',150,'2026-03-15'), (7,'Pen',50,'2026-03-20'), (8,'Paper',100,'2026-03-25');",
        "SELECT strftime('%Y-%m', sale_date) AS month, SUM(amount) AS revenue FROM sales GROUP BY month ORDER BY month;"
    ]
)

easy2 = Task(
    description=(
        "📈  Average Order Value – AVG\n\n"
        "The same `sales` table.\n"
        "Write a query that returns the overall\n"
        "average order value (AVG(amount)).\n"
        "Round to 2 decimal places.\n\n"
        "Expected output: [(293.75,)]"
    ),
    setup_sql=(
        "CREATE TABLE sales (id INTEGER, product TEXT, amount REAL, sale_date TEXT);"
        "INSERT INTO sales VALUES (1,'Laptop',500,'2026-01-15'), (2,'Mouse',300,'2026-01-25'), (3,'Desk',400,'2026-02-10'), (4,'Chair',250,'2026-02-20'), (5,'Monitor',600,'2026-03-05'), (6,'Keyboard',150,'2026-03-15'), (7,'Pen',50,'2026-03-20'), (8,'Paper',100,'2026-03-25');"
    ),
    expected_output="[(293.75,)]",
    level=Level.EASY,
    hints=[
        "SELECT ROUND(AVG(amount), 2) FROM sales;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "📋  Sales Count per Product – GROUP BY\n\n"
        "The `sales` table has 8 rows.\n"
        "Write a query that groups by product and\n"
        "returns product, COUNT(*) as times_sold,\n"
        "and SUM(amount) as total_revenue.\n"
        "Sort by total_revenue descending.\n\n"
        "Expected output:\n[('Monitor',1,600.0), ('Laptop',1,500.0), ('Desk',1,400.0), ('Mouse',1,300.0), ('Chair',1,250.0), ('Keyboard',1,150.0), ('Paper',1,100.0), ('Pen',1,50.0)]"
    ),
    setup_sql=(
        "CREATE TABLE sales (id INTEGER, product TEXT, amount REAL, sale_date TEXT);"
        "INSERT INTO sales VALUES (1,'Laptop',500,'2026-01-15'), (2,'Mouse',300,'2026-01-25'), (3,'Desk',400,'2026-02-10'), (4,'Chair',250,'2026-02-20'), (5,'Monitor',600,'2026-03-05'), (6,'Keyboard',150,'2026-03-15'), (7,'Pen',50,'2026-03-20'), (8,'Paper',100,'2026-03-25');"
    ),
    expected_output="[('Monitor', 1, 600.0), ('Laptop', 1, 500.0), ('Desk', 1, 400.0), ('Mouse', 1, 300.0), ('Chair', 1, 250.0), ('Keyboard', 1, 150.0), ('Paper', 1, 100.0), ('Pen', 1, 50.0)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT product, COUNT(*) AS times_sold, SUM(amount) AS total_revenue FROM sales GROUP BY product ORDER BY total_revenue DESC;"
    ]
)

medium2 = Task(
    description=(
        "🧹  HAVING – High‑Revenue Months\n\n"
        "The `sales` table has 8 rows.\n"
        "Write a query that groups by month and\n"
        "shows only months where total revenue >= 700.\n"
        "Return month, revenue, and order_count.\n"
        "Sort by month.\n\n"
        "Expected output:\n[('2026-01',800.0,2), ('2026-03',900.0,4)]"
    ),
    setup_sql=(
        "CREATE TABLE sales (id INTEGER, product TEXT, amount REAL, sale_date TEXT);"
        "INSERT INTO sales VALUES (1,'Laptop',500,'2026-01-15'), (2,'Mouse',300,'2026-01-25'), (3,'Desk',400,'2026-02-10'), (4,'Chair',250,'2026-02-20'), (5,'Monitor',600,'2026-03-05'), (6,'Keyboard',150,'2026-03-15'), (7,'Pen',50,'2026-03-20'), (8,'Paper',100,'2026-03-25');"
    ),
    expected_output="[('2026-01', 800.0, 2), ('2026-03', 900.0, 4)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT strftime('%Y-%m', sale_date) AS month, SUM(amount) AS revenue, COUNT(*) AS order_count FROM sales GROUP BY month HAVING SUM(amount) >= 700 ORDER BY month;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "📊  Category Breakdown – Conditional SUM\n\n"
        "Create a table `orders` with columns:\n"
        "  • id INTEGER, category TEXT, amount REAL, order_date TEXT.\n"
        "Insert 10 rows across three categories and two months.\n"
        "Write ONE query that returns, for each month:\n"
        "  • month (YYYY-MM)\n"
        "  • electronics_revenue (SUM where category='Electronics')\n"
        "  • furniture_revenue (SUM where category='Furniture')\n"
        "  • office_revenue (SUM where category='Office')\n"
        "  • total_revenue (SUM of all)\n"
        "Sort by month.\n\n"
        "Expected output:\n[('2026-06',1100.0,500.0,200.0,1800.0), ('2026-07',900.0,650.0,300.0,1850.0)]"
    ),
    expected_output="[('2026-06', 1100.0, 500.0, 200.0, 1800.0), ('2026-07', 900.0, 650.0, 300.0, 1850.0)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE orders (id INTEGER, category TEXT, amount REAL, order_date TEXT);",
        "INSERT INTO orders VALUES (1,'Electronics',500,'2026-06-15'), (2,'Furniture',300,'2026-06-20'), (3,'Electronics',600,'2026-06-25'), (4,'Office',200,'2026-06-28'), (5,'Furniture',200,'2026-06-30'), (6,'Electronics',400,'2026-07-05'), (7,'Electronics',500,'2026-07-10'), (8,'Furniture',350,'2026-07-12'), (9,'Office',300,'2026-07-15'), (10,'Furniture',300,'2026-07-20');",
        "SELECT strftime('%Y-%m', order_date) AS month, SUM(CASE WHEN category='Electronics' THEN amount ELSE 0 END) AS electronics_revenue, SUM(CASE WHEN category='Furniture' THEN amount ELSE 0 END) AS furniture_revenue, SUM(CASE WHEN category='Office' THEN amount ELSE 0 END) AS office_revenue, SUM(amount) AS total_revenue FROM orders GROUP BY month ORDER BY month;"
    ]
)

hard2 = Task(
    description=(
        "🧪  Dashboard Summary – Multi‑KPI Single Row\n\n"
        "Create a table `metrics` with columns:\n"
        "  • id INTEGER, region TEXT, product TEXT, amount REAL, sale_date TEXT.\n"
        "Insert 12 rows spanning 3 regions, varied products, Q1 & Q2 2026.\n"
        "Write ONE query that returns a single row with:\n"
        "  • total_sales: SUM(amount)\n"
        "  • q1_sales: SUM where sale_date in Q1 (1‑3)\n"
        "  • q2_sales: SUM where sale_date in Q2 (4‑6)\n"
        "  • north_sales: SUM where region='North'\n"
        "  • south_sales: SUM where region='South'\n"
        "  • top_product: the product with MAX(amount) (use subquery)\n"
        "Use conditional aggregates and a subquery.\n\n"
        "Expected output:\n[(3750.0, 1700.0, 2050.0, 1950.0, 1800.0, 'Laptop')]"
    ),
    expected_output="[(3750.0, 1700.0, 2050.0, 1950.0, 1800.0, 'Laptop')]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE metrics (id INTEGER, region TEXT, product TEXT, amount REAL, sale_date TEXT);",
        "INSERT INTO metrics VALUES (1,'North','Laptop',500,'2026-01-15'), (2,'South','Mouse',300,'2026-01-25'), (3,'North','Desk',400,'2026-02-10'), (4,'South','Chair',200,'2026-02-20'), (5,'North','Monitor',600,'2026-03-05'), (6,'South','Keyboard',150,'2026-03-15'), (7,'North','Pen',50,'2026-04-10'), (8,'South','Paper',100,'2026-04-20'), (9,'North','Laptop',400,'2026-05-05'), (10,'South','Desk',350,'2026-05-18'), (11,'North','Mouse',250,'2026-06-12'), (12,'South','Laptop',450,'2026-06-28');",
        "SELECT SUM(amount) AS total_sales, SUM(CASE WHEN CAST(strftime('%m', sale_date) AS INTEGER) <= 3 THEN amount ELSE 0 END) AS q1_sales, SUM(CASE WHEN CAST(strftime('%m', sale_date) AS INTEGER) > 3 THEN amount ELSE 0 END) AS q2_sales, SUM(CASE WHEN region='North' THEN amount ELSE 0 END) AS north_sales, SUM(CASE WHEN region='South' THEN amount ELSE 0 END) AS south_sales, (SELECT product FROM metrics WHERE amount = (SELECT MAX(amount) FROM metrics) LIMIT 1) AS top_product FROM metrics;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L29.json",
        module_name="Module_03_Aggregation_Grouping",
        lesson_name="L29_Module_Practice_Sales_Dashboard"
    )
