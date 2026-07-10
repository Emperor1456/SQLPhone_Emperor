import sys, sqlite3, os
sys.path.append("../..")
from practice_engine import Task, Level, run_task

DB = "ecommerce.db"

def verify_easy(cur, conn):
    for tbl in ['Category','Supplier','Product','Sale']:
        cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{tbl}'")
        if not cur.fetchone():
            return False
    return True

easy = Task(
    "Build the E‑commerce Inventory: create tables Category, Supplier, Product, Sale with foreign keys.",
    verify_easy, Level.EASY,
    hints=["CREATE TABLE Category(id INTEGER PRIMARY KEY, name TEXT);",
           "CREATE TABLE Supplier(id INTEGER PRIMARY KEY, name TEXT, contact TEXT);",
           "CREATE TABLE Product(id INTEGER PRIMARY KEY, name TEXT, category_id INTEGER, supplier_id INTEGER, unit_price REAL, stock_quantity INTEGER, FOREIGN KEY(category_id) REFERENCES Category(id), FOREIGN KEY(supplier_id) REFERENCES Supplier(id));",
           "CREATE TABLE Sale(id INTEGER PRIMARY KEY, product_id INTEGER, quantity_sold INTEGER, sale_date TEXT, FOREIGN KEY(product_id) REFERENCES Product(id));"]
)

def verify_medium(cur, conn):
    for tbl in ['Category','Supplier','Product','Sale']:
        cur.execute(f"SELECT COUNT(*) FROM {tbl}")
        if cur.fetchone()[0] < 3:
            return False
    cur.execute("SELECT p.name, SUM(s.quantity_sold) FROM Product p JOIN Sale s ON p.id=s.product_id GROUP BY p.name")
    return len(cur.fetchall()) > 0

medium = Task(
    "Insert at least 3 rows per table and write a query showing total units sold per product.",
    verify_medium, Level.MEDIUM,
    hints=["Use JOIN and GROUP BY to aggregate sales."]
)

def verify_hard(cur, conn):
    cur.execute("SELECT c.name, SUM(p.unit_price * s.quantity_sold) as revenue FROM Category c JOIN Product p ON c.id=p.category_id JOIN Sale s ON p.id=s.product_id GROUP BY c.name ORDER BY revenue DESC LIMIT 1")
    row = cur.fetchone()
    return row is not None and row[1] is not None

hard = Task(
    "Find the category with the highest total revenue (price * quantity_sold across all sales).",
    verify_hard, Level.HARD,
    hints=["Join Category -> Product -> Sale, compute revenue, GROUP BY category, ORDER BY revenue DESC LIMIT 1"]
)


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

if __name__ == "__main__": main()
