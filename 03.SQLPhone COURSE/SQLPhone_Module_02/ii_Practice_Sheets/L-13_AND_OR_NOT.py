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
