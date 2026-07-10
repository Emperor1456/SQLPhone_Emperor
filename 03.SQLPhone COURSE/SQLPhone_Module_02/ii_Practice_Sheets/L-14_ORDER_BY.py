import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("SELECT COUNT(*) FROM scores")
    return cur.fetchone()[0] >= 4

easy = Task("Create table 'scores' (player TEXT, score INTEGER, level INTEGER). Insert at least 4 rows with varied scores and levels.",
            verify_easy, Level.EASY,
            hints=["CREATE TABLE scores (player TEXT, score INTEGER, level INTEGER);",
                   "INSERT INTO scores VALUES ('A',100,2),('B',200,1),('C',150,3),('D',200,2);"])

def verify_medium(cur, conn):
    cur.execute("SELECT * FROM scores ORDER BY level DESC, score DESC")
    rows = cur.fetchall()
    return len(rows) >= 4 and rows[0][2] >= rows[1][2]

medium = Task("Sort all columns by level DESC, then score DESC.",
              verify_medium, Level.MEDIUM,
              hints=["SELECT * FROM scores ORDER BY level DESC, score DESC;"])

def verify_hard(cur, conn):
    cur.execute("SELECT player, score*level AS weighted FROM scores ORDER BY weighted DESC")
    return len(cur.fetchall()) >= 4

hard = Task("Add a computed column 'weighted = score * level' and sort by that descending.",
            verify_hard, Level.HARD,
            hints=["SELECT player, score*level AS weighted FROM scores ORDER BY weighted DESC;"])


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
