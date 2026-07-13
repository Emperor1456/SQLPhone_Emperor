import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🧱  BEGIN + COMMIT – Atomic Salary Update\n\n"
        "The `soldiers` table has 4 rows.\n"
        "Start a transaction with BEGIN.\n"
        "Give Hasan a 10% raise: SET salary = salary * 1.1.\n"
        "COMMIT the transaction.\n"
        "Then SELECT the updated row to confirm.\n\n"
        "Expected output:\n[(4, 'Hasan', 'Private', 3850.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Ali','General',4500), (4,'Hasan','Private',3500);"
    ),
    expected_output="[(4, 'Hasan', 'Private', 3850.0)]",
    level=Level.EASY,
    hints=[
        "BEGIN;",
        "UPDATE soldiers SET salary = salary * 1.1 WHERE id = 4;",
        "COMMIT;",
        "SELECT * FROM soldiers WHERE id = 4;"
    ]
)

easy2 = Task(
    description=(
        "🔄  ROLLBACK – Undo a Mistake\n\n"
        "The `soldiers` table has 4 rows.\n"
        "Start a transaction with BEGIN.\n"
        "Give EVERYONE a 50% raise (intentionally wrong).\n"
        "ROLLBACK the transaction.\n"
        "Then SELECT all rows to verify nothing changed.\n\n"
        "Expected output:\n[(1,'Emperor','General',5000.0), (2,'Rahim','Colonel',4000.0), (3,'Ali','General',4500.0), (4,'Hasan','Private',3500.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Ali','General',4500), (4,'Hasan','Private',3500);"
    ),
    expected_output="[(1, 'Emperor', 'General', 5000.0), (2, 'Rahim', 'Colonel', 4000.0), (3, 'Ali', 'General', 4500.0), (4, 'Hasan', 'Private', 3500.0)]",
    level=Level.EASY,
    hints=[
        "BEGIN;",
        "UPDATE soldiers SET salary = salary * 1.5;",
        "ROLLBACK;",
        "SELECT * FROM soldiers ORDER BY id;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "💰  Money Transfer – Two UPDATEs\n\n"
        "Create a table `accounts` with columns\n"
        "  id INTEGER, holder TEXT, balance REAL.\n"
        "Insert two accounts: Emperor (1000), Rahim (500).\n"
        "Use a transaction to transfer 300 from Emperor to Rahim:\n"
        "  • Decrease Emperor's balance by 300\n"
        "  • Increase Rahim's balance by 300\n"
        "COMMIT, then SELECT both accounts.\n\n"
        "Expected output:\n[(1,'Emperor',700.0), (2,'Rahim',800.0)]"
    ),
    expected_output="[(1, 'Emperor', 700.0), (2, 'Rahim', 800.0)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE accounts (id INTEGER, holder TEXT, balance REAL);",
        "INSERT INTO accounts VALUES (1,'Emperor',1000), (2,'Rahim',500);",
        "BEGIN;",
        "UPDATE accounts SET balance = balance - 300 WHERE id = 1;",
        "UPDATE accounts SET balance = balance + 300 WHERE id = 2;",
        "COMMIT;",
        "SELECT * FROM accounts ORDER BY id;"
    ]
)

medium2 = Task(
    description=(
        "⚠️  Transfer with Rollback – Insufficient Funds\n\n"
        "Same `accounts` table (Emperor=1000, Rahim=500).\n"
        "Use a transaction to attempt a transfer of 2000\n"
        "from Emperor to Rahim. But first, check if\n"
        "Emperor has enough balance (you can't with pure SQL,\n"
        "so simulate: try the deduction, and if Emperor goes\n"
        "negative, ROLLBACK.\n"
        "Since 1000 - 2000 < 0, rollback the transaction.\n"
        "Show final balances unchanged.\n\n"
        "Expected output:\n[(1,'Emperor',1000.0), (2,'Rahim',500.0)]"
    ),
    setup_sql=(
        "CREATE TABLE accounts (id INTEGER, holder TEXT, balance REAL);"
        "INSERT INTO accounts VALUES (1,'Emperor',1000), (2,'Rahim',500);"
    ),
    expected_output="[(1, 'Emperor', 1000.0), (2, 'Rahim', 500.0)]",
    level=Level.MEDIUM,
    hints=[
        "BEGIN;",
        "UPDATE accounts SET balance = balance - 2000 WHERE id = 1;",
        "SELECT balance FROM accounts WHERE id = 1; -- check if negative",
        "ROLLBACK;",
        "SELECT * FROM accounts ORDER BY id;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "💾  SAVEPOINT – Partial Rollback\n\n"
        "Create a table `inventory` with columns\n"
        "  id INTEGER, item TEXT, qty INTEGER.\n"
        "Insert three items: Sword(10), Shield(5), Bow(8).\n"
        "Start a transaction with BEGIN.\n"
        "Update Sword to 15.\n"
        "Create a SAVEPOINT named `before_shield`.\n"
        "Update Shield to 0 (mistake – should be 10).\n"
        "ROLLBACK TO before_shield (undo only the Shield change).\n"
        "Update Shield to 12 (correct amount).\n"
        "COMMIT the whole transaction.\n"
        "Show final inventory.\n\n"
        "Expected output:\n[(1,'Sword',15), (2,'Shield',12), (3,'Bow',8)]"
    ),
    expected_output="[(1, 'Sword', 15), (2, 'Shield', 12), (3, 'Bow', 8)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE inventory (id INTEGER, item TEXT, qty INTEGER);",
        "INSERT INTO inventory VALUES (1,'Sword',10), (2,'Shield',5), (3,'Bow',8);",
        "BEGIN;",
        "UPDATE inventory SET qty = 15 WHERE id = 1;",
        "SAVEPOINT before_shield;",
        "UPDATE inventory SET qty = 0 WHERE id = 2;",
        "ROLLBACK TO before_shield;",
        "UPDATE inventory SET qty = 12 WHERE id = 2;",
        "COMMIT;",
        "SELECT * FROM inventory ORDER BY id;"
    ]
)

hard2 = Task(
    description=(
        "📊  Bulk Insert Performance – Transaction Wrapping\n\n"
        "Create a table `log` with columns id INTEGER PRIMARY KEY,\n"
        "message TEXT.\n"
        "Insert 5 rows WITHOUT an explicit transaction.\n"
        "Then insert 5 MORE rows wrapped in BEGIN...COMMIT.\n"
        "(Both should insert successfully, but the second batch\n"
        "is faster because all writes happen at COMMIT.)\n"
        "Show the total row count.\n\n"
        "Expected output: [(10,)]"
    ),
    expected_output="[(10,)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE log (id INTEGER PRIMARY KEY, message TEXT);",
        "INSERT INTO log (message) VALUES ('msg1'), ('msg2'), ('msg3'), ('msg4'), ('msg5');",
        "BEGIN;",
        "INSERT INTO log (message) VALUES ('msg6'), ('msg7'), ('msg8'), ('msg9'), ('msg10');",
        "COMMIT;",
        "SELECT COUNT(*) FROM log;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L58.json",
        module_name="Module_06_Modifying_Data_Schema",
        lesson_name="L58_Transactions"
    )
