import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE temp1(id INTEGER)")
    cur.execute("CREATE TABLE temp2(id INTEGER)")
    return True

easy = Task("We have 'temp1' and 'temp2'. Drop 'temp1' safely using DROP TABLE IF EXISTS. List remaining tables.",
            verify_easy, Level.EASY,
            hints=["DROP TABLE IF EXISTS temp1; SELECT name FROM sqlite_master WHERE type='table';"])

def verify_medium(cur, conn):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [r[0] for r in cur.fetchall()]
    return 'temp1' not in tables and 'temp2' in tables

medium = Task("temp1 should be gone; temp2 still there.",
              verify_medium, Level.MEDIUM,
              hints=["Check that you used DROP TABLE IF EXISTS."])

def verify_hard(cur, conn):
    cur.execute("DROP TABLE IF EXISTS nonexistent")
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    return 'temp2' in [r[0] for r in cur.fetchall()]

hard = Task("Try dropping a non‑existent table with IF EXISTS (should not error), then confirm temp2 remains.",
            verify_hard, Level.HARD,
            hints=["DROP TABLE IF EXISTS nonexistent;"])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
