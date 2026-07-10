import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name IN ('departments','staff')")
    return len(cur.fetchall()) == 2

easy = Task("Create tables 'departments' (id, dept_name) and 'staff' (id, name, dept_id). Insert at least 3 departments and 4 staff.",
            verify_easy, Level.EASY,
            hints=["CREATE TABLE departments (id INTEGER PRIMARY KEY, dept_name TEXT);",
                   "CREATE TABLE staff (id INTEGER PRIMARY KEY, name TEXT, dept_id INTEGER, FOREIGN KEY(dept_id) REFERENCES departments(id));"])

def verify_medium(cur, conn):
    cur.execute("""
        SELECT s.name AS "Employee Name", d.dept_name AS "Department"
        FROM staff s JOIN departments d ON s.dept_id = d.id
    """)
    return len(cur.fetchall()) >= 1

medium = Task("Write a query that joins staff and departments using table aliases (s and d) and column aliases ('Employee Name', 'Department').",
              verify_medium, Level.MEDIUM,
              hints=["SELECT s.name AS \"Employee Name\", d.dept_name AS \"Department\" FROM staff s JOIN departments d ON s.dept_id = d.id;"])

def verify_hard(cur, conn):
    cur.execute("""
        SELECT s.name AS emp, d.dept_name AS dept, s.name || ' - ' || d.dept_name AS combined
        FROM staff s JOIN departments d ON s.dept_id = d.id
        WHERE LENGTH(d.dept_name) > 3
    """)
    return len(cur.fetchall()) >= 1

hard = Task("Add a computed column that concatenates employee name and department with ' - ' and filter departments with name length > 3.",
            verify_hard, Level.HARD,
            hints=["SELECT s.name || ' - ' || d.dept_name AS combined FROM staff s JOIN departments d ON s.dept_id = d.id WHERE LENGTH(d.dept_name) > 3;"])


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
