import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "📏  BETWEEN – Salary Range\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Return name and salary for soldiers\n"
        "whose salary is between 3000 and 5000 (inclusive).\n"
        "Sort by salary ascending.\n\n"
        "Expected output:\n[('Hasan',3500.0), ('Rahim',4000.0), ('Ali',4500.0), ('Emperor',5000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[('Hasan', 3500.0), ('Rahim', 4000.0), ('Ali', 4500.0), ('Emperor', 5000.0)]",
    level=Level.EASY,
    hints=[
        "SELECT name, salary FROM soldiers WHERE salary BETWEEN 3000 AND 5000 ORDER BY salary;"
    ]
)

easy2 = Task(
    description=(
        "📋  IN – Specific Ranks\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Return name and rank for soldiers\n"
        "whose rank is General, Colonel, or Major.\n"
        "Sort by name alphabetically.\n\n"
        "Expected output:\n[('Ali','General'), ('Emperor','General'), ('Hasan','Colonel'), ('Rahim','Colonel')]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[('Ali', 'General'), ('Emperor', 'General'), ('Hasan', 'Colonel'), ('Rahim', 'Colonel')]",
    level=Level.EASY,
    hints=[
        "SELECT name, rank FROM soldiers WHERE rank IN ('General','Colonel','Major') ORDER BY name;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🔍  LIKE – Names Starting with 'A'\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Return name and rank for soldiers\n"
        "whose name starts with the letter 'A'.\n\n"
        "Expected output:\n[('Ali','General')]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[('Ali', 'General')]",
    level=Level.MEDIUM,
    hints=[
        "SELECT name, rank FROM soldiers WHERE name LIKE 'A%';"
    ]
)

medium2 = Task(
    description=(
        "📅  BETWEEN with Dates – Registrations\n\n"
        "Create a table `registrations` with columns:\n"
        "  id INTEGER, citizen TEXT, reg_date TEXT.\n"
        "Insert 4 rows with different dates.\n"
        "Return citizen and reg_date for registrations\n"
        "between '2026-02-01' and '2026-06-30' inclusive.\n"
        "Sort by reg_date.\n\n"
        "Expected output:\n[('Rahim','2026-03-15'), ('Karim','2026-05-20')]"
    ),
    expected_output="[('Rahim', '2026-03-15'), ('Karim', '2026-05-20')]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE registrations (id INTEGER, citizen TEXT, reg_date TEXT);",
        "INSERT INTO registrations VALUES (1,'Emperor','2026-01-10'), (2,'Rahim','2026-03-15'), (3,'Karim','2026-05-20'), (4,'Ali','2026-07-01');",
        "SELECT citizen, reg_date FROM registrations WHERE reg_date BETWEEN '2026-02-01' AND '2026-06-30' ORDER BY reg_date;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  LIKE with Pattern – 5-Letter Names\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Return the names of soldiers whose name\n"
        "has exactly 5 characters.\n"
        "Use the underscore wildcard `_`.\n\n"
        "Expected output:\n[('Rahim',)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[('Rahim',)]",
    level=Level.HARD,
    hints=[
        "SELECT name FROM soldiers WHERE name LIKE '_____';"
    ]
)

hard2 = Task(
    description=(
        "🔎  Combined Filter – LIKE + BETWEEN + IN\n\n"
        "Create a table `inventory` with columns:\n"
        "  id INTEGER, item TEXT, category TEXT, qty INTEGER, price REAL.\n"
        "Insert 6 varied rows.\n"
        "Return item and price for products where:\n"
        "  • item starts with 'S' (LIKE)\n"
        "  • price between 100 and 500 (BETWEEN)\n"
        "  • category IN ('Weapons','Armor')\n"
        "Sort by price descending.\n\n"
        "Expected output:\n[('Steel Sword',250.0), ('Silver Shield',150.0)]"
    ),
    expected_output="[('Steel Sword', 250.0), ('Silver Shield', 150.0)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE inventory (id INTEGER, item TEXT, category TEXT, qty INTEGER, price REAL);",
        "INSERT INTO inventory VALUES (1,'Steel Sword','Weapons',10,250.0), (2,'Iron Shield','Armor',5,80.0), (3,'Silver Shield','Armor',3,150.0), (4,'Gold Helm','Armor',2,600.0), (5,'Short Bow','Weapons',8,90.0), (6,'Stone Axe','Weapons',12,50.0);",
        "SELECT item, price FROM inventory WHERE item LIKE 'S%' AND price BETWEEN 100 AND 500 AND category IN ('Weapons','Armor') ORDER BY price DESC;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L12.json",
        module_name="Module_02_Filtering_Conditional_Logic",
        lesson_name="L12_BETWEEN_IN_LIKE"
    )
