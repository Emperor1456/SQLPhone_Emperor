import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

# ─── Easy: COUNT ────────────────────────────────────
def verify_easy(cur, conn):
    cur.execute("SELECT COUNT(*) FROM employees")
    return cur.fetchone()[0] >= 3

easy = Task(
    description="Create table 'employees' (id INTEGER PRIMARY KEY, name TEXT, department TEXT).\n"
                "Insert at least 3 rows. Write a query that counts the total number of employees.",
    verify_func=verify_easy,
    level=Level.EASY,
    hints=[
        "CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, department TEXT);",
        "INSERT INTO employees VALUES (1,'Alice','Sales'),(2,'Bob','HR'),(3,'Charlie','Sales');",
        "SELECT COUNT(*) FROM employees;"
    ]
)

# ─── Medium: GROUP BY with AVG ─────────────────────
def verify_medium(cur, conn):
    cur.execute("SELECT COUNT(*) FROM employees")
    if cur.fetchone()[0] < 3:
        return False
    cur.execute("SELECT department, AVG(salary) FROM employees GROUP BY department")
    rows = cur.fetchall()
    return len(rows) >= 2

medium = Task(
    description="Add a column 'salary REAL' to the employees table (or recreate it).\n"
                "Insert at least 3 employees with different departments and salaries.\n"
                "Write a query that shows the average salary per department.",
    verify_func=verify_medium,
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, department TEXT, salary REAL);",
        "INSERT INTO employees VALUES (1,'Alice','Sales',50000),(2,'Bob','HR',60000),(3,'Charlie','Sales',70000);",
        "SELECT department, AVG(salary) FROM employees GROUP BY department;"
    ]
)

# ─── Hard: HAVING and complex aggregation ──────────
def verify_hard(cur, conn):
    # Check that employees and orders tables exist with enough rows
    cur.execute("SELECT COUNT(*) FROM employees")
    if cur.fetchone()[0] < 4:
        return False
    cur.execute("SELECT COUNT(*) FROM sales")
    if cur.fetchone()[0] < 4:
        return False
    expected = "Sales 2 120000.00\nHR 1 60000.00"
    cur.execute("""
        SELECT e.department, COUNT(DISTINCT e.id), SUM(s.amount)
        FROM employees e
        JOIN sales s ON e.id = s.employee_id
        GROUP BY e.department
        HAVING SUM(s.amount) > 50000
        ORDER BY e.department
    """)
    rows = cur.fetchall()
    result = "\n".join(f"{r[0]} {r[1]} {r[2]:.2f}" for r in rows)
    return result == expected

hard = Task(
    description="Build a departmental sales summary:\n"
                "1. Create table 'employees' (id INTEGER PRIMARY KEY, name TEXT,\n"
                "   department TEXT, salary REAL).\n"
                "2. Create table 'sales' (id INTEGER PRIMARY KEY, employee_id INTEGER,\n"
                "   amount REAL, FOREIGN KEY(employee_id) REFERENCES employees(id)).\n"
                "3. Insert at least 4 employees and at least 4 sales.\n"
                "4. Write a query that shows, for each department, the number of\n"
                "   distinct employees and the total sales amount.\n"
                "   Only include departments with total sales > 50000.\n"
                "   Sort by department name.\n"
                "The exact output must be:\n"
                "Sales 2 120000.00\n"
                "HR 1 60000.00",
    verify_func=verify_hard,
    level=Level.HARD,
    hints=[
        "CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, department TEXT, salary REAL);",
        "INSERT INTO employees VALUES (1,'Alice','Sales',50000),(2,'Bob','HR',60000),(3,'Charlie','Sales',70000),(4,'Diana','HR',55000);",
        "CREATE TABLE sales (id INTEGER PRIMARY KEY, employee_id INTEGER, amount REAL, FOREIGN KEY(employee_id) REFERENCES employees(id));",
        "INSERT INTO sales VALUES (1,1,80000),(2,3,40000),(3,2,60000),(4,1,0);", # need total sales per dept: Sales=Alice+Charlie=80000+40000=120000? Actually Alice 80000, Charlie 40000 total 120000; HR Bob 60000 total 60000. Need distinct employees count: Sales has Alice and Charlie=2, HR has Bob=1. HAVING >50000 both qualify. Perfect.
        "SELECT e.department, COUNT(DISTINCT e.id), SUM(s.amount) FROM employees e JOIN sales s ON e.id=s.employee_id GROUP BY e.department HAVING SUM(s.amount)>50000 ORDER BY e.department;"
    ]
)

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__":
    main()
