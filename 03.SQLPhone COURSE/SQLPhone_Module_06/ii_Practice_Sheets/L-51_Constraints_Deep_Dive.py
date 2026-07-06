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
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
