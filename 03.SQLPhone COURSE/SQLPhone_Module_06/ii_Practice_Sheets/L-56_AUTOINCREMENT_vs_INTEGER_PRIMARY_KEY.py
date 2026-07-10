import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE standard(id INTEGER PRIMARY KEY, val TEXT)")
    cur.execute("CREATE TABLE autoinc(id INTEGER PRIMARY KEY AUTOINCREMENT, val TEXT)")
    return True

easy = Task("Create two tables: one with INTEGER PRIMARY KEY and one with AUTOINCREMENT.",
            verify_easy, Level.EASY,
            hints=["CREATE TABLE standard(id INTEGER PRIMARY KEY, val TEXT); CREATE TABLE autoinc(id INTEGER PRIMARY KEY AUTOINCREMENT, val TEXT);"])

def verify_medium(cur, conn):
    cur.executemany("INSERT INTO standard(val) VALUES (?)", [('a',),('b',)])
    cur.executemany("INSERT INTO autoinc(val) VALUES (?)", [('a',),('b',)])
    cur.execute("DELETE FROM standard WHERE id = (SELECT MAX(id) FROM standard)")
    cur.execute("DELETE FROM autoinc WHERE id = (SELECT MAX(id) FROM autoinc)")
    cur.execute("INSERT INTO standard(val) VALUES ('c')")
    cur.execute("INSERT INTO autoinc(val) VALUES ('c')")
    cur.execute("SELECT MAX(id) FROM standard")
    std_max = cur.fetchone()[0]
    cur.execute("SELECT MAX(id) FROM autoinc")
    auto_max = cur.fetchone()[0]
    return std_max < auto_max  # standard may reuse id, autoinc won't

medium = Task("Insert 2 rows each, delete the max id row, insert another. Compare max id values; AUTOINCREMENT should be higher.",
              verify_medium, Level.MEDIUM,
              hints=["Standard may reuse id 2, AUTOINCREMENT will be 3."])

def verify_hard(cur, conn):
    return True  # already verified above

hard = Task("Observe and explain the difference in a comment (type :hint to see expected behavior).",
            verify_hard, Level.HARD,
            hints=["Standard reuses the deleted id; AUTOINCREMENT never reuses."])


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

if __name__=="__main__": main()
