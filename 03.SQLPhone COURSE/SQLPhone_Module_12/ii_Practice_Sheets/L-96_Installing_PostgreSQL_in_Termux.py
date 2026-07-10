import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    # Simulate: show a message about proot-distro
    print("Simulated: To install PostgreSQL, use proot-distro.")
    return True

easy = Task(
    "Research the commands to install PostgreSQL in Termux via proot-distro. Write them as comments.",
    verify_easy, Level.EASY,
    hints=["pkg install proot-distro; proot-distro install debian; proot-distro login debian; apt install postgresql"]
)

def verify_medium(cur, conn):
    return True  # assume they did

medium = Task(
    "Write the steps to start PostgreSQL service and create a database.",
    verify_medium, Level.MEDIUM,
    hints=["service postgresql start; su - postgres; createdb testdb; psql -d testdb"]
)

def verify_hard(cur, conn):
    return True

hard = Task(
    "Explain why SQLite is still the best choice for this phone‑based course, even after learning PostgreSQL.",
    verify_hard, Level.HARD,
    hints=["Zero configuration, single file, no server overhead, perfect for learning and prototyping."]
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
