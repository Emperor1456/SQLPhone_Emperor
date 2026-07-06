import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE authors(id INTEGER PRIMARY KEY, name TEXT)")
    cur.execute("CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT, author_id INTEGER)")
    cur.execute("CREATE TABLE reviews(id INTEGER PRIMARY KEY, book_id INTEGER, reviewer_name TEXT)")
    cur.executemany("INSERT INTO authors VALUES (?,?)", [(1,'Author A'),(2,'Author B')])
    cur.executemany("INSERT INTO books VALUES (?,?,?)", [(1,'Book X',1),(2,'Book Y',2)])
    cur.executemany("INSERT INTO reviews VALUES (?,?,?)", [(1,1,'Alice'),(2,1,'Bob'),(3,2,'Charlie')])
    return True

easy = Task("We have authors, books, reviews. Write a query that returns book title, author name, and reviewer name for all reviews (joining 3 tables).",
            verify_easy, Level.EASY,
            hints=["SELECT b.title, a.name, r.reviewer_name FROM reviews r JOIN books b ON r.book_id = b.id JOIN authors a ON b.author_id = a.id;"])

def verify_medium(cur, conn):
    cur.execute("SELECT b.title, a.name, r.reviewer_name FROM reviews r JOIN books b ON r.book_id = b.id JOIN authors a ON b.author_id = a.id")
    rows = cur.fetchall()
    return len(rows) == 3

medium = Task("Your join should return exactly 3 rows (one per review).",
              verify_medium, Level.MEDIUM,
              hints=["Check the join order: reviews -> books -> authors."])

def verify_hard(cur, conn):
    cur.execute("""
        SELECT a.name, COUNT(r.id) as review_count
        FROM authors a
        JOIN books b ON a.id = b.author_id
        JOIN reviews r ON b.id = r.book_id
        GROUP BY a.name
        ORDER BY review_count DESC
    """)
    rows = cur.fetchall()
    return len(rows) >= 1 and rows[0][1] >= 2

hard = Task("Show the number of reviews each author has received, sorted by most reviews first.",
            verify_hard, Level.HARD,
            hints=["SELECT a.name, COUNT(r.id) FROM authors a JOIN books b ON a.id = b.author_id JOIN reviews r ON b.id = r.book_id GROUP BY a.name ORDER BY COUNT(r.id) DESC;"])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
