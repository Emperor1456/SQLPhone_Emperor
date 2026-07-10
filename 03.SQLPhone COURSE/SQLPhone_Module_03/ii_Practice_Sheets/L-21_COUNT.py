import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("SELECT COUNT(*) FROM employees")
    return cur.fetchone()[0] >= 4

easy = Task("Create table 'employees' (id, name, department, phone). Insert at least 4 rows; leave phone NULL for one row.",
            verify_easy, Level.EASY,
            hints=["CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, department TEXT, phone TEXT);",
                   "INSERT INTO employees (name, department, phone) VALUES ('A','Sales','123'),('B','HR',NULL),('C','Sales','456'),('D','HR','789');"])

def verify_medium(cur, conn):
    cur.execute("SELECT COUNT(*) FROM employees")
    total = cur.fetchone()[0]
    cur.execute("SELECT COUNT(phone) FROM employees")
    phone = cur.fetchone()[0]
    return phone < total

medium = Task("Write queries to show total number of employees (COUNT(*)) and number of employees with a phone (COUNT(phone)).",
              verify_medium, Level.MEDIUM,
              hints=["SELECT COUNT(*) FROM employees; SELECT COUNT(phone) FROM employees;"])

def verify_hard(cur, conn):
    cur.execute("SELECT department, COUNT(*) FROM employees GROUP BY department")
    rows = cur.fetchall()
    return len(rows) >= 2

hard = Task("Show the number of employees per department using GROUP BY and COUNT.",
            verify_hard, Level.HARD,
            hints=["SELECT department, COUNT(*) FROM employees GROUP BY department;"])


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
