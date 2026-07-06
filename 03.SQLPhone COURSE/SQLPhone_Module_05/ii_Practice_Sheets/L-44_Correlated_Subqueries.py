import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE employees(id INTEGER PRIMARY KEY, name TEXT, department TEXT, salary REAL)")
    cur.executemany("INSERT INTO employees VALUES (?,?,?,?)", [(1,'Alice','Sales',50000),(2,'Bob','Sales',70000),(3,'Charlie','HR',60000),(4,'Dave','HR',40000)])
    return True

easy = Task("We have employees. Write a correlated subquery to find employees who earn more than the average salary of their own department.",
            verify_easy, Level.EASY,
            hints=["SELECT e.name, e.salary, e.department FROM employees e WHERE e.salary > (SELECT AVG(salary) FROM employees WHERE department = e.department);"])

def verify_medium(cur, conn):
    cur.execute("SELECT e.name FROM employees e WHERE e.salary > (SELECT AVG(salary) FROM employees WHERE department = e.department)")
    rows = cur.fetchall()
    # Sales avg 60k -> Bob > 60k, HR avg 50k -> Charlie > 50k
    return {r[0] for r in rows} == {'Bob', 'Charlie'}

medium = Task("The result should be Bob (Sales) and Charlie (HR).",
              verify_medium, Level.MEDIUM,
              hints=["Check that you referenced the outer e.department."])

def verify_hard(cur, conn):
    cur.execute("SELECT e.name, e.salary, (SELECT AVG(salary) FROM employees WHERE department = e.department) AS dept_avg FROM employees e WHERE e.salary > (SELECT AVG(salary) FROM employees WHERE department = e.department)")
    rows = cur.fetchall()
    return len(rows) == 2

hard = Task("Show the department average alongside the employee salary for those above the department average.",
            verify_hard, Level.HARD,
            hints=["Include the subquery in SELECT as well."])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
