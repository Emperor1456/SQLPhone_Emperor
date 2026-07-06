import sys, sqlite3, os
sys.path.append("../..")
from practice_engine import Task, Level, run_task

DB = "movies.db"

def verify_easy(cur, conn):
    for tbl in ['User','Movie','Rating']:
        cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{tbl}'")
        if not cur.fetchone():
            return False
    return True

easy = Task(
    "Create User, Movie, Rating tables. Rating must have composite PK (user_id, movie_id) and a CHECK rating BETWEEN 1 AND 5.",
    verify_easy, Level.EASY,
    hints=["CREATE TABLE User(id INTEGER PRIMARY KEY, username TEXT);",
           "CREATE TABLE Movie(id INTEGER PRIMARY KEY, title TEXT, release_year INTEGER);",
           "CREATE TABLE Rating(user_id INTEGER, movie_id INTEGER, rating INTEGER CHECK(rating BETWEEN 1 AND 5), review_text TEXT, PRIMARY KEY(user_id, movie_id), FOREIGN KEY(user_id) REFERENCES User(id), FOREIGN KEY(movie_id) REFERENCES Movie(id));"]
)

def verify_medium(cur, conn):
    for tbl in ['User','Movie','Rating']:
        cur.execute(f"SELECT COUNT(*) FROM {tbl}")
        if cur.fetchone()[0] < 3:
            return False
    cur.execute("SELECT m.title, AVG(r.rating) FROM Movie m JOIN Rating r ON m.id=r.movie_id GROUP BY m.id HAVING AVG(r.rating) >= 4")
    return len(cur.fetchall()) > 0

medium = Task(
    "Insert 5 users, 5 movies, diverse ratings. Show top‑rated movies (average >= 4).",
    verify_medium, Level.MEDIUM,
    hints=["Use AVG(rating) and HAVING."]
)

def verify_hard(cur, conn):
    cur.execute("SELECT u.username, COUNT(r.movie_id) as cnt FROM User u JOIN Rating r ON u.id=r.user_id GROUP BY u.id HAVING cnt > 3")
    rows = cur.fetchall()
    return len(rows) >= 0

hard = Task(
    "Find users who have rated more than 3 movies.",
    verify_hard, Level.HARD,
    hints=["GROUP BY user, HAVING COUNT > 3."]
)

def main():
    if os.path.exists(DB): os.remove(DB)
    print("1 Easy  2 Medium  3 Hard")
    c = input("> ")
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))
if __name__ == "__main__": main()
