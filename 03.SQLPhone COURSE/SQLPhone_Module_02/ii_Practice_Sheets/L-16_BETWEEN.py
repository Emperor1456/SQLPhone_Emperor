import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("SELECT COUNT(*) FROM events")
    return cur.fetchone()[0] >= 4

easy = Task("Create table 'events' (id, name, event_date TEXT in YYYY-MM-DD). Insert at least 4 rows covering dates across a range.",
            verify_easy, Level.EASY,
            hints=["CREATE TABLE events (id INTEGER PRIMARY KEY, name TEXT, event_date TEXT);",
                   "INSERT INTO events (name, event_date) VALUES ('E1','2026-06-01'),('E2','2026-06-15'),('E3','2026-07-01'),('E4','2026-05-30');"])

def verify_medium(cur, conn):
    cur.execute("SELECT COUNT(*) FROM events WHERE event_date BETWEEN '2026-06-01' AND '2026-06-30'")
    return cur.fetchone()[0] > 0

medium = Task("Select events happening in June 2026 using BETWEEN.",
              verify_medium, Level.MEDIUM,
              hints=["SELECT * FROM events WHERE event_date BETWEEN '2026-06-01' AND '2026-06-30';"])

def verify_hard(cur, conn):
    cur.execute("SELECT COUNT(*) FROM events WHERE event_date NOT BETWEEN '2026-06-01' AND '2026-06-30'")
    return cur.fetchone()[0] > 0

hard = Task("Select events that are NOT in June 2026 using NOT BETWEEN.",
            verify_hard, Level.HARD,
            hints=["SELECT * FROM events WHERE event_date NOT BETWEEN '2026-06-01' AND '2026-06-30';"])


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
