import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE temp1(id INTEGER)")
    cur.execute("CREATE TABLE temp2(id INTEGER)")
    return True

easy = Task("We have 'temp1' and 'temp2'. Drop 'temp1' safely using DROP TABLE IF EXISTS. List remaining tables.",
            verify_easy, Level.EASY,
            hints=["DROP TABLE IF EXISTS temp1; SELECT name FROM sqlite_master WHERE type='table';"])

def verify_medium(cur, conn):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [r[0] for r in cur.fetchall()]
    return 'temp1' not in tables and 'temp2' in tables

medium = Task("temp1 should be gone; temp2 still there.",
              verify_medium, Level.MEDIUM,
              hints=["Check that you used DROP TABLE IF EXISTS."])

def verify_hard(cur, conn):
    cur.execute("DROP TABLE IF EXISTS nonexistent")
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    return 'temp2' in [r[0] for r in cur.fetchall()]

hard = Task("Try dropping a non‑existent table with IF EXISTS (should not error), then confirm temp2 remains.",
            verify_hard, Level.HARD,
            hints=["DROP TABLE IF EXISTS nonexistent;"])


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
