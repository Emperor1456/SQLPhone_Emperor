import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🏛️  Imperial Registry – First Table\n\n"
        "Create a table `empire` with two columns:\n"
        "  • id INTEGER\n"
        "  • name TEXT\n\n"
        "Then insert one row: id=1, name='Emperor'.\n"
        "Finally, SELECT all rows to confirm.\n\n"
        "Expected output: [(1, 'Emperor')]"
    ),
    expected_output="[(1, 'Emperor')]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE empire (id INTEGER, name TEXT);",
        "INSERT INTO empire VALUES (1, 'Emperor');",
        "SELECT * FROM empire;"
    ]
)

easy2 = Task(
    description=(
        "📋  Imperial Census – Multiple Rows\n\n"
        "Create the same `empire` table, but insert\n"
        "two rows: (1,'Emperor') and (2,'Rahim').\n"
        "Then SELECT only the `name` column\n"
        "for the row where id = 1.\n\n"
        "Expected output: [('Emperor',)]"
    ),
    expected_output="[('Emperor',)]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE empire (id INTEGER, name TEXT);",
        "INSERT INTO empire VALUES (1, 'Emperor'), (2, 'Rahim');",
        "SELECT name FROM empire WHERE id = 1;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🪖  Imperial Ranks – Evolve the Schema\n\n"
        "The empire table already exists with two soldiers:\n"
        "  (1,'Emperor') and (2,'Rahim').\n\n"
        "1. Add a column `rank` TEXT.\n"
        "2. Set Emperor's rank to 'General'.\n"
        "3. SELECT all rows to verify.\n\n"
        "Expected output:\n[(1, 'Emperor', 'General'), (2, 'Rahim', None)]"
    ),
    setup_sql=(
        "CREATE TABLE empire (id INTEGER, name TEXT);"
        "INSERT INTO empire VALUES (1,'Emperor'), (2,'Rahim');"
    ),
    expected_output="[(1, 'Emperor', 'General'), (2, 'Rahim', None)]",
    level=Level.MEDIUM,
    hints=[
        "ALTER TABLE empire ADD COLUMN rank TEXT;",
        "UPDATE empire SET rank = 'General' WHERE id = 1;",
        "SELECT * FROM empire;"
    ]
)

medium2 = Task(
    description=(
        "🎖️  Assign Ranks – Filter by Non‑NULL\n\n"
        "The empire table has soldiers and ranks.\n"
        "Set Rahim's rank to 'Colonel'.\n"
        "Then SELECT name and rank for rows where\n"
        "rank is not NULL.\n\n"
        "Expected output:\n[('Emperor', 'General'), ('Rahim', 'Colonel')]"
    ),
    setup_sql=(
        "CREATE TABLE empire (id INTEGER, name TEXT, rank TEXT);"
        "INSERT INTO empire VALUES (1,'Emperor','General'), (2,'Rahim',NULL);"
    ),
    expected_output="[('Emperor', 'General'), ('Rahim', 'Colonel')]",
    level=Level.MEDIUM,
    hints=[
        "UPDATE empire SET rank = 'Colonel' WHERE id = 2;",
        "SELECT name, rank FROM empire WHERE rank IS NOT NULL;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "👑  Supreme Commander – Multi‑row Sort\n\n"
        "The empire currently has Emperor (General)\n"
        "and Rahim (Colonel).\n\n"
        "1. Insert a third soldier (3,'Karim','Private').\n"
        "2. Promote Emperor to 'Supreme Commander'.\n"
        "3. SELECT all rows sorted by rank alphabetically.\n\n"
        "Expected output:\n[(2, 'Rahim', 'Colonel'), (3, 'Karim', 'Private'), (1, 'Emperor', 'Supreme Commander')]"
    ),
    setup_sql=(
        "CREATE TABLE empire (id INTEGER, name TEXT, rank TEXT);"
        "INSERT INTO empire VALUES (1,'Emperor','General'), (2,'Rahim','Colonel');"
    ),
    expected_output="[(2, 'Rahim', 'Colonel'), (3, 'Karim', 'Private'), (1, 'Emperor', 'Supreme Commander')]",
    level=Level.HARD,
    hints=[
        "INSERT INTO empire VALUES (3, 'Karim', 'Private');",
        "UPDATE empire SET rank = 'Supreme Commander' WHERE id = 1;",
        "SELECT * FROM empire ORDER BY rank;"
    ]
)

hard2 = Task(
    description=(
        "📊  Rank Census – Distinct Ranks\n\n"
        "With three soldiers in the empire, list\n"
        "all distinct ranks currently held.\n\n"
        "Expected output:\n[('Colonel',), ('Private',), ('Supreme Commander',)]"
    ),
    setup_sql=(
        "CREATE TABLE empire (id INTEGER, name TEXT, rank TEXT);"
        "INSERT INTO empire VALUES (1,'Emperor','Supreme Commander'), (2,'Rahim','Colonel'), (3,'Karim','Private');"
    ),
    expected_output="[('Colonel',), ('Private',), ('Supreme Commander',)]",
    level=Level.HARD,
    hints=[
        "SELECT DISTINCT rank FROM empire ORDER BY rank;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L01.json",
        module_name="Module_01_SQL_Core",
        lesson_name="L01_What_is_SQL"
    )
