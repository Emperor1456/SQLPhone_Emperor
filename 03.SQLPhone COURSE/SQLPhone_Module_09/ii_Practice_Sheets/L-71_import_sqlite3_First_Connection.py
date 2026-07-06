import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("SELECT 1")
    return True

easy = Task(
    "Connect to ':memory:' and execute a simple SELECT 1 to test the connection.",
    verify_easy, Level.EASY,
    hints=["conn = sqlite3.connect(':memory:')", "cur = conn.cursor()", "cur.execute('SELECT 1')", "conn.close()"]
)

def verify_medium(cur, conn):
    cur.execute("CREATE TABLE test(id INT)")
    cur.execute("INSERT INTO test VALUES (42)")
    cur.execute("SELECT * FROM test")
    return cur.fetchone() == (42,)

medium = Task(
    "Create a table 'test', insert one row with value 42, then SELECT it back.",
    verify_medium, Level.MEDIUM,
    hints=["cur.execute('CREATE TABLE test (id INT)')", "cur.execute('INSERT INTO test VALUES (42)')", "conn.commit()", "cur.execute('SELECT * FROM test')"]
)

def verify_hard(cur, conn):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [r[0] for r in cur.fetchall()]
    return 'test' in tables

hard = Task(
    "Verify that the 'test' table still exists in sqlite_master (demonstrating persistence within the connection).",
    verify_hard, Level.HARD,
    hints=["SELECT name FROM sqlite_master WHERE type='table'"]
)

def main():
    print("1 Easy  2 Medium  3 Hard")
    c = input("> ")
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))
if __name__ == "__main__": main()
