import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

# ─── Easy: build a single table and insert ──────────────
def verify_easy(cur, conn):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='products'")
    if not cur.fetchone():
        return False
    cur.execute("SELECT COUNT(*) FROM products")
    return cur.fetchone()[0] >= 2

easy = Task(
    description="Create table 'products' (id INTEGER PRIMARY KEY, name TEXT, price REAL).\n"
                "Insert at least two products.",
    verify_func=verify_easy,
    level=Level.EASY,
    hints=[
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price REAL);",
        "INSERT INTO products VALUES (1, 'Mouse', 24.99);",
        "INSERT INTO products VALUES (2, 'Keyboard', 49.95);"
    ]
)

# ─── Medium: add a second table and foreign key ────────
def verify_medium(cur, conn):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='orders'")
    if not cur.fetchone():
        return False
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("SELECT COUNT(*) FROM orders WHERE product_id IS NOT NULL")
    return cur.fetchone()[0] >= 1

medium = Task(
    description="Create table 'orders' (id INTEGER PRIMARY KEY, product_id INTEGER,\n"
                "qty INTEGER, FOREIGN KEY(product_id) REFERENCES products(id)).\n"
                "Insert at least one order referencing an existing product.",
    verify_func=verify_medium,
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE orders (id INTEGER PRIMARY KEY, product_id INTEGER, qty INTEGER,\n"
        "FOREIGN KEY(product_id) REFERENCES products(id));",
        "INSERT INTO orders VALUES (1, 1, 3);"
    ]
)

# ─── Hard: complete sales report with a JOIN ──────────
def verify_hard(cur, conn):
    cur.execute("PRAGMA foreign_keys = ON")
    # check both tables exist and have rows
    for tbl in ['products', 'orders']:
        cur.execute(f"SELECT COUNT(*) FROM {tbl}")
        if cur.fetchone()[0] == 0:
            return False
    # run the required query and compare exact output
    expected_output = "Mouse 3 74.97\nKeyboard 1 49.95"
    try:
        # The user's script must produce that exact output when executed as a whole.
        # We can't capture print output here because the engine doesn't capture prints in SQLPhone.
        # Instead, we'll require a final SELECT that returns that result set.
        # We'll check the result of a specific query: 
        cur.execute("""
            SELECT p.name, SUM(o.qty), SUM(o.qty * p.price)
            FROM products p
            JOIN orders o ON p.id = o.product_id
            GROUP BY p.name
            ORDER BY p.name
        """)
        rows = cur.fetchall()
        # Convert to formatted string
        result_lines = [f"{r[0]} {r[1]} {r[2]:.2f}" for r in rows]
        return "\n".join(result_lines) == expected_output
    except Exception:
        return False

hard = Task(
    description="Build a complete mini‑sales system:\n"
                "1. Ensure 'products' table has at least:\n"
                "   (1,'Mouse',24.99) and (2,'Keyboard',49.95)\n"
                "2. Insert at least two orders:\n"
                "   (1,1,3) and (2,2,1)\n"
                "3. Write a SELECT that joins products and orders,\n"
                "   groups by product name, and shows:\n"
                "   product name, total quantity sold, total revenue\n"
                "   sorted by product name.\n"
                "The exact output must be:\n"
                "Mouse 3 74.97\n"
                "Keyboard 1 49.95",
    verify_func=verify_hard,
    level=Level.HARD,
    hints=[
        "CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price REAL);",
        "INSERT INTO products VALUES (1,'Mouse',24.99),(2,'Keyboard',49.95);",
        "CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, product_id INTEGER, qty INTEGER,\n"
        "FOREIGN KEY(product_id) REFERENCES products(id));",
        "INSERT INTO orders VALUES (1,1,3),(2,2,1);",
        "SELECT p.name, SUM(o.qty), SUM(o.qty * p.price) FROM products p JOIN orders o ON p.id = o.product_id GROUP BY p.name ORDER BY p.name;"
    ]
)

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__":
    main()
