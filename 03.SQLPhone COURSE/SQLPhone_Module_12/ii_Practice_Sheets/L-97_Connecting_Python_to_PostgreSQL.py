import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    # Simulate connection string
    print("In a real scenario, you'd use psycopg2 and connect with host/db/user/password.")
    return True

easy = Task(
    "Write a Python code snippet (as comments) showing how to connect to PostgreSQL using psycopg2.",
    verify_easy, Level.EASY,
    hints=["conn = psycopg2.connect(host='localhost', database='testdb', user='emperor', password='secret')"]
)

def verify_medium(cur, conn):
    return True

medium = Task(
    "Show how to execute a SELECT version() query in PostgreSQL via Python.",
    verify_medium, Level.MEDIUM,
    hints=["cur = conn.cursor(); cur.execute('SELECT version()'); print(cur.fetchone())"]
)

def verify_hard(cur, conn):
    return True

hard = Task(
    "Explain the difference between the SQLite and PostgreSQL Python adapters (sqlite3 vs psycopg2).",
    verify_hard, Level.HARD,
    hints=["Both use cursor/execute/fetch, but psycopg2 uses %s placeholders instead of ?, and requires a running server."]
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
