import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("SELECT COUNT(*) FROM inventory")
    return cur.fetchone()[0] >= 3

easy = Task("Create table 'inventory' (id, product, quantity, price). Insert 3 products.", verify_easy, Level.EASY,
            hints=["CREATE TABLE inventory (id INTEGER PRIMARY KEY, product TEXT, quantity INTEGER, price REAL);",
                   "INSERT INTO inventory (product, quantity, price) VALUES ('A',10,1.0),('B',5,2.0),('C',0,3.0);"])

def verify_medium(cur, conn):
    cur.execute("SELECT product, quantity*price AS total FROM inventory WHERE quantity>0")
    rows = cur.fetchall()
    return len(rows) >= 2

medium = Task("Write a query that shows product name and total value (quantity*price) for items with quantity > 0.",
              verify_medium, Level.MEDIUM,
              hints=["SELECT product, quantity*price AS total_value FROM inventory WHERE quantity > 0;"])

def verify_hard(cur, conn):
    cur.execute("SELECT product, quantity*price AS total FROM inventory WHERE quantity>0 ORDER BY total DESC")
    rows = cur.fetchall()
    return len(rows) >= 2 and rows[0][1] >= rows[1][1]

hard = Task("Enhance the previous query to sort by total value descending, and only show products where total > 5.",
            verify_hard, Level.HARD,
            hints=["ORDER BY total DESC", "HAVING total > 5 (or WHERE quantity*price > 5)"])


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
