import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    return True

easy = Task(
    "List the next three technologies you plan to learn after mastering raw SQL.",
    verify_easy, Level.EASY,
    hints=["ORM (SQLAlchemy), migrations (Alembic), cloud database (Supabase)"]
)

def verify_medium(cur, conn):
    return True

medium = Task(
    "Write a short Python snippet that shows the basic structure of SQLAlchemy model definition.",
    verify_medium, Level.MEDIUM,
    hints=["from sqlalchemy import Column, Integer, String; class User(Base): ..."]
)

def verify_hard(cur, conn):
    return True

hard = Task(
    "Explain how an ORM and migrations together enable team collaboration on a database schema.",
    verify_hard, Level.HARD,
    hints=["ORM abstracts SQL; migrations version‑control schema changes; teams can share and apply changes safely."]
)

def main():
    print("1 Easy  2 Medium  3 Hard")
    c = input("> ")
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))
if __name__ == "__main__": main()
