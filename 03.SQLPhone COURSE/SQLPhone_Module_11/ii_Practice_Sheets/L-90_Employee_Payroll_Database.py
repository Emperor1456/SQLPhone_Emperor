import sys, sqlite3, os
sys.path.append("../..")
from practice_engine import Task, Level, run_task

DB = "payroll.db"

def verify_easy(cur, conn):
    for tbl in ['Department','Employee','Payroll']:
        cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{tbl}'")
        if not cur.fetchone():
            return False
    return True

easy = Task(
    "Create Department, Employee, Payroll tables with foreign keys and CHECK (salary > 0).",
    verify_easy, Level.EASY,
    hints=["CREATE TABLE Department(id INTEGER PRIMARY KEY, name TEXT, location TEXT);",
           "CREATE TABLE Employee(id INTEGER PRIMARY KEY, name TEXT, dept_id INTEGER, hire_date TEXT, base_salary REAL CHECK(base_salary>0), FOREIGN KEY(dept_id) REFERENCES Department(id));",
           "CREATE TABLE Payroll(id INTEGER PRIMARY KEY, employee_id INTEGER, pay_date TEXT, amount REAL, FOREIGN KEY(employee_id) REFERENCES Employee(id));"]
)

def verify_medium(cur, conn):
    for tbl in ['Department','Employee','Payroll']:
        cur.execute(f"SELECT COUNT(*) FROM {tbl}")
        if cur.fetchone()[0] < 3:
            return False
    cur.execute("SELECT d.name, SUM(p.amount) FROM Department d JOIN Employee e ON d.id=e.dept_id JOIN Payroll p ON e.id=p.employee_id GROUP BY d.name")
    return len(cur.fetchall()) > 0

medium = Task(
    "Insert 3 departments, 8 employees, multiple payroll entries. Show total payroll cost per department.",
    verify_medium, Level.MEDIUM,
    hints=["Use JOIN and GROUP BY."]
)

def verify_hard(cur, conn):
    cur.execute("SELECT e.name FROM Employee e JOIN Payroll p ON e.id=p.employee_id GROUP BY e.id HAVING MAX(p.amount) > e.base_salary")
    rows = cur.fetchall()
    return len(rows) >= 0

hard = Task(
    "Find employees who received a bonus (any payroll amount greater than their base_salary).",
    verify_hard, Level.HARD,
    hints=["GROUP BY employee, compare MAX(amount) with base_salary."]
)


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

if __name__ == "__main__": main()
