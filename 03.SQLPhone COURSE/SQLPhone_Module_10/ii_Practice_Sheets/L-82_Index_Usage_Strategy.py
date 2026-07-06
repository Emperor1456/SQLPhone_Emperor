import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE big(id INTEGER PRIMARY KEY, value INT)")
    cur.executemany("INSERT INTO big(value) VALUES (?)", [(i,) for i in range(1000)])
    return True

easy = Task(
    "We have 'big' table with 1000 rows. Run EXPLAIN QUERY PLAN for SELECT * FROM big WHERE value = 500 before creating an index.",
    verify_easy, Level.EASY,
    hints=["EXPLAIN QUERY PLAN SELECT * FROM big WHERE value = 500;"]
)

def verify_medium(cur, conn):
    cur.execute("CREATE INDEX idx_value ON big(value)")
    cur.execute("EXPLAIN QUERY PLAN SELECT * FROM big WHERE value = 500")
    plan = str(cur.fetchall())
    return 'USING INDEX' in plan

medium = Task(
    "Create an index on the 'value' column, then run EXPLAIN QUERY PLAN again. It should now use the index.",
    verify_medium, Level.MEDIUM,
    hints=["CREATE INDEX idx_value ON big(value);", "EXPLAIN QUERY PLAN SELECT * FROM big WHERE value = 500;"]
)

def verify_hard(cur, conn):
    cur.execute("DROP INDEX IF EXISTS idx_value")
    cur.execute("EXPLAIN QUERY PLAN SELECT * FROM big WHERE value = 500")
    plan = str(cur.fetchall())
    return 'SCAN TABLE' in plan

hard = Task(
    "Drop the index and verify the plan reverts to a full table scan.",
    verify_hard, Level.HARD,
    hints=["DROP INDEX idx_value;", "EXPLAIN QUERY PLAN ..."]
)

def main():
    print("1 Easy  2 Medium  3 Hard")
    c = input("> ")
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))
if __name__ == "__main__": main()
