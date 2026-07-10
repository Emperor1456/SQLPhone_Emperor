import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE scores(player TEXT, points INT)")
    cur.executemany("INSERT INTO scores VALUES (?,?)", [('Alice',100),('Bob',200),('Charlie',150)])
    return True

easy = Task(
    "We have 'scores'. Update Alice's points to 120 using a parameterized UPDATE.",
    verify_easy, Level.EASY,
    hints=["cur.execute('UPDATE scores SET points = ? WHERE player = ?', (120, 'Alice'))", "conn.commit()"]
)

def verify_medium(cur, conn):
    cur.execute("SELECT points FROM scores WHERE player='Alice'")
    return cur.fetchone()[0] == 120

medium = Task(
    "Verify Alice's points are now 120.",
    verify_medium, Level.MEDIUM,
    hints=["cur.execute('SELECT points FROM scores WHERE player = ?', ('Alice',))"]
)

def verify_hard(cur, conn):
    cur.execute("DELETE FROM scores WHERE player = 'Charlie'")
    conn.commit()
    cur.execute("SELECT COUNT(*) FROM scores")
    return cur.fetchone()[0] == 2

hard = Task(
    "Delete Charlie from the table, then confirm only 2 rows remain.",
    verify_hard, Level.HARD,
    hints=["cur.execute('DELETE FROM scores WHERE player = ?', ('Charlie',))", "conn.commit()"]
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
