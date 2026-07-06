import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("PRAGMA table_info('employees')")
    return len(cur.fetchall()) == 5

easy = Task("Create table 'employees' (id INT PK, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, salary REAL CHECK(salary>0), hired TEXT DEFAULT (datetime('now'))).",
            verify_easy, Level.EASY,
            hints=["CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, salary REAL CHECK(salary>0), hired TEXT DEFAULT (datetime('now')));"])

def verify_medium(cur, conn):
    cur.execute("SELECT COUNT(*) FROM employees")
    return cur.fetchone()[0] >= 2

medium = Task("Insert two rows: one with all columns, one omitting hired (let default work).",
              verify_medium, Level.MEDIUM,
              hints=["INSERT INTO employees (name, email, salary, hired) VALUES ('Alice','a@x.com',50000,'2026-01-01');",
                     "INSERT INTO employees (name, email, salary) VALUES ('Bob','b@x.com',60000);"])

def verify_hard(cur, conn):
    # try inserting a duplicate email, should fail; we'll catch error later in run_task? No, verify just checks data.
    cur.execute("SELECT email, COUNT(*) FROM employees GROUP BY email HAVING COUNT(*)>1")
    return cur.fetchone() is None   # no duplicate

hard = Task("Try inserting a duplicate email (should be rejected). Show current table with all rows.",
            verify_hard, Level.HARD,
            hints=["INSERT INTO employees (name, email, salary) VALUES ('Charlie','a@x.com',70000); -- will fail",
                   "After error, SELECT * FROM employees;"])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
