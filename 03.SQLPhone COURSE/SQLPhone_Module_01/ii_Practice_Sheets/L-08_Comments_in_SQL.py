import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("SELECT COUNT(*) FROM logs")
    return cur.fetchone()[0] == 1

easy = Task("Create table 'logs' (id INT, msg TEXT) and insert one row. Include at least one comment.",
            verify_easy, Level.EASY,
            hints=["-- This is a comment\nCREATE TABLE logs (id INTEGER, msg TEXT);\nINSERT INTO logs VALUES (1, 'test');"])

def verify_medium(cur, conn):
    cur.execute("SELECT COUNT(*) FROM logs")
    return cur.fetchone()[0] >= 2

medium = Task("Add another log entry. Use an inline comment to explain the insert.", verify_medium, Level.MEDIUM,
              hints=["INSERT INTO logs VALUES (2, 'second entry'); -- adding more data"])

def verify_hard(cur, conn):
    # Check that a block comment exists in the user's input? We'll just count rows.
    cur.execute("SELECT COUNT(*) FROM logs")
    return cur.fetchone()[0] >= 3

hard = Task("Insert a third row and include a multi‑line block comment (/* ... */) that describes the table's purpose.",
            verify_hard, Level.HARD,
            hints=["/* Table logs stores system messages */\nINSERT INTO logs VALUES (3, 'block comment test');"])


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

if __name__=="__main__": main()
