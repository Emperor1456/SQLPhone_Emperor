import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE tasks(id INTEGER PRIMARY KEY, title TEXT, status TEXT DEFAULT 'pending', created TEXT DEFAULT (datetime('now')))")
    return True

easy = Task("Create table 'tasks' with DEFAULT 'pending' for status and current timestamp for created.",
            verify_easy, Level.EASY,
            hints=["CREATE TABLE tasks(id INTEGER PRIMARY KEY, title TEXT, status TEXT DEFAULT 'pending', created TEXT DEFAULT (datetime('now')));"])

def verify_medium(cur, conn):
    cur.execute("INSERT INTO tasks (title) VALUES ('Test task')")
    cur.execute("SELECT status, created FROM tasks WHERE title='Test task'")
    row = cur.fetchone()
    return row and row[0] == 'pending' and row[1] is not None

medium = Task("Insert a row specifying only title. Check that status is 'pending' and created is not NULL.",
              verify_medium, Level.MEDIUM,
              hints=["INSERT INTO tasks (title) VALUES ('Test task'); SELECT * FROM tasks;"])

def verify_hard(cur, conn):
    cur.execute("INSERT INTO tasks (title, status) VALUES ('Urgent', 'high')")
    cur.execute("SELECT status FROM tasks WHERE title='Urgent'")
    return cur.fetchone()[0] == 'high'

hard = Task("Insert a row overriding the default status to 'high'.",
            verify_hard, Level.HARD,
            hints=["INSERT INTO tasks (title, status) VALUES ('Urgent', 'high');"])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
