import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "📊  CASE in ORDER BY – Custom Sort\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Return name, rank, and salary, sorted by\n"
        "a custom rank order (General first, then\n"
        "Colonel, then Private).\n"
        "Use CASE inside ORDER BY.\n\n"
        "Expected output:\n[('Emperor','General',5000.0), ('Ali','General',4500.0), ('Rahim','Colonel',4000.0), ('Hasan','Colonel',3500.0), ('Karim','Private',2000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[('Emperor', 'General', 5000.0), ('Ali', 'General', 4500.0), ('Rahim', 'Colonel', 4000.0), ('Hasan', 'Colonel', 3500.0), ('Karim', 'Private', 2000.0)]",
    level=Level.EASY,
    hints=[
        "SELECT name, rank, salary FROM soldiers ORDER BY CASE rank WHEN 'General' THEN 1 WHEN 'Colonel' THEN 2 WHEN 'Private' THEN 3 ELSE 4 END;"
    ]
)

easy2 = Task(
    description=(
        "📋  CASE in GROUP BY – Pay Brackets\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Group soldiers into pay brackets and count\n"
        "how many fall into each:\n"
        "  • salary >= 4500 → 'Top Tier'\n"
        "  • salary >= 3500 → 'Mid Tier'\n"
        "  • ELSE → 'Entry Tier'\n"
        "Return the bracket name and count.\n"
        "Sort by count descending.\n\n"
        "Expected output:\n[('Mid Tier',2), ('Top Tier',2), ('Entry Tier',1)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[('Mid Tier', 2), ('Top Tier', 2), ('Entry Tier', 1)]",
    level=Level.EASY,
    hints=[
        "SELECT CASE WHEN salary >= 4500 THEN 'Top Tier' WHEN salary >= 3500 THEN 'Mid Tier' ELSE 'Entry Tier' END AS bracket, COUNT(*) AS count FROM soldiers GROUP BY bracket ORDER BY count DESC;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🗂️  CASE in GROUP BY – Dynamic Categories\n\n"
        "Create a table `products` with columns:\n"
        "  id INTEGER, name TEXT, category TEXT, price REAL.\n"
        "Insert 6 products with varied prices.\n"
        "Group products by a CASE expression that\n"
        "creates price ranges:\n"
        "  • price >= 100 → 'Premium'\n"
        "  • price >= 50 → 'Standard'\n"
        "  • ELSE → 'Budget'\n"
        "Return range name, product count, and\n"
        "average price per range, sorted by avg price desc.\n\n"
        "Expected output:\n[('Premium',2,225.0), ('Standard',2,67.5), ('Budget',2,22.5)]"
    ),
    expected_output="[('Premium', 2, 225.0), ('Standard', 2, 67.5), ('Budget', 2, 22.5)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE products (id INTEGER, name TEXT, category TEXT, price REAL);",
        "INSERT INTO products VALUES (1,'Laptop','Electronics',250.0), (2,'Mouse','Electronics',25.0), (3,'Desk','Furniture',200.0), (4,'Pen','Office',20.0), (5,'Keyboard','Electronics',60.0), (6,'Chair','Furniture',75.0);",
        "SELECT CASE WHEN price >= 100 THEN 'Premium' WHEN price >= 50 THEN 'Standard' ELSE 'Budget' END AS range_name, COUNT(*) AS count, AVG(price) AS avg_price FROM products GROUP BY range_name ORDER BY avg_price DESC;"
    ]
)

medium2 = Task(
    description=(
        "📐  Multi‑Level ORDER BY with CASE\n\n"
        "The `shipments` table has 5 rows.\n"
        "Return all columns, sorted first by\n"
        "priority (High=1, Medium=2, Low=3),\n"
        "then by status (delayed=1, pending=2,\n"
        "delivered=3).\n"
        "Use CASE in both ORDER BY clauses.\n\n"
        "Expected output:\n[('TRK-1','High','delayed'), ('TRK-5','High','pending'), ('TRK-2','Medium','delayed'), ('TRK-3','Low','delivered'), ('TRK-4','Low','delayed')]"
    ),
    setup_sql=(
        "CREATE TABLE shipments (id TEXT, priority TEXT, status TEXT, weight REAL);"
        "INSERT INTO shipments VALUES ('TRK-1','High','delayed',12.5), ('TRK-2','Medium','delayed',8.0), ('TRK-3','Low','delivered',5.2), ('TRK-4','Low','delayed',3.1), ('TRK-5','High','pending',10.0);"
    ),
    expected_output="[('TRK-1', 'High', 'delayed'), ('TRK-5', 'High', 'pending'), ('TRK-2', 'Medium', 'delayed'), ('TRK-3', 'Low', 'delivered'), ('TRK-4', 'Low', 'delayed')]",
    level=Level.MEDIUM,
    hints=[
        "SELECT id, priority, status FROM shipments ORDER BY CASE priority WHEN 'High' THEN 1 WHEN 'Medium' THEN 2 WHEN 'Low' THEN 3 END, CASE status WHEN 'delayed' THEN 1 WHEN 'pending' THEN 2 WHEN 'delivered' THEN 3 END;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  CASE in WHERE – Conditional Filter\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Use CASE inside WHERE to apply different\n"
        "filters based on rank:\n"
        "  • For Generals: salary > 4500\n"
        "  • For Colonels: salary > 3500\n"
        "  • For others: salary > 1000\n"
        "Return name, rank, and salary.\n\n"
        "Expected output:\n[('Emperor','General',5000.0), ('Rahim','Colonel',4000.0), ('Karim','Private',2000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[('Emperor', 'General', 5000.0), ('Rahim', 'Colonel', 4000.0), ('Karim', 'Private', 2000.0)]",
    level=Level.HARD,
    hints=[
        "SELECT name, rank, salary FROM soldiers WHERE CASE WHEN rank = 'General' THEN salary > 4500 WHEN rank = 'Colonel' THEN salary > 3500 ELSE salary > 1000 END;"
    ]
)

hard2 = Task(
    description=(
        "📊  CASE + Aggregates – Conditional Summary\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Write a single query that returns:\n"
        "  • total: COUNT(*)\n"
        "  • generals: COUNT(CASE WHEN rank='General' THEN 1 END)\n"
        "  • high_paid: COUNT(CASE WHEN salary>4000 THEN 1 END)\n"
        "  • avg_general_salary: AVG(CASE WHEN rank='General' THEN salary END)\n\n"
        "Expected output: [(5, 2, 2, 4750.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[(5, 2, 2, 4750.0)]",
    level=Level.HARD,
    hints=[
        "SELECT COUNT(*) AS total, COUNT(CASE WHEN rank='General' THEN 1 END) AS generals, COUNT(CASE WHEN salary > 4000 THEN 1 END) AS high_paid, AVG(CASE WHEN rank='General' THEN salary END) AS avg_general_salary FROM soldiers;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L16.json",
        module_name="Module_02_Filtering_Conditional_Logic",
        lesson_name="L16_CASE_in_Clauses"
    )
