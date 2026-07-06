import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE memberships(user_id INTEGER, group_id INTEGER, joined_date TEXT, PRIMARY KEY(user_id, group_id))")
    return True

easy = Task("Create a junction table 'memberships' with composite primary key (user_id, group_id).",
            verify_easy, Level.EASY,
            hints=["CREATE TABLE memberships(user_id INTEGER, group_id INTEGER, joined_date TEXT, PRIMARY KEY(user_id, group_id));"])

def verify_medium(cur, conn):
    cur.execute("INSERT INTO memberships VALUES (1, 1, date('now'))")
    cur.execute("INSERT INTO memberships VALUES (1, 2, date('now'))")
    try:
        cur.execute("INSERT INTO memberships VALUES (1, 1, date('now'))")
        return False
    except sqlite3.IntegrityError:
        return True

medium = Task("Insert two valid rows, then try inserting a duplicate (1,1) pair. Should be rejected.",
              verify_medium, Level.MEDIUM,
              hints=["First INSERT (1,1), then (1,2), then (1,1) again."])

def verify_hard(cur, conn):
    cur.execute("SELECT COUNT(*) FROM memberships")
    return cur.fetchone()[0] == 2

hard = Task("Confirm only 2 rows exist (duplicate rejected).",
            verify_hard, Level.HARD,
            hints=["SELECT COUNT(*) FROM memberships;"])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
