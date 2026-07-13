import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🔍  Correlated Subquery – Above Regimental Average\n\n"
        "Create tables `regiments` and `soldiers` with salaries.\n"
        "Write a query that returns the name and salary of\n"
        "soldiers whose salary is greater than the average\n"
        "salary of their OWN regiment.\n"
        "Use a correlated subquery in WHERE.\n"
        "Sort by name.\n\n"
        "Expected output:\n[('Emperor',5000.0), ('Rahim',4000.0)]"
    ),
    expected_output="[('Emperor', 5000.0), ('Rahim', 4000.0)]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard');",
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER, salary REAL);",
        "INSERT INTO soldiers VALUES (1,'Emperor',1,5000), (2,'Rahim',2,4000), (3,'Ali',2,3500), (4,'Hasan',2,3000);",
        "SELECT name, salary FROM soldiers s1 WHERE salary > (SELECT AVG(salary) FROM soldiers s2 WHERE s2.regiment_id = s1.regiment_id) ORDER BY name;"
    ]
)

easy2 = Task(
    description=(
        "📊  Correlated Subquery in SELECT – Regiment Size\n\n"
        "The same tables exist.\n"
        "Write a query that returns each soldier's name and\n"
        "the total number of soldiers in their regiment.\n"
        "Use a correlated scalar subquery in SELECT.\n"
        "Sort by name.\n\n"
        "Expected output:\n[('Ali',3), ('Emperor',1), ('Hasan',3), ('Rahim',3)]"
    ),
    setup_sql=(
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT);"
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard');"
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor',1,5000), (2,'Rahim',2,4000), (3,'Ali',2,3500), (4,'Hasan',2,3000);"
    ),
    expected_output="[('Ali', 3), ('Emperor', 1), ('Hasan', 3), ('Rahim', 3)]",
    level=Level.EASY,
    hints=[
        "SELECT name, (SELECT COUNT(*) FROM soldiers s2 WHERE s2.regiment_id = s1.regiment_id) AS regiment_size FROM soldiers s1 ORDER BY name;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🧮  Rank Within Regiment – Correlated Subquery\n\n"
        "The same tables exist.\n"
        "Write a query that returns each soldier's name, regiment_id,\n"
        "salary, and their rank within their regiment (1 = highest salary).\n"
        "Use a correlated scalar subquery that counts how many soldiers\n"
        "in the same regiment have a higher salary, then add 1.\n"
        "Sort by regiment_id, then rank.\n\n"
        "Expected output:\n[(1,'Emperor',5000.0,1), (1,'Hasan',3000.0,2), (2,'Rahim',4000.0,1), (2,'Ali',3500.0,2)]"
    ),
    setup_sql=(
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT);"
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard');"
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor',1,5000), (2,'Rahim',2,4000), (3,'Ali',2,3500), (4,'Hasan',2,3000);"
    ),
    expected_output="[(1, 'Emperor', 5000.0, 1), (1, 'Hasan', 3000.0, 2), (2, 'Rahim', 4000.0, 1), (2, 'Ali', 3500.0, 2)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT regiment_id, name, salary, (SELECT COUNT(*) FROM soldiers s2 WHERE s2.regiment_id = s1.regiment_id AND s2.salary > s1.salary) + 1 AS rank FROM soldiers s1 ORDER BY regiment_id, rank;"
    ]
)

medium2 = Task(
    description=(
        "📈  Difference from Regimental Average\n\n"
        "The same tables exist.\n"
        "Write a query that returns name, salary, and a\n"
        "computed column `diff_from_reg_avg` (salary - regimental average).\n"
        "Round to 2 decimals.\n"
        "Use a correlated scalar subquery in SELECT.\n"
        "Sort by diff_from_reg_avg descending.\n\n"
        "Expected output:\n[('Emperor',5000.0,1000.0), ('Rahim',4000.0,500.0), ('Ali',3500.0,0.0), ('Hasan',3000.0,-500.0)]"
    ),
    setup_sql=(
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT);"
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard');"
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor',1,5000), (2,'Rahim',2,4000), (3,'Ali',2,3500), (4,'Hasan',2,3000);"
    ),
    expected_output="[('Emperor', 5000.0, 1000.0), ('Rahim', 4000.0, 500.0), ('Ali', 3500.0, 0.0), ('Hasan', 3000.0, -500.0)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT name, salary, ROUND(salary - (SELECT AVG(salary) FROM soldiers s2 WHERE s2.regiment_id = s1.regiment_id), 2) AS diff_from_reg_avg FROM soldiers s1 ORDER BY diff_from_reg_avg DESC;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  Running Total per Regiment – Correlated Subquery\n\n"
        "The same tables exist.\n"
        "Write a query that returns name, regiment_id, salary,\n"
        "and a running total of salaries within each regiment,\n"
        "ordered by salary descending.\n"
        "Use a correlated subquery that SUMs salaries >= current\n"
        "row's salary within the same regiment.\n"
        "Sort by regiment_id, then salary DESC.\n\n"
        "Expected output:\n[('Emperor',1,5000.0,5000.0), ('Hasan',2,3000.0,3000.0), ('Rahim',2,4000.0,7000.0), ('Ali',2,3500.0,10500.0)]"
    ),
    setup_sql=(
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT);"
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard');"
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor',1,5000), (2,'Rahim',2,4000), (3,'Ali',2,3500), (4,'Hasan',2,3000);"
    ),
    expected_output="[('Emperor', 1, 5000.0, 5000.0), ('Hasan', 2, 3000.0, 3000.0), ('Rahim', 2, 4000.0, 7000.0), ('Ali', 2, 3500.0, 10500.0)]",
    level=Level.HARD,
    hints=[
        "SELECT name, regiment_id, salary, (SELECT SUM(salary) FROM soldiers s2 WHERE s2.regiment_id = s1.regiment_id AND s2.salary >= s1.salary) AS running_total FROM soldiers s1 ORDER BY regiment_id, salary DESC;"
    ]
)

hard2 = Task(
    description=(
        "📊  Percentage of Regimental Payroll – Advanced\n\n"
        "The same tables exist.\n"
        "Write a query that returns name, salary, regiment_id,\n"
        "and the percentage of the regiment's total payroll\n"
        "that this soldier represents (ROUND to 1 decimal).\n"
        "Use correlated subqueries for both the soldier's salary\n"
        "and the regiment's total payroll.\n"
        "Sort by regiment_id, then percentage DESC.\n\n"
        "Expected output:\n[('Emperor',1,5000.0,100.0), ('Rahim',2,4000.0,38.1), ('Ali',2,3500.0,33.3), ('Hasan',2,3000.0,28.6)]"
    ),
    setup_sql=(
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT);"
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard');"
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor',1,5000), (2,'Rahim',2,4000), (3,'Ali',2,3500), (4,'Hasan',2,3000);"
    ),
    expected_output="[('Emperor', 1, 5000.0, 100.0), ('Rahim', 2, 4000.0, 38.1), ('Ali', 2, 3500.0, 33.3), ('Hasan', 2, 3000.0, 28.6)]",
    level=Level.HARD,
    hints=[
        "SELECT name, regiment_id, salary, ROUND(salary * 100.0 / (SELECT SUM(salary) FROM soldiers s2 WHERE s2.regiment_id = s1.regiment_id), 1) AS pct_of_payroll FROM soldiers s1 ORDER BY regiment_id, pct_of_payroll DESC;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L46.json",
        module_name="Module_05_Subqueries_CTEs",
        lesson_name="L46_Correlated_Subqueries"
    )
