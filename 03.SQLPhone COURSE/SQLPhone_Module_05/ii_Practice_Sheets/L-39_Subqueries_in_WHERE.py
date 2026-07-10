import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE employees(id INTEGER PRIMARY KEY, name TEXT, salary REAL)")
    cur.executemany("INSERT INTO employees VALUES (?,?,?)", [(1,'Alice',50000),(2,'Bob',70000),(3,'Charlie',60000)])
    return True

easy = Task("We've created 'employees'. Write a query to find employees earning above the average salary using a subquery in WHERE.",
            verify_easy, Level.EASY,
            hints=["SELECT name, salary FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);"])

def verify_medium(cur, conn):
    cur.execute("SELECT name FROM employees WHERE salary > (SELECT AVG(salary) FROM employees)")
    rows = cur.fetchall()
    return len(rows) >= 1

medium = Task("Your query should return at least one employee (Bob and maybe Charlie).",
              verify_medium, Level.MEDIUM,
              hints=["Check that the subquery is scalar and returns one value."])

def verify_hard(cur, conn):
    cur.execute("SELECT name, salary FROM employees WHERE salary > (SELECT AVG(salary) FROM employees) ORDER BY salary DESC")
    rows = cur.fetchall()
    return rows[0][0] == 'Bob'

hard = Task("Order the results by salary descending; Bob should be first.",
            verify_hard, Level.HARD,
            hints=["Add ORDER BY salary DESC."])


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
