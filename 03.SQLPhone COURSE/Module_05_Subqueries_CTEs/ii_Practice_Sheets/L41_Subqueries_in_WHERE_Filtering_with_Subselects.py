import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🔍  Subquery in WHERE – Above Average Salary\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Write a query that returns the name and salary of\n"
        "soldiers whose salary is greater than the overall\n"
        "average salary.\n"
        "Use a subquery in the WHERE clause.\n"
        "Sort by salary descending.\n\n"
        "Expected output:\n[('Emperor',5000.0), ('Ali',4500.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[('Emperor', 5000.0), ('Ali', 4500.0)]",
    level=Level.EASY,
    hints=[
        "SELECT name, salary FROM soldiers WHERE salary > (SELECT AVG(salary) FROM soldiers) ORDER BY salary DESC;"
    ]
)

easy2 = Task(
    description=(
        "📋  Subquery with IN – Soldiers in Deployed Regiments\n\n"
        "The `regiments` and `soldiers` tables exist.\n"
        "Write a query that returns the names of soldiers\n"
        "whose regiment is located in the 'North' region.\n"
        "Use a subquery with IN.\n"
        "Sort by name.\n\n"
        "Expected output:\n[('Emperor',), ('Hasan',)]"
    ),
    setup_sql=(
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT, region TEXT);"
        "INSERT INTO regiments VALUES (1,'Imperial Guard','North'), (2,'Red Guard','South');"
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER);"
        "INSERT INTO soldiers VALUES (1,'Emperor',1), (2,'Rahim',2), (3,'Ali',2), (4,'Hasan',1);"
    ),
    expected_output="[('Emperor',), ('Hasan',)]",
    level=Level.EASY,
    hints=[
        "SELECT name FROM soldiers WHERE regiment_id IN (SELECT id FROM regiments WHERE region = 'North') ORDER BY name;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🧪  Subquery with NOT IN – Products Never Ordered\n\n"
        "Create tables `products` and `orders`.\n"
        "Write a query that returns the names of products\n"
        "that have NEVER been ordered.\n"
        "Use NOT IN with a subquery.\n"
        "Sort by product name.\n\n"
        "Expected output:\n[('Chair',), ('Desk',)]"
    ),
    expected_output="[('Chair',), ('Desk',)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO products VALUES (1,'Laptop'), (2,'Mouse'), (3,'Chair'), (4,'Desk');",
        "CREATE TABLE orders (id INTEGER PRIMARY KEY, product_id INTEGER);",
        "INSERT INTO orders VALUES (1,1), (2,2), (3,1);",
        "SELECT name FROM products WHERE id NOT IN (SELECT DISTINCT product_id FROM orders) ORDER BY name;"
    ]
)

medium2 = Task(
    description=(
        "📊  Subquery with MAX – Highest Salary per Regiment\n\n"
        "Create tables `regiments` and `soldiers`.\n"
        "Write a query that returns the name and salary of\n"
        "the highest‑paid soldier in the 'Red Guard' regiment.\n"
        "Use a subquery with MAX.\n\n"
        "Expected output:\n[('Ali',4500.0)]"
    ),
    expected_output="[('Ali', 4500.0)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard');",
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER, salary REAL);",
        "INSERT INTO soldiers VALUES (1,'Emperor',1,5000), (2,'Rahim',2,4000), (3,'Ali',2,4500), (4,'Hasan',2,3500);",
        "SELECT name, salary FROM soldiers WHERE regiment_id = (SELECT id FROM regiments WHERE name = 'Red Guard') AND salary = (SELECT MAX(salary) FROM soldiers WHERE regiment_id = 2);"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧮  Correlated Subquery – Above Regimental Average\n\n"
        "Create tables `regiments` and `soldiers`.\n"
        "Write a query that returns the name and salary of\n"
        "soldiers whose salary is greater than the average\n"
        "salary of their OWN regiment.\n"
        "Use a correlated subquery in WHERE.\n"
        "Sort by name.\n\n"
        "Expected output:\n[('Emperor',5000.0), ('Rahim',4000.0)]"
    ),
    expected_output="[('Emperor', 5000.0), ('Rahim', 4000.0)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard');",
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER, salary REAL);",
        "INSERT INTO soldiers VALUES (1,'Emperor',1,5000), (2,'Rahim',2,4000), (3,'Ali',2,3500), (4,'Hasan',2,3000);",
        "SELECT name, salary FROM soldiers s1 WHERE salary > (SELECT AVG(salary) FROM soldiers s2 WHERE s2.regiment_id = s1.regiment_id) ORDER BY name;"
    ]
)

hard2 = Task(
    description=(
        "🔍  Multi‑Level Subquery – Second Highest Salary\n\n"
        "Create a table `employees` with columns (id, name, salary).\n"
        "Write a query that returns the name and salary of the\n"
        "employee with the SECOND highest salary.\n"
        "Use subqueries: one to find the max salary, another to\n"
        "find the max salary excluding that top value.\n\n"
        "Expected output:\n[('Rahim',4000.0)]"
    ),
    expected_output="[('Rahim', 4000.0)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE employees (id INTEGER, name TEXT, salary REAL);",
        "INSERT INTO employees VALUES (1,'Emperor',5000), (2,'Rahim',4000), (3,'Ali',4500), (4,'Hasan',3500);",
        "SELECT name, salary FROM employees WHERE salary = (SELECT MAX(salary) FROM employees WHERE salary < (SELECT MAX(salary) FROM employees));"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L41.json",
        module_name="Module_05_Subqueries_CTEs",
        lesson_name="L41_Subqueries_in_WHERE"
    )
