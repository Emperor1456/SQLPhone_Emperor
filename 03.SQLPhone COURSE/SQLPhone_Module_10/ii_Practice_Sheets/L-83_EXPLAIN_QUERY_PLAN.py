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

if __name__ == "__main__": main()
