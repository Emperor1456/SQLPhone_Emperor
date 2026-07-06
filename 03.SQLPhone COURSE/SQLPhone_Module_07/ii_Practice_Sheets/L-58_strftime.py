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
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
