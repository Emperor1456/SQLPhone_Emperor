import sys, sqlite3, os
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    # create source.db separately
    src = sqlite3.connect("source.db")
    src.execute("CREATE TABLE data(info TEXT)")
    src.execute("INSERT INTO data VALUES ('Emperor')")
    src.commit()
    src.close()
    return True

easy = Task(
    "I've created 'source.db' with a table and row. Write Python code to back it up to 'backup.db' using the .backup() method (or .dump).",
    verify_easy, Level.EASY,
    hints=["import sqlite3; src = sqlite3.connect('source.db'); dst = sqlite3.connect('backup.db'); src.backup(dst); dst.close(); src.close()"]
)

def verify_medium(cur, conn):
    # Check backup.db exists and contains the row
    if os.path.exists("backup.db"):
        dst = sqlite3.connect("backup.db")
        cur2 = dst.cursor()
        cur2.execute("SELECT info FROM data")
        row = cur2.fetchone()
        dst.close()
        return row == ('Emperor',)
    return False

medium = Task(
    "Verify that 'backup.db' contains the same row ('Emperor').",
    verify_medium, Level.MEDIUM,
    hints=["Open backup.db and SELECT * FROM data."]
)

def verify_hard(cur, conn):
    # Restore from backup into a new database
    if os.path.exists("backup.db"):
        dst = sqlite3.connect("backup.db")
        new = sqlite3.connect("restored.db")
        dst.backup(new)
        new.close()
        dst.close()
        # check restored.db
        conn2 = sqlite3.connect("restored.db")
        cur2 = conn2.cursor()
        cur2.execute("SELECT info FROM data")
        row = cur2.fetchone()
        conn2.close()
        return row == ('Emperor',)
    return False

hard = Task(
    "Restore the backup into a new database 'restored.db' and confirm the data.",
    verify_hard, Level.HARD,
    hints=["Use backup method in reverse: dst.backup(new_conn)."]
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
