import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("SELECT COUNT(*) FROM sales")
    return cur.fetchone()[0] >= 4

easy = Task("Create table 'sales' (region, product, quantity). Insert rows covering at least 2 regions and 2 products with varying quantities.",
            verify_easy, Level.EASY,
            hints=["CREATE TABLE sales (region TEXT, product TEXT, quantity INTEGER);",
                   "INSERT INTO sales VALUES ('East','A',10),('East','A',5),('West','A',8),('West','B',12),('East','B',3);"])

def verify_medium(cur, conn):
    cur.execute("SELECT region, product, SUM(quantity) FROM sales GROUP BY region, product")
    rows = cur.fetchall()
    return len(rows) >= 3

medium = Task("Write a query to show total quantity sold per region and product (GROUP BY region, product).",
              verify_medium, Level.MEDIUM,
              hints=["SELECT region, product, SUM(quantity) FROM sales GROUP BY region, product;"])

def verify_hard(cur, conn):
    cur.execute("SELECT region, SUM(quantity) as total FROM sales GROUP BY region ORDER BY total DESC")
    rows = cur.fetchall()
    return len(rows) >= 2 and rows[0][1] >= rows[1][1]

hard = Task("Show total quantity per region, sorted descending by total quantity.",
            verify_hard, Level.HARD,
            hints=["SELECT region, SUM(quantity) AS total FROM sales GROUP BY region ORDER BY total DESC;"])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
