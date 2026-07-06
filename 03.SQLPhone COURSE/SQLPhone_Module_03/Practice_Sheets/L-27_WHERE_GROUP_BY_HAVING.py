import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("SELECT COUNT(*) FROM transactions")
    return cur.fetchone()[0] >= 3

easy = Task("Create table 'transactions' (id, client, amount, status). Insert rows with status 'paid' and 'pending', various amounts.",
            verify_easy, Level.EASY,
            hints=["CREATE TABLE transactions (id INTEGER PRIMARY KEY, client TEXT, amount REAL, status TEXT);",
                   "INSERT INTO transactions (client, amount, status) VALUES ('A',100,'paid'),('A',50,'pending'),('B',200,'paid'),('B',30,'pending');"])

def verify_medium(cur, conn):
    cur.execute("""
        SELECT client, SUM(amount) as total
        FROM transactions
        WHERE status='paid'
        GROUP BY client
        HAVING total > 100
    """)
    return len(cur.fetchall()) > 0

medium = Task("Show total amount per client for paid transactions, only for clients with total > 100.",
              verify_medium, Level.MEDIUM,
              hints=["SELECT client, SUM(amount) FROM transactions WHERE status='paid' GROUP BY client HAVING SUM(amount) > 100;"])

def verify_hard(cur, conn):
    cur.execute("""
        SELECT client, COUNT(*) as cnt, SUM(amount) as total
        FROM transactions
        WHERE status='paid'
        GROUP BY client
        HAVING cnt >= 2 AND total > 150
    """)
    return len(cur.fetchall()) > 0

hard = Task("Show clients with at least 2 paid transactions and total paid > 150.",
            verify_hard, Level.HARD,
            hints=["SELECT client, COUNT(*), SUM(amount) FROM transactions WHERE status='paid' GROUP BY client HAVING COUNT(*) >= 2 AND SUM(amount) > 150;"])

def main():
    print("1 Easy  2 Medium  3 Hard")
    c=input("> ")
    tasks = {"1":easy,"2":medium,"3":hard}
    run_task(tasks.get(c,easy))
if __name__=="__main__": main()
