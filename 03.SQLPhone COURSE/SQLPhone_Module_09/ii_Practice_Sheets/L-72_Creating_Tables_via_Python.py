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
