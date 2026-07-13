import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "💰  Imperial Finance – Build the Schema\n\n"
        "Write Python code that:\n"
        "  1. Connects to ':memory:'\n"
        "  2. Creates the two tables:\n"
        "     categories, expenses\n"
        "     (exact schema from the lecture).\n"
        "  3. Inserts seed data:\n"
        "     • Categories: (1,'Food'), (2,'Transport'),\n"
        "       (3,'Entertainment')\n"
        "     • Expenses (id, amount, cat_id, description, date):\n"
        "       (1,15.50,1,'Lunch','2026-07-01')\n"
        "       (2,30.00,2,'Bus pass','2026-07-02')\n"
        "       (3,12.00,1,'Snacks','2026-08-01')\n"
        "       (4,45.00,3,'Cinema','2026-08-05')\n"
        "       (5,8.00,1,'Breakfast','2026-08-10')\n"
        "  4. Commits, then SELECTs all expenses sorted\n"
        "     by exp_date and prints them.\n\n"
        "Expected output:\n"
        "[(1,15.5,1,'Lunch','2026-07-01'), (2,30.0,2,'Bus pass','2026-07-02'), (3,12.0,1,'Snacks','2026-08-01'), (4,45.0,3,'Cinema','2026-08-05'), (5,8.0,1,'Breakfast','2026-08-10')]"
    ),
    expected_output=(
        "[(1, 15.5, 1, 'Lunch', '2026-07-01'), "
        "(2, 30.0, 2, 'Bus pass', '2026-07-02'), "
        "(3, 12.0, 1, 'Snacks', '2026-08-01'), "
        "(4, 45.0, 3, 'Cinema', '2026-08-05'), "
        "(5, 8.0, 1, 'Breakfast', '2026-08-10')]"
    ),
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.executescript('''",
        "CREATE TABLE categories (cat_id INTEGER PRIMARY KEY, name TEXT NOT NULL);",
        "CREATE TABLE expenses (exp_id INTEGER PRIMARY KEY, amount REAL CHECK(amount > 0), cat_id INTEGER, description TEXT, exp_date TEXT DEFAULT (date('now')), FOREIGN KEY (cat_id) REFERENCES categories(cat_id));",
        "''')",
        "conn.executescript('''",
        "INSERT INTO categories VALUES (1,'Food'), (2,'Transport'), (3,'Entertainment');",
        "INSERT INTO expenses VALUES (1,15.50,1,'Lunch','2026-07-01');",
        "INSERT INTO expenses VALUES (2,30.00,2,'Bus pass','2026-07-02');",
        "INSERT INTO expenses VALUES (3,12.00,1,'Snacks','2026-08-01');",
        "INSERT INTO expenses VALUES (4,45.00,3,'Cinema','2026-08-05');",
        "INSERT INTO expenses VALUES (5,8.00,1,'Breakfast','2026-08-10');",
        "''')",
        "conn.commit()",
        "cursor = conn.execute('SELECT * FROM expenses ORDER BY exp_date')",
        "print(cursor.fetchall())",
    ]
)

easy2 = Task(
    description=(
        "🏷️  Expense Details – Show Category Names\n\n"
        "The finance database is already seeded.\n"
        "Write Python code that lists each expense's\n"
        "description, category name, amount, and date.\n"
        "Sort by exp_date.\n\n"
        "Expected output:\n"
        "[('Lunch','Food',15.5,'2026-07-01'), ('Bus pass','Transport',30.0,'2026-07-02'), ('Snacks','Food',12.0,'2026-08-01'), ('Cinema','Entertainment',45.0,'2026-08-05'), ('Breakfast','Food',8.0,'2026-08-10')]"
    ),
    setup_sql=(
        "CREATE TABLE categories (cat_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO categories VALUES (1,'Food'), (2,'Transport'), (3,'Entertainment');"
        "CREATE TABLE expenses (exp_id INTEGER PRIMARY KEY, amount REAL CHECK(amount > 0), cat_id INTEGER, description TEXT, exp_date TEXT DEFAULT (date('now')), FOREIGN KEY (cat_id) REFERENCES categories(cat_id));"
        "INSERT INTO expenses VALUES (1,15.50,1,'Lunch','2026-07-01');"
        "INSERT INTO expenses VALUES (2,30.00,2,'Bus pass','2026-07-02');"
        "INSERT INTO expenses VALUES (3,12.00,1,'Snacks','2026-08-01');"
        "INSERT INTO expenses VALUES (4,45.00,3,'Cinema','2026-08-05');"
        "INSERT INTO expenses VALUES (5,8.00,1,'Breakfast','2026-08-10');"
    ),
    expected_output=(
        "[('Lunch', 'Food', 15.5, '2026-07-01'), "
        "('Bus pass', 'Transport', 30.0, '2026-07-02'), "
        "('Snacks', 'Food', 12.0, '2026-08-01'), "
        "('Cinema', 'Entertainment', 45.0, '2026-08-05'), "
        "('Breakfast', 'Food', 8.0, '2026-08-10')]"
    ),
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT e.description, c.name, e.amount, e.exp_date",
        "FROM expenses e JOIN categories c ON e.cat_id = c.cat_id",
        "ORDER BY e.exp_date",
        "''')",
        "print(cursor.fetchall())",
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "📅  Monthly Total Spending\n\n"
        "The finance database is seeded.\n"
        "Write Python code that computes the total amount\n"
        "spent per month (YYYY‑MM format), sorted by month.\n\n"
        "Expected output:\n[('2026-07',45.5), ('2026-08',65.0)]"
    ),
    setup_sql=(
        "CREATE TABLE categories (cat_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO categories VALUES (1,'Food'), (2,'Transport'), (3,'Entertainment');"
        "CREATE TABLE expenses (exp_id INTEGER PRIMARY KEY, amount REAL CHECK(amount > 0), cat_id INTEGER, description TEXT, exp_date TEXT DEFAULT (date('now')), FOREIGN KEY (cat_id) REFERENCES categories(cat_id));"
        "INSERT INTO expenses VALUES (1,15.50,1,'Lunch','2026-07-01');"
        "INSERT INTO expenses VALUES (2,30.00,2,'Bus pass','2026-07-02');"
        "INSERT INTO expenses VALUES (3,12.00,1,'Snacks','2026-08-01');"
        "INSERT INTO expenses VALUES (4,45.00,3,'Cinema','2026-08-05');"
        "INSERT INTO expenses VALUES (5,8.00,1,'Breakfast','2026-08-10');"
    ),
    expected_output="[('2026-07', 45.5), ('2026-08', 65.0)]",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT strftime('%Y-%m', exp_date) AS month, SUM(amount) AS total_spent",
        "FROM expenses GROUP BY month ORDER BY month",
        "''')",
        "print(cursor.fetchall())",
    ]
)

medium2 = Task(
    description=(
        "🏆  Top Spending Categories – All Time\n\n"
        "The finance database is seeded.\n"
        "Write Python code that ranks categories by total\n"
        "spending (highest first). Show category name and\n"
        "total amount. Limit to 3.\n\n"
        "Expected output:\n[('Entertainment',45.0), ('Food',35.5), ('Transport',30.0)]"
    ),
    setup_sql=(
        "CREATE TABLE categories (cat_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO categories VALUES (1,'Food'), (2,'Transport'), (3,'Entertainment');"
        "CREATE TABLE expenses (exp_id INTEGER PRIMARY KEY, amount REAL CHECK(amount > 0), cat_id INTEGER, description TEXT, exp_date TEXT DEFAULT (date('now')), FOREIGN KEY (cat_id) REFERENCES categories(cat_id));"
        "INSERT INTO expenses VALUES (1,15.50,1,'Lunch','2026-07-01');"
        "INSERT INTO expenses VALUES (2,30.00,2,'Bus pass','2026-07-02');"
        "INSERT INTO expenses VALUES (3,12.00,1,'Snacks','2026-08-01');"
        "INSERT INTO expenses VALUES (4,45.00,3,'Cinema','2026-08-05');"
        "INSERT INTO expenses VALUES (5,8.00,1,'Breakfast','2026-08-10');"
    ),
    expected_output="[('Entertainment', 45.0), ('Food', 35.5), ('Transport', 30.0)]",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT c.name, SUM(e.amount) AS total",
        "FROM expenses e JOIN categories c ON e.cat_id = c.cat_id",
        "GROUP BY c.cat_id ORDER BY total DESC LIMIT 3",
        "''')",
        "print(cursor.fetchall())",
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "📉  Month‑over‑Month Variance – LAG()\n\n"
        "The finance database is seeded.\n"
        "Write a query using the `LAG` window function to\n"
        "show each month's total spending, the previous\n"
        "month's total, and the change (current – previous).\n"
        "Use a CTE named `monthly` to calculate monthly totals\n"
        "first.\n\n"
        "Expected output:\n[('2026-07',45.5,None,None), ('2026-08',65.0,45.5,19.5)]"
    ),
    setup_sql=(
        "CREATE TABLE categories (cat_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO categories VALUES (1,'Food'), (2,'Transport'), (3,'Entertainment');"
        "CREATE TABLE expenses (exp_id INTEGER PRIMARY KEY, amount REAL CHECK(amount > 0), cat_id INTEGER, description TEXT, exp_date TEXT DEFAULT (date('now')), FOREIGN KEY (cat_id) REFERENCES categories(cat_id));"
        "INSERT INTO expenses VALUES (1,15.50,1,'Lunch','2026-07-01');"
        "INSERT INTO expenses VALUES (2,30.00,2,'Bus pass','2026-07-02');"
        "INSERT INTO expenses VALUES (3,12.00,1,'Snacks','2026-08-01');"
        "INSERT INTO expenses VALUES (4,45.00,3,'Cinema','2026-08-05');"
        "INSERT INTO expenses VALUES (5,8.00,1,'Breakfast','2026-08-10');"
    ),
    expected_output="[('2026-07', 45.5, None, None), ('2026-08', 65.0, 45.5, 19.5)]",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "WITH monthly AS (",
        "    SELECT strftime('%Y-%m', exp_date) AS month, SUM(amount) AS spent",
        "    FROM expenses GROUP BY month",
        ")",
        "SELECT month, spent,",
        "       LAG(spent) OVER (ORDER BY month) AS prev_month,",
        "       ROUND(spent - LAG(spent) OVER (ORDER BY month), 2) AS change",
        "FROM monthly",
        "''')",
        "print(cursor.fetchall())",
    ]
)

hard2 = Task(
    description=(
        "📈  Running Total – SUM() OVER\n\n"
        "The finance database is seeded.\n"
        "Use a window function to compute the running total\n"
        "of expenses, partitioned by year and ordered by date.\n"
        "Show exp_date, amount, and running_total for each\n"
        "expense.\n\n"
        "Expected output:\n"
        "[('2026-07-01',15.5,15.5), ('2026-07-02',30.0,45.5), ('2026-08-01',12.0,57.5), ('2026-08-05',45.0,102.5), ('2026-08-10',8.0,110.5)]"
    ),
    setup_sql=(
        "CREATE TABLE categories (cat_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO categories VALUES (1,'Food'), (2,'Transport'), (3,'Entertainment');"
        "CREATE TABLE expenses (exp_id INTEGER PRIMARY KEY, amount REAL CHECK(amount > 0), cat_id INTEGER, description TEXT, exp_date TEXT DEFAULT (date('now')), FOREIGN KEY (cat_id) REFERENCES categories(cat_id));"
        "INSERT INTO expenses VALUES (1,15.50,1,'Lunch','2026-07-01');"
        "INSERT INTO expenses VALUES (2,30.00,2,'Bus pass','2026-07-02');"
        "INSERT INTO expenses VALUES (3,12.00,1,'Snacks','2026-08-01');"
        "INSERT INTO expenses VALUES (4,45.00,3,'Cinema','2026-08-05');"
        "INSERT INTO expenses VALUES (5,8.00,1,'Breakfast','2026-08-10');"
    ),
    expected_output="[('2026-07-01', 15.5, 15.5), ('2026-07-02', 30.0, 45.5), ('2026-08-01', 12.0, 57.5), ('2026-08-05', 45.0, 102.5), ('2026-08-10', 8.0, 110.5)]",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT exp_date, amount,",
        "       SUM(amount) OVER (PARTITION BY strftime('%Y', exp_date) ORDER BY exp_date) AS running_total",
        "FROM expenses ORDER BY exp_date",
        "''')",
        "print(cursor.fetchall())",
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L86.json",
        module_name="Module_09_Real_World_Projects",
        lesson_name="L86_Expense_Tracker_with_Monthly_Reports"
    )