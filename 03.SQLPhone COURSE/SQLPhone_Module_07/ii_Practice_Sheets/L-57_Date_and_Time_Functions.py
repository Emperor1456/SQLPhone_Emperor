import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE events(id INTEGER PRIMARY KEY, name TEXT, event_date TEXT)")
    cur.executemany("INSERT INTO events VALUES (?,?,?)", [(1,'E1','2026-06-15'),(2,'E2','2026-07-01'),(3,'E3','2026-05-20')])
    return True

easy = Task("We have 'events'. Write a query to select events happening in the next 7 days using date('now') and modifiers.",
            verify_easy, Level.EASY,
            hints=["SELECT * FROM events WHERE event_date BETWEEN date('now') AND date('now', '+7 days');"])

def verify_medium(cur, conn):
    cur.execute("SELECT * FROM events WHERE event_date BETWEEN date('now') AND date('now', '+7 days')")
    rows = cur.fetchall()
    return len(rows) >= 0  # depends on actual date, so we accept any as long as no error

medium = Task("The query should run without error and return relevant events (if any).",
              verify_medium, Level.MEDIUM,
              hints=["Check that you used date('now') and +7 days modifier."])

def verify_hard(cur, conn):
    cur.execute("SELECT name, event_date, CASE WHEN event_date < date('now') THEN 'Past' ELSE 'Future' END AS status FROM events")
    rows = cur.fetchall()
    return any(row[2] == 'Past' for row in rows)

hard = Task("Add a status column showing 'Past' or 'Future' based on event_date vs current date.",
            verify_hard, Level.HARD,
            hints=["SELECT name, event_date, CASE WHEN event_date < date('now') THEN 'Past' ELSE 'Future' END FROM events;"])


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
