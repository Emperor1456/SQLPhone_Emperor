import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE nums(n INT)")
    cur.executemany("INSERT INTO nums VALUES (?)", [(i,) for i in range(1,11)])
    return True

easy = Task(
    "We've created 'nums' with values 1-10. Write Python code to fetch the first row with fetchone().",
    verify_easy, Level.EASY,
    hints=["cur.execute('SELECT n FROM nums')", "row = cur.fetchone()", "print(row)"]
)

def verify_medium(cur, conn):
    cur.execute("SELECT n FROM nums")
    rows = cur.fetchmany(3)
    return len(rows) == 3

medium = Task(
    "Fetch exactly 3 rows using fetchmany(3).",
    verify_medium, Level.MEDIUM,
    hints=["cur.execute('SELECT n FROM nums')", "rows = cur.fetchmany(3)"]
)

def verify_hard(cur, conn):
    cur.execute("SELECT n FROM nums")
    all_rows = cur.fetchall()
    return len(all_rows) == 10

hard = Task(
    "Fetch all remaining rows with fetchall() and confirm there are 10 total.",
    verify_hard, Level.HARD,
    hints=["cur.execute('SELECT n FROM nums')", "rows = cur.fetchall()", "print(len(rows))"]
)

def main():
    print("1 Easy  2 Medium  3 Hard")
    c = input("> ")
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))
if __name__ == "__main__": main()
