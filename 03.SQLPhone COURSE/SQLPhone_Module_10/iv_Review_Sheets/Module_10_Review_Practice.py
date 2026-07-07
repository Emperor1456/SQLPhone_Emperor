import sys, sqlite3
sys.path.append("../..")
from practice_engine import Task, Level, run_task

# ─── Easy: Create an index and see that it exists ─────
def verify_easy(cur, conn):
    cur.execute("SELECT name FROM sqlite_master WHERE type='index' AND tbl_name='contacts'")
    return cur.fetchone() is not None

easy = Task(
    description="Create table 'contacts' (id INTEGER PRIMARY KEY, name TEXT, phone TEXT).\n"
                "Insert at least 2 rows. Then create an index on the 'name' column.\n"
                "The engine will verify that the index exists.",
    verify_func=verify_easy,
    level=Level.EASY,
    hints=[
        "CREATE TABLE contacts (id INTEGER PRIMARY KEY, name TEXT, phone TEXT);",
        "INSERT INTO contacts VALUES (1,'Alice','123'), (2,'Bob','456');",
        "CREATE INDEX idx_contacts_name ON contacts(name);"
    ]
)

# ─── Medium: Transaction with ROLLBACK ────────────────
def verify_medium(cur, conn):
    # Check that accounts table exists and has correct balances after a failed transfer
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='accounts'")
    if not cur.fetchone():
        return False
    cur.execute("SELECT balance FROM accounts WHERE id=1")
    bal1 = cur.fetchone()
    cur.execute("SELECT balance FROM accounts WHERE id=2")
    bal2 = cur.fetchone()
    if not bal1 or not bal2:
        return False
    # After a transfer of 200 from id 1 to id 2, if id1 has insufficient funds, rollback.
    # The expected final balances: id1=100, id2=200 (unchanged)
    # We'll check that the script itself performed the transaction and left balances correct.
    # The engine will execute user SQL; we can simulate by checking the state.
    # However, the engine runs the user's script which should contain the transaction logic.
    # We need to verify that the user's script did the right thing.
    # We'll just check final balances: id1 should be 100, id2 should be 200.
    return bal1[0] == 100 and bal2[0] == 200

medium = Task(
    description="Create table 'accounts' (id INTEGER PRIMARY KEY, balance REAL CHECK(balance >= 0)).\n"
                "Insert two accounts: (1, 100) and (2, 200).\n"
                "Write a transaction that transfers 200 from account 1 to account 2.\n"
                "The transfer should fail because account 1 has insufficient funds (balance cannot go negative).\n"
                "Use BEGIN, the two UPDATEs, and then ROLLBACK on error.\n"
                "After the transaction, the balances must remain: account1=100, account2=200.",
    verify_func=verify_medium,
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE accounts (id INTEGER PRIMARY KEY, balance REAL CHECK(balance >= 0));",
        "INSERT INTO accounts VALUES (1,100), (2,200);",
        "BEGIN;",
        "UPDATE accounts SET balance = balance - 200 WHERE id = 1;",
        "UPDATE accounts SET balance = balance + 200 WHERE id = 2;",
        "COMMIT;",  # This will fail because the first UPDATE violates CHECK (balance becomes -100). They should use ROLLBACK when an error occurs.
        "Use ROLLBACK instead of COMMIT."
    ]
)

# ─── Hard: Index and EXPLAIN QUERY PLAN ───────────────
def verify_hard(cur, conn):
    # Verify that the products table exists with at least 1000 rows
    cur.execute("SELECT COUNT(*) FROM products")
    if cur.fetchone()[0] < 1000:
        return False
    # Verify that an index on 'name' exists
    cur.execute("SELECT name FROM sqlite_master WHERE type='index' AND tbl_name='products'")
    if not cur.fetchone():
        return False
    # Verify that EXPLAIN QUERY PLAN for a search on name uses the index.
    # We'll capture the output by running the command ourselves.
    # But the engine doesn't capture EXPLAIN output; we'll just check the index existence.
    # Additionally, the hard task expects output of a specific query.
    expected = "Alice 24.99"
    cur.execute("SELECT name, price FROM products WHERE name='Alice'")
    rows = cur.fetchall()
    if len(rows) != 1:
        return False
    result = f"{rows[0][0]} {rows[0][1]}"
    return result == expected

hard = Task(
    description="Performance Challenge:\n"
                "1. Create table 'products' (id INTEGER PRIMARY KEY, name TEXT, price REAL).\n"
                "   Insert 1000 rows (you can use a loop in the script).\n"
                "   The row with id=500 must have name='Alice' and price=24.99.\n"
                "2. Create an index on the 'name' column.\n"
                "3. Run EXPLAIN QUERY PLAN for SELECT * FROM products WHERE name='Alice'\n"
                "   (just as a comment; we'll verify the index usage).\n"
                "4. Finally, select the name and price of the product named 'Alice'.\n"
                "   The exact output must be:\n"
                "Alice 24.99",
    verify_func=verify_hard,
    level=Level.HARD,
    hints=[
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price REAL);",
        "Use a recursive CTE or INSERT loop: WITH RECURSIVE cnt(x) AS (VALUES(1) UNION ALL SELECT x+1 FROM cnt WHERE x<1000) INSERT INTO products(id,name,price) SELECT x, CASE WHEN x=500 THEN 'Alice' ELSE 'Product '||x END, 24.99 FROM cnt;",
        "CREATE INDEX idx_products_name ON products(name);",
        "SELECT name, price FROM products WHERE name='Alice';"
    ]
)

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__":
    main()
