import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE orders(id INTEGER PRIMARY KEY, product TEXT, amount REAL)")
    cur.executemany("INSERT INTO orders VALUES (?,?,?)", [(1,'A',100),(2,'A',200),(3,'B',150)])
    return True

easy = Task("We have 'orders'. Simulate a materialized view by creating a summary table 'order_summary' with product and total_amount, and populate it with a SELECT.",
            verify_easy, Level.EASY,
            hints=["CREATE TABLE order_summary AS SELECT product, SUM(amount) AS total FROM orders GROUP BY product;"])

def verify_medium(cur, conn):
    cur.execute("SELECT COUNT(*) FROM order_summary")
    return cur.fetchone()[0] == 2

medium = Task("The summary should have 2 rows (A:300, B:150).",
              verify_medium, Level.MEDIUM,
              hints=["Check that you used SUM and GROUP BY."])

def verify_hard(cur, conn):
    # Refresh the summary manually: delete and re-insert
    cur.execute("DELETE FROM order_summary")
    cur.execute("INSERT INTO order_summary SELECT product, SUM(amount) FROM orders GROUP BY product")
    cur.execute("SELECT total FROM order_summary WHERE product='A'")
    return cur.fetchone()[0] == 300

hard = Task("Refresh the summary by deleting all rows and re-populating from the base table.",
            verify_hard, Level.HARD,
            hints=["DELETE FROM order_summary; INSERT INTO order_summary SELECT product, SUM(amount) FROM orders GROUP BY product;"])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
