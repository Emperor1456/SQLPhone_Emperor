import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🏗️  Step 1 – Create the New Ranks Table\n\n"
        "The old `soldiers` table stores rank as TEXT.\n"
        "Create a new `ranks` table:\n"
        "  • rank_id INTEGER PRIMARY KEY\n"
        "  • rank_name TEXT UNIQUE\n"
        "  • rank_level INTEGER\n\n"
        "Populate `ranks` from the distinct rank values\n"
        "in the old `soldiers` table.\n"
        "Assign rank_level: General=1, Colonel=2,\n"
        "Major=3, Private=4, others=5.\n"
        "Then SELECT all rows from ranks, sorted by rank_level.\n\n"
        "Expected output:\n[(1,'General',1), (2,'Colonel',2), (3,'Major',3), (4,'Private',4)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (soldier_id INTEGER PRIMARY KEY, name TEXT NOT NULL, rank TEXT);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General'), (2,'Rahim','Colonel'), (3,'Karim','Private'), (4,'Ali','Major');"
    ),
    expected_output="[(1, 'General', 1), (2, 'Colonel', 2), (3, 'Major', 3), (4, 'Private', 4)]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE ranks (rank_id INTEGER PRIMARY KEY, rank_name TEXT UNIQUE, rank_level INTEGER);",
        "INSERT INTO ranks (rank_name, rank_level) SELECT DISTINCT rank, CASE rank WHEN 'General' THEN 1 WHEN 'Colonel' THEN 2 WHEN 'Major' THEN 3 WHEN 'Private' THEN 4 ELSE 5 END FROM soldiers WHERE rank IS NOT NULL;",
        "SELECT * FROM ranks ORDER BY rank_level;"
    ]
)

easy2 = Task(
    description=(
        "🧱  Step 2 – Create the New Soldiers Table\n\n"
        "Now create the new `soldiers_new` table:\n"
        "  • soldier_id INTEGER PRIMARY KEY\n"
        "  • name TEXT NOT NULL\n"
        "  • rank_id INTEGER\n"
        "  • FOREIGN KEY (rank_id) REFERENCES ranks(rank_id)\n\n"
        "Do NOT insert any data yet.\n"
        "Just verify the table exists by querying sqlite_master\n"
        "for its CREATE statement.\n\n"
        "Expected output:\n[('CREATE TABLE soldiers_new (soldier_id INTEGER PRIMARY KEY, name TEXT NOT NULL, rank_id INTEGER, FOREIGN KEY (rank_id) REFERENCES ranks(rank_id))',)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (soldier_id INTEGER PRIMARY KEY, name TEXT NOT NULL, rank TEXT);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General'), (2,'Rahim','Colonel'), (3,'Karim','Private'), (4,'Ali','Major');"
        "CREATE TABLE ranks (rank_id INTEGER PRIMARY KEY, rank_name TEXT UNIQUE, rank_level INTEGER);"
        "INSERT INTO ranks (rank_name, rank_level) SELECT DISTINCT rank, CASE rank WHEN 'General' THEN 1 WHEN 'Colonel' THEN 2 WHEN 'Major' THEN 3 WHEN 'Private' THEN 4 ELSE 5 END FROM soldiers WHERE rank IS NOT NULL;"
    ),
    expected_output="[('CREATE TABLE soldiers_new (soldier_id INTEGER PRIMARY KEY, name TEXT NOT NULL, rank_id INTEGER, FOREIGN KEY (rank_id) REFERENCES ranks(rank_id))',)]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE soldiers_new (soldier_id INTEGER PRIMARY KEY, name TEXT NOT NULL, rank_id INTEGER, FOREIGN KEY (rank_id) REFERENCES ranks(rank_id));",
        "SELECT sql FROM sqlite_master WHERE type='table' AND name='soldiers_new';"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "📋  Step 3 – Migrate the Data\n\n"
        "The `soldiers` table still has the old TEXT ranks.\n"
        "The `ranks` table and `soldiers_new` table exist.\n"
        "Write an INSERT INTO soldiers_new that:\n"
        "  • Selects soldier_id and name from soldiers\n"
        "  • JOINs with ranks to get the correct rank_id\n"
        "    (matching old rank TEXT to ranks.rank_name)\n"
        "Use a LEFT JOIN to preserve soldiers whose rank\n"
        "might not exist in the new ranks table.\n"
        "Then SELECT all rows from soldiers_new sorted by soldier_id.\n\n"
        "Expected output:\n[(1,'Emperor',1), (2,'Rahim',2), (3,'Karim',4), (4,'Ali',3)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (soldier_id INTEGER PRIMARY KEY, name TEXT NOT NULL, rank TEXT);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General'), (2,'Rahim','Colonel'), (3,'Karim','Private'), (4,'Ali','Major');"
        "CREATE TABLE ranks (rank_id INTEGER PRIMARY KEY, rank_name TEXT UNIQUE, rank_level INTEGER);"
        "INSERT INTO ranks (rank_name, rank_level) VALUES ('General',1), ('Colonel',2), ('Major',3), ('Private',4);"
        "CREATE TABLE soldiers_new (soldier_id INTEGER PRIMARY KEY, name TEXT NOT NULL, rank_id INTEGER, FOREIGN KEY (rank_id) REFERENCES ranks(rank_id));"
    ),
    expected_output="[(1, 'Emperor', 1), (2, 'Rahim', 2), (3, 'Karim', 4), (4, 'Ali', 3)]",
    level=Level.MEDIUM,
    hints=[
        "INSERT INTO soldiers_new (soldier_id, name, rank_id) SELECT s.soldier_id, s.name, r.rank_id FROM soldiers s LEFT JOIN ranks r ON s.rank = r.rank_name;",
        "SELECT * FROM soldiers_new ORDER BY soldier_id;"
    ]
)

medium2 = Task(
    description=(
        "🔄  Step 4 – Swap the Tables\n\n"
        "The migration data is in `soldiers_new`.\n"
        "Now we must replace the old `soldiers` table.\n"
        "Write the statements to:\n"
        "  1. DROP TABLE soldiers (the old one)\n"
        "  2. ALTER TABLE soldiers_new RENAME TO soldiers\n\n"
        "Then SELECT all rows from the new `soldiers` table\n"
        "to confirm the migration succeeded.\n\n"
        "Expected output:\n[(1,'Emperor',1), (2,'Rahim',2), (3,'Karim',4), (4,'Ali',3)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (soldier_id INTEGER PRIMARY KEY, name TEXT NOT NULL, rank TEXT);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General'), (2,'Rahim','Colonel'), (3,'Karim','Private'), (4,'Ali','Major');"
        "CREATE TABLE ranks (rank_id INTEGER PRIMARY KEY, rank_name TEXT UNIQUE, rank_level INTEGER);"
        "INSERT INTO ranks (rank_name, rank_level) VALUES ('General',1), ('Colonel',2), ('Major',3), ('Private',4);"
        "CREATE TABLE soldiers_new (soldier_id INTEGER PRIMARY KEY, name TEXT NOT NULL, rank_id INTEGER, FOREIGN KEY (rank_id) REFERENCES ranks(rank_id));"
        "INSERT INTO soldiers_new (soldier_id, name, rank_id) SELECT s.soldier_id, s.name, r.rank_id FROM soldiers s LEFT JOIN ranks r ON s.rank = r.rank_name;"
    ),
    expected_output="[(1, 'Emperor', 1), (2, 'Rahim', 2), (3, 'Karim', 4), (4, 'Ali', 3)]",
    level=Level.MEDIUM,
    hints=[
        "DROP TABLE soldiers;",
        "ALTER TABLE soldiers_new RENAME TO soldiers;",
        "SELECT * FROM soldiers ORDER BY soldier_id;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🛡️  Step 5 – Wrap in a Transaction\n\n"
        "Re‑run the entire migration inside a transaction.\n"
        "The initial state is the old `soldiers` table\n"
        "(with TEXT ranks) and the new `ranks` table.\n\n"
        "Write a complete script that:\n"
        "  1. BEGIN\n"
        "  2. Creates soldiers_new (same structure as before)\n"
        "  3. Migrates data\n"
        "  4. Drops old soldiers\n"
        "  5. Renames soldiers_new to soldiers\n"
        "  6. COMMIT\n\n"
        "After the script, SELECT the new soldiers joined\n"
        "with ranks to show name and rank_name.\n\n"
        "Expected output:\n[('Emperor','General'), ('Rahim','Colonel'), ('Karim','Private'), ('Ali','Major')]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (soldier_id INTEGER PRIMARY KEY, name TEXT NOT NULL, rank TEXT);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General'), (2,'Rahim','Colonel'), (3,'Karim','Private'), (4,'Ali','Major');"
        "CREATE TABLE ranks (rank_id INTEGER PRIMARY KEY, rank_name TEXT UNIQUE, rank_level INTEGER);"
        "INSERT INTO ranks (rank_name, rank_level) VALUES ('General',1), ('Colonel',2), ('Major',3), ('Private',4);"
    ),
    expected_output="[('Emperor', 'General'), ('Rahim', 'Colonel'), ('Karim', 'Private'), ('Ali', 'Major')]",
    level=Level.HARD,
    hints=[
        "BEGIN;",
        "CREATE TABLE soldiers_new (soldier_id INTEGER PRIMARY KEY, name TEXT NOT NULL, rank_id INTEGER, FOREIGN KEY (rank_id) REFERENCES ranks(rank_id));",
        "INSERT INTO soldiers_new (soldier_id, name, rank_id) SELECT s.soldier_id, s.name, r.rank_id FROM soldiers s LEFT JOIN ranks r ON s.rank = r.rank_name;",
        "DROP TABLE soldiers;",
        "ALTER TABLE soldiers_new RENAME TO soldiers;",
        "COMMIT;",
        "SELECT s.name, r.rank_name FROM soldiers s JOIN ranks r ON s.rank_id = r.rank_id ORDER BY s.soldier_id;"
    ]
)

hard2 = Task(
    description=(
        "🔍  Step 6 – Verify Referential Integrity\n\n"
        "After the migration, the new `soldiers` table\n"
        "should have a foreign key to `ranks`.\n"
        "Write a query that proves no orphan records exist:\n"
        "  • SELECT any soldier whose rank_id does NOT\n"
        "    exist in the ranks table.\n"
        "  • Use NOT EXISTS or a LEFT JOIN with IS NULL.\n"
        "If the migration was successful, this query should\n"
        "return zero rows.\n\n"
        "Expected output: []"
    ),
    setup_sql=(
        "CREATE TABLE ranks (rank_id INTEGER PRIMARY KEY, rank_name TEXT UNIQUE, rank_level INTEGER);"
        "INSERT INTO ranks (rank_name, rank_level) VALUES ('General',1), ('Colonel',2), ('Major',3), ('Private',4);"
        "CREATE TABLE soldiers (soldier_id INTEGER PRIMARY KEY, name TEXT NOT NULL, rank_id INTEGER, FOREIGN KEY (rank_id) REFERENCES ranks(rank_id));"
        "INSERT INTO soldiers (soldier_id, name, rank_id) VALUES (1,'Emperor',1), (2,'Rahim',2), (3,'Karim',4), (4,'Ali',3);"
    ),
    expected_output="[]",
    level=Level.HARD,
    hints=[
        "SELECT s.soldier_id, s.name FROM soldiers s WHERE NOT EXISTS (SELECT 1 FROM ranks r WHERE r.rank_id = s.rank_id);"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L59.json",
        module_name="Module_06_Modifying_Data_Schema",
        lesson_name="L59_Module_Practice_Data_Migration"
    )
