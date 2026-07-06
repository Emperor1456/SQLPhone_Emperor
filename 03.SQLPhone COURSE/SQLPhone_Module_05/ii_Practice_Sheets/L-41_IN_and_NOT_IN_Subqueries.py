import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE customers(id INTEGER PRIMARY KEY, name TEXT)")
    cur.execute("CREATE TABLE orders(id INTEGER, cust_id INTEGER)")
    cur.executemany("INSERT INTO customers VALUES (?,?)", [(1,'Alice'),(2,'Bob'),(3,'Charlie')])
    cur.executemany("INSERT INTO orders VALUES (?,?)", [(1,1),(2,1),(3,2)])
    return True

easy = Task("We have customers and orders. Write a query using NOT IN to find customers who have never placed an order.",
            verify_easy, Level.EASY,
            hints=["SELECT name FROM customers WHERE id NOT IN (SELECT cust_id FROM orders);"])

def verify_medium(cur, conn):
    cur.execute("SELECT name FROM customers WHERE id NOT IN (SELECT cust_id FROM orders)")
    rows = cur.fetchall()
    return len(rows) == 1 and rows[0][0] == 'Charlie'

medium = Task("The query should return only 'Charlie'.",
              verify_medium, Level.MEDIUM,
              hints=["Check that the subquery returns the correct list of cust_ids."])

def verify_hard(cur, conn):
    cur.execute("SELECT name FROM customers WHERE id IN (SELECT cust_id FROM orders WHERE cust_id IS NOT NULL)")
    rows = cur.fetchall()
    return {'Alice','Bob'} == {r[0] for r in rows}

hard = Task("Find customers who HAVE placed an order using IN.",
            verify_hard, Level.HARD,
            hints=["SELECT name FROM customers WHERE id IN (SELECT cust_id FROM orders);"])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
