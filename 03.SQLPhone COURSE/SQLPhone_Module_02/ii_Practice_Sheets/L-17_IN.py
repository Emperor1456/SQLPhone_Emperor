import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("SELECT COUNT(*) FROM contacts")
    return cur.fetchone()[0] >= 5

easy = Task("Create table 'contacts' (id, name, city). Insert at least 5 rows with different cities.",
            verify_easy, Level.EASY,
            hints=["CREATE TABLE contacts (id INTEGER PRIMARY KEY, name TEXT, city TEXT);",
                   "INSERT INTO contacts (name, city) VALUES ('A','London'),('B','Paris'),('C','Berlin'),('D','Tokyo'),('E','London');"])

def verify_medium(cur, conn):
    cur.execute("SELECT COUNT(*) FROM contacts WHERE city IN ('London','Paris','Berlin')")
    return cur.fetchone()[0] > 0

medium = Task("Select contacts whose city is in ('London','Paris','Berlin').",
              verify_medium, Level.MEDIUM,
              hints=["SELECT * FROM contacts WHERE city IN ('London','Paris','Berlin');"])

def verify_hard(cur, conn):
    cur.execute("SELECT COUNT(*) FROM contacts WHERE city NOT IN ('London','Paris','Berlin')")
    return cur.fetchone()[0] > 0

hard = Task("Select contacts whose city is NOT in that list.",
            verify_hard, Level.HARD,
            hints=["SELECT * FROM contacts WHERE city NOT IN ('London','Paris','Berlin');"])


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
