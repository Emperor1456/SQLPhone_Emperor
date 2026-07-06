import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE departments(id INTEGER PRIMARY KEY, name TEXT)")
    cur.execute("CREATE TABLE employees(id INTEGER PRIMARY KEY, name TEXT, salary REAL, dept_id INTEGER)")
    cur.execute("CREATE TABLE projects(id INTEGER PRIMARY KEY, title TEXT, budget REAL, dept_id INTEGER)")
    cur.execute("CREATE TABLE assignments(emp_id INTEGER, proj_id INTEGER)")
    cur.executemany("INSERT INTO departments VALUES (?,?)", [(1,'Engineering'),(2,'Marketing')])
    cur.executemany("INSERT INTO employees VALUES (?,?,?,?)", [(1,'Alice',90000,1),(2,'Bob',120000,1),(3,'Charlie',80000,2),(4,'Dave',70000,2)])
    cur.executemany("INSERT INTO projects VALUES (?,?,?,?)", [(1,'Proj1',100000,1),(2,'Proj2',50000,1),(3,'Proj3',80000,2)])
    cur.executemany("INSERT INTO assignments VALUES (?,?)", [(1,1),(1,2),(2,1),(3,3),(4,3)])
    return True

easy = Task("We've created the full schema. Write the five required queries from the lecture (subquery in WHERE, EXISTS, correlated, etc.).",
            verify_easy, Level.EASY,
            hints=["Start with: SELECT name FROM employees WHERE salary > (SELECT AVG(salary) FROM employees WHERE dept_id = employees.dept_id);"])

def verify_medium(cur, conn):
    try:
        # Query 1: above department avg
        cur.execute("SELECT e.name FROM employees e WHERE e.salary > (SELECT AVG(salary) FROM employees WHERE dept_id = e.dept_id)")
        # Query 2: EXISTS
        cur.execute("SELECT d.name FROM departments d WHERE EXISTS (SELECT 1 FROM employees e WHERE e.dept_id = d.id AND e.salary > 100000)")
        # Query 3: NOT EXISTS (double negative)
        cur.execute("SELECT e.name FROM employees e WHERE NOT EXISTS (SELECT p.id FROM projects p WHERE p.dept_id = e.dept_id EXCEPT SELECT a.proj_id FROM assignments a WHERE a.emp_id = e.id)")
        # Query 4: ANY
        cur.execute("SELECT title FROM projects WHERE budget > ANY (SELECT budget FROM projects WHERE dept_id = 2)")
        # Query 5: CTE
        cur.execute("WITH dept_total AS (SELECT dept_id, SUM(salary) AS total FROM employees GROUP BY dept_id) SELECT d.name, dt.total FROM departments d JOIN dept_total dt ON d.id = dt.dept_id WHERE dt.total > 150000")
        return True
    except:
        return False

medium = Task("All five queries should execute without error.",
              verify_medium, Level.MEDIUM,
              hints=["Check each query independently before combining."])

def verify_hard(cur, conn):
    cur.execute("""
        SELECT e.name, e.salary, (SELECT AVG(salary) FROM employees WHERE dept_id = e.dept_id) AS dept_avg
        FROM employees e
        WHERE e.salary > (SELECT AVG(salary) FROM employees WHERE dept_id = e.dept_id)
        AND EXISTS (SELECT 1 FROM departments d WHERE d.id = e.dept_id AND d.name = 'Engineering')
    """)
    rows = cur.fetchall()
    return len(rows) == 1 and rows[0][0] == 'Bob'

hard = Task("Find Engineering employees above department average. Should return Bob (120k > avg 105k).",
            verify_hard, Level.HARD,
            hints=["Combine correlated subquery with EXISTS filter."])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
