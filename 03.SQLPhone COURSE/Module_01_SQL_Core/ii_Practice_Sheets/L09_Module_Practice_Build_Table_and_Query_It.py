import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🏗️  Imperial Warehouse – Create & Seed\n\n"
        "Create a table `warehouse` with columns:\n"
        "  • id INTEGER PRIMARY KEY\n"
        "  • product TEXT NOT NULL\n"
        "  • qty INTEGER CHECK(qty >= 0)\n\n"
        "Insert three products:\n"
        "  (1, 'Shield', 10)\n"
        "  (2, 'Sword', 25)\n"
        "  (3, 'Bow', 15)\n"
        "SELECT all rows.\n\n"
        "Expected output:\n[(1,'Shield',10), (2,'Sword',25), (3,'Bow',15)]"
    ),
    expected_output="[(1, 'Shield', 10), (2, 'Sword', 25), (3, 'Bow', 15)]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE warehouse (id INTEGER PRIMARY KEY, product TEXT NOT NULL, qty INTEGER CHECK(qty >= 0));",
        "INSERT INTO warehouse VALUES (1,'Shield',10), (2,'Sword',25), (3,'Bow',15);",
        "SELECT * FROM warehouse;"
    ]
)

easy2 = Task(
    description=(
        "🔍  Stock Check – Basic Filter\n\n"
        "The `warehouse` table has three items.\n"
        "Write a query that returns the product\n"
        "and quantity for items where the quantity\n"
        "is less than 20.\n\n"
        "Expected output:\n[('Shield',10), ('Bow',15)]"
    ),
    setup_sql=(
        "CREATE TABLE warehouse (id INTEGER PRIMARY KEY, product TEXT NOT NULL, qty INTEGER CHECK(qty >= 0));"
        "INSERT INTO warehouse VALUES (1,'Shield',10), (2,'Sword',25), (3,'Bow',15);"
    ),
    expected_output="[('Shield', 10), ('Bow', 15)]",
    level=Level.EASY,
    hints=[
        "SELECT product, qty FROM warehouse WHERE qty < 20;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "📊  Stock Value Report – Computed Column\n\n"
        "The `warehouse` table has a new column:\n"
        "  • price REAL\n\n"
        "The table is seeded with three items.\n"
        "Write a query that returns the product name,\n"
        "quantity, price, and the total value\n"
        "(qty * price) as an alias `total_value`,\n"
        "sorted by total_value descending.\n\n"
        "Expected output:\n[('Sword',25,50.0,1250.0), ('Bow',15,30.0,450.0), ('Shield',10,20.0,200.0)]"
    ),
    setup_sql=(
        "CREATE TABLE warehouse (id INTEGER PRIMARY KEY, product TEXT NOT NULL, qty INTEGER CHECK(qty >= 0), price REAL);"
        "INSERT INTO warehouse VALUES (1,'Shield',10,20.0), (2,'Sword',25,50.0), (3,'Bow',15,30.0);"
    ),
    expected_output="[('Sword', 25, 50.0, 1250.0), ('Bow', 15, 30.0, 450.0), ('Shield', 10, 20.0, 200.0)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT product, qty, price, qty * price AS total_value FROM warehouse ORDER BY total_value DESC;"
    ]
)

medium2 = Task(
    description=(
        "📋  Restock Alert – Filter & Sort\n\n"
        "The `warehouse` table has three items.\n"
        "Write a query that returns product and qty\n"
        "for items where qty <= 15,\n"
        "sorted by qty ascending.\n\n"
        "Expected output:\n[('Shield',10), ('Bow',15)]"
    ),
    setup_sql=(
        "CREATE TABLE warehouse (id INTEGER PRIMARY KEY, product TEXT NOT NULL, qty INTEGER CHECK(qty >= 0));"
        "INSERT INTO warehouse VALUES (1,'Shield',10), (2,'Sword',25), (3,'Bow',15);"
    ),
    expected_output="[('Shield', 10), ('Bow', 15)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT product, qty FROM warehouse WHERE qty <= 15 ORDER BY qty ASC;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧱  Build & Query – Full Workflow\n\n"
        "Create a table `barracks` with columns:\n"
        "  • id INTEGER PRIMARY KEY\n"
        "  • name TEXT NOT NULL\n"
        "  • regiment_id INTEGER\n"
        "  • joined TEXT DEFAULT (date('now'))\n\n"
        "Insert four soldiers with varied\n"
        "regiment assignments and join dates.\n"
        "Then SELECT name, regiment_id, joined\n"
        "for soldiers who joined after '2026-06-01',\n"
        "sorted by joined ascending.\n\n"
        "Expected output:\n[('Ali',2,'2026-06-15'), ('Fatima',3,'2026-07-01')]"
    ),
    expected_output="[('Ali', 2, '2026-06-15'), ('Fatima', 3, '2026-07-01')]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE barracks (id INTEGER PRIMARY KEY, name TEXT NOT NULL, regiment_id INTEGER, joined TEXT DEFAULT (date('now')));",
        "INSERT INTO barracks VALUES (1,'Emperor',1,'2026-01-10'), (2,'Rahim',1,'2026-03-20'), (3,'Ali',2,'2026-06-15'), (4,'Fatima',3,'2026-07-01');",
        "SELECT name, regiment_id, joined FROM barracks WHERE joined > '2026-06-01' ORDER BY joined ASC;"
    ]
)

hard2 = Task(
    description=(
        "📊  Aggregate Preview – Count by Regiment\n\n"
        "The `barracks` table has four soldiers.\n"
        "Write a query that groups by regiment_id\n"
        "and returns the regiment_id and the number\n"
        "of soldiers in each regiment (as `count`),\n"
        "sorted by count descending.\n\n"
        "Expected output:\n[(1,2), (2,1), (3,1)]"
    ),
    setup_sql=(
        "CREATE TABLE barracks (id INTEGER PRIMARY KEY, name TEXT NOT NULL, regiment_id INTEGER, joined TEXT);"
        "INSERT INTO barracks VALUES (1,'Emperor',1,'2026-01-10'), (2,'Rahim',1,'2026-03-20'), (3,'Ali',2,'2026-06-15'), (4,'Fatima',3,'2026-07-01');"
    ),
    expected_output="[(1, 2), (2, 1), (3, 1)]",
    level=Level.HARD,
    hints=[
        "SELECT regiment_id, COUNT(*) AS count FROM barracks GROUP BY regiment_id ORDER BY count DESC;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L09.json",
        module_name="Module_01_SQL_Core",
        lesson_name="L09_Module_Practice"
    )
