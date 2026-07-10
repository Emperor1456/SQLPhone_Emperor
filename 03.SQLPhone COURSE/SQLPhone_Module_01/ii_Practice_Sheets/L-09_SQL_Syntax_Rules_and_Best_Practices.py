import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("SELECT COUNT(*) FROM users")
    return cur.fetchone()[0] >= 2

easy = Task("Create table 'users' (id, username, email, active). Insert two users (one active=1, one active=0).",
            verify_easy, Level.EASY,
            hints=["CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, email TEXT, active INTEGER);",
                   "INSERT INTO users (username, email, active) VALUES ('emperor','e@x.com',1), ('test','t@x.com',0);"])

def verify_medium(cur, conn):
    cur.execute("SELECT username FROM users WHERE active=1")
    return len(cur.fetchall()) >= 1

medium = Task("Write a nicely formatted SELECT (uppercase keywords, line breaks) that shows all active users.",
              verify_medium, Level.MEDIUM,
              hints=["SELECT username, email FROM users WHERE active = 1;"])

def verify_hard(cur, conn):
    cur.execute("SELECT username, email FROM users WHERE active=1 ORDER BY username")
    rows = cur.fetchall()
    return len(rows) >= 1 and rows[0][0].islower()

hard = Task("Rewrite the query with a comment, sorted by username, and using lowercase for column names (still works).",
            verify_hard, Level.HARD,
            hints=["-- Active users sorted\nSELECT username, email FROM users WHERE active = 1 ORDER BY username;"])


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
