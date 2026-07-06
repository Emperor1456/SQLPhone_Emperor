import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("SELECT COUNT(*) FROM employees")
    return cur.fetchone()[0] >= 4

easy = Task("Create table 'employees' (id, name, dept, salary, status). Insert at least 4 rows with different departments, salaries, and statuses (active/inactive).",
            verify_easy, Level.EASY,
            hints=["CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, dept TEXT, salary REAL, status TEXT);",
                   "INSERT INTO employees (name, dept, salary, status) VALUES ('Alice','Sales',60000,'active'),('Bob','Sales',45000,'active'),('Charlie','Marketing',70000,'active'),('Dave','Marketing',50000,'inactive');"])

def verify_medium(cur, conn):
    cur.execute("SELECT COUNT(*) FROM employees WHERE status='active' AND (dept='Sales' OR dept='Marketing') AND salary > 50000")
    return cur.fetchone()[0] > 0

medium = Task("Find active employees in Sales or Marketing with salary > 50000.",
              verify_medium, Level.MEDIUM,
              hints=["SELECT * FROM employees WHERE status='active' AND (dept='Sales' OR dept='Marketing') AND salary > 50000;"])

def verify_hard(cur, conn):
    cur.execute("SELECT COUNT(*) FROM employees WHERE NOT (status='inactive' OR salary <= 50000 OR dept NOT IN ('Sales','Marketing'))")
    return cur.fetchone()[0] > 0

hard = Task("Rewrite the same query using NOT to negate the opposite conditions.",
            verify_hard, Level.HARD,
            hints=["WHERE NOT (status='inactive' OR salary <= 50000 OR dept NOT IN ('Sales','Marketing'))"])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
