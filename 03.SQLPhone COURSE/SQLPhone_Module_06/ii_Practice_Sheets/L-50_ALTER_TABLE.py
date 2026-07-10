import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE devices(id INTEGER PRIMARY KEY, name TEXT)")
    return True

easy = Task("We have 'devices'. Add a column 'os' TEXT using ALTER TABLE.",
            verify_easy, Level.EASY,
            hints=["ALTER TABLE devices ADD COLUMN os TEXT;"])

def verify_medium(cur, conn):
    cur.execute("ALTER TABLE devices RENAME COLUMN name TO device_name")
    cur.execute("PRAGMA table_info('devices')")
    cols = [c[1] for c in cur.fetchall()]
    return 'device_name' in cols and 'name' not in cols

medium = Task("Rename column 'name' to 'device_name'.",
              verify_medium, Level.MEDIUM,
              hints=["ALTER TABLE devices RENAME COLUMN name TO device_name;"])

def verify_hard(cur, conn):
    cur.execute("INSERT INTO devices (device_name, os) VALUES ('Phone', 'Android')")
    cur.execute("SELECT * FROM devices")
    row = cur.fetchone()
    return row[1] == 'Phone' and row[2] == 'Android'

hard = Task("Insert a row with the new schema (device_name and os).",
            verify_hard, Level.HARD,
            hints=["INSERT INTO devices (device_name, os) VALUES ('Phone', 'Android');"])


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
