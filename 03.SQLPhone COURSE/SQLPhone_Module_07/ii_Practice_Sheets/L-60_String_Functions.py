import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, full_name TEXT, email TEXT)")
    cur.executemany("INSERT INTO users VALUES (?,?,?)", [(1,'Alice Smith','alice@test.com'),(2,'Bob Brown','bob@test.com')])
    return True

easy = Task("We have 'users'. Write a query that extracts the first 3 characters of the name and appends '...' (use SUBSTR and ||).",
            verify_easy, Level.EASY,
            hints=["SELECT SUBSTR(full_name, 1, 3) || '...' FROM users;"])

def verify_medium(cur, conn):
    cur.execute("SELECT SUBSTR(full_name, 1, 3) || '...' FROM users")
    rows = cur.fetchall()
    return rows[0][0] == 'Ali...'

medium = Task("First row should show 'Ali...'.",
              verify_medium, Level.MEDIUM,
              hints=["Use SUBSTR(full_name, 1, 3) || '...'."])

def verify_hard(cur, conn):
    cur.execute("SELECT UPPER(email) FROM users WHERE LENGTH(full_name) > 10")
    rows = cur.fetchall()
    return len(rows) >= 1 and rows[0][0] == 'ALICE@TEST.COM'

hard = Task("Show uppercase email of users whose full_name length > 10.",
            verify_hard, Level.HARD,
            hints=["SELECT UPPER(email) FROM users WHERE LENGTH(full_name) > 10;"])


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
