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
