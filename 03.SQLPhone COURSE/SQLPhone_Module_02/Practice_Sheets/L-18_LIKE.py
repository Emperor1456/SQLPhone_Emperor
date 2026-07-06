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
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
