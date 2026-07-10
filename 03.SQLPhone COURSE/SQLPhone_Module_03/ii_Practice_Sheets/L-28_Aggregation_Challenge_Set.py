import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("SELECT COUNT(*) FROM sales")
    return cur.fetchone()[0] >= 6

easy = Task("Create table 'sales' (id, product, category, quantity, price, sale_date). Insert at least 6 rows with varied data covering multiple months of 2026.",
            verify_easy, Level.EASY,
            hints=["CREATE TABLE sales (id INTEGER PRIMARY KEY, product TEXT, category TEXT, quantity INTEGER, price REAL, sale_date TEXT);",
                   "INSERT INTO sales (product, category, quantity, price, sale_date) VALUES ('P1','Cat1',5,10,'2026-01-15'),('P2','Cat2',3,20,'2026-02-20'),('P1','Cat1',8,10,'2026-01-25'),('P3','Cat1',2,30,'2026-03-10'),('P2','Cat2',4,20,'2026-02-05'),('P3','Cat1',1,30,'2026-03-22');"])

def verify_medium(cur, conn):
    try:
        cur.execute("SELECT COUNT(*) FROM sales")
        cur.execute("SELECT product, SUM(quantity) FROM sales GROUP BY product")
        cur.execute("SELECT category, AVG(price) FROM sales GROUP BY category")
        cur.execute("SELECT category, SUM(quantity*price) as rev FROM sales GROUP BY category HAVING rev > 100")
        return True
    except:
        return False

medium = Task("Write the five required queries from the lecture: count total records, total quantity per product, average price per category, categories with revenue > 100, month and sales count for months in 2026.",
              verify_medium, Level.MEDIUM,
              hints=["1: SELECT COUNT(*) FROM sales;",
                     "2: SELECT product, SUM(quantity) FROM sales GROUP BY product;",
                     "3: SELECT category, AVG(price) FROM sales GROUP BY category;",
                     "4: SELECT category, SUM(quantity*price) FROM sales GROUP BY category HAVING SUM(quantity*price) > 100;",
                     "5: SELECT strftime('%m', sale_date) as month, COUNT(*) FROM sales WHERE sale_date LIKE '2026%' GROUP BY month HAVING COUNT(*) > 1;"])

def verify_hard(cur, conn):
    cur.execute("""
        SELECT category,
               SUM(quantity*price) as revenue,
               AVG(quantity*price) as avg_order
        FROM sales
        WHERE sale_date BETWEEN '2026-01-01' AND '2026-03-31'
        GROUP BY category
        HAVING revenue > 150
        ORDER BY revenue DESC
    """)
    return len(cur.fetchall()) > 0

hard = Task("For Q1 2026, show revenue per category and average order value, only for categories with revenue > 150, sorted by revenue descending.",
            verify_hard, Level.HARD,
            hints=["SELECT category, SUM(quantity*price) as revenue, AVG(quantity*price) as avg_order FROM sales WHERE sale_date BETWEEN '2026-01-01' AND '2026-03-31' GROUP BY category HAVING revenue > 150 ORDER BY revenue DESC;"])


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

if __name__=="__main__": main()
