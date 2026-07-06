import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("SELECT COUNT(*) FROM products")
    return cur.fetchone()[0] >= 4

easy = Task("Create table 'products' (id, name, price). Insert at least 4 rows with different prices.",
            verify_easy, Level.EASY,
            hints=["CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price REAL);",
                   "INSERT INTO products (name, price) VALUES ('P1',10),('P2',50),('P3',30),('P4',70);"])

def verify_medium(cur, conn):
    cur.execute("SELECT MIN(price), MAX(price) FROM products")
    row = cur.fetchone()
    return row[0] is not None and row[1] is not None

medium = Task("Write a query that returns the cheapest and most expensive product prices.",
              verify_medium, Level.MEDIUM,
              hints=["SELECT MIN(price), MAX(price) FROM products;"])

def verify_hard(cur, conn):
    cur.execute("SELECT name, price FROM products WHERE price = (SELECT MIN(price) FROM products)")
    min_name = cur.fetchone()
    cur.execute("SELECT name, price FROM products WHERE price = (SELECT MAX(price) FROM products)")
    max_name = cur.fetchone()
    return min_name is not None and max_name is not None

hard = Task("Show the name and price of both the cheapest and most expensive products (use subqueries).",
            verify_hard, Level.HARD,
            hints=["SELECT name, price FROM products WHERE price = (SELECT MIN(price) FROM products);",
                   "SELECT name, price FROM products WHERE price = (SELECT MAX(price) FROM products);"])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
