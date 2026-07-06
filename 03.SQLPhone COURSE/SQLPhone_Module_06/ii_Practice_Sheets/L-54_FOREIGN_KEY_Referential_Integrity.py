import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("CREATE TABLE departments(id INTEGER PRIMARY KEY, name TEXT)")
    cur.execute("CREATE TABLE employees(id INTEGER PRIMARY KEY, name TEXT, dept_id INTEGER, FOREIGN KEY(dept_id) REFERENCES departments(id) ON DELETE CASCADE)")
    return True

easy = Task("Create tables with foreign key ON DELETE CASCADE.",
            verify_easy, Level.EASY,
            hints=["PRAGMA foreign_keys = ON; CREATE TABLE departments... CREATE TABLE employees..."])

def verify_medium(cur, conn):
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("INSERT INTO departments VALUES (1, 'Sales')")
    cur.execute("INSERT INTO employees VALUES (1, 'Alice', 1)")
    cur.execute("DELETE FROM departments WHERE id=1")
    cur.execute("SELECT COUNT(*) FROM employees")
    return cur.fetchone()[0] == 0

medium = Task("Insert department and employee, then delete department; employee should be cascade-deleted.",
              verify_medium, Level.MEDIUM,
              hints=["INSERT INTO departments VALUES (1,'Sales'); INSERT INTO employees VALUES (1,'Alice',1); DELETE FROM departments;"])

def verify_hard(cur, conn):
    cur.execute("PRAGMA foreign_keys = ON")
    try:
        cur.execute("INSERT INTO employees VALUES (2, 'Bob', 999)")
        return False
    except:
        return True

hard = Task("Try inserting an employee with a non-existent dept_id 999 (should fail).",
            verify_hard, Level.HARD,
            hints=["INSERT INTO employees VALUES (2, 'Bob', 999);"])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
