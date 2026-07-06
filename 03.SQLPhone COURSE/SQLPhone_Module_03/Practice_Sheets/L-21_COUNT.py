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
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
