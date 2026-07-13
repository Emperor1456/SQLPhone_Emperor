import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🏗️  Performance Schema – Create Tables & Seed\n\n"
        "Create four tables with full constraints:\n\n"
        "1. `departments` (dept_id PK, dept_name TEXT NOT NULL)\n"
        "2. `employees` (emp_id PK, name TEXT NOT NULL,\n"
        "   dept_id INTEGER REFERENCES departments,\n"
        "   manager_id INTEGER REFERENCES employees,\n"
        "   hire_date TEXT DEFAULT (date('now')))\n"
        "3. `evaluations` (eval_id PK, emp_id INTEGER NOT NULL\n"
        "   REFERENCES employees, eval_date TEXT NOT NULL,\n"
        "   score INTEGER CHECK(score BETWEEN 1 AND 10))\n"
        "4. `goals` (goal_id PK, emp_id INTEGER NOT NULL\n"
        "   REFERENCES employees, description TEXT NOT NULL,\n"
        "   target_date TEXT, completed INTEGER DEFAULT 0\n"
        "   CHECK(completed IN (0,1)))\n\n"
        "Insert 2 departments, 4 employees, 5 evaluations,\n"
        "and 3 goals.\n"
        "Then SELECT all employee names sorted alphabetically.\n\n"
        "Expected output:\n[('Ali',), ('Emperor',), ('Hasan',), ('Rahim',)]"
    ),
    expected_output="[('Ali',), ('Emperor',), ('Hasan',), ('Rahim',)]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE departments (dept_id INTEGER PRIMARY KEY, dept_name TEXT NOT NULL);",
        "INSERT INTO departments VALUES (1,'Engineering'), (2,'Sales');",
        "CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT NOT NULL, dept_id INTEGER REFERENCES departments, manager_id INTEGER REFERENCES employees, hire_date TEXT DEFAULT (date('now')));",
        "INSERT INTO employees VALUES (1,'Emperor',1,NULL,'2025-01-01'), (2,'Rahim',2,1,'2025-03-15'), (3,'Ali',2,1,'2025-06-01'), (4,'Hasan',1,2,'2026-01-10');",
        "CREATE TABLE evaluations (eval_id INTEGER PRIMARY KEY, emp_id INTEGER NOT NULL REFERENCES employees, eval_date TEXT NOT NULL, score INTEGER CHECK(score BETWEEN 1 AND 10));",
        "INSERT INTO evaluations VALUES (1,1,'2026-01-15',9), (2,2,'2026-01-15',7), (3,3,'2026-01-15',6), (4,1,'2026-04-15',8), (5,2,'2026-04-15',8);",
        "CREATE TABLE goals (goal_id INTEGER PRIMARY KEY, emp_id INTEGER NOT NULL REFERENCES employees, description TEXT NOT NULL, target_date TEXT, completed INTEGER DEFAULT 0 CHECK(completed IN (0,1)));",
        "INSERT INTO goals VALUES (1,2,'Complete leadership training','2026-06-30',1), (2,2,'Recruit 10 soldiers','2026-12-31',0), (3,3,'Improve tactical score to 8','2026-09-30',0);",
        "SELECT name FROM employees ORDER BY name;"
    ]
)

easy2 = Task(
    description=(
        "📊  Average Score per Employee – Simple JOIN + GROUP BY\n\n"
        "The tables are seeded.\n"
        "Write a query that returns each employee's name\n"
        "and their average evaluation score.\n"
        "Round to 1 decimal.\n"
        "Include employees with no evaluations (show NULL).\n"
        "Sort by name.\n\n"
        "Expected output:\n[('Ali',6.0), ('Emperor',8.5), ('Hasan',None), ('Rahim',7.5)]"
    ),
    setup_sql=(
        "CREATE TABLE departments (dept_id INTEGER PRIMARY KEY, dept_name TEXT NOT NULL);"
        "INSERT INTO departments VALUES (1,'Engineering'), (2,'Sales');"
        "CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT NOT NULL, dept_id INTEGER REFERENCES departments, manager_id INTEGER REFERENCES employees, hire_date TEXT DEFAULT (date('now')));"
        "INSERT INTO employees VALUES (1,'Emperor',1,NULL,'2025-01-01'), (2,'Rahim',2,1,'2025-03-15'), (3,'Ali',2,1,'2025-06-01'), (4,'Hasan',1,2,'2026-01-10');"
        "CREATE TABLE evaluations (eval_id INTEGER PRIMARY KEY, emp_id INTEGER NOT NULL REFERENCES employees, eval_date TEXT NOT NULL, score INTEGER CHECK(score BETWEEN 1 AND 10));"
        "INSERT INTO evaluations VALUES (1,1,'2026-01-15',9), (2,2,'2026-01-15',7), (3,3,'2026-01-15',6), (4,1,'2026-04-15',8), (5,2,'2026-04-15',8);"
        "CREATE TABLE goals (goal_id INTEGER PRIMARY KEY, emp_id INTEGER NOT NULL REFERENCES employees, description TEXT NOT NULL, target_date TEXT, completed INTEGER DEFAULT 0 CHECK(completed IN (0,1)));"
        "INSERT INTO goals VALUES (1,2,'Complete leadership training','2026-06-30',1), (2,2,'Recruit 10 soldiers','2026-12-31',0), (3,3,'Improve tactical score to 8','2026-09-30',0);"
    ),
    expected_output="[('Ali', 6.0), ('Emperor', 8.5), ('Hasan', None), ('Rahim', 7.5)]",
    level=Level.EASY,
    hints=[
        "SELECT e.name, ROUND(AVG(ev.score), 1) AS avg_score FROM employees e LEFT JOIN evaluations ev ON e.emp_id = ev.emp_id GROUP BY e.emp_id ORDER BY e.name;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🧮  Employee vs Department Average – Correlated Subquery\n\n"
        "The tables are seeded.\n"
        "Write a query that returns each employee's name,\n"
        "their average score, and the average score of\n"
        "their department.\n"
        "Use a correlated subquery to compute the department avg.\n"
        "Round both to 1 decimal.\n"
        "Sort by name.\n\n"
        "Expected output:\n[('Ali',6.0,6.5), ('Emperor',8.5,8.5), ('Hasan',None,8.5), ('Rahim',7.5,6.5)]"
    ),
    setup_sql=(
        "CREATE TABLE departments (dept_id INTEGER PRIMARY KEY, dept_name TEXT NOT NULL);"
        "INSERT INTO departments VALUES (1,'Engineering'), (2,'Sales');"
        "CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT NOT NULL, dept_id INTEGER REFERENCES departments, manager_id INTEGER REFERENCES employees, hire_date TEXT DEFAULT (date('now')));"
        "INSERT INTO employees VALUES (1,'Emperor',1,NULL,'2025-01-01'), (2,'Rahim',2,1,'2025-03-15'), (3,'Ali',2,1,'2025-06-01'), (4,'Hasan',1,2,'2026-01-10');"
        "CREATE TABLE evaluations (eval_id INTEGER PRIMARY KEY, emp_id INTEGER NOT NULL REFERENCES employees, eval_date TEXT NOT NULL, score INTEGER CHECK(score BETWEEN 1 AND 10));"
        "INSERT INTO evaluations VALUES (1,1,'2026-01-15',9), (2,2,'2026-01-15',7), (3,3,'2026-01-15',6), (4,1,'2026-04-15',8), (5,2,'2026-04-15',8);"
        "CREATE TABLE goals (goal_id INTEGER PRIMARY KEY, emp_id INTEGER NOT NULL REFERENCES employees, description TEXT NOT NULL, target_date TEXT, completed INTEGER DEFAULT 0 CHECK(completed IN (0,1)));"
        "INSERT INTO goals VALUES (1,2,'Complete leadership training','2026-06-30',1), (2,2,'Recruit 10 soldiers','2026-12-31',0), (3,3,'Improve tactical score to 8','2026-09-30',0);"
    ),
    expected_output="[('Ali', 6.0, 6.5), ('Emperor', 8.5, 8.5), ('Hasan', None, 8.5), ('Rahim', 7.5, 6.5)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT e.name, ROUND(AVG(ev.score), 1) AS emp_avg, (SELECT ROUND(AVG(ev2.score), 1) FROM evaluations ev2 JOIN employees e2 ON ev2.emp_id = e2.emp_id WHERE e2.dept_id = e.dept_id) AS dept_avg FROM employees e LEFT JOIN evaluations ev ON e.emp_id = ev.emp_id GROUP BY e.emp_id ORDER BY e.name;"
    ]
)

medium2 = Task(
    description=(
        "📈  Goal Completion Rate – LEFT JOIN + Aggregation\n\n"
        "The tables are seeded.\n"
        "Write a query that returns each employee's name,\n"
        "total goals, completed goals, and completion percentage.\n"
        "Round percentage to 1 decimal.\n"
        "Include employees with no goals (show 0).\n"
        "Sort by name.\n\n"
        "Expected output:\n[('Ali',1,0,0.0), ('Emperor',0,0,None), ('Hasan',0,0,None), ('Rahim',2,1,50.0)]"
    ),
    setup_sql=(
        "CREATE TABLE departments (dept_id INTEGER PRIMARY KEY, dept_name TEXT NOT NULL);"
        "INSERT INTO departments VALUES (1,'Engineering'), (2,'Sales');"
        "CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT NOT NULL, dept_id INTEGER REFERENCES departments, manager_id INTEGER REFERENCES employees, hire_date TEXT DEFAULT (date('now')));"
        "INSERT INTO employees VALUES (1,'Emperor',1,NULL,'2025-01-01'), (2,'Rahim',2,1,'2025-03-15'), (3,'Ali',2,1,'2025-06-01'), (4,'Hasan',1,2,'2026-01-10');"
        "CREATE TABLE evaluations (eval_id INTEGER PRIMARY KEY, emp_id INTEGER NOT NULL REFERENCES employees, eval_date TEXT NOT NULL, score INTEGER CHECK(score BETWEEN 1 AND 10));"
        "INSERT INTO evaluations VALUES (1,1,'2026-01-15',9), (2,2,'2026-01-15',7), (3,3,'2026-01-15',6), (4,1,'2026-04-15',8), (5,2,'2026-04-15',8);"
        "CREATE TABLE goals (goal_id INTEGER PRIMARY KEY, emp_id INTEGER NOT NULL REFERENCES employees, description TEXT NOT NULL, target_date TEXT, completed INTEGER DEFAULT 0 CHECK(completed IN (0,1)));"
        "INSERT INTO goals VALUES (1,2,'Complete leadership training','2026-06-30',1), (2,2,'Recruit 10 soldiers','2026-12-31',0), (3,3,'Improve tactical score to 8','2026-09-30',0);"
    ),
    expected_output="[('Ali', 1, 0, 0.0), ('Emperor', 0, 0, None), ('Hasan', 0, 0, None), ('Rahim', 2, 1, 50.0)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT e.name, COUNT(g.goal_id) AS total_goals, SUM(g.completed) AS completed, ROUND(100.0 * SUM(g.completed) / NULLIF(COUNT(g.goal_id), 0), 1) AS completion_pct FROM employees e LEFT JOIN goals g ON e.emp_id = g.emp_id GROUP BY e.emp_id ORDER BY e.name;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧬  Org Chart with Performance – Recursive CTE\n\n"
        "The tables are seeded.\n"
        "Write a recursive CTE named `org` that returns the\n"
        "full org chart with each employee's average score.\n"
        "Start from the CEO (manager_id IS NULL) with level=1.\n"
        "Include a subquery to get each employee's avg_score.\n"
        "Return name, level, and avg_score (rounded to 1 decimal).\n"
        "Sort by level, then name.\n\n"
        "Expected output:\n[('Emperor',1,8.5), ('Ali',2,6.0), ('Rahim',2,7.5), ('Hasan',3,None)]"
    ),
    setup_sql=(
        "CREATE TABLE departments (dept_id INTEGER PRIMARY KEY, dept_name TEXT NOT NULL);"
        "INSERT INTO departments VALUES (1,'Engineering'), (2,'Sales');"
        "CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT NOT NULL, dept_id INTEGER REFERENCES departments, manager_id INTEGER REFERENCES employees, hire_date TEXT DEFAULT (date('now')));"
        "INSERT INTO employees VALUES (1,'Emperor',1,NULL,'2025-01-01'), (2,'Rahim',2,1,'2025-03-15'), (3,'Ali',2,1,'2025-06-01'), (4,'Hasan',1,2,'2026-01-10');"
        "CREATE TABLE evaluations (eval_id INTEGER PRIMARY KEY, emp_id INTEGER NOT NULL REFERENCES employees, eval_date TEXT NOT NULL, score INTEGER CHECK(score BETWEEN 1 AND 10));"
        "INSERT INTO evaluations VALUES (1,1,'2026-01-15',9), (2,2,'2026-01-15',7), (3,3,'2026-01-15',6), (4,1,'2026-04-15',8), (5,2,'2026-04-15',8);"
        "CREATE TABLE goals (goal_id INTEGER PRIMARY KEY, emp_id INTEGER NOT NULL REFERENCES employees, description TEXT NOT NULL, target_date TEXT, completed INTEGER DEFAULT 0 CHECK(completed IN (0,1)));"
        "INSERT INTO goals VALUES (1,2,'Complete leadership training','2026-06-30',1), (2,2,'Recruit 10 soldiers','2026-12-31',0), (3,3,'Improve tactical score to 8','2026-09-30',0);"
    ),
    expected_output="[('Emperor', 1, 8.5), ('Ali', 2, 6.0), ('Rahim', 2, 7.5), ('Hasan', 3, None)]",
    level=Level.HARD,
    hints=[
        "WITH RECURSIVE org AS (SELECT emp_id, name, manager_id, 1 AS level FROM employees WHERE manager_id IS NULL UNION ALL SELECT e.emp_id, e.name, e.manager_id, o.level + 1 FROM employees e JOIN org o ON e.manager_id = o.emp_id) SELECT o.name, o.level, (SELECT ROUND(AVG(ev.score), 1) FROM evaluations ev WHERE ev.emp_id = o.emp_id) AS avg_score FROM org o ORDER BY o.level, o.name;"
    ]
)

hard2 = Task(
    description=(
        "📊  Low Performers with Overdue Goals – CTE + Subquery\n\n"
        "The tables are seeded.\n"
        "Write a query that identifies low performers\n"
        "(average score < 6) who have overdue goals\n"
        "(target_date < date('now') AND completed = 0).\n"
        "Use a CTE `low_performers` to find emp_ids with\n"
        "avg score < 6, then JOIN with goals to find\n"
        "overdue items.\n"
        "Return employee name, avg_score (rounded), goal description,\n"
        "and target_date.\n"
        "Sort by target_date.\n\n"
        "Expected output:\n[('Ali',6.0,'Improve tactical score to 8','2026-09-30')]"
    ),
    setup_sql=(
        "CREATE TABLE departments (dept_id INTEGER PRIMARY KEY, dept_name TEXT NOT NULL);"
        "INSERT INTO departments VALUES (1,'Engineering'), (2,'Sales');"
        "CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT NOT NULL, dept_id INTEGER REFERENCES departments, manager_id INTEGER REFERENCES employees, hire_date TEXT DEFAULT (date('now')));"
        "INSERT INTO employees VALUES (1,'Emperor',1,NULL,'2025-01-01'), (2,'Rahim',2,1,'2025-03-15'), (3,'Ali',2,1,'2025-06-01'), (4,'Hasan',1,2,'2026-01-10');"
        "CREATE TABLE evaluations (eval_id INTEGER PRIMARY KEY, emp_id INTEGER NOT NULL REFERENCES employees, eval_date TEXT NOT NULL, score INTEGER CHECK(score BETWEEN 1 AND 10));"
        "INSERT INTO evaluations VALUES (1,1,'2026-01-15',9), (2,2,'2026-01-15',7), (3,3,'2026-01-15',6), (4,1,'2026-04-15',8), (5,2,'2026-04-15',8);"
        "CREATE TABLE goals (goal_id INTEGER PRIMARY KEY, emp_id INTEGER NOT NULL REFERENCES employees, description TEXT NOT NULL, target_date TEXT, completed INTEGER DEFAULT 0 CHECK(completed IN (0,1)));"
        "INSERT INTO goals VALUES (1,2,'Complete leadership training','2026-06-30',1), (2,2,'Recruit 10 soldiers','2026-12-31',0), (3,3,'Improve tactical score to 8','2026-09-30',0);"
    ),
    expected_output="[('Ali', 6.0, 'Improve tactical score to 8', '2026-09-30')]",
    level=Level.HARD,
    hints=[
        "WITH low_performers AS (SELECT emp_id, ROUND(AVG(score), 1) AS avg_score FROM evaluations GROUP BY emp_id HAVING AVG(score) < 6) SELECT e.name, lp.avg_score, g.description, g.target_date FROM low_performers lp JOIN employees e ON lp.emp_id = e.emp_id JOIN goals g ON e.emp_id = g.emp_id WHERE g.completed = 0 AND g.target_date < date('now') ORDER BY g.target_date;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L50.json",
        module_name="Module_05_Subqueries_CTEs",
        lesson_name="L50_Module_5_Capstone"
    )
