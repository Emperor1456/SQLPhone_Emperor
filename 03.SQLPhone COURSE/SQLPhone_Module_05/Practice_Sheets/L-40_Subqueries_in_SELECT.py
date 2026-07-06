import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE products(id INTEGER PRIMARY KEY, name TEXT, price REAL)")
    cur.executemany("INSERT INTO products VALUES (?,?,?)", [(1,'A',10),(2,'B',30),(3,'C',20)])
    return True

easy = Task("We've created 'products'. Write a query that shows each product's name, price, and the overall average price using a scalar subquery in SELECT.",
            verify_easy, Level.EASY,
            hints=["SELECT name, price, (SELECT AVG(price) FROM products) AS avg_price FROM products;"])

def verify_medium(cur, conn):
    cur.execute("SELECT name, price, (SELECT AVG(price) FROM products) AS avg_price FROM products")
    rows = cur.fetchall()
    return all(row[2] == 20.0 for row in rows)

medium = Task("The avg_price column should be the same for all rows (20.0).",
              verify_medium, Level.MEDIUM,
              hints=["Check that the subquery is uncorrelated."])

def verify_hard(cur, conn):
    cur.execute("SELECT name, price, (SELECT AVG(price) FROM products) AS avg_price FROM products WHERE price > (SELECT AVG(price) FROM products)")
    rows = cur.fetchall()
    return len(rows) == 1 and rows[0][0] == 'B'

hard = Task("Show only products with price above the average (combine subquery in SELECT and WHERE).",
            verify_hard, Level.HARD,
            hints=["SELECT name, price, (SELECT AVG(price) FROM products) FROM products WHERE price > (SELECT AVG(price) FROM products);"])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
