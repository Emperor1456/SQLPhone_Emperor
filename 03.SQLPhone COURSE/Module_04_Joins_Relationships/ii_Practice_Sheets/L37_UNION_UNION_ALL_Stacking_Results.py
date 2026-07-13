import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "➕  UNION ALL – Combine Two Lists\n\n"
        "The `active_soldiers` table has 3 rows.\n"
        "The `reserve_soldiers` table has 2 rows.\n"
        "Write a query using UNION ALL to combine both tables\n"
        "into a single list of soldier names.\n"
        "Sort the result alphabetically.\n\n"
        "Expected output:\n[('Ali',), ('Emperor',), ('Fatima',), ('Hasan',), ('Rahim',)]"
    ),
    setup_sql=(
        "CREATE TABLE active_soldiers (name TEXT);"
        "INSERT INTO active_soldiers VALUES ('Emperor'), ('Ali'), ('Fatima');"
        "CREATE TABLE reserve_soldiers (name TEXT);"
        "INSERT INTO reserve_soldiers VALUES ('Rahim'), ('Hasan');"
    ),
    expected_output="[('Ali',), ('Emperor',), ('Fatima',), ('Hasan',), ('Rahim',)]",
    level=Level.EASY,
    hints=[
        "SELECT name FROM active_soldiers UNION ALL SELECT name FROM reserve_soldiers ORDER BY name;"
    ]
)

easy2 = Task(
    description=(
        "🏷️  UNION with Source Label – Identify Origin\n\n"
        "The same `active_soldiers` and `reserve_soldiers` tables exist.\n"
        "Write a query that returns each soldier's name and a\n"
        "literal column 'status' indicating 'active' or 'reserve'.\n"
        "Use UNION ALL with literal strings.\n"
        "Sort by name.\n\n"
        "Expected output:\n[('Ali','active'), ('Emperor','active'), ('Fatima','active'), ('Hasan','reserve'), ('Rahim','reserve')]"
    ),
    setup_sql=(
        "CREATE TABLE active_soldiers (name TEXT);"
        "INSERT INTO active_soldiers VALUES ('Emperor'), ('Ali'), ('Fatima');"
        "CREATE TABLE reserve_soldiers (name TEXT);"
        "INSERT INTO reserve_soldiers VALUES ('Rahim'), ('Hasan');"
    ),
    expected_output="[('Ali', 'active'), ('Emperor', 'active'), ('Fatima', 'active'), ('Hasan', 'reserve'), ('Rahim', 'reserve')]",
    level=Level.EASY,
    hints=[
        "SELECT name, 'active' AS status FROM active_soldiers UNION ALL SELECT name, 'reserve' AS status FROM reserve_soldiers ORDER BY name;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🧹  UNION vs UNION ALL – Duplicate Removal\n\n"
        "Create two tables with overlapping names.\n"
        "Write TWO queries:\n"
        "  1. UNION ALL (keeps duplicates)\n"
        "  2. UNION (removes duplicates)\n"
        "The test expects the output of the UNION (deduplicated) version.\n"
        "Sort the result.\n\n"
        "Expected output (UNION – no duplicates):\n[('Ali',), ('Emperor',), ('Hasan',), ('Rahim',)]"
    ),
    expected_output="[('Ali',), ('Emperor',), ('Hasan',), ('Rahim',)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE unit_a (name TEXT);",
        "INSERT INTO unit_a VALUES ('Emperor'), ('Ali'), ('Rahim');",
        "CREATE TABLE unit_b (name TEXT);",
        "INSERT INTO unit_b VALUES ('Rahim'), ('Hasan'), ('Ali');",
        "SELECT name FROM unit_a UNION SELECT name FROM unit_b ORDER BY name;"
    ]
)

medium2 = Task(
    description=(
        "📊  UNION ALL + Aggregation – Total Count\n\n"
        "Create a table `sales_north` and `sales_south` with\n"
        "identical columns (product TEXT, amount REAL).\n"
        "Insert 3 rows in each.\n"
        "Use UNION ALL to combine them, then wrap the whole\n"
        "thing in a subquery to compute SUM(amount) and COUNT(*)\n"
        "across all regions.\n\n"
        "Expected output: [(6, 1550.0)]"
    ),
    expected_output="[(6, 1550.0)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE sales_north (product TEXT, amount REAL);",
        "INSERT INTO sales_north VALUES ('Laptop',500), ('Mouse',200), ('Keyboard',300);",
        "CREATE TABLE sales_south (product TEXT, amount REAL);",
        "INSERT INTO sales_south VALUES ('Monitor',400), ('Desk',100), ('Chair',50);",
        "SELECT COUNT(*) AS total_orders, SUM(amount) AS total_revenue FROM (SELECT amount FROM sales_north UNION ALL SELECT amount FROM sales_south);"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  UNION ALL with Different Columns – Full Personnel Roster\n\n"
        "Create `officers` table (name, rank, salary) and\n"
        "`enlisted` table (name, rank).\n"
        "Write a UNION ALL query that returns a unified roster\n"
        "with columns: name, rank, salary.\n"
        "For enlisted (who have no salary), show NULL for salary.\n"
        "Add a `role` column: 'Officer' or 'Enlisted'.\n"
        "Sort by role, then name.\n\n"
        "Expected output:\n[('Ali','Private',NULL,'Enlisted'), ('Hasan','Corporal',NULL,'Enlisted'), ('Emperor','General',5000.0,'Officer'), ('Rahim','Colonel',4000.0,'Officer')]"
    ),
    expected_output="[('Ali', 'Private', None, 'Enlisted'), ('Hasan', 'Corporal', None, 'Enlisted'), ('Emperor', 'General', 5000.0, 'Officer'), ('Rahim', 'Colonel', 4000.0, 'Officer')]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE officers (name TEXT, rank TEXT, salary REAL);",
        "INSERT INTO officers VALUES ('Emperor','General',5000), ('Rahim','Colonel',4000);",
        "CREATE TABLE enlisted (name TEXT, rank TEXT);",
        "INSERT INTO enlisted VALUES ('Ali','Private'), ('Hasan','Corporal');",
        "SELECT name, rank, salary, 'Officer' AS role FROM officers UNION ALL SELECT name, rank, NULL, 'Enlisted' AS role FROM enlisted ORDER BY role, name;"
    ]
)

hard2 = Task(
    description=(
        "📊  Full Consolidation – UNION ALL + JOIN\n\n"
        "Create `domestic_shipments` and `international_shipments`\n"
        "tables with identical columns (id, destination, weight, carrier).\n"
        "Insert 3 rows each.\n"
        "Write a query that uses UNION ALL to combine both,\n"
        "then JOIN the result with a `carriers` table (carrier name → country)\n"
        "to show every shipment with its carrier's country.\n"
        "Return tracking_id, destination, weight, carrier name, country.\n"
        "Sort by destination.\n\n"
        "Expected output:\n[('D1','Chittagong',12.5,'FastShip','BD'), ('D2','Dhaka',8.0,'FastShip','BD'), ('I2','Dubai',20.0,'GlobalLog','UAE'), ('I3','London',15.5,'GlobalLog','UK'), ('D3','Sylhet',5.0,'SwiftLog','BD'), ('I1','Tokyo',25.0,'TransWorld','JP')]"
    ),
    expected_output="[('D1', 'Chittagong', 12.5, 'FastShip', 'BD'), ('D2', 'Dhaka', 8.0, 'FastShip', 'BD'), ('I2', 'Dubai', 20.0, 'GlobalLog', 'UAE'), ('I3', 'London', 15.5, 'GlobalLog', 'UK'), ('D3', 'Sylhet', 5.0, 'SwiftLog', 'BD'), ('I1', 'Tokyo', 25.0, 'TransWorld', 'JP')]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE domestic_shipments (id TEXT, destination TEXT, weight REAL, carrier TEXT);",
        "INSERT INTO domestic_shipments VALUES ('D1','Chittagong',12.5,'FastShip'), ('D2','Dhaka',8.0,'FastShip'), ('D3','Sylhet',5.0,'SwiftLog');",
        "CREATE TABLE international_shipments (id TEXT, destination TEXT, weight REAL, carrier TEXT);",
        "INSERT INTO international_shipments VALUES ('I1','Tokyo',25.0,'TransWorld'), ('I2','Dubai',20.0,'GlobalLog'), ('I3','London',15.5,'GlobalLog');",
        "CREATE TABLE carriers (name TEXT, country TEXT);",
        "INSERT INTO carriers VALUES ('FastShip','BD'), ('SwiftLog','BD'), ('TransWorld','JP'), ('GlobalLog','UK');",
        "SELECT s.id, s.destination, s.weight, s.carrier, c.country FROM (SELECT id, destination, weight, carrier FROM domestic_shipments UNION ALL SELECT id, destination, weight, carrier FROM international_shipments) s JOIN carriers c ON s.carrier = c.name ORDER BY s.destination;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L37.json",
        module_name="Module_04_Joins_Relationships",
        lesson_name="L37_UNION_UNION_ALL"
    )
