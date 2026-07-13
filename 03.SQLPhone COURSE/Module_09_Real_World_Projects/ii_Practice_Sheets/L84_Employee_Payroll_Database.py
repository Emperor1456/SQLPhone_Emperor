import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🏢  Imperial Payroll – Build the Schema\n\n"
        "Write Python code that:\n"
        "  1. Connects to ':memory:'\n"
        "  2. Creates the three tables:\n"
        "     departments, employees, deductions\n"
        "     (exact schema from the lecture).\n"
        "  3. Inserts seed data:\n"
        "     • Departments: Engineering (1), Sales (2)\n"
        "     • Employees: Emperor (1, Engineering, 5000, 0.1),\n"
        "       Rahim (2, Sales, 4000, 0.1)\n"
        "     • Deductions: Emperor – 200 for 'Health Insurance'\n"
        "  4. Commits, then SELECTs all employee names\n"
        "     sorted alphabetically and prints them.\n\n"
        "Expected output:\n[('Emperor',), ('Rahim',)]"
    ),
    expected_output="[('Emperor',), ('Rahim',)]",
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.executescript('''",
        "CREATE TABLE departments (dept_id INTEGER PRIMARY KEY, name TEXT NOT NULL);",
        "CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT NOT NULL, dept_id INTEGER, base_salary REAL CHECK(base_salary > 0), tax_rate REAL DEFAULT 0.1, FOREIGN KEY (dept_id) REFERENCES departments(dept_id));",
        "CREATE TABLE deductions (ded_id INTEGER PRIMARY KEY, emp_id INTEGER, amount REAL CHECK(amount > 0), reason TEXT, ded_date TEXT DEFAULT (date('now')), FOREIGN KEY (emp_id) REFERENCES employees(emp_id));",
        "''')",
        "conn.executescript('''",
        "INSERT INTO departments VALUES (1,'Engineering'), (2,'Sales');",
        "INSERT INTO employees VALUES (1,'Emperor',1,5000,0.1);",
        "INSERT INTO employees VALUES (2,'Rahim',2,4000,0.1);",
        "INSERT INTO deductions VALUES (1,1,200,'Health Insurance','2026-07-01');",
        "''')",
        "conn.commit()",
        "cursor = conn.execute('SELECT name FROM employees ORDER BY name')",
        "print(cursor.fetchall())",
    ]
)

easy2 = Task(
    description=(
        "💰  Net Pay – Single Employee\n\n"
        "The payroll database is seeded.\n"
        "Write Python code that computes the net pay for\n"
        "Emperor (emp_id=1) as:\n"
        "  base_salary * (1 - tax_rate) – SUM(deductions)\n"
        "Print only the net pay value (a number).\n\n"
        "Expected output:\n4300.0"
    ),
    setup_sql=(
        "CREATE TABLE departments (dept_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO departments VALUES (1,'Engineering'), (2,'Sales');"
        "CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT NOT NULL, dept_id INTEGER, base_salary REAL CHECK(base_salary > 0), tax_rate REAL DEFAULT 0.1, FOREIGN KEY (dept_id) REFERENCES departments(dept_id));"
        "INSERT INTO employees VALUES (1,'Emperor',1,5000,0.1);"
        "INSERT INTO employees VALUES (2,'Rahim',2,4000,0.1);"
        "CREATE TABLE deductions (ded_id INTEGER PRIMARY KEY, emp_id INTEGER, amount REAL CHECK(amount > 0), reason TEXT, ded_date TEXT DEFAULT (date('now')), FOREIGN KEY (emp_id) REFERENCES employees(emp_id));"
        "INSERT INTO deductions VALUES (1,1,200,'Health Insurance','2026-07-01');"
    ),
    expected_output="4300.0",
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT e.base_salary * (1 - e.tax_rate) - COALESCE(SUM(d.amount), 0)",
        "FROM employees e LEFT JOIN deductions d ON e.emp_id = d.emp_id",
        "WHERE e.emp_id = 1",
        "''')",
        "print(cursor.fetchone()[0])",
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "📊  Net Pay Report – All Employees\n\n"
        "The payroll database is seeded.\n"
        "Write Python code that produces a net pay report\n"
        "for all employees showing:\n"
        "  • employee name\n"
        "  • base_salary\n"
        "  • total_deductions\n"
        "  • net_pay (computed as base_salary*(1‑tax_rate)‑total_deductions)\n"
        "Sort by net_pay descending.\n\n"
        "Expected output:\n"
        "[('Emperor',5000.0,200.0,4300.0), ('Rahim',4000.0,0.0,3600.0)]"
    ),
    setup_sql=(
        "CREATE TABLE departments (dept_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO departments VALUES (1,'Engineering'), (2,'Sales');"
        "CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT NOT NULL, dept_id INTEGER, base_salary REAL CHECK(base_salary > 0), tax_rate REAL DEFAULT 0.1, FOREIGN KEY (dept_id) REFERENCES departments(dept_id));"
        "INSERT INTO employees VALUES (1,'Emperor',1,5000,0.1);"
        "INSERT INTO employees VALUES (2,'Rahim',2,4000,0.1);"
        "CREATE TABLE deductions (ded_id INTEGER PRIMARY KEY, emp_id INTEGER, amount REAL CHECK(amount > 0), reason TEXT, ded_date TEXT DEFAULT (date('now')), FOREIGN KEY (emp_id) REFERENCES employees(emp_id));"
        "INSERT INTO deductions VALUES (1,1,200,'Health Insurance','2026-07-01');"
    ),
    expected_output="[('Emperor', 5000.0, 200.0, 4300.0), ('Rahim', 4000.0, 0.0, 3600.0)]",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT e.name, e.base_salary,",
        "       COALESCE(SUM(d.amount), 0) AS total_deductions,",
        "       e.base_salary * (1 - e.tax_rate) - COALESCE(SUM(d.amount), 0) AS net_pay",
        "FROM employees e LEFT JOIN deductions d ON e.emp_id = d.emp_id",
        "GROUP BY e.emp_id ORDER BY net_pay DESC",
        "''')",
        "print(cursor.fetchall())",
    ]
)

medium2 = Task(
    description=(
        "🧾  Add a Deduction – Recalculate Net Pay\n\n"
        "The payroll database is seeded.\n"
        "Write Python code that:\n"
        "  1. Inserts a new deduction for Rahim (emp_id=2):\n"
        "     150 for 'Gym Membership'.\n"
        "  2. Commits.\n"
        "  3. Recalculates Rahim's net pay and prints it.\n\n"
        "Expected output:\n3450.0"
    ),
    setup_sql=(
        "CREATE TABLE departments (dept_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO departments VALUES (1,'Engineering'), (2,'Sales');"
        "CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT NOT NULL, dept_id INTEGER, base_salary REAL CHECK(base_salary > 0), tax_rate REAL DEFAULT 0.1, FOREIGN KEY (dept_id) REFERENCES departments(dept_id));"
        "INSERT INTO employees VALUES (1,'Emperor',1,5000,0.1);"
        "INSERT INTO employees VALUES (2,'Rahim',2,4000,0.1);"
        "CREATE TABLE deductions (ded_id INTEGER PRIMARY KEY, emp_id INTEGER, amount REAL CHECK(amount > 0), reason TEXT, ded_date TEXT DEFAULT (date('now')), FOREIGN KEY (emp_id) REFERENCES employees(emp_id));"
        "INSERT INTO deductions VALUES (1,1,200,'Health Insurance','2026-07-01');"
    ),
    expected_output="3450.0",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.execute(\"INSERT INTO deductions (emp_id, amount, reason) VALUES (2,150,'Gym Membership')\")",
        "conn.commit()",
        "cursor = conn.execute('''",
        "SELECT e.base_salary * (1 - e.tax_rate) - COALESCE(SUM(d.amount), 0)",
        "FROM employees e LEFT JOIN deductions d ON e.emp_id = d.emp_id",
        "WHERE e.emp_id = 2",
        "''')",
        "print(cursor.fetchone()[0])",
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🏢  Department Payroll Summary\n\n"
        "The payroll database is seeded.\n"
        "Write Python code that produces a department‑wise\n"
        "summary showing:\n"
        "  • department name\n"
        "  • number of employees\n"
        "  • total base salary\n"
        "  • total tax collected\n"
        "  • net total (sum of net pay after tax, before deductions)\n"
        "Sort by department name.\n\n"
        "Expected output:\n"
        "[('Engineering',1,5000.0,500.0,4500.0), ('Sales',1,4000.0,400.0,3600.0)]"
    ),
    setup_sql=(
        "CREATE TABLE departments (dept_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO departments VALUES (1,'Engineering'), (2,'Sales');"
        "CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT NOT NULL, dept_id INTEGER, base_salary REAL CHECK(base_salary > 0), tax_rate REAL DEFAULT 0.1, FOREIGN KEY (dept_id) REFERENCES departments(dept_id));"
        "INSERT INTO employees VALUES (1,'Emperor',1,5000,0.1);"
        "INSERT INTO employees VALUES (2,'Rahim',2,4000,0.1);"
        "CREATE TABLE deductions (ded_id INTEGER PRIMARY KEY, emp_id INTEGER, amount REAL CHECK(amount > 0), reason TEXT, ded_date TEXT DEFAULT (date('now')), FOREIGN KEY (emp_id) REFERENCES employees(emp_id));"
        "INSERT INTO deductions VALUES (1,1,200,'Health Insurance','2026-07-01');"
    ),
    expected_output="[('Engineering', 1, 5000.0, 500.0, 4500.0), ('Sales', 1, 4000.0, 400.0, 3600.0)]",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT d.name, COUNT(e.emp_id) AS employees,",
        "       SUM(e.base_salary) AS total_base,",
        "       SUM(e.base_salary * e.tax_rate) AS total_tax,",
        "       SUM(e.base_salary * (1 - e.tax_rate)) AS net_total",
        "FROM departments d LEFT JOIN employees e ON d.dept_id = e.dept_id",
        "GROUP BY d.dept_id ORDER BY d.name",
        "''')",
        "print(cursor.fetchall())",
    ]
)

hard2 = Task(
    description=(
        "🔍  Employees with No Deductions\n\n"
        "The payroll database is seeded.\n"
        "Write Python code that finds the names of all\n"
        "employees who have zero deductions.\n"
        "Sort by name.\n\n"
        "Expected output:\n[('Rahim',)]"
    ),
    setup_sql=(
        "CREATE TABLE departments (dept_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO departments VALUES (1,'Engineering'), (2,'Sales');"
        "CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT NOT NULL, dept_id INTEGER, base_salary REAL CHECK(base_salary > 0), tax_rate REAL DEFAULT 0.1, FOREIGN KEY (dept_id) REFERENCES departments(dept_id));"
        "INSERT INTO employees VALUES (1,'Emperor',1,5000,0.1);"
        "INSERT INTO employees VALUES (2,'Rahim',2,4000,0.1);"
        "CREATE TABLE deductions (ded_id INTEGER PRIMARY KEY, emp_id INTEGER, amount REAL CHECK(amount > 0), reason TEXT, ded_date TEXT DEFAULT (date('now')), FOREIGN KEY (emp_id) REFERENCES employees(emp_id));"
        "INSERT INTO deductions VALUES (1,1,200,'Health Insurance','2026-07-01');"
    ),
    expected_output="[('Rahim',)]",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT name FROM employees WHERE emp_id NOT IN (SELECT emp_id FROM deductions) ORDER BY name",
        "''')",
        "print(cursor.fetchall())",
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L84.json",
        module_name="Module_09_Real_World_Projects",
        lesson_name="L84_Employee_Payroll_Database"
    )