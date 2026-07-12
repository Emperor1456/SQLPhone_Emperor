import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🏛️  Imperial Registry – Create Tables\n\n"
        "Create two tables with all constraints:\n\n"
        "1. `households`:\n"
        "  • household_id INTEGER PRIMARY KEY\n"
        "  • address TEXT NOT NULL\n"
        "  • head_of_household TEXT NOT NULL\n"
        "  • registered_date TEXT DEFAULT (date('now'))\n\n"
        "2. `citizens`:\n"
        "  • citizen_id INTEGER PRIMARY KEY\n"
        "  • full_name TEXT NOT NULL\n"
        "  • birth_date TEXT NOT NULL\n"
        "  • gender TEXT CHECK(gender IN ('M','F','Other'))\n"
        "  • household_id INTEGER NOT NULL\n"
        "  • FOREIGN KEY (household_id) REFERENCES households(household_id)\n\n"
        "After creating both, query sqlite_master to confirm.\n"
        "Expected output: [('citizens',), ('households',)]"
    ),
    expected_output="[('citizens',), ('households',)]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE households (household_id INTEGER PRIMARY KEY, address TEXT NOT NULL, head_of_household TEXT NOT NULL, registered_date TEXT DEFAULT (date('now')));",
        "CREATE TABLE citizens (citizen_id INTEGER PRIMARY KEY, full_name TEXT NOT NULL, birth_date TEXT NOT NULL, gender TEXT CHECK(gender IN ('M','F','Other')), household_id INTEGER NOT NULL, FOREIGN KEY (household_id) REFERENCES households(household_id));",
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
    ]
)

easy2 = Task(
    description=(
        "📋  Seed the Registry – Insert Data\n\n"
        "Insert data into both tables.\n\n"
        "Households:\n"
        "  (1, '12 Imperial Way, Dhaka', 'Emperor', '2026-01-15')\n"
        "  (2, '45 Warrior Lane, Chittagong', 'Rahim', '2026-02-10')\n\n"
        "Citizens:\n"
        "  (101, 'Emperor', '2008-07-10', 'M', 1)\n"
        "  (102, 'Rahim', '1995-03-22', 'M', 2)\n"
        "  (103, 'Karim', '2000-11-05', 'M', 2)\n\n"
        "Then SELECT the full_name and birth_date\n"
        "of all citizens sorted by full_name.\n\n"
        "Expected output:\n[('Emperor','2008-07-10'), ('Karim','2000-11-05'), ('Rahim','1995-03-22')]"
    ),
    expected_output="[('Emperor', '2008-07-10'), ('Karim', '2000-11-05'), ('Rahim', '1995-03-22')]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE households (household_id INTEGER PRIMARY KEY, address TEXT NOT NULL, head_of_household TEXT NOT NULL, registered_date TEXT DEFAULT (date('now')));",
        "CREATE TABLE citizens (citizen_id INTEGER PRIMARY KEY, full_name TEXT NOT NULL, birth_date TEXT NOT NULL, gender TEXT CHECK(gender IN ('M','F','Other')), household_id INTEGER NOT NULL, FOREIGN KEY (household_id) REFERENCES households(household_id));",
        "INSERT INTO households VALUES (1,'12 Imperial Way, Dhaka','Emperor','2026-01-15'), (2,'45 Warrior Lane, Chittagong','Rahim','2026-02-10');",
        "INSERT INTO citizens VALUES (101,'Emperor','2008-07-10','M',1), (102,'Rahim','1995-03-22','M',2), (103,'Karim','2000-11-05','M',2);",
        "SELECT full_name, birth_date FROM citizens ORDER BY full_name;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🔗  Household Directory – JOIN Query\n\n"
        "The registry database has households and citizens.\n"
        "Write a query that shows each citizen's full_name\n"
        "along with their household address.\n"
        "Sort by citizen full_name.\n\n"
        "Expected output:\n[('Emperor','12 Imperial Way, Dhaka'), ('Karim','45 Warrior Lane, Chittagong'), ('Rahim','45 Warrior Lane, Chittagong')]"
    ),
    setup_sql=(
        "CREATE TABLE households (household_id INTEGER PRIMARY KEY, address TEXT NOT NULL, head_of_household TEXT NOT NULL, registered_date TEXT DEFAULT (date('now')));"
        "CREATE TABLE citizens (citizen_id INTEGER PRIMARY KEY, full_name TEXT NOT NULL, birth_date TEXT NOT NULL, gender TEXT CHECK(gender IN ('M','F','Other')), household_id INTEGER NOT NULL, FOREIGN KEY (household_id) REFERENCES households(household_id));"
        "INSERT INTO households VALUES (1,'12 Imperial Way, Dhaka','Emperor','2026-01-15'), (2,'45 Warrior Lane, Chittagong','Rahim','2026-02-10');"
        "INSERT INTO citizens VALUES (101,'Emperor','2008-07-10','M',1), (102,'Rahim','1995-03-22','M',2), (103,'Karim','2000-11-05','M',2);"
    ),
    expected_output="[('Emperor', '12 Imperial Way, Dhaka'), ('Karim', '45 Warrior Lane, Chittagong'), ('Rahim', '45 Warrior Lane, Chittagong')]",
    level=Level.MEDIUM,
    hints=[
        "SELECT c.full_name, h.address FROM citizens c JOIN households h ON c.household_id = h.household_id ORDER BY c.full_name;"
    ]
)

medium2 = Task(
    description=(
        "📊  Census Summary – Count per Household\n\n"
        "The registry database has data for two households.\n"
        "Write a query that shows each household address\n"
        "and the number of citizens living there.\n"
        "Include households with zero citizens (use LEFT JOIN).\n"
        "Sort by count descending.\n\n"
        "Expected output:\n[('45 Warrior Lane, Chittagong',2), ('12 Imperial Way, Dhaka',1)]"
    ),
    setup_sql=(
        "CREATE TABLE households (household_id INTEGER PRIMARY KEY, address TEXT NOT NULL, head_of_household TEXT NOT NULL, registered_date TEXT DEFAULT (date('now')));"
        "CREATE TABLE citizens (citizen_id INTEGER PRIMARY KEY, full_name TEXT NOT NULL, birth_date TEXT NOT NULL, gender TEXT CHECK(gender IN ('M','F','Other')), household_id INTEGER NOT NULL, FOREIGN KEY (household_id) REFERENCES households(household_id));"
        "INSERT INTO households VALUES (1,'12 Imperial Way, Dhaka','Emperor','2026-01-15'), (2,'45 Warrior Lane, Chittagong','Rahim','2026-02-10');"
        "INSERT INTO citizens VALUES (101,'Emperor','2008-07-10','M',1), (102,'Rahim','1995-03-22','M',2), (103,'Karim','2000-11-05','M',2);"
    ),
    expected_output="[('45 Warrior Lane, Chittagong', 2), ('12 Imperial Way, Dhaka', 1)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT h.address, COUNT(c.citizen_id) AS members FROM households h LEFT JOIN citizens c ON h.household_id = c.household_id GROUP BY h.household_id ORDER BY members DESC;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧱  Age Report – Date Calculation\n\n"
        "The registry database stores birth dates.\n"
        "Write a query that returns each citizen's\n"
        "full_name and their age in years (as of today).\n"
        "Use strftime to compute the difference.\n"
        "Sort by age descending (oldest first).\n\n"
        "Expected output:\n[('Rahim',31), ('Karim',25), ('Emperor',17)]"
    ),
    setup_sql=(
        "CREATE TABLE households (household_id INTEGER PRIMARY KEY, address TEXT NOT NULL, head_of_household TEXT NOT NULL, registered_date TEXT DEFAULT (date('now')));"
        "CREATE TABLE citizens (citizen_id INTEGER PRIMARY KEY, full_name TEXT NOT NULL, birth_date TEXT NOT NULL, gender TEXT CHECK(gender IN ('M','F','Other')), household_id INTEGER NOT NULL, FOREIGN KEY (household_id) REFERENCES households(household_id));"
        "INSERT INTO households VALUES (1,'12 Imperial Way, Dhaka','Emperor','2026-01-15'), (2,'45 Warrior Lane, Chittagong','Rahim','2026-02-10');"
        "INSERT INTO citizens VALUES (101,'Emperor','2008-07-10','M',1), (102,'Rahim','1995-03-22','M',2), (103,'Karim','2000-11-05','M',2);"
    ),
    expected_output="[('Rahim', 31), ('Karim', 25), ('Emperor', 17)]",
    level=Level.HARD,
    hints=[
        "SELECT full_name, (strftime('%Y','now') - strftime('%Y', birth_date)) - (strftime('%m-%d','now') < strftime('%m-%d', birth_date)) AS age FROM citizens ORDER BY age DESC;"
    ]
)

hard2 = Task(
    description=(
        "👑  Complete Registry Report – Multi‑table\n\n"
        "Create the full registry with:\n"
        "  • 3 households\n"
        "  • 6 citizens distributed among them\n\n"
        "Then write a query that shows:\n"
        "  • head_of_household (from households)\n"
        "  • address (from households)\n"
        "  • citizen_count (count of citizens per household)\n"
        "  • oldest_citizen (the earliest birth_date in that household)\n"
        "Sort by citizen_count descending.\n\n"
        "Expected output:\n[('Rahim','45 Warrior Lane',3,'1995-03-22'), ('Fatima','78 River Road',2,'2001-01-01'), ('Emperor','12 Imperial Way',1,'2008-07-10')]"
    ),
    expected_output="[('Rahim', '45 Warrior Lane', 3, '1995-03-22'), ('Fatima', '78 River Road', 2, '2001-01-01'), ('Emperor', '12 Imperial Way', 1, '2008-07-10')]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE households (household_id INTEGER PRIMARY KEY, address TEXT NOT NULL, head_of_household TEXT NOT NULL, registered_date TEXT DEFAULT (date('now')));",
        "CREATE TABLE citizens (citizen_id INTEGER PRIMARY KEY, full_name TEXT NOT NULL, birth_date TEXT NOT NULL, gender TEXT CHECK(gender IN ('M','F','Other')), household_id INTEGER NOT NULL, FOREIGN KEY (household_id) REFERENCES households(household_id));",
        "INSERT INTO households VALUES (1,'12 Imperial Way','Emperor','2026-01-15'), (2,'45 Warrior Lane','Rahim','2026-02-10'), (3,'78 River Road','Fatima','2026-03-01');",
        "INSERT INTO citizens VALUES (101,'Emperor','2008-07-10','M',1), (102,'Rahim','1995-03-22','M',2), (103,'Karim','2000-11-05','M',2), (104,'Ali','1998-08-17','M',2), (105,'Fatima','2001-01-01','F',3), (106,'Hasan','2005-12-25','M',3);",
        "SELECT h.head_of_household, h.address, COUNT(c.citizen_id) AS citizen_count, MIN(c.birth_date) AS oldest_citizen FROM households h LEFT JOIN citizens c ON h.household_id = c.household_id GROUP BY h.household_id ORDER BY citizen_count DESC;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L10.json",
        module_name="Module_01_SQL_Core",
        lesson_name="L10_Module_1_Capstone"
    )
