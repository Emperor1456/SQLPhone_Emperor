import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("SELECT COUNT(*) FROM tasks")
    return cur.fetchone()[0] >= 3

easy = Task("Create table 'tasks' (id, description, completed_date TEXT). Insert at least 3 rows, some with NULL completed_date.",
            verify_easy, Level.EASY,
            hints=["CREATE TABLE tasks (id INTEGER PRIMARY KEY, description TEXT, completed_date TEXT);",
                   "INSERT INTO tasks (description, completed_date) VALUES ('T1','2026-01-01'),('T2',NULL),('T3',NULL);"])

def verify_medium(cur, conn):
    cur.execute("SELECT COUNT(*) FROM tasks WHERE completed_date IS NULL")
    return cur.fetchone()[0] > 0

medium = Task("Select tasks where completed_date IS NULL.",
              verify_medium, Level.MEDIUM,
              hints=["SELECT * FROM tasks WHERE completed_date IS NULL;"])

def verify_hard(cur, conn):
    cur.execute("SELECT description, COALESCE(completed_date, 'Pending') AS status FROM tasks")
    rows = cur.fetchall()
    return any(row[1] == 'Pending' for row in rows)

hard = Task("Use COALESCE to display 'Pending' for NULL completed_date.",
            verify_hard, Level.HARD,
            hints=["SELECT description, COALESCE(completed_date, 'Pending') AS status FROM tasks;"])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
