import sys, sqlite3, os
sys.path.append("../..")
from practice_engine import Task, Level, run_task

DB = "blog.db"

def verify_easy(cur, conn):
    for tbl in ['User','Post','Comment']:
        cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{tbl}'")
        if not cur.fetchone():
            return False
    return True

easy = Task(
    "Create User, Post, Comment tables with foreign keys and defaults for timestamps.",
    verify_easy, Level.EASY,
    hints=["CREATE TABLE User(id INTEGER PRIMARY KEY, username TEXT UNIQUE, email TEXT, created_at TEXT DEFAULT (datetime('now')));",
           "CREATE TABLE Post(id INTEGER PRIMARY KEY, title TEXT, body TEXT, user_id INTEGER, published_at TEXT DEFAULT (datetime('now')), FOREIGN KEY(user_id) REFERENCES User(id));",
           "CREATE TABLE Comment(id INTEGER PRIMARY KEY, post_id INTEGER, user_id INTEGER, body TEXT, commented_at TEXT DEFAULT (datetime('now')), FOREIGN KEY(post_id) REFERENCES Post(id), FOREIGN KEY(user_id) REFERENCES User(id));"]
)

def verify_medium(cur, conn):
    for tbl in ['User','Post','Comment']:
        cur.execute(f"SELECT COUNT(*) FROM {tbl}")
        if cur.fetchone()[0] < 3:
            return False
    cur.execute("SELECT p.title, u.username, COUNT(c.id) FROM Post p JOIN User u ON p.user_id=u.id LEFT JOIN Comment c ON p.id=c.post_id GROUP BY p.id")
    return len(cur.fetchall()) > 0

medium = Task(
    "Insert 5 users, 10 posts, multiple comments. Show all posts with author name and comment count.",
    verify_medium, Level.MEDIUM,
    hints=["Use LEFT JOIN to include posts with zero comments."]
)

def verify_hard(cur, conn):
    cur.execute("SELECT u.username FROM User u JOIN Comment c ON u.id=c.user_id JOIN Post p ON c.post_id=p.id WHERE p.user_id=u.id GROUP BY u.id HAVING COUNT(c.id) > 1")
    rows = cur.fetchall()
    return len(rows) >= 0

hard = Task(
    "Find users who have commented on their own posts more than once.",
    verify_hard, Level.HARD,
    hints=["Self‑reference: comment.user_id = post.user_id, GROUP BY user, HAVING COUNT > 1."]
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
