import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🔢  HAVING – Count Filter\n\n"
        "The `soldiers` table has 6 rows.\n"
        "Group soldiers by rank and count them.\n"
        "Show only ranks that have at least 2 soldiers.\n"
        "Sort by count descending.\n\n"
        "Expected output:\n[('General',2), ('Colonel',2)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500), (6,'Fatima','Private',1800);"
    ),
    expected_output="[('General', 2), ('Colonel', 2)]",
    level=Level.EASY,
    hints=[
        "SELECT rank, COUNT(*) AS count FROM soldiers GROUP BY rank HAVING COUNT(*) >= 2 ORDER BY count DESC;"
    ]
)

easy2 = Task(
    description=(
        "💰  HAVING – Average Salary Filter\n\n"
        "The same `soldiers` table.\n"
        "Group by rank and compute the average salary.\n"
        "Show only ranks where the average salary\n"
        "is greater than 3000.\n"
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
        "SELECT rank, AVG(salary) AS avg_salary FROM soldiers GROUP BY rank HAVING AVG(salary) > 3000 ORDER BY avg_salary DESC;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "📊  HAVING – Total Revenue per Category\n\n"
        "Create a table `sales` with columns:\n"
        "  • id INTEGER, category TEXT, amount REAL.\n"
        "Insert 8 rows with varied categories.\n"
        "Group by category, compute SUM(amount).\n"
        "Show only categories with total revenue >= 500.\n"
        "Sort by total descending.\n\n"
        "Expected output:\n[('Electronics',950.0), ('Furniture',600.0)]"
    ),
    expected_output="[('Electronics', 950.0), ('Furniture', 600.0)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE sales (id INTEGER, category TEXT, amount REAL);",
        "INSERT INTO sales VALUES (1,'Electronics',500), (2,'Furniture',300), (3,'Electronics',450), (4,'Furniture',300), (5,'Office',200), (6,'Office',150), (7,'Electronics',0), (8,'Furniture',0);",
        "SELECT category, SUM(amount) AS total FROM sales GROUP BY category HAVING SUM(amount) >= 500 ORDER BY total DESC;"
    ]
)

medium2 = Task(
    description=(
        "🧮  HAVING with Multiple Conditions\n\n"
        "Create a table `inventory` with columns:\n"
        "  • id INTEGER, category TEXT, qty INTEGER, price REAL.\n"
        "Insert 6 rows.\n"
        "Group by category, compute COUNT(*) and AVG(price).\n"
        "Show only categories that have at least 2 items\n"
        "AND average price > 100.\n"
        "Sort by avg_price descending.\n\n"
        "Expected output:\n[('Electronics',3,250.0), ('Armor',2,175.0)]"
    ),
    expected_output="[('Electronics', 3, 250.0), ('Armor', 2, 175.0)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE inventory (id INTEGER, category TEXT, qty INTEGER, price REAL);",
        "INSERT INTO inventory VALUES (1,'Electronics',10,200), (2,'Weapons',5,50), (3,'Electronics',8,300), (4,'Armor',3,150), (5,'Armor',2,200), (6,'Electronics',15,250);",
        "SELECT category, COUNT(*) AS items, AVG(price) AS avg_price FROM inventory GROUP BY category HAVING COUNT(*) >= 2 AND AVG(price) > 100 ORDER BY avg_price DESC;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "⚠️  HAVING vs WHERE – Combine Both\n\n"
        "Create a table `transactions` with columns:\n"
        "  • id INTEGER, account_id INTEGER, type TEXT, amount REAL.\n"
        "Insert 10 rows (mix deposits/withdrawals, multiple accounts).\n"
        "Write a query that:\n"
        "  1. Filters to only 'deposit' rows (WHERE)\n"
        "  2. Groups by account_id\n"
        "  3. Shows only accounts with total deposits > 1000 (HAVING)\n"
        "Return account_id, total_deposits, and deposit_count.\n"
        "Sort by total_deposits descending.\n\n"
        "Expected output:\n[(1, 1700.0, 3), (2, 1100.0, 2)]"
    ),
    expected_output="[(1, 1700.0, 3), (2, 1100.0, 2)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE transactions (id INTEGER, account_id INTEGER, type TEXT, amount REAL);",
        "INSERT INTO transactions VALUES (1,1,'deposit',500), (2,1,'withdrawal',200), (3,2,'deposit',600), (4,1,'deposit',700), (5,3,'deposit',300), (6,2,'deposit',500), (7,1,'deposit',500), (8,3,'withdrawal',100), (9,2,'withdrawal',50), (10,1,'withdrawal',100);",
        "SELECT account_id, SUM(amount) AS total_deposits, COUNT(*) AS deposit_count FROM transactions WHERE type = 'deposit' GROUP BY account_id HAVING SUM(amount) > 1000 ORDER BY total_deposits DESC;"
    ]
)

hard2 = Task(
    description=(
        "📊  HAVING on Computed Column – High Performers\n\n"
        "Create a table `employees` with columns:\n"
        "  • id INTEGER, name TEXT, dept TEXT, salary REAL, bonus REAL.\n"
        "Insert 8 rows.\n"
        "Group by dept. For each dept, compute:\n"
        "  • avg_total_comp: AVG(salary + COALESCE(bonus,0))\n"
        "Show only departments where the average total\n"
        "compensation exceeds 5000.\n"
        "Return dept, ROUND(avg_total_comp,2), and headcount.\n"
        "Sort by avg_total_comp descending.\n\n"
        "Expected output:\n[('Engineering',6250.0,2), ('Sales',5333.33,3)]"
    ),
    expected_output="[('Engineering', 6250.0, 2), ('Sales', 5333.33, 3)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE employees (id INTEGER, name TEXT, dept TEXT, salary REAL, bonus REAL);",
        "INSERT INTO employees VALUES (1,'Emperor','Engineering',5000,1000), (2,'Rahim','Sales',4000,500), (3,'Karim','Engineering',6000,2000), (4,'Ali','Sales',4500,1000), (5,'Hasan','Sales',3500,NULL), (6,'Fatima','HR',3000,200), (7,'Akbar','HR',3500,300), (8,'Rana','Sales',6000,2000);",
        "SELECT dept, ROUND(AVG(salary + COALESCE(bonus,0)), 2) AS avg_total_comp, COUNT(*) AS headcount FROM employees GROUP BY dept HAVING AVG(salary + COALESCE(bonus,0)) > 5000 ORDER BY avg_total_comp DESC;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L25.json",
        module_name="Module_03_Aggregation_Grouping",
        lesson_name="L25_HAVING"
    )
