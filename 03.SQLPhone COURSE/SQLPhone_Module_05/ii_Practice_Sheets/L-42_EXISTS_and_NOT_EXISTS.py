import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE customers(id INTEGER PRIMARY KEY, name TEXT)")
    cur.execute("CREATE TABLE orders(id INTEGER, cust_id INTEGER)")
    cur.executemany("INSERT INTO customers VALUES (?,?)", [(1,'Alice'),(2,'Bob'),(3,'Charlie')])
    cur.executemany("INSERT INTO orders VALUES (?,?)", [(1,1),(2,1),(3,2)])
    return True

easy = Task("We have the same data as L‑41. Write a query using NOT EXISTS to find customers with no orders.",
            verify_easy, Level.EASY,
            hints=["SELECT name FROM customers c WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.cust_id = c.id);"])

def verify_medium(cur, conn):
    cur.execute("SELECT name FROM customers c WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.cust_id = c.id)")
    rows = cur.fetchall()
    return len(rows) == 1 and rows[0][0] == 'Charlie'

medium = Task("Your NOT EXISTS should return 'Charlie'.",
              verify_medium, Level.MEDIUM,
              hints=["Make sure the subquery references the outer c.id."])

def verify_hard(cur, conn):
    cur.execute("SELECT name FROM customers c WHERE EXISTS (SELECT 1 FROM orders o WHERE o.cust_id = c.id)")
    rows = cur.fetchall()
    return {'Alice','Bob'} == {r[0] for r in rows}

hard = Task("Find customers who HAVE placed an order using EXISTS.",
            verify_hard, Level.HARD,
            hints=["SELECT name FROM customers c WHERE EXISTS (SELECT 1 FROM orders o WHERE o.cust_id = c.id);"])


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
