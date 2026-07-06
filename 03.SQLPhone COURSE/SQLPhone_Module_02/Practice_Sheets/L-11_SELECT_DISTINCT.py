import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("SELECT COUNT(*) FROM orders")
    return cur.fetchone()[0] >= 4

easy = Task("Create table 'orders' (id, customer_name, city, country). Insert at least 4 rows, some with duplicate city/country pairs.",
            verify_easy, Level.EASY,
            hints=["CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_name TEXT, city TEXT, country TEXT);",
                   "INSERT INTO orders (customer_name, city, country) VALUES ('A','Berlin','Germany'),('B','Berlin','Germany'),('C','Paris','France'),('D','Madrid','Spain');"])

def verify_medium(cur, conn):
    cur.execute("SELECT COUNT(*) FROM (SELECT DISTINCT city, country FROM orders)")
    unique = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM orders")
    total = cur.fetchone()[0]
    return unique < total

medium = Task("Write a query that returns all unique city/country pairs using SELECT DISTINCT.",
              verify_medium, Level.MEDIUM,
              hints=["SELECT DISTINCT city, country FROM orders;"])

def verify_hard(cur, conn):
    cur.execute("SELECT COUNT(DISTINCT city || country) FROM orders")
    distinct_count = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM orders")
    total = cur.fetchone()[0]
    return distinct_count < total

hard = Task("Count the number of distinct city/country pairs using COUNT(DISTINCT ...).",
            verify_hard, Level.HARD,
            hints=["SELECT COUNT(DISTINCT city || country) FROM orders;"])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
