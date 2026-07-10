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
    levels = {"1": easy, "2": medium, "3": hard}
    while True:
        print("
Choose difficulty:")
        print("1 - Easy")
        print("2 - Medium")
        print("3 - Hard")
        print("0 - Exit")
        c = input("> ").strip()
        if c == "0":
            break
        task = levels.get(c)
        if task:
            run_task(task)
            cont = input("Try next level? (y/n): ").strip().lower()
            if cont != "y":
                continue
            next_key = str(min(int(c)+1, 3))
            next_task = levels.get(next_key)
            if next_task:
                print(f"
Moving to {next_task.level}...")
                run_task(next_task)

if __name__=="__main__": main()
