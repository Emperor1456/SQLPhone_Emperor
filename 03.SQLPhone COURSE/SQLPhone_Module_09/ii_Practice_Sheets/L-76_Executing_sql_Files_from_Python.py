import sys, sqlite3, os
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    # Write a small .sql file
    with open("test.sql", "w") as f:
        f.write("CREATE TABLE temp(id INT);\nINSERT INTO temp VALUES (42);")
    return True

easy = Task(
    "I've created 'test.sql' with DDL and DML. Write Python code to read and execute it using conn.executescript().",
    verify_easy, Level.EASY,
    hints=["with open('test.sql') as f: sql = f.read()", "conn.executescript(sql)", "conn.commit()"]
)

def verify_medium(cur, conn):
    cur.execute("SELECT * FROM temp")
    return cur.fetchone() == (42,)

medium = Task(
    "Verify the table 'temp' exists and contains the value 42.",
    verify_medium, Level.MEDIUM,
    hints=["cur.execute('SELECT * FROM temp')"]
)

def verify_hard(cur, conn):
    # Remove test.sql and also show cleanup
    if os.path.exists("test.sql"):
        os.unlink("test.sql")
    return not os.path.exists("test.sql")

hard = Task(
    "Clean up: delete the 'test.sql' file from disk.",
    verify_hard, Level.HARD,
    hints=["import os; os.unlink('test.sql')"]
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
