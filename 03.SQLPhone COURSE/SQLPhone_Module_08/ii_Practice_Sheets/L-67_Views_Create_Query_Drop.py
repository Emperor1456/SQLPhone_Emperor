import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE employees(id INTEGER PRIMARY KEY, name TEXT, dept TEXT, salary REAL)")
    cur.executemany("INSERT INTO employees VALUES (?,?,?,?)", [(1,'Alice','Sales',50000),(2,'Bob','HR',60000),(3,'Charlie','Sales',70000)])
    return True

easy = Task("We have 'employees'. Create a view 'sales_staff' that shows only employees in department 'Sales'.",
            verify_easy, Level.EASY,
            hints=["CREATE VIEW sales_staff AS SELECT * FROM employees WHERE dept = 'Sales';"])

def verify_medium(cur, conn):
    cur.execute("SELECT COUNT(*) FROM sales_staff")
    return cur.fetchone()[0] == 2

medium = Task("Query the view; it should return 2 rows (Alice and Charlie).",
              verify_medium, Level.MEDIUM,
              hints=["SELECT * FROM sales_staff;"])

def verify_hard(cur, conn):
    cur.execute("DROP VIEW IF EXISTS sales_staff")
    cur.execute("SELECT name FROM sqlite_master WHERE type='view' AND name='sales_staff'")
    return cur.fetchone() is None

hard = Task("Drop the view and confirm it no longer exists.",
            verify_hard, Level.HARD,
            hints=["DROP VIEW sales_staff; SELECT name FROM sqlite_master WHERE type='view' AND name='sales_staff';"])


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
