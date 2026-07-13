import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🔢  COUNT – Total Soldiers\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Write a query that returns the total number\n"
        "of rows in the table. Use COUNT(*).\n\n"
        "Expected output: [(5,)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[(5,)]",
    level=Level.EASY,
    hints=[
        "SELECT COUNT(*) FROM soldiers;"
    ]
)

easy2 = Task(
    description=(
        "➕  SUM – Total Payroll\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Write a query that returns the sum of all\n"
        "salaries. Use SUM(salary).\n\n"
        "Expected output: [(19000.0,)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[(19000.0,)]",
    level=Level.EASY,
    hints=[
        "SELECT SUM(salary) FROM soldiers;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "📊  AVG – Average Salary\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Write a query that returns the average salary\n"
        "of all soldiers. Use AVG(salary).\n\n"
        "Expected output: [(3800.0,)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[(3800.0,)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT AVG(salary) FROM soldiers;"
    ]
)

medium2 = Task(
    description=(
        "🧮  COUNT with DISTINCT – Unique Ranks\n\n"
        "The `soldiers` table has 5 rows, but only\n"
        "3 unique ranks (General, Colonel, Private).\n"
        "Write a query that counts how many DISTINCT\n"
        "ranks exist.\n\n"
        "Expected output: [(3,)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[(3,)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT COUNT(DISTINCT rank) FROM soldiers;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "⚠️  NULL in Aggregates – Know the Trap\n\n"
        "Create a table `missions` with columns:\n"
        "  • id INTEGER, name TEXT, reward REAL.\n"
        "Insert 5 rows where TWO have NULL reward.\n"
        "Then write a query that returns ALL of these\n"
        "in a single row:\n"
        "  • total_rows: COUNT(*)\n"
        "  • counted_rewards: COUNT(reward)\n"
        "  • total_reward: SUM(reward)\n"
        "  • avg_reward: AVG(reward)\n\n"
        "Expected output: [(5, 3, 7500.0, 2500.0)]"
    ),
    expected_output="[(5, 3, 7500.0, 2500.0)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE missions (id INTEGER, name TEXT, reward REAL);",
        "INSERT INTO missions VALUES (1,'Patrol',2000), (2,'Recon',NULL), (3,'Supply',2500), (4,'Guard',3000), (5,'Train',NULL);",
        "SELECT COUNT(*) AS total_rows, COUNT(reward) AS counted_rewards, SUM(reward) AS total_reward, AVG(reward) AS avg_reward FROM missions;"
    ]
)

hard2 = Task(
    description=(
        "💰  Aggregates + WHERE – Active Payroll\n\n"
        "Create a table `employees` with columns:\n"
        "  • id INTEGER, name TEXT, status TEXT, salary REAL.\n"
        "Insert 6 rows with mixed statuses ('active','reserve').\n"
        "Write a query that returns, for ACTIVE employees only:\n"
        "  • count: COUNT(*)\n"
        "  • total_pay: SUM(salary)\n"
        "  • avg_pay: ROUND(AVG(salary), 2)\n"
        "  • highest: MAX(salary)\n"
        "  • lowest: MIN(salary)\n\n"
        "Expected output: [(3, 10500.0, 3500.0, 4500.0, 2500.0)]"
    ),
    expected_output="[(3, 10500.0, 3500.0, 4500.0, 2500.0)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE employees (id INTEGER, name TEXT, status TEXT, salary REAL);",
        "INSERT INTO employees VALUES (1,'Emperor','active',4500), (2,'Rahim','reserve',4000), (3,'Karim','active',2500), (4,'Ali','reserve',3000), (5,'Hasan','active',3500), (6,'Fatima','reserve',5000);",
        "SELECT COUNT(*) AS count, SUM(salary) AS total_pay, ROUND(AVG(salary), 2) AS avg_pay, MAX(salary) AS highest, MIN(salary) AS lowest FROM employees WHERE status = 'active';"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L21.json",
        module_name="Module_03_Aggregation_Grouping",
        lesson_name="L21_COUNT_SUM_AVG"
    )
