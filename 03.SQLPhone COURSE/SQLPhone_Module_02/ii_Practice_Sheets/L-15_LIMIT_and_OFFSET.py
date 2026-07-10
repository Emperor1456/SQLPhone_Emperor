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
