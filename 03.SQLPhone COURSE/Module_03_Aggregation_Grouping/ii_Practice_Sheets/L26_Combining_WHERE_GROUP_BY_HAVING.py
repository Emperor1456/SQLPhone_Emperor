import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🔍  WHERE + GROUP BY – Active Only\n\n"
        "The `soldiers` table has 6 rows with a `status` column.\n"
        "Filter to only active soldiers, then group by rank\n"
        "and count them.\n"
        "Sort by count descending.\n\n"
        "Expected output:\n[('General',2), ('Private',1)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, status TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General','active',5000), (2,'Rahim','Colonel','reserve',4000), (3,'Karim','Private','active',2000), (4,'Ali','General','active',4500), (5,'Hasan','Colonel','reserve',3500), (6,'Fatima','Private','reserve',1800);"
    ),
    expected_output="[('General', 2), ('Private', 1)]",
    level=Level.EASY,
    hints=[
        "SELECT rank, COUNT(*) FROM soldiers WHERE status = 'active' GROUP BY rank ORDER BY COUNT(*) DESC;"
    ]
)

easy2 = Task(
    description=(
        "📊  WHERE + GROUP BY – High Earners\n\n"
        "The `soldiers` table has 6 rows.\n"
        "Filter to soldiers with salary > 3000,\n"
        "then group by rank and compute AVG(salary).\n"
        "Round to 2 decimals.\n"
        "Sort by avg_salary descending.\n\n"
        "Expected output:\n[('General',4750.0), ('Colonel',3750.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500), (6,'Fatima','Private',1800);"
    ),
    expected_output="[('General', 4750.0), ('Colonel', 3750.0)]",
    level=Level.EASY,
    hints=[
        "SELECT rank, ROUND(AVG(salary), 2) AS avg_sal FROM soldiers WHERE salary > 3000 GROUP BY rank ORDER BY avg_sal DESC;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🧪  Full Pipeline – WHERE → GROUP BY → HAVING\n\n"
        "The `soldiers` table has 6 rows.\n"
        "1. Filter to soldiers with salary > 2500 (WHERE)\n"
        "2. Group by rank (GROUP BY)\n"
        "3. Show only groups with COUNT >= 2 (HAVING)\n"
        "Return rank, count, and AVG(salary).\n"
        "Sort by count descending.\n\n"
        "Expected output:\n[('General',2,4750.0), ('Colonel',2,3750.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500), (6,'Fatima','Private',1800);"
    ),
    expected_output="[('General', 2, 4750.0), ('Colonel', 2, 3750.0)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT rank, COUNT(*) AS cnt, AVG(salary) AS avg_sal FROM soldiers WHERE salary > 2500 GROUP BY rank HAVING COUNT(*) >= 2 ORDER BY cnt DESC;"
    ]
)

medium2 = Task(
    description=(
        "💰  Full Pipeline – Department Budget\n\n"
        "Create a table `employees` with columns:\n"
        "  • id INTEGER, name TEXT, dept TEXT, salary REAL.\n"
        "Insert 8 rows.\n"
        "1. Filter to salary > 3000 (WHERE)\n"
        "2. Group by dept (GROUP BY)\n"
        "3. Show only depts with total payroll > 8000 (HAVING)\n"
        "Return dept, SUM(salary), and COUNT(*).\n"
        "Sort by SUM(salary) descending.\n\n"
        "Expected output:\n[('Engineering',11000.0,2), ('Sales',8500.0,2)]"
    ),
    expected_output="[('Engineering', 11000.0, 2), ('Sales', 8500.0, 2)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE employees (id INTEGER, name TEXT, dept TEXT, salary REAL);",
        "INSERT INTO employees VALUES (1,'Emperor','Engineering',5000), (2,'Rahim','Sales',4000), (3,'Karim','Engineering',6000), (4,'Ali','Sales',4500), (5,'Hasan','HR',3500), (6,'Fatima','HR',2800), (7,'Akbar','Sales',3000), (8,'Rana','Engineering',3000);",
        "SELECT dept, SUM(salary) AS total_payroll, COUNT(*) AS headcount FROM employees WHERE salary > 3000 GROUP BY dept HAVING SUM(salary) > 8000 ORDER BY total_payroll DESC;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "📊  Multi‑Level Filter – Sales Analysis\n\n"
        "Create a table `sales` with columns:\n"
        "  • id INTEGER, region TEXT, product TEXT, amount REAL, sale_date TEXT.\n"
        "Insert 10 rows with varied data.\n"
        "1. Filter to sales in 2026 (WHERE)\n"
        "2. Group by region and product (GROUP BY)\n"
        "3. Show only groups with SUM(amount) >= 400 (HAVING)\n"
        "Return region, product, total_amount, and sale_count.\n"
        "Sort by region, then total_amount descending.\n\n"
        "Expected output:\n[('East','Laptop',500.0,1), ('North','Laptop',800.0,2), ('North','Mouse',400.0,2), ('South','Desk',450.0,1), ('South','Laptop',600.0,1)]"
    ),
    expected_output="[('East', 'Laptop', 500.0, 1), ('North', 'Laptop', 800.0, 2), ('North', 'Mouse', 400.0, 2), ('South', 'Desk', 450.0, 1), ('South', 'Laptop', 600.0, 1)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE sales (id INTEGER, region TEXT, product TEXT, amount REAL, sale_date TEXT);",
        "INSERT INTO sales VALUES (1,'North','Laptop',500,'2026-01-15'), (2,'North','Mouse',200,'2026-02-20'), (3,'South','Laptop',600,'2026-03-10'), (4,'East','Desk',300,'2026-04-05'), (5,'North','Laptop',300,'2025-12-01'), (6,'South','Desk',450,'2026-05-18'), (7,'East','Laptop',500,'2026-06-22'), (8,'North','Mouse',200,'2026-07-01'), (9,'South','Mouse',150,'2026-07-05'), (10,'North','Desk',250,'2026-07-10');",
        "SELECT region, product, SUM(amount) AS total_amount, COUNT(*) AS sale_count FROM sales WHERE strftime('%Y', sale_date) = '2026' GROUP BY region, product HAVING SUM(amount) >= 400 ORDER BY region, total_amount DESC;"
    ]
)

hard2 = Task(
    description=(
        "🧮  Complex HAVING – High‑Value Active Accounts\n\n"
        "Create a table `transactions` with columns:\n"
        "  • id INTEGER, account_id INTEGER, type TEXT, amount REAL, txn_date TEXT.\n"
        "Insert 12 rows (deposits & withdrawals, multiple accounts, varied dates).\n"
        "Write a query that:\n"
        "  1. Includes only 'deposit' AND txn_date in 2026 (WHERE)\n"
        "  2. Groups by account_id (GROUP BY)\n"
        "  3. Shows only accounts with total deposits > 800\n"
        "     AND at least 2 deposits (HAVING)\n"
        "Return account_id, total_deposits, deposit_count.\n"
        "Sort by total_deposits descending.\n\n"
        "Expected output:\n[(1, 1700.0, 3), (2, 1100.0, 2)]"
    ),
    expected_output="[(1, 1700.0, 3), (2, 1100.0, 2)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE transactions (id INTEGER, account_id INTEGER, type TEXT, amount REAL, txn_date TEXT);",
        "INSERT INTO transactions VALUES (1,1,'deposit',500,'2026-01-15'), (2,1,'withdrawal',200,'2026-02-20'), (3,2,'deposit',600,'2026-03-10'), (4,1,'deposit',700,'2026-04-05'), (5,3,'deposit',300,'2025-12-01'), (6,2,'deposit',500,'2026-05-18'), (7,1,'deposit',500,'2026-06-22'), (8,3,'withdrawal',100,'2026-07-01'), (9,2,'withdrawal',50,'2026-07-05'), (10,1,'withdrawal',100,'2026-07-10'), (11,2,'deposit',200,'2025-11-01'), (12,3,'deposit',400,'2026-07-12');",
        "SELECT account_id, SUM(amount) AS total_deposits, COUNT(*) AS deposit_count FROM transactions WHERE type = 'deposit' AND strftime('%Y', txn_date) = '2026' GROUP BY account_id HAVING SUM(amount) > 800 AND COUNT(*) >= 2 ORDER BY total_deposits DESC;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L26.json",
        module_name="Module_03_Aggregation_Grouping",
        lesson_name="L26_Combining_WHERE_GROUP_BY_HAVING"
    )
