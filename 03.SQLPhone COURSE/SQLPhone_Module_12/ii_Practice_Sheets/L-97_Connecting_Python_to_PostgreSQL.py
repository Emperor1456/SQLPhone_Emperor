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
    print("1 Easy  2 Medium  3 Hard")
    c = input("> ")
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))
if __name__ == "__main__": main()
