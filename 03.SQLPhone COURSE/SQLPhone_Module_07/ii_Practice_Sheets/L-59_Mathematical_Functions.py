import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE products(name TEXT, price REAL, discount_pct INTEGER)")
    cur.executemany("INSERT INTO products VALUES (?,?,?)", [('A',100,10),('B',200,5),('C',150,0)])
    return True

easy = Task("We have 'products'. Write a query that shows the final price after discount, rounded to 2 decimals.",
            verify_easy, Level.EASY,
            hints=["SELECT name, ROUND(price * (100 - discount_pct) / 100.0, 2) AS final_price FROM products;"])

def verify_medium(cur, conn):
    cur.execute("SELECT name, ROUND(price * (100 - discount_pct) / 100.0, 2) FROM products")
    rows = cur.fetchall()
    return rows[0][1] == 90.0

medium = Task("Product A (100, 10% off) should be 90.0.",
              verify_medium, Level.MEDIUM,
              hints=["Use ROUND(..., 2)."])

def verify_hard(cur, conn):
    cur.execute("SELECT ABS(price - (SELECT AVG(price) FROM products)) AS deviation FROM products")
    rows = cur.fetchall()
    return len(rows) == 3

hard = Task("For each product, show the absolute deviation from the average price (use ABS and subquery).",
            verify_hard, Level.HARD,
            hints=["SELECT ABS(price - (SELECT AVG(price) FROM products)) FROM products;"])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
