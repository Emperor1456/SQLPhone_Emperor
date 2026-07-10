import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("SELECT COUNT(*) FROM products")
    return cur.fetchone()[0] >= 3

easy = Task("Create table 'products' (id, name, price, stock). Insert at least 3 products with varied prices and stocks.",
            verify_easy, Level.EASY,
            hints=["CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price REAL, stock INTEGER);",
                   "INSERT INTO products (name, price, stock) VALUES ('A',30,10),('B',15,0),('C',50,5);"])

def verify_medium(cur, conn):
    cur.execute("SELECT COUNT(*) FROM products WHERE price > 20 AND stock > 0")
    return cur.fetchone()[0] > 0

medium = Task("Write a SELECT that returns products with price > 20 AND stock > 0.",
              verify_medium, Level.MEDIUM,
              hints=["SELECT * FROM products WHERE price > 20 AND stock > 0;"])

def verify_hard(cur, conn):
    cur.execute("SELECT COUNT(*) FROM products WHERE price > 20 AND stock > 0")
    count1 = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM products WHERE NOT (price <= 20 OR stock <= 0)")
    count2 = cur.fetchone()[0]
    return count1 == count2

hard = Task("Rewrite the previous query using NOT and parentheses to achieve the same logic.",
            verify_hard, Level.HARD,
            hints=["SELECT * FROM products WHERE NOT (price <= 20 OR stock <= 0);"])


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
