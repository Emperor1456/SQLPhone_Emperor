import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE stats(item TEXT, total_sales REAL, quantity INTEGER)")
    cur.executemany("INSERT INTO stats VALUES (?,?,?)", [('A',100,5),('B',200,0),('C',150,3)])
    return True

easy = Task("We have 'stats'. Write a query that calculates average sale per item (total_sales / quantity), but returns NULL if quantity is 0 using NULLIF.",
            verify_easy, Level.EASY,
            hints=["SELECT item, total_sales / NULLIF(quantity, 0) AS avg_sale FROM stats;"])

def verify_medium(cur, conn):
    cur.execute("SELECT item, total_sales / NULLIF(quantity, 0) FROM stats")
    rows = cur.fetchall()
    return rows[1][1] is None

medium = Task("The row with quantity 0 should show NULL for the average.",
              verify_medium, Level.MEDIUM,
              hints=["Use NULLIF(quantity, 0)."])

def verify_hard(cur, conn):
    cur.execute("SELECT item, COALESCE(total_sales / NULLIF(quantity, 0), 0) AS avg_sale FROM stats")
    rows = cur.fetchall()
    return rows[1][1] == 0

hard = Task("Replace the NULL with 0 using COALESCE for a cleaner output.",
            verify_hard, Level.HARD,
            hints=["COALESCE(total_sales / NULLIF(quantity, 0), 0)"])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
