import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE customers(id INTEGER PRIMARY KEY, name TEXT)")
    cur.execute("CREATE TABLE orders(id INTEGER PRIMARY KEY, customer_id INTEGER, product TEXT)")
    cur.executemany("INSERT INTO customers VALUES (?,?)", [(1,'Alice'),(2,'Bob'),(3,'Charlie')])
    cur.executemany("INSERT INTO orders VALUES (?,?,?)", [(1,1,'Pen'),(2,1,'Book')])
    return True

easy = Task("We've created customers (3 rows) and orders (2 rows for Alice). Write a LEFT JOIN that lists all customers and any product they ordered (NULL if none).",
            verify_easy, Level.EASY,
            hints=["SELECT c.name, o.product FROM customers c LEFT JOIN orders o ON c.id = o.customer_id;"])

def verify_medium(cur, conn):
    cur.execute("SELECT c.name, o.product FROM customers c LEFT JOIN orders o ON c.id = o.customer_id")
    rows = cur.fetchall()
    return len(rows) == 3 and any(r[1] is None for r in rows)

medium = Task("Your LEFT JOIN should return 3 rows, one with NULL product (Charlie).",
              verify_medium, Level.MEDIUM,
              hints=["Check that you used LEFT JOIN."])

def verify_hard(cur, conn):
    cur.execute("SELECT c.name FROM customers c LEFT JOIN orders o ON c.id = o.customer_id WHERE o.id IS NULL")
    rows = cur.fetchall()
    return len(rows) == 1 and rows[0][0] == 'Charlie'

hard = Task("Using LEFT JOIN and IS NULL, find the customer(s) with no orders.",
            verify_hard, Level.HARD,
            hints=["SELECT c.name FROM customers c LEFT JOIN orders o ON c.id = o.customer_id WHERE o.id IS NULL;"])


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
