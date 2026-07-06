import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='products'")
    return cur.fetchone() is not None

easy = Task(
    "Write Python code to execute a CREATE TABLE for 'products' (id, name, price).",
    verify_easy, Level.EASY,
    hints=["cur.execute('CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price REAL)')", "conn.commit()"]
)

def verify_medium(cur, conn):
    cur.execute("PRAGMA table_info('products')")
    cols = [c[1] for c in cur.fetchall()]
    return cols == ['id','name','price']

medium = Task(
    "Verify the column names are exactly 'id', 'name', 'price'.",
    verify_medium, Level.MEDIUM,
    hints=["PRAGMA table_info('products')"]
)

def verify_hard(cur, conn):
    cur.execute("INSERT INTO products (name, price) VALUES ('Test', 9.99)")
    conn.commit()
    cur.execute("SELECT name, price FROM products WHERE name='Test'")
    row = cur.fetchone()
    return row == ('Test', 9.99)

hard = Task(
    "Insert a product using Python and then fetch it back to confirm.",
    verify_hard, Level.HARD,
    hints=["cur.execute('INSERT INTO products (name, price) VALUES (?,?)', ('Test', 9.99))", "conn.commit()"]
)

def main():
    print("1 Easy  2 Medium  3 Hard")
    c = input("> ")
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))
if __name__ == "__main__": main()
