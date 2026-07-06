import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("SELECT COUNT(*) FROM items")
    return cur.fetchone()[0] >= 10

easy = Task("Create table 'items' (id INTEGER PRIMARY KEY, name TEXT, price REAL). Insert at least 10 rows with different prices.",
            verify_easy, Level.EASY,
            hints=["CREATE TABLE items (id INTEGER PRIMARY KEY, name TEXT, price REAL);",
                   "INSERT INTO items (name, price) VALUES ('i1',10),('i2',20),...,('i10',100); -- use a loop or manually insert 10 values"])

def verify_medium(cur, conn):
    cur.execute("SELECT * FROM items ORDER BY price DESC LIMIT 3 OFFSET 6")
    return len(cur.fetchall()) == 3

medium = Task("Retrieve the 3rd page of results (page size 3) ordered by price DESC. That's rows 7-9.",
              verify_medium, Level.MEDIUM,
              hints=["SELECT * FROM items ORDER BY price DESC LIMIT 3 OFFSET 6;"])

def verify_hard(cur, conn):
    cur.execute("SELECT COUNT(*) FROM items")
    total = cur.fetchone()[0]
    # count distinct prices to simulate? just verify offset limit works for last page
    cur.execute("SELECT * FROM items ORDER BY price DESC LIMIT 3 OFFSET ((SELECT COUNT(*)-3 FROM items))")
    return len(cur.fetchall()) == 3

hard = Task("Generalize: Write a query that returns the last 3 rows (using a subquery to calculate offset dynamically).",
            verify_hard, Level.HARD,
            hints=["SELECT * FROM items ORDER BY price DESC LIMIT 3 OFFSET (SELECT COUNT(*)-3 FROM items);"])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
