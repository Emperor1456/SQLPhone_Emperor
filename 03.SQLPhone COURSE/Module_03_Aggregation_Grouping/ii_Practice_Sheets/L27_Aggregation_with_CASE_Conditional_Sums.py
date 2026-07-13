import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "📊  Conditional COUNT – Generals vs Privates\n\n"
        "The `soldiers` table has 6 rows.\n"
        "Write ONE query that returns:\n"
        "  • total: COUNT(*)\n"
        "  • generals: COUNT of rows where rank='General'\n"
        "  • privates: COUNT of rows where rank='Private'\n"
        "Use COUNT(CASE WHEN … THEN 1 END).\n\n"
        "Expected output: [(6, 2, 2)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500), (6,'Fatima','Private',1800);"
    ),
    expected_output="[(6, 2, 2)]",
    level=Level.EASY,
    hints=[
        "SELECT COUNT(*) AS total, COUNT(CASE WHEN rank='General' THEN 1 END) AS generals, COUNT(CASE WHEN rank='Private' THEN 1 END) AS privates FROM soldiers;"
    ]
)

easy2 = Task(
    description=(
        "💰  Conditional SUM – Payroll by Rank\n\n"
        "The same `soldiers` table.\n"
        "Write ONE query that returns:\n"
        "  • total_payroll: SUM(salary)\n"
        "  • general_payroll: SUM of salaries where rank='General'\n"
        "  • private_payroll: SUM of salaries where rank='Private'\n"
        "Use SUM(CASE WHEN … THEN salary ELSE 0 END).\n\n"
        "Expected output: [(19000.0, 9500.0, 3800.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500), (6,'Fatima','Private',1800);"
    ),
    expected_output="[(19000.0, 9500.0, 3800.0)]",
    level=Level.EASY,
    hints=[
        "SELECT SUM(salary) AS total_payroll, SUM(CASE WHEN rank='General' THEN salary ELSE 0 END) AS general_payroll, SUM(CASE WHEN rank='Private' THEN salary ELSE 0 END) AS private_payroll FROM soldiers;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "📈  Conditional AVG – Compare Groups\n\n"
        "The `soldiers` table has 6 rows.\n"
        "Write ONE query that returns:\n"
        "  • overall_avg: AVG(salary)\n"
        "  • general_avg: AVG of salaries for Generals\n"
        "  • colonel_avg: AVG of salaries for Colonels\n"
        "Round all averages to 1 decimal.\n"
        "For AVG with CASE, do NOT use ELSE 0.\n\n"
        "Expected output: [(3166.7, 4750.0, 3750.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500), (6,'Fatima','Private',1800);"
    ),
    expected_output="[(3166.7, 4750.0, 3750.0)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT ROUND(AVG(salary),1) AS overall_avg, ROUND(AVG(CASE WHEN rank='General' THEN salary END),1) AS general_avg, ROUND(AVG(CASE WHEN rank='Colonel' THEN salary END),1) AS colonel_avg FROM soldiers;"
    ]
)

medium2 = Task(
    description=(
        "📋  Multi‑Metric Report – One Row Summary\n\n"
        "Create a table `inventory` with columns:\n"
        "  • id INTEGER, item TEXT, category TEXT, qty INTEGER, price REAL.\n"
        "Insert 6 items.\n"
        "Write ONE query that returns a single row with:\n"
        "  • total_items: COUNT(*)\n"
        "  • weapons_count: COUNT where category='Weapons'\n"
        "  • armor_count: COUNT where category='Armor'\n"
        "  • total_value: SUM(qty * price)\n"
        "  • weapons_value: SUM(qty*price) for Weapons only\n\n"
        "Expected output: [(6, 3, 2, 3400.0, 1900.0)]"
    ),
    expected_output="[(6, 3, 2, 3400.0, 1900.0)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE inventory (id INTEGER, item TEXT, category TEXT, qty INTEGER, price REAL);",
        "INSERT INTO inventory VALUES (1,'Sword','Weapons',10,100), (2,'Shield','Armor',5,200), (3,'Bow','Weapons',8,50), (4,'Helm','Armor',3,100), (5,'Axe','Weapons',12,75), (6,'Rations','Supplies',50,5);",
        "SELECT COUNT(*) AS total_items, COUNT(CASE WHEN category='Weapons' THEN 1 END) AS weapons_count, COUNT(CASE WHEN category='Armor' THEN 1 END) AS armor_count, SUM(qty * price) AS total_value, SUM(CASE WHEN category='Weapons' THEN qty*price ELSE 0 END) AS weapons_value FROM inventory;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "📊  Pivot Table – Monthly Status Breakdown\n\n"
        "Create a table `shipments` with columns:\n"
        "  • id INTEGER, status TEXT, ship_date TEXT.\n"
        "Insert 8 rows across different months and statuses.\n"
        "Write ONE query that returns, for each month:\n"
        "  • month (YYYY-MM via strftime)\n"
        "  • total: COUNT(*)\n"
        "  • delivered: COUNT where status='delivered'\n"
        "  • delayed: COUNT where status='delayed'\n"
        "  • in_transit: COUNT where status='in transit'\n"
        "Group by month, sort by month.\n\n"
        "Expected output:\n[('2026-06',3,1,1,1), ('2026-07',5,2,2,1)]"
    ),
    expected_output="[('2026-06', 3, 1, 1, 1), ('2026-07', 5, 2, 2, 1)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE shipments (id INTEGER, status TEXT, ship_date TEXT);",
        "INSERT INTO shipments VALUES (1,'delivered','2026-06-10'), (2,'delayed','2026-06-15'), (3,'in transit','2026-06-20'), (4,'delivered','2026-07-01'), (5,'delayed','2026-07-05'), (6,'in transit','2026-07-10'), (7,'delivered','2026-07-15'), (8,'delayed','2026-07-20');",
        "SELECT strftime('%Y-%m', ship_date) AS month, COUNT(*) AS total, COUNT(CASE WHEN status='delivered' THEN 1 END) AS delivered, COUNT(CASE WHEN status='delayed' THEN 1 END) AS delayed, COUNT(CASE WHEN status='in transit' THEN 1 END) AS in_transit FROM shipments GROUP BY month ORDER BY month;"
    ]
)

hard2 = Task(
    description=(
        "🧪  Performance Dashboard – Multi‑KPI\n\n"
        "Create a table `employees` with columns:\n"
        "  • id INTEGER, name TEXT, dept TEXT, salary REAL, rating INTEGER.\n"
        "Insert 8 rows with varied departments and ratings (1‑5).\n"
        "Write ONE query that returns, for each department:\n"
        "  • dept\n"
        "  • headcount: COUNT(*)\n"
        "  • avg_salary: ROUND(AVG(salary), 0)\n"
        "  • high_performers: COUNT where rating >= 4\n"
        "  • low_performers: COUNT where rating <= 2\n"
        "  • total_payroll: SUM(salary)\n"
        "Sort by headcount descending.\n\n"
        "Expected output:\n[('Sales',4,4112.0,2,1,16450.0), ('Engineering',2,5500.0,2,0,11000.0), ('HR',2,3400.0,0,1,6800.0)]"
    ),
    expected_output="[('Sales', 4, 4112.0, 2, 1, 16450.0), ('Engineering', 2, 5500.0, 2, 0, 11000.0), ('HR', 2, 3400.0, 0, 1, 6800.0)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE employees (id INTEGER, name TEXT, dept TEXT, salary REAL, rating INTEGER);",
        "INSERT INTO employees VALUES (1,'Emperor','Engineering',5000,5), (2,'Rahim','Sales',4000,3), (3,'Karim','Engineering',6000,4), (4,'Ali','Sales',4500,4), (5,'Hasan','Sales',3500,1), (6,'Fatima','HR',3000,2), (7,'Akbar','Sales',4000,4), (8,'Rana','HR',3800,3);",
        "SELECT dept, COUNT(*) AS headcount, ROUND(AVG(salary), 0) AS avg_salary, COUNT(CASE WHEN rating >= 4 THEN 1 END) AS high_performers, COUNT(CASE WHEN rating <= 2 THEN 1 END) AS low_performers, SUM(salary) AS total_payroll FROM employees GROUP BY dept ORDER BY headcount DESC;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L27.json",
        module_name="Module_03_Aggregation_Grouping",
        lesson_name="L27_Aggregation_with_CASE"
    )
