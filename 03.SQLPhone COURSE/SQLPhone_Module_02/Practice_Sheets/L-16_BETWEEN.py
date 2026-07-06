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
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
