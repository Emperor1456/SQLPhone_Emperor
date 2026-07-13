import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "📈  MAX – Highest Salary\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Return the single highest salary.\n"
        "Use MAX(salary).\n\n"
        "Expected output: [(5000.0,)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[(5000.0,)]",
    level=Level.EASY,
    hints=[
        "SELECT MAX(salary) FROM soldiers;"
    ]
)

easy2 = Task(
    description=(
        "📉  MIN – Lowest Salary\n\n"
        "The same `soldiers` table.\n"
        "Return the single lowest salary.\n"
        "Use MIN(salary).\n\n"
        "Expected output: [(2000.0,)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[(2000.0,)]",
    level=Level.EASY,
    hints=[
        "SELECT MIN(salary) FROM soldiers;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "📊  Salary Range – MAX - MIN\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Compute the range of salaries:\n"
        "  range = MAX(salary) - MIN(salary)\n"
        "Return a single value as `salary_range`.\n\n"
        "Expected output: [(3000.0,)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[(3000.0,)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT MAX(salary) - MIN(salary) AS salary_range FROM soldiers;"
    ]
)

medium2 = Task(
    description=(
        "📅  Date Range – First & Last Joined\n\n"
        "Create a table `recruits` with columns:\n"
        "  • id INTEGER, name TEXT, joined TEXT.\n"
        "Insert 4 rows with different join dates.\n"
        "Return the earliest join date (MIN) and\n"
        "the latest join date (MAX) in a single row.\n\n"
        "Expected output:\n[('2026-01-10','2026-07-01')]"
    ),
    expected_output="[('2026-01-10', '2026-07-01')]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE recruits (id INTEGER, name TEXT, joined TEXT);",
        "INSERT INTO recruits VALUES (1,'Emperor','2026-01-10'), (2,'Rahim','2026-03-20'), (3,'Karim','2026-05-15'), (4,'Ali','2026-07-01');",
        "SELECT MIN(joined), MAX(joined) FROM recruits;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  MAX on Text – Last Alphabetically\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Return the name that comes last alphabetically.\n"
        "Use MAX(name).\n\n"
        "Expected output: [('Rahim',)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[('Rahim',)]",
    level=Level.HARD,
    hints=[
        "SELECT MAX(name) FROM soldiers;"
    ]
)

hard2 = Task(
    description=(
        "📊  MIN/MAX with Filter – Top & Bottom\n\n"
        "Create a table `inventory` with columns:\n"
        "  • id INTEGER, item TEXT, qty INTEGER, price REAL.\n"
        "Insert 6 rows with varied data.\n"
        "Write ONE query that returns:\n"
        "  • most_expensive: MAX(price) with its item name\n"
        "  • cheapest: MIN(price) with its item name\n"
        "Hint: Use subqueries or a UNION.\n\n"
        "Expected output:\n[('Laptop',250.0), ('Pen',20.0)]"
    ),
    expected_output="[('Laptop', 250.0), ('Pen', 20.0)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE inventory (id INTEGER, item TEXT, qty INTEGER, price REAL);",
        "INSERT INTO inventory VALUES (1,'Laptop',10,250.0), (2,'Mouse',50,25.0), (3,'Desk',5,200.0), (4,'Pen',100,20.0), (5,'Chair',8,75.0), (6,'Monitor',15,150.0);",
        "SELECT item, price FROM inventory WHERE price = (SELECT MAX(price) FROM inventory) UNION ALL SELECT item, price FROM inventory WHERE price = (SELECT MIN(price) FROM inventory);"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L22.json",
        module_name="Module_03_Aggregation_Grouping",
        lesson_name="L22_MIN_MAX"
    )
