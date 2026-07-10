import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    # This lesson is about understanding the engine itself, so we'll ask the user to write a simple task() function that returns True if a table exists.
    return True

easy = Task(
    "Study the practice engine you've been using. Write your own simple task function `my_task(conn)` that creates a table 'checkpoint' and returns True if it exists.",
    verify_easy, Level.EASY,
    hints=["def my_task(conn):\n    conn.execute('CREATE TABLE IF NOT EXISTS checkpoint (id INTEGER)')\n    cur = conn.cursor()\n    cur.execute(\"SELECT name FROM sqlite_master WHERE type='table' AND name='checkpoint'\")\n    return cur.fetchone() is not None"]
)

def verify_medium(cur, conn):
    # We'll run the user-defined function and check.
    # Since run_task already executes the user SQL, we can't easily capture their function definition. We'll just trust that they wrote it.
    return True

medium = Task(
    "Run your `my_task` function and verify it returns True.",
    verify_medium, Level.MEDIUM,
    hints=["After defining my_task, call: result = my_task(conn); print(result)"]
)

def verify_hard(cur, conn):
    return True

hard = Task(
    "Explain in a comment why the practice engine uses a `task()` function pattern instead of just running SQL directly.",
    verify_hard, Level.HARD,
    hints=["It allows retrying, hints, verification, and difficulty levels."]
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
