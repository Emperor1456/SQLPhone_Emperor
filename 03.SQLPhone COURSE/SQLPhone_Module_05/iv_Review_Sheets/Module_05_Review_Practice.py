import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

# ─── Easy: scalar subquery ──────────────────────────
def verify_easy(cur, conn):
    cur.execute("SELECT COUNT(*) FROM employees")
    if cur.fetchone()[0] < 3: return False
    cur.execute("SELECT name, salary FROM employees WHERE salary > (SELECT AVG(salary) FROM employees)")
    rows = cur.fetchall()
    return len(rows) >= 1

easy = Task(
    description="Create table 'employees' (id INTEGER PRIMARY KEY, name TEXT, salary REAL).\n"
                "Insert at least 3 rows with different salaries.\n"
                "Write a query that shows employees earning above the average salary\n"
                "using a subquery in WHERE.",
    verify_func=verify_easy,
    level=Level.EASY,
    hints=[
        "CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, salary REAL);",
        "INSERT INTO employees VALUES (1,'Alice',50000),(2,'Bob',70000),(3,'Charlie',60000);",
        "SELECT name, salary FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);"
    ]
)

# ─── Medium: EXISTS / NOT EXISTS ────────────────────
def verify_medium(cur, conn):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name IN ('customers','orders')")
    if len(cur.fetchall()) != 2: return False
    cur.execute("SELECT COUNT(*) FROM customers")
    if cur.fetchone()[0] < 3: return False
    cur.execute("SELECT COUNT(*) FROM orders")
    if cur.fetchone()[0] < 2: return False
    # verify that NOT EXISTS returns the correct customer without orders
    cur.execute("""
        SELECT c.name
        FROM customers c
        WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.cust_id = c.id)
    """)
    rows = cur.fetchall()
    return len(rows) == 1 and rows[0][0] == 'Charlie'

medium = Task(
    description="Create tables: customers (id, name), orders (id, cust_id, product).\n"
                "Insert at least 3 customers, but only 2 have orders.\n"
                "Write a query using NOT EXISTS that lists customers who have never placed an order.\n"
                "The output must show 'Charlie'.",
    verify_func=verify_medium,
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT);",
        "CREATE TABLE orders (id INTEGER PRIMARY KEY, cust_id INTEGER, product TEXT);",
        "INSERT INTO customers VALUES (1,'Alice'),(2,'Bob'),(3,'Charlie');",
        "INSERT INTO orders VALUES (1,1,'Pen'),(2,2,'Book');",
        "SELECT name FROM customers c WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.cust_id = c.id);"
    ]
)

# ─── Hard: correlated subquery + CTE ────────────────
def verify_hard(cur, conn):
    # tables: employees, departments
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name IN ('employees','departments')")
    if len(cur.fetchall()) != 2: return False
    cur.execute("SELECT COUNT(*) FROM employees")
    if cur.fetchone()[0] < 4: return False
    cur.execute("SELECT COUNT(*) FROM departments")
    if cur.fetchone()[0] < 2: return False
    expected = "Alice 50000 60000.00\nBob 70000 60000.00\nDave 55000 45000.00"
    cur.execute("""
        WITH dept_avg AS (
            SELECT department, AVG(salary) AS avg_sal
            FROM employees GROUP BY department
        )
        SELECT e.name, e.salary, da.avg_sal
        FROM employees e
        JOIN dept_avg da ON e.department = da.department
        WHERE e.salary > da.avg_sal
        ORDER BY e.name
    """)
    rows = cur.fetchall()
    result = "\n".join(f"{r[0]} {r[1]} {r[2]:.2f}" for r in rows)
    return result == expected

hard = Task(
    description="Build a CTE‑based report of high earners.\n"
                "1. Create table 'employees' (id INTEGER, name TEXT, department TEXT, salary REAL).\n"
                "2. Insert the following rows exactly:\n"
                "   (1,'Alice','Sales',50000),\n"
                "   (2,'Bob','Sales',70000),\n"
                "   (3,'Charlie','HR',60000),\n"
                "   (4,'Dave','HR',55000).\n"
                "3. Write a query that uses a CTE to compute the average salary per department,\n"
                "   then joins it back to the employees table.\n"
                "   Show name, salary, and the department average (rounded to two decimals)\n"
                "   for employees who earn above their department average.\n"
                "   Sort by name.\n"
                "Expected output:\n"
                "Alice 50000 60000.00\n"
                "Bob 70000 60000.00\n"
                "Dave 55000 45000.00",
    verify_func=verify_hard,
    level=Level.HARD,
    hints=[
        "CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, department TEXT, salary REAL);",
        "INSERT INTO employees VALUES (1,'Alice','Sales',50000),(2,'Bob','Sales',70000),(3,'Charlie','HR',60000),(4,'Dave','HR',55000);",
        "WITH dept_avg AS ( SELECT department, AVG(salary) AS avg_sal FROM employees GROUP BY department )",
        "SELECT e.name, e.salary, da.avg_sal FROM employees e JOIN dept_avg da ON e.department = da.department WHERE e.salary > da.avg_sal ORDER BY e.name;"
    ]
)

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__":
    main()
