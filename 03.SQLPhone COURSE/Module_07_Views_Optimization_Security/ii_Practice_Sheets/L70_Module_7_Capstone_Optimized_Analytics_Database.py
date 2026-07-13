import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🏗️  Imperial Analytics – Build Core Schema\n\n"
        "Create four tables with full constraints:\n\n"
        "1. `regions`:\n"
        "  • region_id INTEGER PRIMARY KEY\n"
        "  • region_name TEXT UNIQUE\n\n"
        "2. `branches`:\n"
        "  • branch_id INTEGER PRIMARY KEY\n"
        "  • branch_name TEXT\n"
        "  • region_id INTEGER REFERENCES regions(region_id)\n\n"
        "3. `accounts`:\n"
        "  • account_id INTEGER PRIMARY KEY\n"
        "  • branch_id INTEGER REFERENCES branches(branch_id)\n"
        "  • balance REAL CHECK(balance >= 0)\n\n"
        "4. `transactions`:\n"
        "  • txn_id INTEGER PRIMARY KEY\n"
        "  • account_id INTEGER REFERENCES accounts(account_id)\n"
        "  • amount REAL\n"
        "  • txn_date TEXT DEFAULT (date('now'))\n\n"
        "Insert seed data:\n"
        "  Regions: North, South\n"
        "  Branches: Dhaka (North), Chittagong (South)\n"
        "  Accounts: Emperor (Dhaka, 5000), Rahim (Chittagong, 3000)\n"
        "  Transactions: Emperor deposit 1000, Emperor withdrawal -200,\n"
        "    Rahim deposit 500\n\n"
        "Then SELECT all region names, sorted alphabetically.\n\n"
        "Expected output: [('North',), ('South',)]"
    ),
    expected_output="[('North',), ('South',)]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE regions (region_id INTEGER PRIMARY KEY, region_name TEXT UNIQUE);",
        "INSERT INTO regions VALUES (1,'North'), (2,'South');",
        "CREATE TABLE branches (branch_id INTEGER PRIMARY KEY, branch_name TEXT, region_id INTEGER REFERENCES regions(region_id));",
        "INSERT INTO branches VALUES (1,'Dhaka',1), (2,'Chittagong',2);",
        "CREATE TABLE accounts (account_id INTEGER PRIMARY KEY, branch_id INTEGER REFERENCES branches(branch_id), balance REAL CHECK(balance >= 0));",
        "INSERT INTO accounts VALUES (1,1,5000), (2,2,3000);",
        "CREATE TABLE transactions (txn_id INTEGER PRIMARY KEY, account_id INTEGER REFERENCES accounts(account_id), amount REAL, txn_date TEXT DEFAULT (date('now')));",
        "INSERT INTO transactions (account_id, amount, txn_date) VALUES (1,1000,'2026-07-01'), (1,-200,'2026-07-02'), (2,500,'2026-07-03');",
        "SELECT region_name FROM regions ORDER BY region_name;"
    ]
)

easy2 = Task(
    description=(
        "📊  Branch Summary View – JOIN + Aggregation\n\n"
        "Using the seeded tables, create a view named\n"
        "`v_branch_summary` that shows:\n"
        "  • branch_name\n"
        "  • region_name\n"
        "  • total_accounts (COUNT of accounts)\n"
        "  • total_balance (SUM of balances)\n\n"
        "Join branches → regions → accounts.\n"
        "Use LEFT JOIN to include branches with no accounts.\n"
        "Then SELECT from the view sorted by branch_name.\n\n"
        "Expected output:\n[('Chittagong','South',1,3000.0), ('Dhaka','North',1,5000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE regions (region_id INTEGER PRIMARY KEY, region_name TEXT UNIQUE);"
        "INSERT INTO regions VALUES (1,'North'), (2,'South');"
        "CREATE TABLE branches (branch_id INTEGER PRIMARY KEY, branch_name TEXT, region_id INTEGER REFERENCES regions(region_id));"
        "INSERT INTO branches VALUES (1,'Dhaka',1), (2,'Chittagong',2);"
        "CREATE TABLE accounts (account_id INTEGER PRIMARY KEY, branch_id INTEGER REFERENCES branches(branch_id), balance REAL CHECK(balance >= 0));"
        "INSERT INTO accounts VALUES (1,1,5000), (2,2,3000);"
        "CREATE TABLE transactions (txn_id INTEGER PRIMARY KEY, account_id INTEGER REFERENCES accounts(account_id), amount REAL, txn_date TEXT DEFAULT (date('now')));"
        "INSERT INTO transactions (account_id, amount, txn_date) VALUES (1,1000,'2026-07-01'), (1,-200,'2026-07-02'), (2,500,'2026-07-03');"
    ),
    expected_output="[('Chittagong', 'South', 1, 3000.0), ('Dhaka', 'North', 1, 5000.0)]",
    level=Level.EASY,
    hints=[
        "CREATE VIEW v_branch_summary AS SELECT b.branch_name, r.region_name, COUNT(a.account_id) AS total_accounts, COALESCE(SUM(a.balance), 0) AS total_balance FROM branches b JOIN regions r ON b.region_id = r.region_id LEFT JOIN accounts a ON b.branch_id = a.branch_id GROUP BY b.branch_id;",
        "SELECT * FROM v_branch_summary ORDER BY branch_name;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "💾  Materialized Summary – Monthly Aggregates\n\n"
        "Create a table `monthly_summary` with columns:\n"
        "  • month TEXT\n"
        "  • branch_id INTEGER\n"
        "  • total_txns INTEGER\n"
        "  • total_amount REAL\n"
        "  • PRIMARY KEY (month, branch_id)\n\n"
        "Populate it with a single INSERT that aggregates\n"
        "transactions by month (strftime) and branch (via\n"
        "accounts). Use the seed data which has 3 transactions\n"
        "all in July 2026, spread across 2 branches.\n\n"
        "Then SELECT from the summary table sorted by month,\n"
        "branch_id.\n\n"
        "Expected output:\n[('2026-07',1,2,800.0), ('2026-07',2,1,500.0)]"
    ),
    setup_sql=(
        "CREATE TABLE regions (region_id INTEGER PRIMARY KEY, region_name TEXT UNIQUE);"
        "INSERT INTO regions VALUES (1,'North'), (2,'South');"
        "CREATE TABLE branches (branch_id INTEGER PRIMARY KEY, branch_name TEXT, region_id INTEGER REFERENCES regions(region_id));"
        "INSERT INTO branches VALUES (1,'Dhaka',1), (2,'Chittagong',2);"
        "CREATE TABLE accounts (account_id INTEGER PRIMARY KEY, branch_id INTEGER REFERENCES branches(branch_id), balance REAL CHECK(balance >= 0));"
        "INSERT INTO accounts VALUES (1,1,5000), (2,2,3000);"
        "CREATE TABLE transactions (txn_id INTEGER PRIMARY KEY, account_id INTEGER REFERENCES accounts(account_id), amount REAL, txn_date TEXT DEFAULT (date('now')));"
        "INSERT INTO transactions (account_id, amount, txn_date) VALUES (1,1000,'2026-07-01'), (1,-200,'2026-07-02'), (2,500,'2026-07-03');"
    ),
    expected_output="[('2026-07', 1, 2, 800.0), ('2026-07', 2, 1, 500.0)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE monthly_summary (month TEXT, branch_id INTEGER, total_txns INTEGER, total_amount REAL, PRIMARY KEY(month, branch_id));",
        "INSERT INTO monthly_summary SELECT strftime('%Y-%m', t.txn_date) AS month, a.branch_id, COUNT(*) AS total_txns, SUM(t.amount) AS total_amount FROM transactions t JOIN accounts a ON t.account_id = a.account_id GROUP BY month, a.branch_id;",
        "SELECT * FROM monthly_summary ORDER BY month, branch_id;"
    ]
)

medium2 = Task(
    description=(
        "⚡  Index for Performance – EXPLAIN\n\n"
        "Create indexes on:\n"
        "  • transactions(account_id)\n"
        "  • transactions(txn_date)\n"
        "Run EXPLAIN QUERY PLAN on a SELECT that JOINs\n"
        "transactions with accounts filtered by account_id.\n"
        "The plan should show SEARCH TABLE transactions\n"
        "USING INDEX idx_transactions_account.\n\n"
        "Expected output:\n[('SEARCH TABLE transactions USING INDEX idx_transactions_account',)]"
    ),
    setup_sql=(
        "CREATE TABLE regions (region_id INTEGER PRIMARY KEY, region_name TEXT UNIQUE);"
        "INSERT INTO regions VALUES (1,'North'), (2,'South');"
        "CREATE TABLE branches (branch_id INTEGER PRIMARY KEY, branch_name TEXT, region_id INTEGER REFERENCES regions(region_id));"
        "INSERT INTO branches VALUES (1,'Dhaka',1), (2,'Chittagong',2);"
        "CREATE TABLE accounts (account_id INTEGER PRIMARY KEY, branch_id INTEGER REFERENCES branches(branch_id), balance REAL CHECK(balance >= 0));"
        "INSERT INTO accounts VALUES (1,1,5000), (2,2,3000);"
        "CREATE TABLE transactions (txn_id INTEGER PRIMARY KEY, account_id INTEGER REFERENCES accounts(account_id), amount REAL, txn_date TEXT DEFAULT (date('now')));"
        "INSERT INTO transactions (account_id, amount, txn_date) VALUES (1,1000,'2026-07-01'), (1,-200,'2026-07-02'), (2,500,'2026-07-03');"
        "CREATE INDEX idx_transactions_account ON transactions(account_id);"
        "CREATE INDEX idx_transactions_date ON transactions(txn_date);"
    ),
    expected_output="[('SEARCH TABLE transactions USING INDEX idx_transactions_account',)]",
    level=Level.MEDIUM,
    hints=[
        "EXPLAIN QUERY PLAN SELECT * FROM transactions WHERE account_id = 1;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🛡️  Secure View – Hide Sensitive Data\n\n"
        "Create a view `v_public_accounts` that shows:\n"
        "  • account_id\n"
        "  • branch_name (via JOIN with branches)\n"
        "  • region_name (via JOIN with regions)\n"
        "but does NOT expose the `balance` column.\n\n"
        "Then write a parameterized SELECT from this view\n"
        "filtering by region_name = ?.\n"
        "Return account_id, branch_name, region_name,\n"
        "sorted by account_id.\n\n"
        "Expected output:\n[(1,'Dhaka','North')]"
    ),
    setup_sql=(
        "CREATE TABLE regions (region_id INTEGER PRIMARY KEY, region_name TEXT UNIQUE);"
        "INSERT INTO regions VALUES (1,'North'), (2,'South');"
        "CREATE TABLE branches (branch_id INTEGER PRIMARY KEY, branch_name TEXT, region_id INTEGER REFERENCES regions(region_id));"
        "INSERT INTO branches VALUES (1,'Dhaka',1), (2,'Chittagong',2);"
        "CREATE TABLE accounts (account_id INTEGER PRIMARY KEY, branch_id INTEGER REFERENCES branches(branch_id), balance REAL CHECK(balance >= 0));"
        "INSERT INTO accounts VALUES (1,1,5000), (2,2,3000);"
        "CREATE TABLE transactions (txn_id INTEGER PRIMARY KEY, account_id INTEGER REFERENCES accounts(account_id), amount REAL, txn_date TEXT DEFAULT (date('now')));"
        "INSERT INTO transactions (account_id, amount, txn_date) VALUES (1,1000,'2026-07-01'), (1,-200,'2026-07-02'), (2,500,'2026-07-03');"
        "CREATE VIEW v_public_accounts AS SELECT a.account_id, b.branch_name, r.region_name FROM accounts a JOIN branches b ON a.branch_id = b.branch_id JOIN regions r ON b.region_id = r.region_id;"
    ),
    expected_output="[(1, 'Dhaka', 'North')]",
    level=Level.HARD,
    hints=[
        "SELECT * FROM v_public_accounts WHERE region_name = ? ORDER BY account_id;",
        "-- Engine supplies: 'North'"
    ]
)

hard2 = Task(
    description=(
        "🔄  Backup & Restore – Disaster Recovery\n\n"
        "Simulate a disaster recovery scenario:\n"
        "  1. Create a backup table `accounts_backup` with the\n"
        "     same columns as `accounts` (account_id, branch_id,\n"
        "     balance).\n"
        "  2. Copy ALL rows from `accounts` into `accounts_backup`.\n"
        "  3. DELETE all rows from `accounts` (simulating data loss).\n"
        "  4. RESTORE by inserting all rows from `accounts_backup`\n"
        "     back into `accounts`.\n"
        "  5. SELECT the restored `accounts` table, sorted by\n"
        "     account_id.\n\n"
        "Expected output:\n[(1,1,5000.0), (2,2,3000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE regions (region_id INTEGER PRIMARY KEY, region_name TEXT UNIQUE);"
        "INSERT INTO regions VALUES (1,'North'), (2,'South');"
        "CREATE TABLE branches (branch_id INTEGER PRIMARY KEY, branch_name TEXT, region_id INTEGER REFERENCES regions(region_id));"
        "INSERT INTO branches VALUES (1,'Dhaka',1), (2,'Chittagong',2);"
        "CREATE TABLE accounts (account_id INTEGER PRIMARY KEY, branch_id INTEGER REFERENCES branches(branch_id), balance REAL CHECK(balance >= 0));"
        "INSERT INTO accounts VALUES (1,1,5000), (2,2,3000);"
        "CREATE TABLE transactions (txn_id INTEGER PRIMARY KEY, account_id INTEGER REFERENCES accounts(account_id), amount REAL, txn_date TEXT DEFAULT (date('now')));"
        "INSERT INTO transactions (account_id, amount, txn_date) VALUES (1,1000,'2026-07-01'), (1,-200,'2026-07-02'), (2,500,'2026-07-03');"
    ),
    expected_output="[(1, 1, 5000.0), (2, 2, 3000.0)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE accounts_backup AS SELECT * FROM accounts;",
        "DELETE FROM accounts;",
        "INSERT INTO accounts SELECT * FROM accounts_backup;",
        "SELECT * FROM accounts ORDER BY account_id;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L70.json",
        module_name="Module_07_Views_Optimization_Security",
        lesson_name="L70_Module_7_Capstone"
    )
