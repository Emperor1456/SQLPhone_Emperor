import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE profiles(username TEXT, bio TEXT, avatar_url TEXT)")
    cur.executemany("INSERT INTO profiles VALUES (?,?,?)", [('alice','I love SQL','a.png'),('bob',NULL,NULL),('charlie','Hello',NULL)])
    return True

easy = Task("We have 'profiles'. Write a query that displays username, bio (or 'No bio' if NULL), and avatar (or 'default.png' if NULL) using COALESCE.",
            verify_easy, Level.EASY,
            hints=["SELECT username, COALESCE(bio, 'No bio'), COALESCE(avatar_url, 'default.png') FROM profiles;"])

def verify_medium(cur, conn):
    cur.execute("SELECT username, COALESCE(bio, 'No bio'), COALESCE(avatar_url, 'default.png') FROM profiles")
    rows = cur.fetchall()
    return rows[1][1] == 'No bio' and rows[1][2] == 'default.png'

medium = Task("Bob's row should show 'No bio' and 'default.png'.",
              verify_medium, Level.MEDIUM,
              hints=["Use COALESCE for both columns."])

def verify_hard(cur, conn):
    cur.execute("SELECT COUNT(*), COALESCE(avatar_url, 'none') AS avatar FROM profiles GROUP BY avatar")
    rows = cur.fetchall()
    return len(rows) >= 2

hard = Task("Group by avatar status (COALESCE to 'none') and count.",
            verify_hard, Level.HARD,
            hints=["SELECT COUNT(*), COALESCE(avatar_url, 'none') FROM profiles GROUP BY COALESCE(avatar_url, 'none');"])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
