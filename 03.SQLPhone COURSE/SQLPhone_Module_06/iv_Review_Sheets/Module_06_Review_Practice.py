import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

# ─── Easy: UPDATE a row ─────────────────────────────
def verify_easy(cur, conn):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='inventory'")
    if not cur.fetchone():
        return False
    cur.execute("SELECT price FROM inventory WHERE name='Widget'")
    row = cur.fetchone()
    return row is not None and row[0] == 19.99

easy = Task(
    description="Create table 'inventory' (id INTEGER PRIMARY KEY, name TEXT, price REAL).\n"
                "Insert a row: (1,'Widget',24.99).\n"
                "Then update the price to 19.99.",
    verify_func=verify_easy,
    level=Level.EASY,
    hints=[
        "CREATE TABLE inventory (id INTEGER PRIMARY KEY, name TEXT, price REAL);",
        "INSERT INTO inventory VALUES (1,'Widget',24.99);",
        "UPDATE inventory SET price = 19.99 WHERE name = 'Widget';"
    ]
)

# ─── Medium: ADD COLUMN with DEFAULT ────────────────
def verify_medium(cur, conn):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='inventory'")
    if not cur.fetchone():
        return False
    # Check that the 'stock' column exists and has default 0
    cur.execute("PRAGMA table_info('inventory')")
    cols = {row[1]: row for row in cur.fetchall()}
    if 'stock' not in cols:
        return False
    # Insert a row without specifying stock, then check
    # (The user's script should have already inserted a row with default)
    cur.execute("SELECT stock FROM inventory WHERE name='Gadget'")
    row = cur.fetchone()
    return row is not None and row[0] == 0

medium = Task(
    description="Using the same 'inventory' table, add a column 'stock INTEGER DEFAULT 0'.\n"
                "Then insert a new product 'Gadget' with price 9.99, without specifying stock.\n"
                "The default should apply.",
    verify_func=verify_medium,
    level=Level.MEDIUM,
    hints=[
        "ALTER TABLE inventory ADD COLUMN stock INTEGER DEFAULT 0;",
        "INSERT INTO inventory (name, price) VALUES ('Gadget', 9.99);"
    ]
)

# ─── Hard: Constraints, Foreign Keys, and Index ─────
def verify_hard(cur, conn):
    # Verify that tables exist with correct constraints
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name IN ('categories','products')")
    if len(cur.fetchall()) != 2:
        return False
    cur.execute("PRAGMA foreign_keys = ON")
    # Check that 'Books' category deletion cascaded
    cur.execute("SELECT COUNT(*) FROM categories WHERE name='Books'")
    if cur.fetchone()[0] != 0:
        return False
    # Check that the product 'Novel' is gone
    cur.execute("SELECT COUNT(*) FROM products WHERE name='Novel'")
    if cur.fetchone()[0] != 0:
        return False
    # Check that index exists (any index on products)
    cur.execute("SELECT name FROM sqlite_master WHERE type='index' AND tbl_name='products'")
    if not cur.fetchone():
        return False
    # Final expected output
    expected = "Keyboard 49.95 Electronics\nMouse 29.99 Electronics"
    cur.execute("""
        SELECT p.name, p.price, c.name
        FROM products p
        JOIN categories c ON p.category_id = c.id
        ORDER BY p.name
    """)
    rows = cur.fetchall()
    result = "\n".join(f"{r[0]} {r[1]} {r[2]}" for r in rows)
    return result == expected

hard = Task(
    description="Build an inventory system with integrity:\n"
                "1. Create table 'categories' (id INTEGER PRIMARY KEY, name TEXT).\n"
                "   Insert: (1,'Electronics'), (2,'Books').\n"
                "2. Create table 'products' (id INTEGER PRIMARY KEY, name TEXT, price REAL,\n"
                "   stock INTEGER DEFAULT 0 CHECK(stock >= 0),\n"
                "   category_id INTEGER,\n"
                "   FOREIGN KEY(category_id) REFERENCES categories(id) ON DELETE CASCADE).\n"
                "3. Insert products:\n"
                "   (1,'Mouse',24.99,100,1),\n"
                "   (2,'Keyboard',49.95,50,1),\n"
                "   (3,'Novel',19.99,200,2).\n"
                "4. Create an index on 'products(name)'.\n"
                "5. Update the price of 'Mouse' to 29.99.\n"
                "6. Delete the 'Books' category (cascade should remove 'Novel').\n"
                "7. Finally, write a SELECT that shows product name, price, and category name\n"
                "   for all remaining products, sorted by product name.\n"
                "Expected output:\n"
                "Keyboard 49.95 Electronics\n"
                "Mouse 29.99 Electronics",
    verify_func=verify_hard,
    level=Level.HARD,
    hints=[
        "CREATE TABLE categories (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO categories VALUES (1,'Electronics'), (2,'Books');",
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price REAL, stock INTEGER DEFAULT 0 CHECK(stock >= 0), category_id INTEGER, FOREIGN KEY(category_id) REFERENCES categories(id) ON DELETE CASCADE);",
        "INSERT INTO products VALUES (1,'Mouse',24.99,100,1), (2,'Keyboard',49.95,50,1), (3,'Novel',19.99,200,2);",
        "CREATE INDEX idx_product_name ON products(name);",
        "UPDATE products SET price = 29.99 WHERE name = 'Mouse';",
        "DELETE FROM categories WHERE name = 'Books';",
        "SELECT p.name, p.price, c.name FROM products p JOIN categories c ON p.category_id = c.id ORDER BY p.name;"
    ]
)

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__":
    main()
