import sys, sqlite3, os
sys.path.append("../..")
from practice_engine import Task, Level, run_task

DB = "expenses.db"

def verify_easy(cur, conn):
    for tbl in ['Category','Expense']:
        cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{tbl}'")
        if not cur.fetchone():
            return False
    return True

easy = Task(
    "Create Category and Expense tables. Include CHECK (amount > 0) and a date column.",
    verify_easy, Level.EASY,
    hints=["CREATE TABLE Category(id INTEGER PRIMARY KEY, name TEXT);",
           "CREATE TABLE Expense(id INTEGER PRIMARY KEY, amount REAL CHECK(amount>0), category_id INTEGER, expense_date TEXT, description TEXT, FOREIGN KEY(category_id) REFERENCES Category(id));"]
)

def verify_medium(cur, conn):
    cur.execute("SELECT COUNT(*) FROM Expense")
    if cur.fetchone()[0] < 20:
        return False
    cur.execute("SELECT strftime('%Y-%m', expense_date) AS month, SUM(amount) FROM Expense GROUP BY month")
    return len(cur.fetchall()) >= 2

medium = Task(
    "Insert at least 20 expenses across different categories and months. Show total expenses per month.",
    verify_medium, Level.MEDIUM,
    hints=["Use strftime('%Y-%m', expense_date) and GROUP BY."]
)

def verify_hard(cur, conn):
    cur.execute("SELECT c.name, SUM(e.amount) as total FROM Category c JOIN Expense e ON c.id=e.category_id WHERE expense_date BETWEEN '2026-01-01' AND '2026-06-30' GROUP BY c.name ORDER BY total DESC LIMIT 3")
    rows = cur.fetchall()
    return len(rows) >= 1

hard = Task(
    "Find the top 3 categories by total spend in the first half of 2026.",
    verify_hard, Level.HARD,
    hints=["Filter date range, GROUP BY category, ORDER BY SUM DESC LIMIT 3."]
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
