import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🔗  AND – Electronics in Stock\n\n"
        "Create a table `products` with columns:\n"
        "  • id INTEGER, name TEXT, category TEXT, stock INTEGER.\n"
        "Insert 4 products.\n"
        "Return name and stock for products that are\n"
        "BOTH in the 'Electronics' category AND have stock > 0.\n\n"
        "Expected output:\n[('Laptop',10), ('Mouse',50)]"
    ),
    expected_output="[('Laptop', 10), ('Mouse', 50)]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE products (id INTEGER, name TEXT, category TEXT, stock INTEGER);",
        "INSERT INTO products VALUES (1,'Laptop','Electronics',10), (2,'Desk','Furniture',5), (3,'Mouse','Electronics',50), (4,'Chair','Furniture',0);",
        "SELECT name, stock FROM products WHERE category = 'Electronics' AND stock > 0;"
    ]
)

easy2 = Task(
    description=(
        "🔀  OR – Electronics or Furniture\n\n"
        "The same `products` table.\n"
        "Return name and category for products that are\n"
        "EITHER Electronics OR Furniture.\n\n"
        "Expected output:\n[('Laptop','Electronics'), ('Desk','Furniture'), ('Mouse','Electronics'), ('Chair','Furniture')]"
    ),
    setup_sql=(
        "CREATE TABLE products (id INTEGER, name TEXT, category TEXT, stock INTEGER);"
        "INSERT INTO products VALUES (1,'Laptop','Electronics',10), (2,'Desk','Furniture',5), (3,'Mouse','Electronics',50), (4,'Chair','Furniture',0);"
    ),
    expected_output="[('Laptop', 'Electronics'), ('Desk', 'Furniture'), ('Mouse', 'Electronics'), ('Chair', 'Furniture')]",
    level=Level.EASY,
    hints=[
        "SELECT name, category FROM products WHERE category = 'Electronics' OR category = 'Furniture';"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🚫  NOT – Exclude Category\n\n"
        "The `products` table has 4 rows.\n"
        "Return name and category for products that\n"
        "are NOT in the 'Furniture' category.\n\n"
        "Expected output:\n[('Laptop','Electronics'), ('Mouse','Electronics')]"
    ),
    setup_sql=(
        "CREATE TABLE products (id INTEGER, name TEXT, category TEXT, stock INTEGER);"
        "INSERT INTO products VALUES (1,'Laptop','Electronics',10), (2,'Desk','Furniture',5), (3,'Mouse','Electronics',50), (4,'Chair','Furniture',0);"
    ),
    expected_output="[('Laptop', 'Electronics'), ('Mouse', 'Electronics')]",
    level=Level.MEDIUM,
    hints=[
        "SELECT name, category FROM products WHERE NOT category = 'Furniture';"
    ]
)

medium2 = Task(
    description=(
        "🧠  AND + OR – Complex Filter\n\n"
        "The `products` table has 4 rows.\n"
        "Return name, category, and stock for products\n"
        "where (category = 'Electronics' OR category = 'Furniture')\n"
        "AND stock > 0.\n\n"
        "Expected output:\n[('Laptop','Electronics',10), ('Desk','Furniture',5), ('Mouse','Electronics',50)]"
    ),
    setup_sql=(
        "CREATE TABLE products (id INTEGER, name TEXT, category TEXT, stock INTEGER);"
        "INSERT INTO products VALUES (1,'Laptop','Electronics',10), (2,'Desk','Furniture',5), (3,'Mouse','Electronics',50), (4,'Chair','Furniture',0);"
    ),
    expected_output="[('Laptop', 'Electronics', 10), ('Desk', 'Furniture', 5), ('Mouse', 'Electronics', 50)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT name, category, stock FROM products WHERE (category = 'Electronics' OR category = 'Furniture') AND stock > 0;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🛡️  Soldier Filter – Multiple AND\n\n"
        "Create a table `soldiers` with columns:\n"
        "  id INTEGER, name TEXT, rank TEXT, status TEXT, salary REAL.\n"
        "Insert 5 rows with varied ranks and statuses.\n"
        "Return name, rank, salary for soldiers who:\n"
        "  • status = 'active'\n"
        "  • rank = 'General' OR 'Colonel' (use IN)\n"
        "  • salary > 4000\n"
        "Sort by salary descending.\n\n"
        "Expected output:\n[('Emperor','General',5000.0), ('Ali','General',4500.0)]"
    ),
    expected_output="[('Emperor', 'General', 5000.0), ('Ali', 'General', 4500.0)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, status TEXT, salary REAL);",
        "INSERT INTO soldiers VALUES (1,'Emperor','General','active',5000), (2,'Rahim','Colonel','reserve',4000), (3,'Karim','Private','active',2000), (4,'Ali','General','active',4500), (5,'Hasan','Colonel','active',3500);",
        "SELECT name, rank, salary FROM soldiers WHERE status = 'active' AND rank IN ('General','Colonel') AND salary > 4000 ORDER BY salary DESC;"
    ]
)

hard2 = Task(
    description=(
        "⚠️  NOT + AND – Exclude with Conditions\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Return name, rank, and status for soldiers\n"
        "who are NOT Privates AND are active.\n"
        "Also exclude anyone with salary < 3000.\n"
        "Sort by rank (custom: General=1, Colonel=2, Major=3).\n\n"
        "Expected output:\n[('Emperor','General','active'), ('Ali','General','active'), ('Hasan','Colonel','active')]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, status TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General','active',5000), (2,'Rahim','Colonel','reserve',4000), (3,'Karim','Private','active',2000), (4,'Ali','General','active',4500), (5,'Hasan','Colonel','active',3500);"
    ),
    expected_output="[('Emperor', 'General', 'active'), ('Ali', 'General', 'active'), ('Hasan', 'Colonel', 'active')]",
    level=Level.HARD,
    hints=[
        "SELECT name, rank, status FROM soldiers WHERE NOT rank = 'Private' AND status = 'active' AND salary >= 3000 ORDER BY CASE rank WHEN 'General' THEN 1 WHEN 'Colonel' THEN 2 ELSE 3 END;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L11.json",
        module_name="Module_02_Filtering_Conditional_Logic",
        lesson_name="L11_AND_OR_NOT"
    )
