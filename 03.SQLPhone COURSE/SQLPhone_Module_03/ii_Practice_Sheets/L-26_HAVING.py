import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("SELECT COUNT(*) FROM departments")
    return cur.fetchone()[0] >= 4

easy = Task("Create table 'departments' (dept_name, employee_count). Insert at least 4 rows with different counts.",
            verify_easy, Level.EASY,
            hints=["CREATE TABLE departments (dept_name TEXT, employee_count INTEGER);",
                   "INSERT INTO departments VALUES ('Sales',10),('HR',3),('IT',8),('Marketing',6);"])

def verify_medium(cur, conn):
    cur.execute("SELECT dept_name, employee_count FROM departments GROUP BY dept_name HAVING employee_count > 5")
    return len(cur.fetchall()) > 0

medium = Task("Write a query that shows departments with more than 5 employees using HAVING.",
              verify_medium, Level.MEDIUM,
              hints=["SELECT dept_name, employee_count FROM departments GROUP BY dept_name HAVING employee_count > 5;"])

def verify_hard(cur, conn):
    cur.execute("SELECT dept_name, MAX(employee_count) FROM departments GROUP BY dept_name HAVING MAX(employee_count) BETWEEN 5 AND 10")
    return len(cur.fetchall()) > 0

hard = Task("Show departments where the maximum employee count is between 5 and 10 (use HAVING with MAX).",
            verify_hard, Level.HARD,
            hints=["SELECT dept_name, MAX(employee_count) FROM departments GROUP BY dept_name HAVING MAX(employee_count) BETWEEN 5 AND 10;"])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
