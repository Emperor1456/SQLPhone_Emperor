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
    levels = {"1": easy, "2": medium, "3": hard}
    while True:
        print("
Choose difficulty:")
        print("1 - Easy")
        print("2 - Medium")
        print("3 - Hard")
        print("0 - Exit")
        c = input("> ").strip()
        if c == "0":
            break
        task = levels.get(c)
        if task:
            run_task(task)
            cont = input("Try next level? (y/n): ").strip().lower()
            if cont != "y":
                continue
            next_key = str(min(int(c)+1, 3))
            next_task = levels.get(next_key)
            if next_task:
                print(f"
Moving to {next_task.level}...")
                run_task(next_task)

if __name__=="__main__": main()
