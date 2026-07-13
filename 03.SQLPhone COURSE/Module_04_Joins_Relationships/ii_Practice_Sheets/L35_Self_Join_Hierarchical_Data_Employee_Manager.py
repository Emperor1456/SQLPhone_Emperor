import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🧬  Self‑Join – Employee + Manager\n\n"
        "Create a table `employees` with columns:\n"
        "  • emp_id INTEGER PRIMARY KEY\n"
        "  • name TEXT NOT NULL\n"
        "  • manager_id INTEGER REFERENCES employees(emp_id)\n\n"
        "Insert 5 employees: Emperor (CEO, no manager),\n"
        "Rahim and Ali (report to Emperor),\n"
        "Hasan (reports to Rahim), Fatima (reports to Ali).\n\n"
        "Write a self‑join that returns each employee's name\n"
        "and their manager's name. Use LEFT JOIN so the CEO\n"
        "appears with NULL manager.\n"
        "Sort by employee name.\n\n"
        "Expected output:\n[('Ali','Emperor'), ('Emperor',None), ('Fatima','Ali'), ('Hasan','Rahim'), ('Rahim','Emperor')]"
    ),
    expected_output="[('Ali', 'Emperor'), ('Emperor', None), ('Fatima', 'Ali'), ('Hasan', 'Rahim'), ('Rahim', 'Emperor')]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT NOT NULL, manager_id INTEGER REFERENCES employees(emp_id));",
        "INSERT INTO employees VALUES (1,'Emperor',NULL), (2,'Rahim',1), (3,'Ali',1), (4,'Hasan',2), (5,'Fatima',3);",
        "SELECT e.name, m.name AS manager FROM employees e LEFT JOIN employees m ON e.manager_id = m.emp_id ORDER BY e.name;"
    ]
)

easy2 = Task(
    description=(
        "🔍  Find Top‑Level – WHERE manager_id IS NULL\n\n"
        "The same `employees` table exists.\n"
        "Write a query that returns the names of employees\n"
        "who have no manager (i.e., the CEO).\n\n"
        "Expected output: [('Emperor',)]"
    ),
    setup_sql=(
        "CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT NOT NULL, manager_id INTEGER REFERENCES employees(emp_id));"
        "INSERT INTO employees VALUES (1,'Emperor',NULL), (2,'Rahim',1), (3,'Ali',1), (4,'Hasan',2), (5,'Fatima',3);"
    ),
    expected_output="[('Emperor',)]",
    level=Level.EASY,
    hints=[
        "SELECT name FROM employees WHERE manager_id IS NULL;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "📊  Count Direct Reports – GROUP BY Self‑Join\n\n"
        "The `employees` table has 5 rows.\n"
        "Write a query that shows each manager and how many\n"
        "employees report directly to them.\n"
        "Include managers with zero direct reports.\n"
        "Use a LEFT JOIN and GROUP BY.\n"
        "Return manager name and the count.\n"
        "Sort by count descending.\n\n"
        "Expected output:\n[('Emperor',2), ('Ali',1), ('Rahim',1), ('Fatima',0), ('Hasan',0)]"
    ),
    setup_sql=(
        "CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT NOT NULL, manager_id INTEGER REFERENCES employees(emp_id));"
        "INSERT INTO employees VALUES (1,'Emperor',NULL), (2,'Rahim',1), (3,'Ali',1), (4,'Hasan',2), (5,'Fatima',3);"
    ),
    expected_output="[('Emperor', 2), ('Ali', 1), ('Rahim', 1), ('Fatima', 0), ('Hasan', 0)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT m.name AS manager, COUNT(e.emp_id) AS direct_reports FROM employees m LEFT JOIN employees e ON m.emp_id = e.manager_id GROUP BY m.emp_id ORDER BY direct_reports DESC;"
    ]
)

medium2 = Task(
    description=(
        "🧪  Find Managers – DISTINCT with Self‑Join\n\n"
        "The `employees` table has 5 rows.\n"
        "Write a query that returns the names of all employees\n"
        "who are managers (i.e., their emp_id appears in\n"
        "someone else's manager_id).\n"
        "Use a self‑join or a subquery.\n"
        "Sort by name.\n\n"
        "Expected output:\n[('Ali',), ('Emperor',), ('Rahim',)]"
    ),
    setup_sql=(
        "CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT NOT NULL, manager_id INTEGER REFERENCES employees(emp_id));"
        "INSERT INTO employees VALUES (1,'Emperor',NULL), (2,'Rahim',1), (3,'Ali',1), (4,'Hasan',2), (5,'Fatima',3);"
    ),
    expected_output="[('Ali',), ('Emperor',), ('Rahim',)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT DISTINCT m.name FROM employees m JOIN employees e ON m.emp_id = e.manager_id ORDER BY m.name;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🔗  Reporting Chain – Two‑Level Self‑Join\n\n"
        "The `employees` table has 5 rows.\n"
        "Write a query that shows each employee, their\n"
        "direct manager, and their grand‑manager\n"
        "(manager's manager). Use two LEFT JOINs.\n"
        "Return employee name, manager name, grand_manager name.\n"
        "Sort by employee name.\n\n"
        "Expected output:\n[('Ali','Emperor',None), ('Emperor',None,None), ('Fatima','Ali','Emperor'), ('Hasan','Rahim','Emperor'), ('Rahim','Emperor',None)]"
    ),
    setup_sql=(
        "CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT NOT NULL, manager_id INTEGER REFERENCES employees(emp_id));"
        "INSERT INTO employees VALUES (1,'Emperor',NULL), (2,'Rahim',1), (3,'Ali',1), (4,'Hasan',2), (5,'Fatima',3);"
    ),
    expected_output="[('Ali', 'Emperor', None), ('Emperor', None, None), ('Fatima', 'Ali', 'Emperor'), ('Hasan', 'Rahim', 'Emperor'), ('Rahim', 'Emperor', None)]",
    level=Level.HARD,
    hints=[
        "SELECT e.name, m.name AS manager, gm.name AS grand_manager FROM employees e LEFT JOIN employees m ON e.manager_id = m.emp_id LEFT JOIN employees gm ON m.manager_id = gm.emp_id ORDER BY e.name;"
    ]
)

hard2 = Task(
    description=(
        "📊  Team Size – Including Sub‑Reports\n\n"
        "Create a slightly larger `employees` table with 8 rows\n"
        "and three levels of hierarchy.\n"
        "Write a query that returns, for each manager:\n"
        "  • manager name\n"
        "  • direct_reports (count of employees who report directly)\n"
        "  • total_team_size (direct_reports + their direct_reports\n"
        "    i.e., all people under them, computed via two self‑joins)\n"
        "Use subqueries or multiple self‑joins.\n"
        "Sort by total_team_size descending.\n\n"
        "Expected output:\n[('Emperor',2,4), ('Rahim',2,2), ('Ali',1,1), ('Fatima',0,0), ('Hasan',0,0), ('Karim',0,0), ('Akbar',0,0)]"
    ),
    expected_output="[('Emperor', 2, 4), ('Rahim', 2, 2), ('Ali', 1, 1), ('Fatima', 0, 0), ('Hasan', 0, 0), ('Karim', 0, 0), ('Akbar', 0, 0)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT NOT NULL, manager_id INTEGER REFERENCES employees(emp_id));",
        "INSERT INTO employees VALUES (1,'Emperor',NULL), (2,'Rahim',1), (3,'Ali',1), (4,'Hasan',2), (5,'Fatima',3), (6,'Karim',2), (7,'Akbar',4);",
        "SELECT m.name AS manager, COUNT(DISTINCT e.emp_id) AS direct_reports, COUNT(DISTINCT sub.emp_id) AS total_team_size FROM employees m LEFT JOIN employees e ON m.emp_id = e.manager_id LEFT JOIN employees sub ON e.emp_id = sub.manager_id OR m.emp_id = sub.manager_id GROUP BY m.emp_id ORDER BY total_team_size DESC;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L35.json",
        module_name="Module_04_Joins_Relationships",
        lesson_name="L35_Self_Join"
    )
