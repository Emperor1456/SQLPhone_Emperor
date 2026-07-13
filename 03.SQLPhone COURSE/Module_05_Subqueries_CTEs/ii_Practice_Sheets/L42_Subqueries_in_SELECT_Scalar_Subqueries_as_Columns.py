import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "📊  Scalar Subquery – Overall Average\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Write a query that returns each soldier's name, salary,\n"
        "and the overall average salary as a third column.\n"
        "Use a scalar subquery in the SELECT list.\n"
        "Sort by name.\n\n"
        "Expected output:\n[('Ali',4500.0,3800.0), ('Emperor',5000.0,3800.0), ('Hasan',3500.0,3800.0), ('Karim',2000.0,3800.0), ('Rahim',4000.0,3800.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[('Ali', 4500.0, 3800.0), ('Emperor', 5000.0, 3800.0), ('Hasan', 3500.0, 3800.0), ('Karim', 2000.0, 3800.0), ('Rahim', 4000.0, 3800.0)]",
    level=Level.EASY,
    hints=[
        "SELECT name, salary, (SELECT AVG(salary) FROM soldiers) AS overall_avg FROM soldiers ORDER BY name;"
    ]
)

easy2 = Task(
    description=(
        "📈  Scalar Subquery – Count per Regiment\n\n"
        "Create tables `regiments` and `soldiers`.\n"
        "Write a query that returns each soldier's name and\n"
        "the total number of soldiers in their regiment.\n"
        "Use a correlated scalar subquery in SELECT.\n"
        "Sort by name.\n\n"
        "Expected output:\n[('Ali',3), ('Emperor',1), ('Hasan',3), ('Rahim',3)]"
    ),
    expected_output="[('Ali', 3), ('Emperor', 1), ('Hasan', 3), ('Rahim', 3)]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard');",
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER);",
        "INSERT INTO soldiers VALUES (1,'Emperor',1), (2,'Rahim',2), (3,'Ali',2), (4,'Hasan',2);",
        "SELECT name, (SELECT COUNT(*) FROM soldiers s2 WHERE s2.regiment_id = s1.regiment_id) AS regiment_size FROM soldiers s1 ORDER BY name;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "💰  Difference from Average – Scalar Subquery\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Write a query that returns name, salary, and a\n"
        "computed column `diff_from_avg` (salary - overall avg).\n"
        "Round the difference to 2 decimal places.\n"
        "Use a scalar subquery in SELECT.\n"
        "Sort by diff_from_avg descending.\n\n"
        "Expected output:\n[('Emperor',5000.0,1200.0), ('Ali',4500.0,700.0), ('Rahim',4000.0,200.0), ('Hasan',3500.0,-300.0), ('Karim',2000.0,-1800.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[('Emperor', 5000.0, 1200.0), ('Ali', 4500.0, 700.0), ('Rahim', 4000.0, 200.0), ('Hasan', 3500.0, -300.0), ('Karim', 2000.0, -1800.0)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT name, salary, ROUND(salary - (SELECT AVG(salary) FROM soldiers), 2) AS diff_from_avg FROM soldiers ORDER BY diff_from_avg DESC;"
    ]
)

medium2 = Task(
    description=(
        "📊  Product Price vs Category Average\n\n"
        "Create a table `products` with columns (id, name, category, price).\n"
        "Write a query that returns name, price, and a column\n"
        "showing the average price of products in the same category.\n"
        "Use a correlated scalar subquery.\n"
        "Sort by category, then name.\n\n"
        "Expected output:\n[('Laptop','Electronics',1000.0,750.0), ('Mouse','Electronics',50.0,750.0), ('Monitor','Electronics',300.0,750.0), ('Chair','Furniture',250.0,375.0), ('Desk','Furniture',500.0,375.0)]"
    ),
    expected_output="[('Laptop', 'Electronics', 1000.0, 750.0), ('Mouse', 'Electronics', 50.0, 750.0), ('Monitor', 'Electronics', 300.0, 750.0), ('Chair', 'Furniture', 250.0, 375.0), ('Desk', 'Furniture', 500.0, 375.0)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, category TEXT, price REAL);",
        "INSERT INTO products VALUES (1,'Laptop','Electronics',1000), (2,'Mouse','Electronics',50), (3,'Desk','Furniture',500), (4,'Chair','Furniture',250), (5,'Monitor','Electronics',300);",
        "SELECT name, category, price, (SELECT AVG(price) FROM products p2 WHERE p2.category = p1.category) AS category_avg FROM products p1 ORDER BY category, name;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  Rank Within Regiment – Correlated Subquery\n\n"
        "Create tables `regiments` and `soldiers` with salaries.\n"
        "Write a query that returns each soldier's name, regiment_id,\n"
        "salary, and their rank within their regiment (1 = highest salary).\n"
        "Use a correlated scalar subquery that counts how many soldiers\n"
        "in the same regiment have a higher salary, then add 1.\n"
        "Sort by regiment_id, then rank.\n\n"
        "Expected output:\n[(1,'Emperor',5000.0,1), (1,'Hasan',3500.0,2), (2,'Ali',4500.0,1), (2,'Rahim',4000.0,2), (2,'Karim',2000.0,3)]"
    ),
    expected_output="[(1, 'Emperor', 5000.0, 1), (1, 'Hasan', 3500.0, 2), (2, 'Ali', 4500.0, 1), (2, 'Rahim', 4000.0, 2), (2, 'Karim', 2000.0, 3)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard');",
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER, salary REAL);",
        "INSERT INTO soldiers VALUES (1,'Emperor',1,5000), (2,'Rahim',2,4000), (3,'Karim',2,2000), (4,'Ali',2,4500), (5,'Hasan',1,3500);",
        "SELECT regiment_id, name, salary, (SELECT COUNT(*) FROM soldiers s2 WHERE s2.regiment_id = s1.regiment_id AND s2.salary > s1.salary) + 1 AS rank FROM soldiers s1 ORDER BY regiment_id, rank;"
    ]
)

hard2 = Task(
    description=(
        "📊  Multi‑Scalar Dashboard – One Row Summary\n\n"
        "Create a table `transactions` with columns (id, type, amount).\n"
        "Write ONE query that returns a single row with:\n"
        "  • total_txns: COUNT(*)\n"
        "  • total_amount: SUM(amount)\n"
        "  • deposit_count: (scalar subquery: COUNT where type='deposit')\n"
        "  • withdrawal_count: (scalar subquery: COUNT where type='withdrawal')\n"
        "  • max_deposit: (scalar subquery: MAX where type='deposit')\n\n"
        "Expected output: [(5, 2500.0, 3, 2, 1200.0)]"
    ),
    expected_output="[(5, 2500.0, 3, 2, 1200.0)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE transactions (id INTEGER, type TEXT, amount REAL);",
        "INSERT INTO transactions VALUES (1,'deposit',500), (2,'withdrawal',200), (3,'deposit',1200), (4,'withdrawal',300), (5,'deposit',700);",
        "SELECT COUNT(*) AS total_txns, SUM(amount) AS total_amount, (SELECT COUNT(*) FROM transactions WHERE type='deposit') AS deposit_count, (SELECT COUNT(*) FROM transactions WHERE type='withdrawal') AS withdrawal_count, (SELECT MAX(amount) FROM transactions WHERE type='deposit') AS max_deposit FROM transactions;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L42.json",
        module_name="Module_05_Subqueries_CTEs",
        lesson_name="L42_Subqueries_in_SELECT"
    )
