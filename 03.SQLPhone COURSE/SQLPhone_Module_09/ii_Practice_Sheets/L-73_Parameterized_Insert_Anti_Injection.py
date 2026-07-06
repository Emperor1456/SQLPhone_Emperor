import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    return True

easy = Task(
    "Create a 'users' table. Then write Python code to safely insert a user using parameterized query (?, ?).",
    verify_easy, Level.EASY,
    hints=["cur.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('emperor', 'secret'))", "conn.commit()"]
)

def verify_medium(cur, conn):
    cur.execute("SELECT COUNT(*) FROM users")
    return cur.fetchone()[0] >= 1

medium = Task(
    "Confirm that at least one user was inserted.",
    verify_medium, Level.MEDIUM,
    hints=["cur.execute('SELECT * FROM users')"]
)

def verify_hard(cur, conn):
    # Try a malicious string: if user didn't parameterize, it might inject.
    # We'll just check that a row with a single quote in username works correctly.
    cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("mal'icious", "inject"))
    conn.commit()
    cur.execute("SELECT username FROM users WHERE username = ?", ("mal'icious",))
    return cur.fetchone()[0] == "mal'icious"

hard = Task(
    "Insert a username containing a single quote (mal'icious) safely. Then retrieve it to prove no injection occurred.",
    verify_hard, Level.HARD,
    hints=["Use parameterized query with ?.", "cur.execute('INSERT INTO users (username, password) VALUES (?, ?)', (\"mal'icious\", 'inject'))"]
)

def main():
    print("1 Easy  2 Medium  3 Hard")
    c = input("> ")
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))
if __name__ == "__main__": main()
