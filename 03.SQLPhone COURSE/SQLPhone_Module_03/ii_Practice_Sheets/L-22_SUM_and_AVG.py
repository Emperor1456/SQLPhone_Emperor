import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("SELECT COUNT(*) FROM sales")
    return cur.fetchone()[0] >= 4

easy = Task("Create table 'sales' (id, product, amount). Insert at least 4 rows with different amounts.",
            verify_easy, Level.EASY,
            hints=["CREATE TABLE sales (id INTEGER PRIMARY KEY, product TEXT, amount REAL);",
                   "INSERT INTO sales (product, amount) VALUES ('A',100),('B',200),('C',300),('D',400);"])

def verify_medium(cur, conn):
    cur.execute("SELECT SUM(amount), AVG(amount) FROM sales")
    row = cur.fetchone()
    return row[0] is not None and row[1] is not None

medium = Task("Write a query that shows total sum of amounts and average amount.",
              verify_medium, Level.MEDIUM,
              hints=["SELECT SUM(amount), AVG(amount) FROM sales;"])

def verify_hard(cur, conn):
    cur.execute("SELECT product, SUM(amount) FROM sales GROUP BY product")
    return len(cur.fetchall()) >= 4

hard = Task("Group by product and show total amount per product (using SUM).",
            verify_hard, Level.HARD,
            hints=["SELECT product, SUM(amount) FROM sales GROUP BY product;"])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
