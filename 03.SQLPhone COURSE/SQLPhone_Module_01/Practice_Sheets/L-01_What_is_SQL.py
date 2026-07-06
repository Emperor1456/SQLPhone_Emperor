# L-01_What_is_SQL.py — Upgraded with Hints & Levels

import sys
sys.path.append("../..")   # allow importing practice_engine
from practice_engine import Task, Level, run_task

# Verification function for Easy
def verify_easy(cur, conn):
    cur.execute("SELECT id, name FROM empire WHERE id=1")
    row = cur.fetchone()
    return row is not None and row[0] == 1 and row[1] == 'Emperor'

# Easy task
easy_task = Task(
    description="Create a table 'empire' with columns 'id' (INTEGER) and 'name' (TEXT). Insert one row: id=1, name='Emperor'. Then SELECT all rows.",
    verify_func=verify_easy,
    level=Level.EASY,
    hints=[
        "Use CREATE TABLE empire (id INTEGER, name TEXT);",
        "INSERT INTO empire VALUES (1, 'Emperor');",
        "SELECT * FROM empire;"
    ]
)

# Medium task
def verify_medium(cur, conn):
    # expects table 'empire' with an additional 'rank' column
    cur.execute("SELECT id, name, rank FROM empire WHERE id=1")
    row = cur.fetchone()
    return row and row[0]==1 and row[1]=='Emperor' and row[2]=='General'

medium_task = Task(
    description="Alter the 'empire' table to add a column 'rank' TEXT. Set Emperor's rank to 'General'. Then SELECT all rows.",
    verify_func=verify_medium,
    level=Level.MEDIUM,
    hints=[
        "ALTER TABLE empire ADD COLUMN rank TEXT;",
        "UPDATE empire SET rank = 'General' WHERE id = 1;",
        "SELECT * FROM empire;"
    ]
)

# Hard task
def verify_hard(cur, conn):
    # expects two rows: Emperor and another soldier
    cur.execute("SELECT COUNT(*) FROM empire")
    count = cur.fetchone()[0]
    cur.execute("SELECT name FROM empire WHERE rank = 'General'")
    general = cur.fetchone()
    return count == 2 and general and general[0] == 'Emperor'

hard_task = Task(
    description="Insert a second soldier into 'empire' with a different rank. Then update Emperor to be 'Supreme Commander'. Show all rows sorted by rank.",
    verify_func=verify_hard,
    level=Level.HARD,
    hints=[
        "INSERT INTO empire (id, name, rank) VALUES (2, 'Soldier', 'Private');",
        "UPDATE empire SET rank = 'Supreme Commander' WHERE id = 1;",
        "SELECT * FROM empire ORDER BY rank;"
    ]
)

def main():
    print("Choose difficulty:")
    print("1 - Easy")
    print("2 - Medium")
    print("3 - Hard")
    choice = input("> ").strip()
    if choice == "1":
        run_task(easy_task)
    elif choice == "2":
        run_task(medium_task)
    elif choice == "3":
        run_task(hard_task)
    else:
        print("Invalid choice, defaulting to Easy.")
        run_task(easy_task)

if __name__ == "__main__":
    main()
