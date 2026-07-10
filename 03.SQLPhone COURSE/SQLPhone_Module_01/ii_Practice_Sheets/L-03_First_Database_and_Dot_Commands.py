import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='people'")
    return cur.fetchone() is not None

easy = Task("Create a table 'people' with columns 'name' TEXT and 'age' INT.", verify_easy, Level.EASY,
            hints=["CREATE TABLE people (name TEXT, age INT);"])

def verify_medium(cur, conn):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='people'")
    if not cur.fetchone(): return False
    cur.execute("SELECT * FROM people")
    return len(cur.fetchall()) >= 1

medium = Task("Insert at least one person into 'people' and SELECT all rows.", verify_medium, Level.MEDIUM,
              hints=["INSERT INTO people VALUES ('Emperor', 18);","SELECT * FROM people;"])

def verify_hard(cur, conn):
    cur.execute("SELECT sql FROM sqlite_master WHERE name='people'")
    schema = cur.fetchone()
    if not schema: return False
    cur.execute("PRAGMA table_info('people')")
    cols = cur.fetchall()
    return len(cols) >= 2 and 'people' in schema[0]

hard = Task("Display the schema of 'people' using a dot-command (simulate by querying sqlite_master).", verify_hard, Level.HARD,
            hints=["SELECT sql FROM sqlite_master WHERE name='people';","Use .schema in CLI, but we simulate."])


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
