import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("SELECT COUNT(*) FROM users")
    return cur.fetchone()[0] >= 4

easy = Task("Create table 'users' (id, username, email). Insert at least 4 rows, some with emails ending '@example.com'.",
            verify_easy, Level.EASY,
            hints=["CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, email TEXT);",
                   "INSERT INTO users (username, email) VALUES ('u1','u1@example.com'),('u2','u2@gmail.com'),('u3','u3@example.com'),('u4','u4@yahoo.com');"])

def verify_medium(cur, conn):
    cur.execute("SELECT COUNT(*) FROM users WHERE email LIKE '%@example.com'")
    return cur.fetchone()[0] > 0

medium = Task("Select users whose email LIKE '%@example.com'.",
              verify_medium, Level.MEDIUM,
              hints=["SELECT * FROM users WHERE email LIKE '%@example.com';"])

def verify_hard(cur, conn):
    cur.execute("SELECT COUNT(*) FROM users WHERE username LIKE '_u%'")
    return cur.fetchone()[0] > 0

hard = Task("Select users whose username has 'u' as the second character (pattern: '_u%').",
            verify_hard, Level.HARD,
            hints=["SELECT * FROM users WHERE username LIKE '_u%';"])


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
