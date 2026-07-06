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
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
