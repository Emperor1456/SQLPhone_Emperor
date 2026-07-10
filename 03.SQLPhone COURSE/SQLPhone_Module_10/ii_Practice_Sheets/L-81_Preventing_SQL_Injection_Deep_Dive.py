import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    cur.execute("INSERT INTO users (username, password) VALUES ('admin', 'secret')")
    return True

easy = Task(
    "We have a 'users' table with an admin row. Simulate a dangerous string‑built query: SELECT * FROM users WHERE username = 'input'. Try injecting to return the admin row without knowing the username.",
    verify_easy, Level.EASY,
    hints=["Try input: ' OR 1=1 --"]
)

def verify_medium(cur, conn):
    # The user should demonstrate the attack, then fix it with parameterized query.
    # We'll just check that they now write a safe query using ?.
    safe_input = input("Now write the safe parameterized query to find admin (use ? and pass 'admin' as parameter):\n> ")
    # We'll execute it with parameter
    try:
        cur.execute(safe_input, ('admin',))
        row = cur.fetchone()
        if row and row[1] == 'admin':
            print("✅ Safe query works!")
            return True
        else:
            print("❌ Safe query did not return admin.")
            return False
    except Exception as e:
        print(f"❌ {e}")
        return False

medium = Task(
    "Fix the vulnerability by rewriting the query with a parameterized placeholder (?).",
    verify_medium, Level.MEDIUM,
    hints=["cur.execute('SELECT * FROM users WHERE username = ?', ('admin',))"]
)

def verify_hard(cur, conn):
    # Use both validation and parameterization
    try:
        cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", ("admin", "' OR 1=1 --"))
        if cur.fetchone():
            print("❌ Injection still worked (should not match).")
            return False
        else:
            print("✅ Injection prevented.")
            return True
    except Exception as e:
        print(f"❌ {e}")
        return False

hard = Task(
    "Show that even with malicious input as password, the query is safe and doesn't return the admin row.",
    verify_hard, Level.HARD,
    hints=["pass malicious string as parameter, it will be escaped"]
)


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

if __name__ == "__main__": main()
