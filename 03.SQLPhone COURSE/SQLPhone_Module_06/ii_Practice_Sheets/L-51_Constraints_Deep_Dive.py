import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, username TEXT NOT NULL UNIQUE, age INTEGER CHECK(age>=18), email TEXT UNIQUE)")
    return True

easy = Task("Create a table 'users' with NOT NULL, UNIQUE, CHECK constraints.",
            verify_easy, Level.EASY,
            hints=["CREATE TABLE users(id INTEGER PRIMARY KEY, username TEXT NOT NULL UNIQUE, age INTEGER CHECK(age>=18), email TEXT UNIQUE);"])

def verify_medium(cur, conn):
    try:
        cur.execute("INSERT INTO users (username, age, email) VALUES ('admin', 30, 'admin@test.com')")
        conn.commit()
        cur.execute("INSERT INTO users (username, age, email) VALUES ('admin', 25, 'admin2@test.com')")
        return False  # should fail
    except sqlite3.IntegrityError:
        return True

medium = Task("Insert a valid row, then try inserting a duplicate username (should be rejected).",
              verify_medium, Level.MEDIUM,
              hints=["First INSERT: ('admin', 30, 'admin@test.com'); second with same username."])

def verify_hard(cur, conn):
    try:
        cur.execute("INSERT INTO users (username, age, email) VALUES ('test', 15, 'test@test.com')")
        return False
    except sqlite3.IntegrityError:
        return True

hard = Task("Try inserting an age < 18 (should be rejected by CHECK).",
            verify_hard, Level.HARD,
            hints=["INSERT INTO users (username, age, email) VALUES ('test', 15, 'test@test.com');"])


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
