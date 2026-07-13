import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "📊  Two‑Column GROUP BY – Rank & Status\n\n"
        "Create a table `soldiers` with columns:\n"
        "  • id INTEGER, name TEXT, rank TEXT, status TEXT, salary REAL.\n"
        "Insert 6 rows with mixed ranks and statuses.\n"
        "Write a query that groups by rank AND status,\n"
        "returning rank, status, and COUNT(*).\n"
        "Sort by rank, then status.\n\n"
        "Expected output:\n[('Colonel','active',1), ('Colonel','reserve',1), ('General','active',2), ('Private','active',1), ('Private','reserve',1)]"
    ),
    expected_output="[('Colonel', 'active', 1), ('Colonel', 'reserve', 1), ('General', 'active', 2), ('Private', 'active', 1), ('Private', 'reserve', 1)]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, status TEXT, salary REAL);",
        "INSERT INTO soldiers VALUES (1,'Emperor','General','active',5000), (2,'Rahim','Colonel','active',4000), (3,'Karim','Private','reserve',2000), (4,'Ali','General','active',4500), (5,'Hasan','Colonel','reserve',3500), (6,'Fatima','Private','active',1800);",
        "SELECT rank, status, COUNT(*) AS count FROM soldiers GROUP BY rank, status ORDER BY rank, status;"
    ]
)

easy2 = Task(
    description=(
        "📈  Two‑Column GROUP BY – Average per Group\n\n"
        "The same `soldiers` table.\n"
        "Write a query that returns rank, status,\n"
        "and the average salary for each combination.\n"
        "Round to 2 decimal places.\n"
        "Sort by rank, then avg_salary descending.\n\n"
        "Expected output:\n[('Colonel','active',4000.0), ('Colonel','reserve',3500.0), ('General','active',4750.0), ('Private','active',1800.0), ('Private','reserve',2000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, status TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General','active',5000), (2,'Rahim','Colonel','active',4000), (3,'Karim','Private','reserve',2000), (4,'Ali','General','active',4500), (5,'Hasan','Colonel','reserve',3500), (6,'Fatima','Private','active',1800);"
    ),
    expected_output="[('Colonel', 'active', 4000.0), ('Colonel', 'reserve', 3500.0), ('General', 'active', 4750.0), ('Private', 'active', 1800.0), ('Private', 'reserve', 2000.0)]",
    level=Level.EASY,
    hints=[
        "SELECT rank, status, ROUND(AVG(salary), 2) AS avg_salary FROM soldiers GROUP BY rank, status ORDER BY rank, avg_salary DESC;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🗂️  Multi‑Column GROUP BY – Region & Category\n\n"
        "Create a table `sales` with columns:\n"
        "  • id INTEGER, region TEXT, category TEXT, amount REAL.\n"
        "Insert 6 rows with varied regions and categories.\n"
        "Write a query that groups by region AND category,\n"
        "returning region, category, SUM(amount), and COUNT(*).\n"
        "Sort by region, then total_amount descending.\n\n"
        "Expected output:\n[('East','Electronics',350.0,1), ('East','Furniture',200.0,1), ('North','Electronics',1000.0,2), ('North','Furniture',500.0,1), ('South','Electronics',150.0,1)]"
    ),
    expected_output="[('East', 'Electronics', 350.0, 1), ('East', 'Furniture', 200.0, 1), ('North', 'Electronics', 1000.0, 2), ('North', 'Furniture', 500.0, 1), ('South', 'Electronics', 150.0, 1)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE sales (id INTEGER, region TEXT, category TEXT, amount REAL);",
        "INSERT INTO sales VALUES (1,'North','Electronics',600), (2,'North','Furniture',500), (3,'North','Electronics',400), (4,'South','Electronics',150), (5,'East','Furniture',200), (6,'East','Electronics',350);",
        "SELECT region, category, SUM(amount) AS total_amount, COUNT(*) AS count FROM sales GROUP BY region, category ORDER BY region, total_amount DESC;"
    ]
)

medium2 = Task(
    description=(
        "📅  GROUP BY with Date – Month & Type\n\n"
        "Create a table `transactions` with columns:\n"
        "  • id INTEGER, txn_date TEXT, type TEXT, amount REAL.\n"
        "Insert 6 rows across different months and types.\n"
        "Write a query that groups by month (use strftime)\n"
        "AND type, returning month, type, COUNT(*), and\n"
        "SUM(amount), sorted by month, then type.\n\n"
        "Expected output:\n[('2026-01','credit',1,500.0), ('2026-01','debit',1,300.0), ('2026-02','credit',1,200.0), ('2026-02','debit',2,550.0), ('2026-03','credit',1,1000.0)]"
    ),
    expected_output="[('2026-01', 'credit', 1, 500.0), ('2026-01', 'debit', 1, 300.0), ('2026-02', 'credit', 1, 200.0), ('2026-02', 'debit', 2, 550.0), ('2026-03', 'credit', 1, 1000.0)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE transactions (id INTEGER, txn_date TEXT, type TEXT, amount REAL);",
        "INSERT INTO transactions VALUES (1,'2026-01-15','credit',500), (2,'2026-01-20','debit',300), (3,'2026-02-05','debit',250), (4,'2026-02-18','credit',200), (5,'2026-02-25','debit',300), (6,'2026-03-10','credit',1000);",
        "SELECT strftime('%Y-%m', txn_date) AS month, type, COUNT(*) AS count, SUM(amount) AS total FROM transactions GROUP BY month, type ORDER BY month, type;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  Three‑Column GROUP BY – Full Drilldown\n\n"
        "Create a table `shipments` with columns:\n"
        "  • id INTEGER, region TEXT, carrier TEXT, status TEXT.\n"
        "Insert 8 rows with varied data.\n"
        "Write a query that groups by region, carrier,\n"
        "and status, returning all three columns plus\n"
        "COUNT(*), sorted by region, carrier, status.\n\n"
        "Expected output:\n[('East','FastShip','delayed',1), ('East','FastShip','delivered',1), ('East','SwiftLog','delivered',1), ('North','FastShip','in transit',2), ('North','SwiftLog','delayed',1), ('South','FastShip','delivered',1), ('South','SwiftLog','in transit',1)]"
    ),
    expected_output="[('East', 'FastShip', 'delayed', 1), ('East', 'FastShip', 'delivered', 1), ('East', 'SwiftLog', 'delivered', 1), ('North', 'FastShip', 'in transit', 2), ('North', 'SwiftLog', 'delayed', 1), ('South', 'FastShip', 'delivered', 1), ('South', 'SwiftLog', 'in transit', 1)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE shipments (id INTEGER, region TEXT, carrier TEXT, status TEXT);",
        "INSERT INTO shipments VALUES (1,'North','FastShip','in transit'), (2,'North','FastShip','in transit'), (3,'North','SwiftLog','delayed'), (4,'South','FastShip','delivered'), (5,'South','SwiftLog','in transit'), (6,'East','FastShip','delayed'), (7,'East','FastShip','delivered'), (8,'East','SwiftLog','delivered');",
        "SELECT region, carrier, status, COUNT(*) AS count FROM shipments GROUP BY region, carrier, status ORDER BY region, carrier, status;"
    ]
)

hard2 = Task(
    description=(
        "📊  Multi‑Column GROUP BY with HAVING – Filtered Groups\n\n"
        "Create a table `orders` with columns:\n"
        "  • id INTEGER, customer TEXT, category TEXT, amount REAL.\n"
        "Insert 8 rows with varied data.\n"
        "Write a query that groups by customer AND category,\n"
        "returning customer, category, COUNT(*), and SUM(amount).\n"
        "Filter to show only groups with COUNT >= 2.\n"
        "Sort by customer, then SUM(amount) descending.\n\n"
        "Expected output:\n[('Emperor','Electronics',2,850.0), ('Rahim','Furniture',2,600.0)]"
    ),
    expected_output="[('Emperor', 'Electronics', 2, 850.0), ('Rahim', 'Furniture', 2, 600.0)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE orders (id INTEGER, customer TEXT, category TEXT, amount REAL);",
        "INSERT INTO orders VALUES (1,'Emperor','Electronics',500), (2,'Emperor','Electronics',350), (3,'Emperor','Furniture',200), (4,'Rahim','Furniture',400), (5,'Rahim','Furniture',200), (6,'Rahim','Electronics',150), (7,'Karim','Electronics',600), (8,'Karim','Furniture',100);",
        "SELECT customer, category, COUNT(*) AS order_count, SUM(amount) AS total FROM orders GROUP BY customer, category HAVING COUNT(*) >= 2 ORDER BY customer, total DESC;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L24.json",
        module_name="Module_03_Aggregation_Grouping",
        lesson_name="L24_GROUP_BY_Multiple_Columns"
    )
