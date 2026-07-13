import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🪖  Simple CASE – Rank Labels\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Use a simple CASE to return name, rank,\n"
        "and a new column `category`:\n"
        "  • 'General' → 'Top Brass'\n"
        "  • 'Colonel' → 'Senior Officer'\n"
        "  • 'Private' → 'Enlisted'\n"
        "  • ELSE → 'Other'\n"
        "Sort by name.\n\n"
        "Expected output:\n[('Ali','General','Top Brass'), ('Emperor','General','Top Brass'), ('Hasan','Colonel','Senior Officer'), ('Karim','Private','Enlisted'), ('Rahim','Colonel','Senior Officer')]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[('Ali', 'General', 'Top Brass'), ('Emperor', 'General', 'Top Brass'), ('Hasan', 'Colonel', 'Senior Officer'), ('Karim', 'Private', 'Enlisted'), ('Rahim', 'Colonel', 'Senior Officer')]",
    level=Level.EASY,
    hints=[
        "SELECT name, rank, CASE rank WHEN 'General' THEN 'Top Brass' WHEN 'Colonel' THEN 'Senior Officer' WHEN 'Private' THEN 'Enlisted' ELSE 'Other' END AS category FROM soldiers ORDER BY name;"
    ]
)

easy2 = Task(
    description=(
        "📊  Simple CASE – Product Type\n\n"
        "Create a table `inventory` with columns\n"
        "  id INTEGER, item TEXT, category TEXT.\n"
        "Insert 4 items.\n"
        "Use a simple CASE on `category` to label:\n"
        "  • 'Weapons' → 'Arsenal'\n"
        "  • 'Armor' → 'Defense'\n"
        "  • 'Food' → 'Supplies'\n"
        "  • ELSE → 'Misc'\n"
        "Return item, category, and the label, sorted by item.\n\n"
        "Expected output:\n[('Bow','Weapons','Arsenal'), ('Helm','Armor','Defense'), ('Rations','Food','Supplies'), ('Sword','Weapons','Arsenal')]"
    ),
    expected_output="[('Bow', 'Weapons', 'Arsenal'), ('Helm', 'Armor', 'Defense'), ('Rations', 'Food', 'Supplies'), ('Sword', 'Weapons', 'Arsenal')]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE inventory (id INTEGER, item TEXT, category TEXT);",
        "INSERT INTO inventory VALUES (1,'Sword','Weapons'), (2,'Helm','Armor'), (3,'Rations','Food'), (4,'Bow','Weapons');",
        "SELECT item, category, CASE category WHEN 'Weapons' THEN 'Arsenal' WHEN 'Armor' THEN 'Defense' WHEN 'Food' THEN 'Supplies' ELSE 'Misc' END AS label FROM inventory ORDER BY item;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "💰  Searched CASE – Salary Band\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Use a searched CASE to return name, salary,\n"
        "and a new column `pay_band`:\n"
        "  • salary >= 5000 → 'High'\n"
        "  • salary >= 4000 → 'Medium'\n"
        "  • ELSE → 'Low'\n"
        "Sort by salary descending.\n\n"
        "Expected output:\n[('Emperor',5000.0,'High'), ('Ali',4500.0,'Medium'), ('Rahim',4000.0,'Medium'), ('Hasan',3500.0,'Low'), ('Karim',2000.0,'Low')]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[('Emperor', 5000.0, 'High'), ('Ali', 4500.0, 'Medium'), ('Rahim', 4000.0, 'Medium'), ('Hasan', 3500.0, 'Low'), ('Karim', 2000.0, 'Low')]",
    level=Level.MEDIUM,
    hints=[
        "SELECT name, salary, CASE WHEN salary >= 5000 THEN 'High' WHEN salary >= 4000 THEN 'Medium' ELSE 'Low' END AS pay_band FROM soldiers ORDER BY salary DESC;"
    ]
)

medium2 = Task(
    description=(
        "📦  Stock Status – Searched CASE\n\n"
        "Create a table `warehouse` with columns\n"
        "  id INTEGER, product TEXT, qty INTEGER.\n"
        "Insert 5 rows with varied quantities.\n"
        "Return product, qty, and a `status` column:\n"
        "  • qty = 0 → 'Out of Stock'\n"
        "  • qty < 10 → 'Low Stock'\n"
        "  • qty < 30 → 'Moderate'\n"
        "  • ELSE → 'Well Stocked'\n"
        "Sort by qty ascending.\n\n"
        "Expected output:\n[('Arrow',0,'Out of Stock'), ('Shield',5,'Low Stock'), ('Sword',15,'Moderate'), ('Bow',25,'Moderate'), ('Rations',50,'Well Stocked')]"
    ),
    expected_output="[('Arrow', 0, 'Out of Stock'), ('Shield', 5, 'Low Stock'), ('Sword', 15, 'Moderate'), ('Bow', 25, 'Moderate'), ('Rations', 50, 'Well Stocked')]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE warehouse (id INTEGER, product TEXT, qty INTEGER);",
        "INSERT INTO warehouse VALUES (1,'Sword',15), (2,'Shield',5), (3,'Arrow',0), (4,'Bow',25), (5,'Rations',50);",
        "SELECT product, qty, CASE WHEN qty = 0 THEN 'Out of Stock' WHEN qty < 10 THEN 'Low Stock' WHEN qty < 30 THEN 'Moderate' ELSE 'Well Stocked' END AS status FROM warehouse ORDER BY qty;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  Complex CASE – Multi‑Column Condition\n\n"
        "Create a table `shipments` with columns:\n"
        "  id INTEGER, priority TEXT, status TEXT, weight REAL.\n"
        "Insert 6 varied rows.\n"
        "Return id, priority, status, and a `handling` column:\n"
        "  • priority='high' AND status='delayed' → 'Critical'\n"
        "  • priority='high' → 'Rush'\n"
        "  • status='delayed' → 'Follow Up'\n"
        "  • ELSE → 'Standard'\n"
        "Sort by id.\n\n"
        "Expected output:\n[(1,'high','delayed','Critical'), (2,'high','in transit','Rush'), (3,'low','delayed','Follow Up'), (4,'low','in transit','Standard'), (5,'high','delivered','Rush'), (6,'low','delivered','Standard')]"
    ),
    expected_output="[('high', 'delayed', 'Critical'), ('high', 'in transit', 'Rush'), ('low', 'delayed', 'Follow Up'), ('low', 'in transit', 'Standard'), ('high', 'delivered', 'Rush'), ('low', 'delivered', 'Standard')]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE shipments (id INTEGER, priority TEXT, status TEXT, weight REAL);",
        "INSERT INTO shipments VALUES (1,'high','delayed',12.5), (2,'high','in transit',8.0), (3,'low','delayed',5.2), (4,'low','in transit',3.1), (5,'high','delivered',10.0), (6,'low','delivered',2.0);",
        "SELECT priority, status, CASE WHEN priority='high' AND status='delayed' THEN 'Critical' WHEN priority='high' THEN 'Rush' WHEN status='delayed' THEN 'Follow Up' ELSE 'Standard' END AS handling FROM shipments ORDER BY id;"
    ]
)

hard2 = Task(
    description=(
        "📊  CASE in ORDER BY – Custom Sort\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Return name, rank, and salary, but sort\n"
        "by a custom rank priority (not alphabetical).\n"
        "Use CASE inside ORDER BY:\n"
        "  • 'General' → 1\n"
        "  • 'Colonel' → 2\n"
        "  • 'Private' → 3\n"
        "  • ELSE → 4\n"
        "Expected output:\n[('Emperor','General',5000.0), ('Ali','General',4500.0), ('Rahim','Colonel',4000.0), ('Hasan','Colonel',3500.0), ('Karim','Private',2000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[('Emperor', 'General', 5000.0), ('Ali', 'General', 4500.0), ('Rahim', 'Colonel', 4000.0), ('Hasan', 'Colonel', 3500.0), ('Karim', 'Private', 2000.0)]",
    level=Level.HARD,
    hints=[
        "SELECT name, rank, salary FROM soldiers ORDER BY CASE rank WHEN 'General' THEN 1 WHEN 'Colonel' THEN 2 WHEN 'Private' THEN 3 ELSE 4 END;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L15.json",
        module_name="Module_02_Filtering_Conditional_Logic",
        lesson_name="L15_CASE_Simple_Searched"
    )
