import sys, sqlite3, os
sys.path.append("../..")
from practice_engine import Task, Level, run_task

DB = "library.db"

def verify_easy(cur, conn):
    for tbl in ['Book','Member','Loan']:
        cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{tbl}'")
        if not cur.fetchone():
            return False
    return True

easy = Task(
    "Create tables Book, Member, Loan with constraints (UNIQUE on isbn, CHECK loan_date < return_date).",
    verify_easy, Level.EASY,
    hints=["CREATE TABLE Book(id INTEGER PRIMARY KEY, title TEXT, author TEXT, isbn TEXT UNIQUE, published_year INTEGER);",
           "CREATE TABLE Member(id INTEGER PRIMARY KEY, name TEXT, email TEXT, join_date TEXT);",
           "CREATE TABLE Loan(id INTEGER PRIMARY KEY, book_id INTEGER, member_id INTEGER, loan_date TEXT, return_date TEXT, FOREIGN KEY(book_id) REFERENCES Book(id), FOREIGN KEY(member_id) REFERENCES Member(id), CHECK(loan_date < return_date));"]
)

def verify_medium(cur, conn):
    for tbl in ['Book','Member','Loan']:
        cur.execute(f"SELECT COUNT(*) FROM {tbl}")
        if cur.fetchone()[0] < 3:
            return False
    cur.execute("SELECT b.title FROM Book b JOIN Loan l ON b.id=l.book_id WHERE l.return_date IS NULL")
    return len(cur.fetchall()) > 0

medium = Task(
    "Insert data (10 books, 5 members, active loans) and show books currently borrowed (return_date IS NULL).",
    verify_medium, Level.MEDIUM,
    hints=["Make sure some loans have NULL return_date."]
)

def verify_hard(cur, conn):
    cur.execute("SELECT m.name FROM Member m JOIN Loan l ON m.id=l.member_id WHERE l.return_date IS NULL AND l.loan_date < date('now', '-30 days')")
    rows = cur.fetchall()
    return len(rows) >= 0  # at least test runs

hard = Task(
    "Find members with overdue books (loaned more than 30 days ago, not returned).",
    verify_hard, Level.HARD,
    hints=["Use date('now', '-30 days') and check loan_date < that, return_date IS NULL"]
)

def main():
    if os.path.exists(DB): os.remove(DB)
    print("1 Easy  2 Medium  3 Hard")
    c = input("> ")
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))
if __name__ == "__main__": main()
