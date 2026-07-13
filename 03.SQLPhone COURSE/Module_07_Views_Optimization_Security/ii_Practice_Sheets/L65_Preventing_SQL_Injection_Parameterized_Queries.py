import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🔒  Parameterized SELECT – Safe Lookup\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Write a parameterized SELECT that takes a soldier's\n"
        "name as a parameter and returns their id and salary.\n"
        "Use a `?` placeholder.\n\n"
        "Expected output:\n[(1, 5000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor',5000), (2,'Rahim',4000), (3,'Karim',2000), (4,'Ali',4500), (5,'Hasan',3500);"
    ),
    expected_output="[(1, 5000.0)]",
    level=Level.EASY,
    hints=[
        "SELECT id, salary FROM soldiers WHERE name = ?;",
        "-- The engine will supply 'Emperor' as the parameter"
    ]
)

easy2 = Task(
    description=(
        "🔐  Parameterized INSERT – Add a Soldier\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Write a parameterized INSERT that adds a new\n"
        "soldier. Use `?` placeholders for all three values.\n"
        "Then SELECT the newly inserted row (id = 6).\n\n"
        "Expected output:\n[(6, 'Fatima', 'Private', 1800.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[(6, 'Fatima', 'Private', 1800.0)]",
    level=Level.EASY,
    hints=[
        "INSERT INTO soldiers (name, rank, salary) VALUES (?, ?, ?);",
        "-- The engine will supply 'Fatima', 'Private', 1800.0",
        "SELECT * FROM soldiers WHERE id = 6;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "⚠️  Unsafe vs Safe – Injection Demo\n\n"
        "Create a table `users` with columns:\n"
        "  • id INTEGER, username TEXT, password TEXT.\n"
        "Insert two users.\n"
        "Write TWO queries:\n"
        "  1. An UNSAFE query using string concatenation\n"
        "     (simulate with a direct value: 'admin' OR '1'='1')\n"
        "  2. A SAFE parameterized query\n"
        "Show that the unsafe query could return all rows\n"
        "(simulate by selecting where username is the\n"
        "malicious string). Return the result of the\n"
        "SAFE query with username = 'admin'.\n\n"
        "Expected output:\n[(1, 'admin', 'secret')]"
    ),
    expected_output="[(1, 'admin', 'secret')]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE users (id INTEGER, username TEXT, password TEXT);",
        "INSERT INTO users VALUES (1,'admin','secret'), (2,'user','pass');",
        "SELECT * FROM users WHERE username = ?;",
        "-- The engine will supply 'admin'"
    ]
)

medium2 = Task(
    description=(
        "🧪  Parameterized UPDATE – Safe Raise\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Write a parameterized UPDATE that gives a raise\n"
        "to a soldier by name. Use `?` for both the new\n"
        "salary and the name.\n"
        "Then SELECT the updated row.\n\n"
        "Expected output:\n[(1, 'Emperor', 'General', 5500.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[(1, 'Emperor', 'General', 5500.0)]",
    level=Level.MEDIUM,
    hints=[
        "UPDATE soldiers SET salary = ? WHERE name = ?;",
        "-- The engine will supply 5500.0, 'Emperor'",
        "SELECT * FROM soldiers WHERE id = 1;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🛡️  Bulk Parameterized INSERT – Many Rows\n\n"
        "The `soldiers` table is empty.\n"
        "Write a parameterized INSERT statement that\n"
        "accepts values for three rows at once using\n"
        "multiple `?` placeholders.\n"
        "Then SELECT all rows to confirm they were inserted.\n\n"
        "Expected output:\n[(1,'Emperor','General',5000.0), (2,'Rahim','Colonel',4000.0), (3,'Karim','Private',2000.0)]"
    ),
    expected_output="[(1, 'Emperor', 'General', 5000.0), (2, 'Rahim', 'Colonel', 4000.0), (3, 'Karim', 'Private', 2000.0)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, rank TEXT, salary REAL);",
        "INSERT INTO soldiers (name, rank, salary) VALUES (?,?,?), (?,?,?), (?,?,?);",
        "-- Engine supplies: Emperor, General, 5000, Rahim, Colonel, 4000, Karim, Private, 2000",
        "SELECT * FROM soldiers ORDER BY id;"
    ]
)

hard2 = Task(
    description=(
        "🧱  Full CRUD with Parameters – Secure Application\n\n"
        "Create a table `products` with columns:\n"
        "  • id INTEGER PRIMARY KEY\n"
        "  • name TEXT NOT NULL\n"
        "  • price REAL CHECK(price > 0)\n"
        "  • stock INTEGER DEFAULT 0\n\n"
        "Write parameterized statements for:\n"
        "  1. INSERT a new product (name, price, stock)\n"
        "  2. SELECT products with stock below a threshold (?) \n"
        "  3. UPDATE price of a product by id (new_price, id)\n"
        "  4. DELETE a product by id (?)\n\n"
        "First INSERT three products. Then SELECT low stock\n"
        "(threshold 50). Then UPDATE a price. Then DELETE\n"
        "a product. Show final table.\n\n"
        "Expected output:\n[(2,'Mouse',60.0,25), (3,'Keyboard',80.0,60)]"
    ),
    expected_output="[(2, 'Mouse', 60.0, 25), (3, 'Keyboard', 80.0, 60)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, price REAL CHECK(price > 0), stock INTEGER DEFAULT 0);",
        "INSERT INTO products (name, price, stock) VALUES (?,?,?), (?,?,?), (?,?,?);",
        "-- Insert: Laptop,1000,50, Mouse,50,25, Keyboard,80,60",
        "SELECT name, price, stock FROM products WHERE stock < ?;",
        "-- Select with threshold 50: shows Mouse",
        "UPDATE products SET price = ? WHERE id = ?;",
        "-- Update Mouse price from 50 to 60",
        "DELETE FROM products WHERE id = ?;",
        "-- Delete Laptop (id=1)",
        "SELECT * FROM products ORDER BY id;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L65.json",
        module_name="Module_07_Views_Optimization_Security",
        lesson_name="L65_Preventing_SQL_Injection"
    )
