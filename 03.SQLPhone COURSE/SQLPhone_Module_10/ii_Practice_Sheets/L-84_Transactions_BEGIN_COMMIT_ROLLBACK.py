import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(cur, conn):
    cur.execute("CREATE TABLE accounts(id INTEGER PRIMARY KEY, balance REAL)")
    cur.executemany("INSERT INTO accounts(id, balance) VALUES (?,?)", [(1,100.0),(2,100.0)])
    return True

easy = Task(
    "We have two accounts with 100 each. Write a transaction that transfers 50 from account 1 to account 2.",
    verify_easy, Level.EASY,
    hints=["BEGIN; UPDATE accounts SET balance = balance - 50 WHERE id=1; UPDATE accounts SET balance = balance + 50 WHERE id=2; COMMIT;"]
)

def verify_medium(cur, conn):
    cur.execute("SELECT balance FROM accounts WHERE id=1")
    bal1 = cur.fetchone()[0]
    cur.execute("SELECT balance FROM accounts WHERE id=2")
    bal2 = cur.fetchone()[0]
    return bal1 == 50.0 and bal2 == 150.0

medium = Task(
    "After transfer, account 1 should have 50 and account 2 should have 150.",
    verify_medium, Level.MEDIUM,
    hints=["Use COMMIT and then SELECT to verify."]
)

def verify_hard(cur, conn):
    # Simulate insufficient funds: transfer 200 from account 1, which will go negative unless CHECK exists; we'll add CHECK.
    cur.execute("CREATE TABLE accounts_strict(id INTEGER PRIMARY KEY, balance REAL CHECK(balance >= 0))")
    cur.executemany("INSERT INTO accounts_strict VALUES (?,?)", [(1,100.0),(2,100.0)])
    try:
        cur.execute("BEGIN; UPDATE accounts_strict SET balance = balance - 200 WHERE id=1; UPDATE accounts_strict SET balance = balance + 200 WHERE id=2; COMMIT;")
        return False
    except:
        cur.execute("ROLLBACK;")
        cur.execute("SELECT balance FROM accounts_strict WHERE id=1")
        return cur.fetchone()[0] == 100.0

hard = Task(
    "Create a new table 'accounts_strict' with a CHECK(balance>=0). Try a transfer of 200 from account 1; it should fail and rollback.",
    verify_hard, Level.HARD,
    hints=["Use BEGIN, try UPDATE, catch error, ROLLBACK."]
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
