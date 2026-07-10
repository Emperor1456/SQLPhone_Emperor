import sys, sqlite3, os
sys.path.append("../..")
from practice_engine import Task, Level, run_task

DB = "custom_project.db"

def verify_easy(cur, conn):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [r[0] for r in cur.fetchall()]
    return len(tables) >= 4

easy = Task(
    "Design any database with at least 4 tables. Include a many‑to‑many relationship and constraints.",
    verify_easy, Level.EASY,
    hints=["Choose a domain you love: recipes, workouts, music playlists, etc. Create your tables."]
)

def verify_medium(cur, conn):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [r[0] for r in cur.fetchall()]
    for t in tables:
        cur.execute(f"SELECT COUNT(*) FROM {t}")
        if cur.fetchone()[0] < 5:
            return False
    # Check for at least one junction/join table (many‑to‑many)
    has_junction = any(t.lower() in ['enrollment','recipe_ingredient','playlist_song','assignment'] for t in tables)
    return has_junction

medium = Task(
    "Insert at least 5 rows per table. Ensure one table clearly models a many‑to‑many relationship.",
    verify_medium, Level.MEDIUM,
    hints=["Use a junction table with two foreign keys."]
)

def verify_hard(cur, conn):
    # We'll ask the user to write a complex query; they can demonstrate.
    # We'll just check that a query joining at least 3 tables runs.
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [r[0] for r in cur.fetchall()]
    if len(tables) >= 3:
        # try a generic join across three tables
        try:
            cur.execute(f"SELECT * FROM {tables[0]} JOIN {tables[1]} JOIN {tables[2]} LIMIT 1")
            return True
        except:
            return False
    return False

hard = Task(
    "Write a complex query that joins at least 3 tables and uses an aggregate function with HAVING.",
    verify_hard, Level.HARD,
    hints=["Be creative – this is your portfolio piece."]
)


def main():
    levels = {"1": easy, "2": medium, "3": hard}
    while True:
        print("
Choose difficulty:")
        print("1 - Easy")
        print("2 - Medium")
        print("3 - Hard")
        print("0 - Exit")
        c = input("> ").strip()
        if c == "0":
            break
        task = levels.get(c)
        if task:
            run_task(task)
            cont = input("Try next level? (y/n): ").strip().lower()
            if cont != "y":
                continue
            next_key = str(min(int(c)+1, 3))
            next_task = levels.get(next_key)
            if next_task:
                print(f"
Moving to {next_task.level}...")
                run_task(next_task)

if __name__ == "__main__": main()
