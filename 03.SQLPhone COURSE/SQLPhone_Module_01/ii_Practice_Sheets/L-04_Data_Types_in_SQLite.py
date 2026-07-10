import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("PRAGMA table_info('products')")
    return len(cur.fetchall()) == 5

easy = Task("Create table 'products' (id INT PK, name TEXT NOT NULL, price REAL, quantity INT, photo BLOB).", verify_easy, Level.EASY,
            hints=["CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, price REAL, quantity INTEGER, photo BLOB);"])

def verify_medium(cur, conn):
    cur.execute("SELECT * FROM products")
    row = cur.fetchone()
    return row is not None and len(row) == 5

medium = Task("Insert one row into products (use X'0000' for blob).", verify_medium, Level.MEDIUM,
              hints=["INSERT INTO products VALUES (1, 'Widget', 9.99, 100, X'0000');","SELECT * FROM products;"])

def verify_hard(cur, conn):
    cur.execute("SELECT COUNT(*) FROM products")
    return cur.fetchone()[0] >= 2

hard = Task("Insert a second product with a different name and price, then SELECT all products sorted by price descending.", verify_hard, Level.HARD,
            hints=["INSERT INTO products VALUES (2, 'Gadget', 19.99, 50, X'1111');","SELECT * FROM products ORDER BY price DESC;"])


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
