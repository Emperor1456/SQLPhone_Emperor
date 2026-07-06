import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='test'")
    return cur.fetchone() is not None

easy = Task("Create a table named 'test' with column 'id' INT.", verify_easy, Level.EASY,
            hints=["CREATE TABLE test (id INT);","Make sure the statement ends with a semicolon."])

def verify_medium(cur, conn):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='test'")
    if not cur.fetchone(): return False
    cur.execute("INSERT INTO test VALUES (42)")
    conn.commit()
    cur.execute("SELECT * FROM test")
    return cur.fetchone() == (42,)

medium = Task("Insert a row into 'test' with value 42 and SELECT it.", verify_medium, Level.MEDIUM,
              hints=["INSERT INTO test VALUES (42);","SELECT * FROM test;"])

def verify_hard(cur, conn):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='test'")
    if not cur.fetchone(): return False
    cur.execute("SELECT COUNT(*) FROM test")
    return cur.fetchone()[0] >= 2

hard = Task("Insert two more rows into 'test' (any values). Then run SELECT * to see all three rows.", verify_hard, Level.HARD,
            hints=["INSERT INTO test VALUES (7);","INSERT INTO test VALUES (100);","SELECT * FROM test;"])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
