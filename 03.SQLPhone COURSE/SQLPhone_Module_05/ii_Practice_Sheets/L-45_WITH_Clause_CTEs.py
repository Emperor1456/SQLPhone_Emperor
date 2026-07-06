import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE sales(id INTEGER PRIMARY KEY, product TEXT, amount REAL, region TEXT)")
    cur.executemany("INSERT INTO sales VALUES (?,?,?,?)", [(1,'A',100,'East'),(2,'B',200,'East'),(3,'A',300,'West'),(4,'B',400,'West'),(5,'A',500,'West')])
    return True

easy = Task("We have 'sales'. Write a query using a CTE to compute total sales per region, then select regions where total > 300.",
            verify_easy, Level.EASY,
            hints=["WITH region_totals AS (SELECT region, SUM(amount) AS total FROM sales GROUP BY region) SELECT region, total FROM region_totals WHERE total > 300;"])

def verify_medium(cur, conn):
    cur.execute("WITH region_totals AS (SELECT region, SUM(amount) AS total FROM sales GROUP BY region) SELECT region, total FROM region_totals WHERE total > 300")
    rows = cur.fetchall()
    return len(rows) >= 1

medium = Task("Your CTE should return at least one region (East=300? Actually East 300 not >300, West=1200>300, so West).",
              verify_medium, Level.MEDIUM,
              hints=["Ensure the HAVING condition is in the outer query, not inside CTE."])

def verify_hard(cur, conn):
    cur.execute("WITH region_totals AS (SELECT region, SUM(amount) AS total FROM sales GROUP BY region) SELECT region, total FROM region_totals WHERE total = (SELECT MAX(total) FROM region_totals)")
    rows = cur.fetchall()
    return len(rows) == 1 and rows[0][0] == 'West'

hard = Task("Using the CTE, find the region with the maximum total sales.",
            verify_hard, Level.HARD,
            hints=["WITH ... SELECT ... WHERE total = (SELECT MAX(total) FROM region_totals);"])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
