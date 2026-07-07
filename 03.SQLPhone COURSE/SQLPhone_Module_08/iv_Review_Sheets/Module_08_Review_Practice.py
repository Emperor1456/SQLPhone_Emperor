import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

# ─── Easy: CREATE VIEW and query it ─────────────────
def verify_easy(cur, conn):
    cur.execute("SELECT name FROM sqlite_master WHERE type='view' AND name='high_earners'")
    if not cur.fetchone():
        return False
    cur.execute("SELECT COUNT(*) FROM high_earners")
    return cur.fetchone()[0] >= 1

easy = Task(
    description="Create table 'employees' (id INTEGER PRIMARY KEY, name TEXT, salary REAL).\n"
                "Insert rows: (1,'Alice',50000),(2,'Bob',80000),(3,'Charlie',60000).\n"
                "Create a view 'high_earners' that selects employees with salary > 55000.\n"
                "Then query the view (the engine will verify view existence and row count).",
    verify_func=verify_easy,
    level=Level.EASY,
    hints=[
        "CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, salary REAL);",
        "INSERT INTO employees VALUES (1,'Alice',50000),(2,'Bob',80000),(3,'Charlie',60000);",
        "CREATE VIEW high_earners AS SELECT name, salary FROM employees WHERE salary > 55000;",
        "SELECT * FROM high_earners;"
    ]
)

# ─── Medium: CASE expression ────────────────────────
def verify_medium(cur, conn):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='products'")
    if not cur.fetchone(): return False
    cur.execute("SELECT COUNT(*) FROM products")
    if cur.fetchone()[0] < 3: return False
    cur.execute("""
        SELECT name, price,
               CASE
                   WHEN price < 50 THEN 'Budget'
                   WHEN price < 200 THEN 'Standard'
                   ELSE 'Premium'
               END AS category
        FROM products
        ORDER BY name
    """)
    rows = cur.fetchall()
    if len(rows) < 3: return False
    # Check that the categories match expected for known data
    expected = [("Keyboard", 49.95, "Budget"), ("Monitor", 199.99, "Standard"), ("Mouse", 24.99, "Budget")]
    return rows == expected

medium = Task(
    description="Using 'products' table with columns (id, name, price),\n"
                "insert at least three products with different prices:\n"
                "(1,'Mouse',24.99), (2,'Keyboard',49.95), (3,'Monitor',199.99).\n"
                "Write a query that adds a column 'category' using CASE:\n"
                "  price < 50 → 'Budget', price < 200 → 'Standard', else 'Premium'.\n"
                "Sort by name. The exact output must be:\n"
                "Keyboard 49.95 Budget\n"
                "Monitor 199.99 Standard\n"
                "Mouse 24.99 Budget",
    verify_func=verify_medium,
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price REAL);",
        "INSERT INTO products VALUES (1,'Mouse',24.99), (2,'Keyboard',49.95), (3,'Monitor',199.99);",
        "SELECT name, price, CASE WHEN price<50 THEN 'Budget' WHEN price<200 THEN 'Standard' ELSE 'Premium' END AS category FROM products ORDER BY name;"
    ]
)

# ─── Hard: View with CASE and subquery ──────────────
def verify_hard(cur, conn):
    # Check required tables and view
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name IN ('orders','order_items')")
    if len(cur.fetchall()) != 2: return False
    cur.execute("SELECT name FROM sqlite_master WHERE type='view' AND name='order_summary'")
    if not cur.fetchone(): return False
    # Query the view and expect exact output
    expected = "Order 1 Large\nOrder 2 Small"
    cur.execute("SELECT * FROM order_summary ORDER BY order_id")
    rows = cur.fetchall()
    result = "\n".join(f"Order {r[0]} {r[1]}" for r in rows)
    return result == expected

hard = Task(
    description="Build an order classification system:\n"
                "1. Create table 'orders' (id INTEGER PRIMARY KEY, customer TEXT).\n"
                "   Insert (1,'Alice'), (2,'Bob').\n"
                "2. Create table 'order_items' (order_id INTEGER, product TEXT, qty INTEGER, price REAL,\n"
                "   FOREIGN KEY(order_id) REFERENCES orders(id)).\n"
                "   Insert items: (1,'Mouse',2,24.99), (1,'Keyboard',1,49.95), (2,'Monitor',1,199.99).\n"
                "3. Create a view 'order_summary' that shows each order's ID and a size label:\n"
                "   - 'Large' if total order value >= 100\n"
                "   - 'Small' otherwise.\n"
                "   Compute total value as SUM(qty*price) grouped by order_id.\n"
                "4. Finally, query the view sorted by order_id.\n"
                "Exact output must be:\n"
                "Order 1 Large\n"
                "Order 2 Small",
    verify_func=verify_hard,
    level=Level.HARD,
    hints=[
        "CREATE TABLE orders (id INTEGER PRIMARY KEY, customer TEXT);",
        "INSERT INTO orders VALUES (1,'Alice'), (2,'Bob');",
        "CREATE TABLE order_items (order_id INTEGER, product TEXT, qty INTEGER, price REAL, FOREIGN KEY(order_id) REFERENCES orders(id));",
        "INSERT INTO order_items VALUES (1,'Mouse',2,24.99), (1,'Keyboard',1,49.95), (2,'Monitor',1,199.99);",
        "CREATE VIEW order_summary AS SELECT o.id, CASE WHEN SUM(oi.qty*oi.price) >= 100 THEN 'Large' ELSE 'Small' END AS size FROM orders o JOIN order_items oi ON o.id=oi.order_id GROUP BY o.id;",
        "SELECT * FROM order_summary ORDER BY order_id;"
    ]
)

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__":
    main()
