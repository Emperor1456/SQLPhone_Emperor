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
