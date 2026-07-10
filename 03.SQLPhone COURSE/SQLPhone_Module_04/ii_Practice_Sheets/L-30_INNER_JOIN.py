import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE customers(id INTEGER PRIMARY KEY, name TEXT)")
    cur.execute("CREATE TABLE orders(id INTEGER PRIMARY KEY, customer_id INTEGER, product TEXT)")
    cur.executemany("INSERT INTO customers VALUES (?,?)", [(1,'Alice'),(2,'Bob'),(3,'Charlie')])
    cur.executemany("INSERT INTO orders VALUES (?,?,?)", [(1,1,'Pen'),(2,1,'Book'),(3,2,'Eraser')])
    return True

easy = Task("We'll create 'customers' and 'orders' for you. Now write an INNER JOIN query that returns customer name and product for all orders.",
            verify_easy, Level.EASY,
            hints=["SELECT c.name, o.product FROM customers c JOIN orders o ON c.id = o.customer_id;"])

def verify_medium(cur, conn):
    cur.execute("SELECT c.name, o.product FROM customers c INNER JOIN orders o ON c.id = o.customer_id")
    return len(cur.fetchall()) == 3

medium = Task("Your join should return exactly 3 rows (matching orders).",
              verify_medium, Level.MEDIUM,
              hints=["Check your ON condition: c.id = o.customer_id"])

def verify_hard(cur, conn):
    cur.execute("SELECT c.name, COUNT(o.id) as order_count FROM customers c INNER JOIN orders o ON c.id = o.customer_id GROUP BY c.id")
    rows = cur.fetchall()
    return len(rows) == 2 and any(r[1]==2 for r in rows)

hard = Task("Group by customer and show the count of orders per customer using INNER JOIN.",
            verify_hard, Level.HARD,
            hints=["SELECT c.name, COUNT(o.id) FROM customers c JOIN orders o ON c.id = o.customer_id GROUP BY c.id;"])


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
