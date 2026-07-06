import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("PRAGMA foreign_keys = ON")
    try:
        cur.execute("CREATE TABLE departments(id INTEGER PRIMARY KEY, name TEXT)")
        cur.execute("CREATE TABLE employees(id INTEGER PRIMARY KEY, name TEXT, dept_id INTEGER, FOREIGN KEY(dept_id) REFERENCES departments(id))")
        return True
    except:
        return False

easy = Task("Create two tables: 'departments' and 'employees' with a foreign key from employees.dept_id to departments.id.",
            verify_easy, Level.EASY,
            hints=["CREATE TABLE departments (id INTEGER PRIMARY KEY, name TEXT);",
                   "CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, dept_id INTEGER, FOREIGN KEY(dept_id) REFERENCES departments(id));"])

def verify_medium(cur, conn):
    cur.execute("PRAGMA foreign_keys = ON")
    try:
        cur.execute("INSERT INTO departments VALUES (1, 'Sales')")
        cur.execute("INSERT INTO employees VALUES (1, 'Alice', 1)")
        return True
    except:
        return False

medium = Task("Insert a department and an employee referencing that department.",
              verify_medium, Level.MEDIUM,
              hints=["INSERT INTO departments VALUES (1, 'Sales');",
                     "INSERT INTO employees VALUES (1, 'Alice', 1);"])

def verify_hard(cur, conn):
    cur.execute("PRAGMA foreign_keys = ON")
    try:
        cur.execute("INSERT INTO employees VALUES (2, 'Bob', 999)")
        return False  # should fail
    except:
        return True

hard = Task("Try inserting an employee with a non-existent dept_id (999). It should fail due to foreign key enforcement.",
            verify_hard, Level.HARD,
            hints=["INSERT INTO employees VALUES (2, 'Bob', 999); -- will fail"])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
