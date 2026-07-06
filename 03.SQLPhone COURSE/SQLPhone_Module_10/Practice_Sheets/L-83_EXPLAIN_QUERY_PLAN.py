import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE items(id INTEGER PRIMARY KEY, name TEXT, price REAL)")
    cur.execute("CREATE INDEX idx_name ON items(name)")
    cur.executemany("INSERT INTO items(name, price) VALUES (?,?)", [('apple',1.0),('banana',2.0),('cherry',3.0)])
    return True

easy = Task(
    "We have 'items' with an index on name. Run EXPLAIN QUERY PLAN for two queries: one that searches on name (should use index) and one that searches on price (should scan).",
    verify_easy, Level.EASY,
    hints=["EXPLAIN QUERY PLAN SELECT * FROM items WHERE name = 'apple';", "EXPLAIN QUERY PLAN SELECT * FROM items WHERE price > 1.0;"]
)

def verify_medium(cur, conn):
    cur.execute("EXPLAIN QUERY PLAN SELECT * FROM items WHERE name = 'apple'")
    plan1 = str(cur.fetchall())
    cur.execute("EXPLAIN QUERY PLAN SELECT * FROM items WHERE price > 1.0")
    plan2 = str(cur.fetchall())
    return ('USING INDEX' in plan1) and ('SCAN TABLE' in plan2)

medium = Task(
    "The first plan should mention USING INDEX, the second SCAN TABLE.",
    verify_medium, Level.MEDIUM,
    hints=["Observe the output carefully."]
)

def verify_hard(cur, conn):
    cur.execute("EXPLAIN QUERY PLAN SELECT * FROM items ORDER BY name")
    plan = str(cur.fetchall())
    return 'USING INDEX' in plan

hard = Task(
    "Check if ORDER BY name also uses the index (it should).",
    verify_hard, Level.HARD,
    hints=["EXPLAIN QUERY PLAN SELECT * FROM items ORDER BY name;"]
)

def main():
    print("1 Easy  2 Medium  3 Hard")
    c = input("> ")
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))
if __name__ == "__main__": main()
