import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "✏️  UPDATE Single Row – Promote a Soldier\n\n"
        "The `soldiers` table has 4 rows.\n"
        "Write an UPDATE that changes Rahim's rank\n"
        "from 'Colonel' to 'General'.\n"
        "Then SELECT the updated row to confirm.\n\n"
        "Expected output:\n[(2, 'Rahim', 'General', 4000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Ali','Colonel',4500), (4,'Hasan','Private',3500);"
    ),
    expected_output="[(2, 'Rahim', 'General', 4000.0)]",
    level=Level.EASY,
    hints=[
        "UPDATE soldiers SET rank = 'General' WHERE id = 2;",
        "SELECT * FROM soldiers WHERE id = 2;"
    ]
)

easy2 = Task(
    description=(
        "💰  UPDATE Multiple Columns – Raise & Bonus\n\n"
        "The `soldiers` table has 4 rows.\n"
        "Write an UPDATE that increases Hasan's salary\n"
        "by 500 AND changes his rank to 'Sergeant'.\n"
        "Use SET salary = salary + 500, rank = 'Sergeant'.\n"
        "Then SELECT the updated row.\n\n"
        "Expected output:\n[(4, 'Hasan', 'Sergeant', 4000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Ali','Colonel',4500), (4,'Hasan','Private',3500);"
    ),
    expected_output="[(4, 'Hasan', 'Sergeant', 4000.0)]",
    level=Level.EASY,
    hints=[
        "UPDATE soldiers SET salary = salary + 500, rank = 'Sergeant' WHERE id = 4;",
        "SELECT * FROM soldiers WHERE id = 4;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "📊  Batch UPDATE – Raise for Entire Regiment\n\n"
        "Create a `soldiers` table with a `regiment_id` column.\n"
        "Insert 5 soldiers across 2 regiments.\n"
        "Write an UPDATE that increases the salary of ALL\n"
        "soldiers in regiment 1 by 10%.\n"
        "Then SELECT all soldiers in regiment 1, sorted by id.\n\n"
        "Expected output:\n[(1,'Emperor','General',5500.0,1), (3,'Ali','General',4950.0,1)]"
    ),
    expected_output="[(1, 'Emperor', 'General', 5500.0, 1), (3, 'Ali', 'General', 4950.0, 1)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL, regiment_id INTEGER);",
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000,1), (2,'Rahim','Colonel',4000,2), (3,'Ali','General',4500,1), (4,'Hasan','Private',3500,2), (5,'Karim','Private',2000,2);",
        "UPDATE soldiers SET salary = salary * 1.1 WHERE regiment_id = 1;",
        "SELECT * FROM soldiers WHERE regiment_id = 1 ORDER BY id;"
    ]
)

medium2 = Task(
    description=(
        "🔄  UPDATE with Subquery – Set to Average\n\n"
        "The same `soldiers` table with salaries.\n"
        "Write an UPDATE that sets each soldier's salary\n"
        "to the average salary of their regiment.\n"
        "Use a correlated subquery in the SET clause.\n"
        "Then SELECT all rows, sorted by id.\n\n"
        "Expected output:\n[(1,'Emperor','General',4750.0,1), (2,'Rahim','Colonel',3166.66666666667,2), (3,'Ali','General',4750.0,1), (4,'Hasan','Private',3166.66666666667,2), (5,'Karim','Private',3166.66666666667,2)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL, regiment_id INTEGER);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000,1), (2,'Rahim','Colonel',4000,2), (3,'Ali','General',4500,1), (4,'Hasan','Private',3500,2), (5,'Karim','Private',2000,2);"
    ),
    expected_output="[(1, 'Emperor', 'General', 4750.0, 1), (2, 'Rahim', 'Colonel', 3166.66666666667, 2), (3, 'Ali', 'General', 4750.0, 1), (4, 'Hasan', 'Private', 3166.66666666667, 2), (5, 'Karim', 'Private', 3166.66666666667, 2)]",
    level=Level.MEDIUM,
    hints=[
        "UPDATE soldiers SET salary = (SELECT AVG(salary) FROM soldiers s2 WHERE s2.regiment_id = soldiers.regiment_id);",
        "SELECT * FROM soldiers ORDER BY id;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "⚠️  Safe UPDATE – Test with SELECT First\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Before updating, write a SELECT to verify which\n"
        "rows would be affected: soldiers with salary < 3000\n"
        "AND rank = 'Private'.\n"
        "Then write the UPDATE to set their salary to 3000.\n"
        "Show the final state of those rows.\n\n"
        "Expected output:\n[(5,'Karim','Private',3000.0,2)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL, regiment_id INTEGER);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000,1), (2,'Rahim','Colonel',4000,2), (3,'Ali','General',4500,1), (4,'Hasan','Private',3500,2), (5,'Karim','Private',2000,2);"
    ),
    expected_output="[(5, 'Karim', 'Private', 3000.0, 2)]",
    level=Level.HARD,
    hints=[
        "SELECT * FROM soldiers WHERE salary < 3000 AND rank = 'Private';",
        "UPDATE soldiers SET salary = 3000 WHERE salary < 3000 AND rank = 'Private';",
        "SELECT * FROM soldiers WHERE salary = 3000 AND rank = 'Private';"
    ]
)

hard2 = Task(
    description=(
        "🧪  UPDATE with Transaction – Safe Bulk Change\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Write a transaction that gives a 15% raise to all\n"
        "soldiers, but if any salary would exceed 6000,\n"
        "rollback the entire update.\n"
        "First, check if any salary * 1.15 would exceed 6000.\n"
        "If yes, print 'Rollback' (just run a SELECT showing\n"
        "the problematic rows). If no, execute the UPDATE.\n"
        "In this case, Emperor's salary would be 5750 (safe),\n"
        "so proceed with the update and show all rows.\n\n"
        "Expected output:\n[(1,'Emperor','General',5750.0,1), (2,'Rahim','Colonel',4600.0,2), (3,'Ali','General',5175.0,1), (4,'Hasan','Private',4025.0,2), (5,'Karim','Private',2300.0,2)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL, regiment_id INTEGER);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000,1), (2,'Rahim','Colonel',4000,2), (3,'Ali','General',4500,1), (4,'Hasan','Private',3500,2), (5,'Karim','Private',2000,2);"
    ),
    expected_output="[(1, 'Emperor', 'General', 5750.0, 1), (2, 'Rahim', 'Colonel', 4600.0, 2), (3, 'Ali', 'General', 5175.0, 1), (4, 'Hasan', 'Private', 4025.0, 2), (5, 'Karim', 'Private', 2300.0, 2)]",
    level=Level.HARD,
    hints=[
        "SELECT * FROM soldiers WHERE salary * 1.15 > 6000;",
        "UPDATE soldiers SET salary = salary * 1.15;",
        "SELECT * FROM soldiers ORDER BY id;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L51.json",
        module_name="Module_06_Modifying_Data_Schema",
        lesson_name="L51_UPDATE"
    )
