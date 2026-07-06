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
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
