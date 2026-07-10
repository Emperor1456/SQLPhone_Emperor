import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE events(id INTEGER PRIMARY KEY, name TEXT, event_date TEXT)")
    cur.executemany("INSERT INTO events VALUES (?,?,?)", [(1,'E1','2026-06-15'),(2,'E2','2026-07-01'),(3,'E3','2026-06-30')])
    return True

easy = Task("We have 'events'. Write a query that displays each event's name and its formatted date as 'DD/MM/YYYY' using strftime.",
            verify_easy, Level.EASY,
            hints=["SELECT name, strftime('%d/%m/%Y', event_date) FROM events;"])

def verify_medium(cur, conn):
    cur.execute("SELECT name, strftime('%d/%m/%Y', event_date) FROM events")
    rows = cur.fetchall()
    return rows[0][1] == '15/06/2026'

medium = Task("The first row should show '15/06/2026'.",
              verify_medium, Level.MEDIUM,
              hints=["Check format string: %d/%m/%Y"])

def verify_hard(cur, conn):
    cur.execute("SELECT strftime('%Y-%m', event_date) AS month, COUNT(*) FROM events GROUP BY month")
    rows = cur.fetchall()
    return len(rows) >= 2

hard = Task("Group by year-month and count events per month.",
            verify_hard, Level.HARD,
            hints=["SELECT strftime('%Y-%m', event_date) AS month, COUNT(*) FROM events GROUP BY month;"])


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
