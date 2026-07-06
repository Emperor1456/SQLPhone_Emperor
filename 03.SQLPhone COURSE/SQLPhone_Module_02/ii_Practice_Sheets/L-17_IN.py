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
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
