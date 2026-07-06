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
    print("1 Easy  2 Medium  3 Hard")
    c = input("> ")
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))
if __name__ == "__main__": main()
