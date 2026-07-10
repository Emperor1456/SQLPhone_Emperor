import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE compare(id INTEGER PRIMARY KEY, feature TEXT)")
    cur.executemany("INSERT INTO compare(feature) VALUES (?)", [('SQLite is serverless',), ('PostgreSQL supports advanced types',), ('MySQL widely used for web',)])
    return True

easy = Task(
    "We have a 'compare' table with some features. Write a query that returns all rows.",
    verify_easy, Level.EASY,
    hints=["SELECT * FROM compare;"]
)

def verify_medium(cur, conn):
    cur.execute("SELECT feature FROM compare WHERE feature LIKE '%SQLite%' OR feature LIKE '%PostgreSQL%'")
    return len(cur.fetchall()) == 2

medium = Task(
    "Find features mentioning SQLite or PostgreSQL.",
    verify_medium, Level.MEDIUM,
    hints=["Use LIKE with OR."]
)

def verify_hard(cur, conn):
    # Open-ended: ask user to write a short paragraph in a comment about when to use each DB.
    # We'll just accept any input.
    return True

hard = Task(
    "In a comment, explain one key strength of each: SQLite, PostgreSQL, MySQL.",
    verify_hard, Level.HARD,
    hints=["SQLite: embedded/phone, PostgreSQL: advanced features, MySQL: web apps."]
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
