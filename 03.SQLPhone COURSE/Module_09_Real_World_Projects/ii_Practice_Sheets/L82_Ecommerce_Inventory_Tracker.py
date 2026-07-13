import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🏬  Imperial Store – Build Inventory Schema\n\n"
        "Write Python code that:\n"
        "  1. Connects to ':memory:'\n"
        "  2. Creates the three tables:\n"
        "     suppliers, products, stock_movements\n"
        "     (exact schema from the lecture).\n"
        "  3. Inserts seed data:\n"
        "     • 1 supplier: 'TechSupplier Inc.' (id=1)\n"
        "     • 5 products:\n"
        "       (1,'Wireless Mouse',1,24.99,150)\n"
        "       (2,'Keyboard',1,49.99,85)\n"
        "       (3,'USB Hub',1,12.99,200)\n"
        "       (4,'Monitor',1,199.99,5)\n"
        "       (5,'Desk Lamp',1,35.00,8)\n"
        "  4. Commits, then SELECTs all product names\n"
        "     sorted alphabetically and prints them.\n\n"
        "Expected output:\n[('Desk Lamp',), ('Keyboard',), ('Monitor',), ('USB Hub',), ('Wireless Mouse',)]"
    ),
    expected_output="[('Desk Lamp',), ('Keyboard',), ('Monitor',), ('USB Hub',), ('Wireless Mouse',)]",
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.executescript('''",
        "CREATE TABLE suppliers (supplier_id INTEGER PRIMARY KEY, name TEXT NOT NULL);",
        "CREATE TABLE products (product_id INTEGER PRIMARY KEY, name TEXT NOT NULL, supplier_id INTEGER, price REAL CHECK(price > 0), stock INTEGER DEFAULT 0 CHECK(stock >= 0), FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id));",
        "CREATE TABLE stock_movements (movement_id INTEGER PRIMARY KEY, product_id INTEGER, quantity INTEGER, movement_type TEXT CHECK(movement_type IN ('in','out')), movement_date TEXT DEFAULT (datetime('now')), FOREIGN KEY (product_id) REFERENCES products(product_id));",
        "''')",
        "conn.executescript('''",
        "INSERT INTO suppliers VALUES (1,'TechSupplier Inc.');",
        "INSERT INTO products VALUES (1,'Wireless Mouse',1,24.99,150);",
        "INSERT INTO products VALUES (2,'Keyboard',1,49.99,85);",
        "INSERT INTO products VALUES (3,'USB Hub',1,12.99,200);",
        "INSERT INTO products VALUES (4,'Monitor',1,199.99,5);",
        "INSERT INTO products VALUES (5,'Desk Lamp',1,35.00,8);",
        "''')",
        "conn.commit()",
        "cursor = conn.execute('SELECT name FROM products ORDER BY name')",
        "print(cursor.fetchall())",
    ]
)

easy2 = Task(
    description=(
        "🔗  Product‑Supplier Join\n\n"
        "The inventory database is already seeded.\n"
        "Write Python code that:\n"
        "  1. Executes a JOIN between products and suppliers\n"
        "     to show product_name, supplier_name for all\n"
        "     products, sorted by product_name.\n"
        "  2. Prints the result.\n\n"
        "Expected output:\n[('Desk Lamp','TechSupplier Inc.'), ('Keyboard','TechSupplier Inc.'), ('Monitor','TechSupplier Inc.'), ('USB Hub','TechSupplier Inc.'), ('Wireless Mouse','TechSupplier Inc.')]"
    ),
    setup_sql=(
        "CREATE TABLE suppliers (supplier_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO suppliers VALUES (1,'TechSupplier Inc.');"
        "CREATE TABLE products (product_id INTEGER PRIMARY KEY, name TEXT NOT NULL, supplier_id INTEGER, price REAL CHECK(price > 0), stock INTEGER DEFAULT 0 CHECK(stock >= 0), FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id));"
        "INSERT INTO products VALUES (1,'Wireless Mouse',1,24.99,150);"
        "INSERT INTO products VALUES (2,'Keyboard',1,49.99,85);"
        "INSERT INTO products VALUES (3,'USB Hub',1,12.99,200);"
        "INSERT INTO products VALUES (4,'Monitor',1,199.99,5);"
        "INSERT INTO products VALUES (5,'Desk Lamp',1,35.00,8);"
        "CREATE TABLE stock_movements (movement_id INTEGER PRIMARY KEY, product_id INTEGER, quantity INTEGER, movement_type TEXT CHECK(movement_type IN ('in','out')), movement_date TEXT DEFAULT (datetime('now')), FOREIGN KEY (product_id) REFERENCES products(product_id));"
    ),
    expected_output="[('Desk Lamp', 'TechSupplier Inc.'), ('Keyboard', 'TechSupplier Inc.'), ('Monitor', 'TechSupplier Inc.'), ('USB Hub', 'TechSupplier Inc.'), ('Wireless Mouse', 'TechSupplier Inc.')]",
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''SELECT p.name, s.name FROM products p JOIN suppliers s ON p.supplier_id = s.supplier_id ORDER BY p.name''')",
        "print(cursor.fetchall())",
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "⚠️  Low‑Stock Alert – Reorder Needed\n\n"
        "The inventory database is seeded with 5 products,\n"
        "some with very low stock.\n"
        "Write Python code that lists the name and stock\n"
        "of all products whose stock is less than 10.\n"
        "Sort by name.\n\n"
        "Expected output:\n[('Desk Lamp', 8), ('Monitor', 5)]"
    ),
    setup_sql=(
        "CREATE TABLE suppliers (supplier_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO suppliers VALUES (1,'TechSupplier Inc.');"
        "CREATE TABLE products (product_id INTEGER PRIMARY KEY, name TEXT NOT NULL, supplier_id INTEGER, price REAL CHECK(price > 0), stock INTEGER DEFAULT 0 CHECK(stock >= 0), FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id));"
        "INSERT INTO products VALUES (1,'Wireless Mouse',1,24.99,150);"
        "INSERT INTO products VALUES (2,'Keyboard',1,49.99,85);"
        "INSERT INTO products VALUES (3,'USB Hub',1,12.99,200);"
        "INSERT INTO products VALUES (4,'Monitor',1,199.99,5);"
        "INSERT INTO products VALUES (5,'Desk Lamp',1,35.00,8);"
        "CREATE TABLE stock_movements (movement_id INTEGER PRIMARY KEY, product_id INTEGER, quantity INTEGER, movement_type TEXT CHECK(movement_type IN ('in','out')), movement_date TEXT DEFAULT (datetime('now')), FOREIGN KEY (product_id) REFERENCES products(product_id));"
    ),
    expected_output="[('Desk Lamp', 8), ('Monitor', 5)]",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('SELECT name, stock FROM products WHERE stock < 10 ORDER BY name')",
        "print(cursor.fetchall())",
    ]
)

medium2 = Task(
    description=(
        "📊  Supplier Performance – Products Supplied\n\n"
        "The inventory database is seeded.\n"
        "Write Python code that shows every supplier and\n"
        "the number of products they supply. Use a LEFT JOIN\n"
        "to include suppliers with no products.\n"
        "Sort by supplier name.\n\n"
        "Expected output:\n[('TechSupplier Inc.', 5)]"
    ),
    setup_sql=(
        "CREATE TABLE suppliers (supplier_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO suppliers VALUES (1,'TechSupplier Inc.');"
        "CREATE TABLE products (product_id INTEGER PRIMARY KEY, name TEXT NOT NULL, supplier_id INTEGER, price REAL CHECK(price > 0), stock INTEGER DEFAULT 0 CHECK(stock >= 0), FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id));"
        "INSERT INTO products VALUES (1,'Wireless Mouse',1,24.99,150);"
        "INSERT INTO products VALUES (2,'Keyboard',1,49.99,85);"
        "INSERT INTO products VALUES (3,'USB Hub',1,12.99,200);"
        "INSERT INTO products VALUES (4,'Monitor',1,199.99,5);"
        "INSERT INTO products VALUES (5,'Desk Lamp',1,35.00,8);"
        "CREATE TABLE stock_movements (movement_id INTEGER PRIMARY KEY, product_id INTEGER, quantity INTEGER, movement_type TEXT CHECK(movement_type IN ('in','out')), movement_date TEXT DEFAULT (datetime('now')), FOREIGN KEY (product_id) REFERENCES products(product_id));"
    ),
    expected_output="[('TechSupplier Inc.', 5)]",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''SELECT s.name, COUNT(p.product_id) FROM suppliers s LEFT JOIN products p ON s.supplier_id = p.supplier_id GROUP BY s.supplier_id ORDER BY s.name''')",
        "print(cursor.fetchall())",
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "⚡  Trigger – Auto‑Update Stock on Sale\n\n"
        "The inventory database is seeded.\n"
        "Write Python code that:\n"
        "  1. Creates the trigger `after_stock_out`:\n"
        "     AFTER INSERT ON stock_movements\n"
        "     FOR EACH ROW\n"
        "     WHEN NEW.movement_type = 'out'\n"
        "     BEGIN\n"
        "       UPDATE products SET stock = stock - NEW.quantity\n"
        "       WHERE product_id = NEW.product_id;\n"
        "     END;\n"
        "  2. Inserts a stock movement for product_id=1\n"
        "     (Wireless Mouse), quantity=3, type='out'.\n"
        "  3. SELECTs the new stock for product 1 and prints it.\n\n"
        "Expected output:\n147"
    ),
    setup_sql=(
        "CREATE TABLE suppliers (supplier_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO suppliers VALUES (1,'TechSupplier Inc.');"
        "CREATE TABLE products (product_id INTEGER PRIMARY KEY, name TEXT NOT NULL, supplier_id INTEGER, price REAL CHECK(price > 0), stock INTEGER DEFAULT 0 CHECK(stock >= 0), FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id));"
        "INSERT INTO products VALUES (1,'Wireless Mouse',1,24.99,150);"
        "INSERT INTO products VALUES (2,'Keyboard',1,49.99,85);"
        "INSERT INTO products VALUES (3,'USB Hub',1,12.99,200);"
        "INSERT INTO products VALUES (4,'Monitor',1,199.99,5);"
        "INSERT INTO products VALUES (5,'Desk Lamp',1,35.00,8);"
        "CREATE TABLE stock_movements (movement_id INTEGER PRIMARY KEY, product_id INTEGER, quantity INTEGER, movement_type TEXT CHECK(movement_type IN ('in','out')), movement_date TEXT DEFAULT (datetime('now')), FOREIGN KEY (product_id) REFERENCES products(product_id));"
    ),
    expected_output="147",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.executescript('''",
        "CREATE TRIGGER after_stock_out AFTER INSERT ON stock_movements",
        "FOR EACH ROW WHEN NEW.movement_type = 'out'",
        "BEGIN",
        "    UPDATE products SET stock = stock - NEW.quantity WHERE product_id = NEW.product_id;",
        "END;",
        "''')",
        "conn.execute(\"INSERT INTO stock_movements (product_id, quantity, movement_type) VALUES (1,3,'out')\")",
        "conn.commit()",
        "cursor = conn.execute('SELECT stock FROM products WHERE product_id = 1')",
        "print(cursor.fetchone()[0])",
    ]
)

hard2 = Task(
    description=(
        "📈  Daily Stock Movement Summary\n\n"
        "The inventory database is seeded with some movements\n"
        "already recorded.\n"
        "Write Python code that aggregates total quantity\n"
        "per day and per movement type.\n"
        "Use date() to extract the day from movement_date.\n"
        "Sort by day, then movement_type.\n\n"
        "Expected output:\n[('2026-07-13','in',10), ('2026-07-13','out',3)]"
    ),
    setup_sql=(
        "CREATE TABLE suppliers (supplier_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO suppliers VALUES (1,'TechSupplier Inc.');"
        "CREATE TABLE products (product_id INTEGER PRIMARY KEY, name TEXT NOT NULL, supplier_id INTEGER, price REAL CHECK(price > 0), stock INTEGER DEFAULT 0 CHECK(stock >= 0), FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id));"
        "INSERT INTO products VALUES (1,'Wireless Mouse',1,24.99,150);"
        "INSERT INTO products VALUES (2,'Keyboard',1,49.99,85);"
        "INSERT INTO products VALUES (3,'USB Hub',1,12.99,200);"
        "INSERT INTO products VALUES (4,'Monitor',1,199.99,5);"
        "INSERT INTO products VALUES (5,'Desk Lamp',1,35.00,8);"
        "CREATE TABLE stock_movements (movement_id INTEGER PRIMARY KEY, product_id INTEGER, quantity INTEGER, movement_type TEXT CHECK(movement_type IN ('in','out')), movement_date TEXT DEFAULT (datetime('now')), FOREIGN KEY (product_id) REFERENCES products(product_id));"
        "INSERT INTO stock_movements (product_id, quantity, movement_type, movement_date) VALUES (1,3,'out','2026-07-13 10:00:00');"
        "INSERT INTO stock_movements (product_id, quantity, movement_type, movement_date) VALUES (2,10,'in','2026-07-13 12:00:00');"
    ),
    expected_output="[('2026-07-13', 'in', 10), ('2026-07-13', 'out', 3)]",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT date(movement_date) AS day, movement_type, SUM(quantity) AS total",
        "FROM stock_movements GROUP BY day, movement_type ORDER BY day, movement_type",
        "''')",
        "print(cursor.fetchall())",
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L82.json",
        module_name="Module_09_Real_World_Projects",
        lesson_name="L82_Ecommerce_Inventory_Tracker"
    )