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
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
