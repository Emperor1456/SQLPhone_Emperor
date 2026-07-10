import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE scores(player TEXT, points INTEGER)")
    cur.executemany("INSERT INTO scores VALUES (?,?)", [('Alice',50),('Alice',80),('Bob',60),('Charlie',90)])
    return True

easy = Task("We have 'scores'. Write a query to find players with points greater than ANY score of 'Alice'.",
            verify_easy, Level.EASY,
            hints=["SELECT player, points FROM scores WHERE points > ANY (SELECT points FROM scores WHERE player='Alice') AND player != 'Alice';"])

def verify_medium(cur, conn):
    cur.execute("SELECT player, points FROM scores WHERE points > ANY (SELECT points FROM scores WHERE player='Alice') AND player != 'Alice'")
    rows = cur.fetchall()
    # Bob(60) and Charlie(90) both >50 (Alice's min)
    return len(rows) == 2

medium = Task("Your query should return Bob and Charlie (both > 50).",
              verify_medium, Level.MEDIUM,
              hints=["The subquery returns (50,80). ANY means >50 OR >80 -> >50."])

def verify_hard(cur, conn):
    cur.execute("SELECT player, points FROM scores WHERE points > ALL (SELECT points FROM scores WHERE player='Alice')")
    rows = cur.fetchall()
    return len(rows) == 1 and rows[0][0] == 'Charlie'

hard = Task("Find players with points greater than ALL of Alice's scores (should be only Charlie, 90 > 80).",
            verify_hard, Level.HARD,
            hints=["SELECT player, points FROM scores WHERE points > ALL (SELECT points FROM scores WHERE player='Alice');"])


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
