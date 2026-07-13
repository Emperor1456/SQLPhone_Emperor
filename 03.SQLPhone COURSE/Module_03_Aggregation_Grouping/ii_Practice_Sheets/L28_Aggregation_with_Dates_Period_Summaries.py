import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "📅  Monthly Count – Group by Year‑Month\n\n"
        "Create a table `missions` with columns:\n"
        "  • id INTEGER, name TEXT, mission_date TEXT.\n"
        "Insert 6 rows across different months.\n"
        "Write a query that groups by month (use strftime)\n"
        "and returns the month and COUNT(*).\n"
        "Sort by month.\n\n"
        "Expected output:\n[('2026-01',2), ('2026-02',1), ('2026-03',2), ('2026-04',1)]"
    ),
    expected_output="[('2026-01', 2), ('2026-02', 1), ('2026-03', 2), ('2026-04', 1)]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE missions (id INTEGER, name TEXT, mission_date TEXT);",
        "INSERT INTO missions VALUES (1,'Patrol','2026-01-10'), (2,'Recon','2026-01-25'), (3,'Supply','2026-02-15'), (4,'Guard','2026-03-05'), (5,'Raid','2026-03-20'), (6,'Train','2026-04-01');",
        "SELECT strftime('%Y-%m', mission_date) AS month, COUNT(*) AS count FROM missions GROUP BY month ORDER BY month;"
    ]
)

easy2 = Task(
    description=(
        "📈  Yearly Totals – Sum by Year\n\n"
        "The same `missions` table, but with a `duration_hours` column.\n"
        "Write a query that groups by year and returns the\n"
        "year and SUM(duration_hours) as total_hours.\n"
        "Sort by year.\n\n"
        "Expected output:\n[('2026', 45.0), ('2027', 55.0)]"
    ),
    expected_output="[('2026', 45.0), ('2027', 55.0)]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE missions (id INTEGER, name TEXT, mission_date TEXT, duration_hours REAL);",
        "INSERT INTO missions VALUES (1,'Patrol','2026-01-10',10), (2,'Recon','2026-06-20',15), (3,'Supply','2026-09-05',20), (4,'Guard','2027-02-14',25), (5,'Raid','2027-08-30',30), (6,'Train','2027-12-01',0);",
        "SELECT strftime('%Y', mission_date) AS year, SUM(duration_hours) AS total_hours FROM missions GROUP BY year ORDER BY year;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "📊  Quarterly Breakdown – CASE + Grouping\n\n"
        "Create a table `sales` with columns:\n"
        "  • id INTEGER, product TEXT, amount REAL, sale_date TEXT.\n"
        "Insert 8 rows spanning all quarters.\n"
        "Write a query that groups by quarter using CASE:\n"
        "  • month 1‑3 → Q1, 4‑6 → Q2, 7‑9 → Q3, 10‑12 → Q4\n"
        "Include the year in the quarter label (e.g., '2026-Q1').\n"
        "Return quarter and SUM(amount), sorted by quarter.\n\n"
        "Expected output:\n[('2026-Q1',600.0), ('2026-Q2',700.0), ('2026-Q3',450.0), ('2026-Q4',350.0)]"
    ),
    expected_output="[('2026-Q1', 600.0), ('2026-Q2', 700.0), ('2026-Q3', 450.0), ('2026-Q4', 350.0)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE sales (id INTEGER, product TEXT, amount REAL, sale_date TEXT);",
        "INSERT INTO sales VALUES (1,'Laptop',500,'2026-01-15'), (2,'Mouse',100,'2026-02-20'), (3,'Desk',300,'2026-04-10'), (4,'Chair',200,'2026-05-05'), (5,'Monitor',200,'2026-06-18'), (6,'Keyboard',150,'2026-07-22'), (7,'Pen',50,'2026-09-01'), (8,'Paper',250,'2026-10-12');",
        "SELECT strftime('%Y', sale_date) || '-Q' || ((CAST(strftime('%m', sale_date) AS INTEGER) + 2) / 3) AS quarter, SUM(amount) AS total FROM sales GROUP BY quarter ORDER BY quarter;"
    ]
)

medium2 = Task(
    description=(
        "📅  Day of Week Analysis – strftime('%w')\n\n"
        "Create a table `orders` with columns:\n"
        "  • id INTEGER, customer TEXT, order_date TEXT.\n"
        "Insert 7 rows, one per day of a week (use a real week in 2026).\n"
        "Group by day of week (0=Sunday, 6=Saturday) and count orders.\n"
        "Return day number and count, sorted by count descending.\n\n"
        "Expected output (varies based on seed, but structure is):\n"
        "  day_num, count\n"
        "Sort by count desc, then day_num asc.\n\n"
        "Example expected (if today is 2026-07-12, we use a fixed week):\n"
        "We'll use 2026-07-06 (Mon) to 2026-07-12 (Sun), with varied counts."
    ),
    expected_output=None,
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE orders (id INTEGER, customer TEXT, order_date TEXT);",
        "INSERT INTO orders VALUES (1,'A','2026-07-06'), (2,'B','2026-07-06'), (3,'C','2026-07-07'), (4,'D','2026-07-08'), (5,'E','2026-07-09'), (6,'F','2026-07-09'), (7,'G','2026-07-10');",
        "SELECT strftime('%w', order_date) AS day_num, COUNT(*) AS count FROM orders GROUP BY day_num ORDER BY count DESC;"
    ],
    verify_func=lambda conn: (
        len(conn.execute("SELECT strftime('%w', order_date) AS day_num, COUNT(*) FROM orders GROUP BY day_num").fetchall()) > 0
    )
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "📊  Month‑over‑Month Growth – Window Function\n\n"
        "Create a table `revenue` with columns:\n"
        "  • month TEXT, amount REAL.\n"
        "Insert 6 months of data (2026‑01 to 2026‑06).\n"
        "Use LAG() window function to calculate the\n"
        "previous month's revenue and the growth percentage.\n"
        "Return month, amount, prev_month, and\n"
        "ROUND((amount - prev) / prev * 100, 1) as growth_pct.\n"
        "Sort by month.\n\n"
        "Expected output:\n[('2026-01',1000.0,None,None), ('2026-02',1200.0,1000.0,20.0), ('2026-03',900.0,1200.0,-25.0), ('2026-04',1500.0,900.0,66.7), ('2026-05',1800.0,1500.0,20.0), ('2026-06',1600.0,1800.0,-11.1)]"
    ),
    expected_output="[('2026-01', 1000.0, None, None), ('2026-02', 1200.0, 1000.0, 20.0), ('2026-03', 900.0, 1200.0, -25.0), ('2026-04', 1500.0, 900.0, 66.7), ('2026-05', 1800.0, 1500.0, 20.0), ('2026-06', 1600.0, 1800.0, -11.1)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE revenue (month TEXT, amount REAL);",
        "INSERT INTO revenue VALUES ('2026-01',1000), ('2026-02',1200), ('2026-03',900), ('2026-04',1500), ('2026-05',1800), ('2026-06',1600);",
        "SELECT month, amount, LAG(amount) OVER (ORDER BY month) AS prev_month, ROUND((amount - LAG(amount) OVER (ORDER BY month)) * 100.0 / LAG(amount) OVER (ORDER BY month), 1) AS growth_pct FROM revenue ORDER BY month;"
    ]
)

hard2 = Task(
    description=(
        "🧪  Running Total – Cumulative SUM\n\n"
        "The same `revenue` table from Hard1.\n"
        "Write a query that returns month, amount,\n"
        "and a running total (SUM OVER ORDER BY month).\n"
        "Sort by month.\n\n"
        "Expected output:\n[('2026-01',1000.0,1000.0), ('2026-02',1200.0,2200.0), ('2026-03',900.0,3100.0), ('2026-04',1500.0,4600.0), ('2026-05',1800.0,6400.0), ('2026-06',1600.0,8000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE revenue (month TEXT, amount REAL);"
        "INSERT INTO revenue VALUES ('2026-01',1000), ('2026-02',1200), ('2026-03',900), ('2026-04',1500), ('2026-05',1800), ('2026-06',1600);"
    ),
    expected_output="[('2026-01', 1000.0, 1000.0), ('2026-02', 1200.0, 2200.0), ('2026-03', 900.0, 3100.0), ('2026-04', 1500.0, 4600.0), ('2026-05', 1800.0, 6400.0), ('2026-06', 1600.0, 8000.0)]",
    level=Level.HARD,
    hints=[
        "SELECT month, amount, SUM(amount) OVER (ORDER BY month) AS running_total FROM revenue ORDER BY month;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L28.json",
        module_name="Module_03_Aggregation_Grouping",
        lesson_name="L28_Aggregation_with_Dates"
    )
