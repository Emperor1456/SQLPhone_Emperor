import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("SELECT COUNT(*) FROM orders")
    return cur.fetchone()[0] >= 5

easy = Task("Create table 'orders' (id, customer, amount). Insert at least 5 rows with multiple orders per customer.",
            verify_easy, Level.EASY,
            hints=["CREATE TABLE orders (id INTEGER PRIMARY KEY, customer TEXT, amount REAL);",
                   "INSERT INTO orders (customer, amount) VALUES ('A',10),('A',20),('B',30),('B',40),('B',50);"])

def verify_medium(cur, conn):
    cur.execute("SELECT customer, SUM(amount) FROM orders GROUP BY customer")
    rows = cur.fetchall()
    return len(rows) >= 2

medium = Task("Write a query that shows total amount spent per customer (GROUP BY customer).",
              verify_medium, Level.MEDIUM,
              hints=["SELECT customer, SUM(amount) FROM orders GROUP BY customer;"])

def verify_hard(cur, conn):
    cur.execute("SELECT customer, AVG(amount) FROM orders GROUP BY customer HAVING AVG(amount) > 20")
    rows = cur.fetchall()
    return len(rows) > 0

hard = Task("Show customers whose average order amount > 20, using HAVING.",
            verify_hard, Level.HARD,
            hints=["SELECT customer, AVG(amount) FROM orders GROUP BY customer HAVING AVG(amount) > 20;"])


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
