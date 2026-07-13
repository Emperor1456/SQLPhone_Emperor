import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "📈  ANY – Salary Greater Than Any in Regiment 2\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Write a query that returns the name and salary of\n"
        "soldiers whose salary is greater than ANY salary\n"
        "in Regiment 2.\n"
        "Use > ANY with a subquery.\n"
        "Sort by salary descending.\n\n"
        "Expected output:\n[('Emperor',5000.0), ('Ali',4500.0), ('Rahim',4000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, regiment_id INTEGER, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor',1,5000), (2,'Rahim',2,4000), (3,'Karim',2,2000), (4,'Ali',1,4500), (5,'Hasan',1,3500);"
    ),
    expected_output="[('Emperor', 5000.0), ('Ali', 4500.0), ('Rahim', 4000.0)]",
    level=Level.EASY,
    hints=[
        "SELECT name, salary FROM soldiers WHERE salary > ANY (SELECT salary FROM soldiers WHERE regiment_id = 2) ORDER BY salary DESC;"
    ]
)

easy2 = Task(
    description=(
        "📉  ALL – Salary Greater Than All in Regiment 2\n\n"
        "The same `soldiers` table.\n"
        "Write a query that returns the name and salary of\n"
        "soldiers whose salary is greater than ALL salaries\n"
        "in Regiment 2.\n"
        "Use > ALL with a subquery.\n"
        "Sort by salary descending.\n\n"
        "Expected output:\n[('Emperor',5000.0), ('Ali',4500.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, regiment_id INTEGER, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor',1,5000), (2,'Rahim',2,4000), (3,'Karim',2,2000), (4,'Ali',1,4500), (5,'Hasan',1,3500);"
    ),
    expected_output="[('Emperor', 5000.0), ('Ali', 4500.0)]",
    level=Level.EASY,
    hints=[
        "SELECT name, salary FROM soldiers WHERE salary > ALL (SELECT salary FROM soldiers WHERE regiment_id = 2) ORDER BY salary DESC;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🧪  = ANY – Equivalent to IN\n\n"
        "The `regiments` and `soldiers` tables exist.\n"
        "Write a query that returns the names of soldiers\n"
        "whose regiment_id matches ANY regiment that has\n"
        "been deployed.\n"
        "Use = ANY (which is equivalent to IN).\n"
        "Sort by name.\n\n"
        "Expected output:\n[('Ali',), ('Emperor',), ('Hasan',)]"
    ),
    setup_sql=(
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT);"
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard'), (3,'Blue Shield');"
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER);"
        "INSERT INTO soldiers VALUES (1,'Emperor',1), (2,'Rahim',3), (3,'Ali',1), (4,'Hasan',2);"
        "CREATE TABLE deployments (id INTEGER PRIMARY KEY, regiment_id INTEGER);"
        "INSERT INTO deployments VALUES (1,1), (2,2);"
    ),
    expected_output="[('Ali',), ('Emperor',), ('Hasan',)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT name FROM soldiers WHERE regiment_id = ANY (SELECT regiment_id FROM deployments) ORDER BY name;"
    ]
)

medium2 = Task(
    description=(
        "📊  <> ALL – Equivalent to NOT IN (Safe)\n\n"
        "The same tables exist.\n"
        "Write a query that returns the names of soldiers\n"
        "whose regiment_id does NOT match ANY deployed regiment.\n"
        "Use <> ALL (safer than NOT IN with NULLs).\n"
        "Sort by name.\n\n"
        "Expected output: [('Rahim',)]"
    ),
    setup_sql=(
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT);"
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard'), (3,'Blue Shield');"
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER);"
        "INSERT INTO soldiers VALUES (1,'Emperor',1), (2,'Rahim',3), (3,'Ali',1), (4,'Hasan',2);"
        "CREATE TABLE deployments (id INTEGER PRIMARY KEY, regiment_id INTEGER);"
        "INSERT INTO deployments VALUES (1,1), (2,2);"
    ),
    expected_output="[('Rahim',)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT name FROM soldiers WHERE regiment_id <> ALL (SELECT regiment_id FROM deployments) ORDER BY name;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧮  ALL with Correlated Subquery – Top in Regiment\n\n"
        "Create tables `regiments` and `soldiers` with salaries.\n"
        "Write a query that returns the name and salary of\n"
        "soldiers whose salary >= ALL salaries in their OWN regiment\n"
        "(i.e., the highest‑paid soldier in each regiment).\n"
        "Use a correlated subquery with >= ALL.\n"
        "Sort by name.\n\n"
        "Expected output:\n[('Ali',4500.0), ('Emperor',5000.0)]"
    ),
    expected_output="[('Ali', 4500.0), ('Emperor', 5000.0)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard');",
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER, salary REAL);",
        "INSERT INTO soldiers VALUES (1,'Emperor',1,5000), (2,'Rahim',2,4000), (3,'Ali',2,4500), (4,'Hasan',2,3500);",
        "SELECT name, salary FROM soldiers s1 WHERE salary >= ALL (SELECT salary FROM soldiers s2 WHERE s2.regiment_id = s1.regiment_id) ORDER BY name;"
    ]
)

hard2 = Task(
    description=(
        "📊  ALL with HAVING – Above All Averages\n\n"
        "Create a table `departments` and `employees` with salaries.\n"
        "Write a query that returns department names whose\n"
        "AVG(salary) > ALL average salaries of other departments.\n"
        "Use GROUP BY, HAVING, and a subquery with ALL.\n"
        "Sort by department name.\n\n"
        "Expected output: [('Engineering',)]"
    ),
    expected_output="[('Engineering',)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE departments (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO departments VALUES (1,'Engineering'), (2,'Sales'), (3,'HR');",
        "CREATE TABLE employees (id INTEGER, name TEXT, dept_id INTEGER, salary REAL);",
        "INSERT INTO employees VALUES (1,'Emperor',1,5000), (2,'Rahim',2,4000), (3,'Ali',1,4500), (4,'Hasan',2,3500), (5,'Fatima',3,3000), (6,'Karim',3,2800);",
        "SELECT d.name FROM departments d JOIN employees e ON d.id = e.dept_id GROUP BY d.id HAVING AVG(e.salary) > ALL (SELECT AVG(e2.salary) FROM employees e2 WHERE e2.dept_id <> d.id);"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L45.json",
        module_name="Module_05_Subqueries_CTEs",
        lesson_name="L45_ANY_ALL"
    )
