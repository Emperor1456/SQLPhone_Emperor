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
    print("1 Easy  2 Medium  3 Hard")
    c = input("> ")
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))
if __name__ == "__main__": main()
