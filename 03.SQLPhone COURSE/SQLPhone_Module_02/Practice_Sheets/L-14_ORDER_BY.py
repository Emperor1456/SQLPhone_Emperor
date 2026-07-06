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
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
