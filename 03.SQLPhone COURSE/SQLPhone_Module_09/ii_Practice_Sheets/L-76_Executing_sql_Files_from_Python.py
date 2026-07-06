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
    print("1 Easy  2 Medium  3 Hard")
    c = input("> ")
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))
if __name__ == "__main__": main()
