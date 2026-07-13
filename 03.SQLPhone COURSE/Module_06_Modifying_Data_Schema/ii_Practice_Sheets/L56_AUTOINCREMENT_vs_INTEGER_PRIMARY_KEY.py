import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🔢  INTEGER PRIMARY KEY – Auto‑Assign\n\n"
        "Create a table `soldiers` with columns:\n"
        "  • id INTEGER PRIMARY KEY\n"
        "  • name TEXT NOT NULL\n\n"
        "Insert three soldiers without specifying id\n"
        "(or use NULL). SQLite will auto‑assign ids.\n"
        "Then SELECT all rows sorted by id.\n\n"
        "Expected output:\n[(1,'Emperor'), (2,'Rahim'), (3,'Ali')]"
    ),
    expected_output="[(1, 'Emperor'), (2, 'Rahim'), (3, 'Ali')]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT NOT NULL);",
        "INSERT INTO soldiers (name) VALUES ('Emperor'), ('Rahim'), ('Ali');",
        "SELECT * FROM soldiers ORDER BY id;"
    ]
)

easy2 = Task(
    description=(
        "🔒  AUTOINCREMENT – No Reuse\n\n"
        "Create a table `audit_log` with columns:\n"
        "  • log_id INTEGER PRIMARY KEY AUTOINCREMENT\n"
        "  • message TEXT\n\n"
        "Insert two rows. Then DELETE the row with the\n"
        "highest log_id. Insert another row.\n"
        "Observe that the new log_id does NOT reuse\n"
        "the deleted id; it continues incrementing.\n"
        "Finally, SELECT all remaining rows sorted by log_id.\n\n"
        "Expected output:\n[(1,'First'), (3,'Third')]"
    ),
    expected_output="[(1, 'First'), (3, 'Third')]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE audit_log (log_id INTEGER PRIMARY KEY AUTOINCREMENT, message TEXT);",
        "INSERT INTO audit_log (message) VALUES ('First'), ('Second');",
        "DELETE FROM audit_log WHERE log_id = 2;",
        "INSERT INTO audit_log (message) VALUES ('Third');",
        "SELECT * FROM audit_log ORDER BY log_id;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🔄  Demonstrate ID Reuse – INTEGER PRIMARY KEY\n\n"
        "Create a table `temp_items` with\n"
        "  • id INTEGER PRIMARY KEY (no AUTOINCREMENT)\n"
        "  • item TEXT\n\n"
        "Insert three rows. DELETE the row with the highest id.\n"
        "Insert another row. Because INTEGER PRIMARY KEY may\n"
        "reuse the maximum rowid, the new row could take the\n"
        "deleted id. Show the final table sorted by id.\n\n"
        "Expected output:\n[(1,'Item1'), (2,'Item2'), (3,'Item4')] (Item3 deleted, new gets id 3)\n"
        "Note: actual behavior depends on SQLite internals; we'll simulate by\n"
        "inserting a row and expecting the max+1 pattern, but without AUTOINCREMENT\n"
        "the engine might reuse 3. To make it deterministic, we'll force a\n"
        "different approach: after deleting max, insert a new row; the id may be 3\n"
        "because SQLite finds the max existing rowid and adds 1. So the new row\n"
        "should get 3, effectively reusing the deleted number."
    ),
    expected_output="[(1, 'Item1'), (2, 'Item2'), (3, 'Item4')]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE temp_items (id INTEGER PRIMARY KEY, item TEXT);",
        "INSERT INTO temp_items (item) VALUES ('Item1'), ('Item2'), ('Item3');",
        "DELETE FROM temp_items WHERE id = 3;",
        "INSERT INTO temp_items (item) VALUES ('Item4');",
        "SELECT * FROM temp_items ORDER BY id;"
    ]
)

medium2 = Task(
    description=(
        "📊  Query sqlite_sequence – AUTOINCREMENT Tracking\n\n"
        "Create a table `events` with\n"
        "  • event_id INTEGER PRIMARY KEY AUTOINCREMENT\n"
        "  • name TEXT\n\n"
        "Insert two rows. The sqlite_sequence table now\n"
        "tracks the highest used event_id for 'events'.\n"
        "Query sqlite_sequence to see the current seq value.\n"
        "Then delete both rows and query again. Even though\n"
        "the table is empty, the sequence remains.\n\n"
        "Expected output:\n[(2,), (2,)] (first after inserts, second after deletes)\n"
        "Note: the second query should still return 2 because\n"
        "AUTOINCREMENT never decreases the sequence."
    ),
    expected_output="[(2,), (2,)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE events (event_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT);",
        "INSERT INTO events (name) VALUES ('Login'), ('Logout');",
        "SELECT seq FROM sqlite_sequence WHERE name='events';",
        "DELETE FROM events;",
        "SELECT seq FROM sqlite_sequence WHERE name='events';"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  When AUTOINCREMENT Matters – Invoice Numbers\n\n"
        "Create a table `invoices` with columns:\n"
        "  • invoice_id INTEGER PRIMARY KEY AUTOINCREMENT\n"
        "  • customer TEXT\n"
        "  • amount REAL\n\n"
        "Insert three invoices. Then delete the second one.\n"
        "Insert a new invoice. Because AUTOINCREMENT guarantees\n"
        "no reuse, the new invoice gets id 4, not 2.\n"
        "Show the final table sorted by invoice_id.\n"
        "Then write a short comment explaining why this is\n"
        "important for audit trails (comments allowed in SQL).\n\n"
        "Expected output:\n[(1,'Emperor',500.0), (3,'Ali',300.0), (4,'Rahim',700.0)]"
    ),
    expected_output="[(1, 'Emperor', 500.0), (3, 'Ali', 300.0), (4, 'Rahim', 700.0)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE invoices (invoice_id INTEGER PRIMARY KEY AUTOINCREMENT, customer TEXT, amount REAL);",
        "INSERT INTO invoices (customer, amount) VALUES ('Emperor',500), ('Rahim',200), ('Ali',300);",
        "DELETE FROM invoices WHERE invoice_id = 2;",
        "INSERT INTO invoices (customer, amount) VALUES ('Rahim',700);",
        "SELECT * FROM invoices ORDER BY invoice_id;"
    ]
)

hard2 = Task(
    description=(
        "📊  Performance Comparison – Bulk Insert\n\n"
        "Create two identical tables:\n"
        "  • `fast` with INTEGER PRIMARY KEY\n"
        "  • `slow` with INTEGER PRIMARY KEY AUTOINCREMENT\n\n"
        "Insert 100 rows into each using a recursive CTE\n"
        "(simulate with a loop of individual inserts? We'll use\n"
        "a single INSERT with a CTE to generate numbers).\n"
        "Then compare the time? The engine can't measure time,\n"
        "so we'll just verify both have 100 rows.\n"
        "The point is: AUTOINCREMENT writes to sqlite_sequence\n"
        "on every insert, making it marginally slower.\n"
        "Show row counts.\n\n"
        "Expected output:\n[(100,), (100,)]"
    ),
    expected_output="[(100,), (100,)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE fast (id INTEGER PRIMARY KEY, val TEXT);",
        "CREATE TABLE slow (id INTEGER PRIMARY KEY AUTOINCREMENT, val TEXT);",
        "WITH RECURSIVE cnt(x) AS (SELECT 1 UNION ALL SELECT x+1 FROM cnt WHERE x<100) INSERT INTO fast (val) SELECT 'data' FROM cnt;",
        "WITH RECURSIVE cnt(x) AS (SELECT 1 UNION ALL SELECT x+1 FROM cnt WHERE x<100) INSERT INTO slow (val) SELECT 'data' FROM cnt;",
        "SELECT (SELECT COUNT(*) FROM fast), (SELECT COUNT(*) FROM slow);"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L56.json",
        module_name="Module_06_Modifying_Data_Schema",
        lesson_name="L56_AUTOINCREMENT"
    )
