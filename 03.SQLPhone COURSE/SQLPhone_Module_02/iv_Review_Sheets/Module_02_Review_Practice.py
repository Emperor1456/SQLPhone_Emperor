import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

# ─── Easy: DISTINCT ──────────────────────────────────
def verify_easy(cur, conn):
    cur.execute("SELECT COUNT(*) FROM customers")
    if cur.fetchone()[0] < 3:
        return False
    cur.execute("SELECT DISTINCT city FROM customers")
    return len(cur.fetchall()) >= 2

easy = Task(
    description="Create table 'customers' (id INTEGER PRIMARY KEY, name TEXT, city TEXT).\n"
                "Insert at least 3 rows, with at least two different cities.\n"
                "Then write a query that shows all distinct cities.",
    verify_func=verify_easy,
    level=Level.EASY,
    hints=[
        "CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT, city TEXT);",
        "INSERT INTO customers VALUES (1,'Alice','Dhaka'),(2,'Bob','Dhaka'),(3,'Charlie','Khulna');",
        "SELECT DISTINCT city FROM customers;"
    ]
)

# ─── Medium: WHERE + ORDER BY ────────────────────────
def verify_medium(cur, conn):
    cur.execute("SELECT COUNT(*) FROM products")
    if cur.fetchone()[0] < 3:
        return False
    cur.execute("SELECT name, price FROM products WHERE price > 20 ORDER BY price DESC")
    rows = cur.fetchall()
    if len(rows) < 1:
        return False
    # check descending order
    prices = [r[1] for r in rows]
    return prices == sorted(prices, reverse=True)

medium = Task(
    description="Create table 'products' (id INTEGER PRIMARY KEY, name TEXT, price REAL, stock INTEGER).\n"
                "Insert at least 3 products. Then write a query that shows products with price > 20,\n"
                "sorted by price descending.",
    verify_func=verify_medium,
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price REAL, stock INTEGER);",
        "INSERT INTO products VALUES (1,'Mouse',15.99,100),(2,'Keyboard',45.00,50),(3,'Monitor',199.99,20);",
        "SELECT name, price FROM products WHERE price > 20 ORDER BY price DESC;"
    ]
)

# ─── Hard: Complex filter + LIMIT ─────────────────────
def verify_hard(cur, conn):
    # Check that required rows exist, then verify the exact output of a complex query.
    cur.execute("SELECT COUNT(*) FROM orders")
    if cur.fetchone()[0] < 4:
        return False
    expected = "Alice 2\nCharlie 1"
    cur.execute("""
        SELECT c.name, COUNT(o.id) AS order_count
        FROM customers c
        JOIN orders o ON c.id = o.customer_id
        WHERE o.amount BETWEEN 50 AND 500
        GROUP BY c.name
        HAVING order_count >= 1
        ORDER BY order_count DESC
        LIMIT 2
    """)
    rows = cur.fetchall()
    result = "\n".join(f"{r[0]} {r[1]}" for r in rows)
    return result == expected

hard = Task(
    description="Build a mini order‑tracking system:\n"
                "1. Reuse 'customers' table (or recreate) with at least 3 customers.\n"
                "2. Create table 'orders' (id INTEGER PRIMARY KEY, customer_id INTEGER,\n"
                "   amount REAL, order_date TEXT, FOREIGN KEY(customer_id) REFERENCES customers(id)).\n"
                "3. Insert at least 4 orders with varying amounts and dates.\n"
                "4. Write a query that shows customer name and number of orders\n"
                "   where the order amount is between 50 and 500, grouped by customer,\n"
                "   sorted by order count descending, and limited to the top 2 customers.\n"
                "The exact output must be:\n"
                "Alice 2\n"
                "Charlie 1",
    verify_func=verify_hard,
    level=Level.HARD,
    hints=[
        "CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY, name TEXT, city TEXT);",
        "INSERT INTO customers VALUES (1,'Alice','Dhaka'),(2,'Bob','Dhaka'),(3,'Charlie','Khulna');",
        "CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER, amount REAL, order_date TEXT,\n"
        "FOREIGN KEY(customer_id) REFERENCES customers(id));",
        "INSERT INTO orders VALUES (1,1,100,'2026-01-01'),(2,1,200,'2026-01-02'),(3,2,30,'2026-01-03'),(4,3,150,'2026-01-04');",
        "SELECT c.name, COUNT(o.id) AS order_count FROM customers c JOIN orders o ON c.id=o.customer_id\n"
        "WHERE o.amount BETWEEN 50 AND 500 GROUP BY c.name HAVING order_count>=1 ORDER BY order_count DESC LIMIT 2;"
    ]
)

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__":
    main()
