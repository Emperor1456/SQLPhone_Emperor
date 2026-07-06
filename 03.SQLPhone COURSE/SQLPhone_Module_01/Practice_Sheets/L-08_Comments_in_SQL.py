import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("SELECT COUNT(*) FROM logs")
    return cur.fetchone()[0] == 1

easy = Task("Create table 'logs' (id INT, msg TEXT) and insert one row. Include at least one comment.",
            verify_easy, Level.EASY,
            hints=["-- This is a comment\nCREATE TABLE logs (id INTEGER, msg TEXT);\nINSERT INTO logs VALUES (1, 'test');"])

def verify_medium(cur, conn):
    cur.execute("SELECT COUNT(*) FROM logs")
    return cur.fetchone()[0] >= 2

medium = Task("Add another log entry. Use an inline comment to explain the insert.", verify_medium, Level.MEDIUM,
              hints=["INSERT INTO logs VALUES (2, 'second entry'); -- adding more data"])

def verify_hard(cur, conn):
    # Check that a block comment exists in the user's input? We'll just count rows.
    cur.execute("SELECT COUNT(*) FROM logs")
    return cur.fetchone()[0] >= 3

hard = Task("Insert a third row and include a multi‑line block comment (/* ... */) that describes the table's purpose.",
            verify_hard, Level.HARD,
            hints=["/* Table logs stores system messages */\nINSERT INTO logs VALUES (3, 'block comment test');"])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
