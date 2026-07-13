import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🧮  ABS & ROUND – Clean Up Numbers\n\n"
        "Create a table `transactions` with columns:\n"
        "  • id INTEGER\n"
        "  • amount REAL\n\n"
        "Insert 3 rows with some negative values:\n"
        "  (1, -150.567)\n"
        "  (2, 200.3)\n"
        "  (3, -45.89)\n\n"
        "Return id, original amount, ABS(amount)\n"
        "as `abs_amount`, and ROUND(amount, 1)\n"
        "as `rounded`, sorted by id.\n\n"
        "Expected output:\n[(1, -150.567, 150.567, -150.6), (2, 200.3, 200.3, 200.3), (3, -45.89, 45.89, -45.9)]"
    ),
    expected_output="[(1, -150.567, 150.567, -150.6), (2, 200.3, 200.3, 200.3), (3, -45.89, 45.89, -45.9)]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE transactions (id INTEGER, amount REAL);",
        "INSERT INTO transactions VALUES (1, -150.567), (2, 200.3), (3, -45.89);",
        "SELECT id, amount, ABS(amount) AS abs_amount, ROUND(amount, 1) AS rounded FROM transactions ORDER BY id;"
    ]
)

easy2 = Task(
    description=(
        "📈  MAX & MIN – Salary Range\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Write a single query that returns the\n"
        "highest salary (max_sal) and the lowest\n"
        "salary (min_sal) from the table.\n\n"
        "Expected output: [(5000.0, 2000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[(5000.0, 2000.0)]",
    level=Level.EASY,
    hints=[
        "SELECT MAX(salary), MIN(salary) FROM soldiers;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🔄  CAST – String to Number\n\n"
        "Create a table `imported` with columns:\n"
        "  • id INTEGER\n"
        "  • value_text TEXT\n\n"
        "Insert 3 rows with numeric strings:\n"
        "  (1, '100')\n"
        "  (2, '200')\n"
        "  (3, '50')\n\n"
        "Use CAST to convert value_text to INTEGER,\n"
        "then multiply by 2. Return id, value_text,\n"
        "and the doubled value as `doubled`.\n\n"
        "Expected output:\n[(1, '100', 200), (2, '200', 400), (3, '50', 100)]"
    ),
    expected_output="[(1, '100', 200), (2, '200', 400), (3, '50', 100)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE imported (id INTEGER, value_text TEXT);",
        "INSERT INTO imported VALUES (1, '100'), (2, '200'), (3, '50');",
        "SELECT id, value_text, CAST(value_text AS INTEGER) * 2 AS doubled FROM imported;"
    ]
)

medium2 = Task(
    description=(
        "💰  ROUND – Tax Calculation\n\n"
        "Create a table `prices` with columns:\n"
        "  • id INTEGER, product TEXT, price REAL, tax_rate REAL.\n"
        "Insert 3 rows:\n"
        "  (1, 'Laptop', 999.99, 0.075)\n"
        "  (2, 'Mouse', 24.99, 0.05)\n"
        "  (3, 'Keyboard', 79.99, 0.075)\n\n"
        "Return product, price, tax (price * tax_rate)\n"
        "rounded to 2 decimal places as `tax_rounded`.\n\n"
        "Expected output:\n[('Laptop', 999.99, 75.0), ('Mouse', 24.99, 1.25), ('Keyboard', 79.99, 6.0)]"
    ),
    expected_output="[('Laptop', 999.99, 75.0), ('Mouse', 24.99, 1.25), ('Keyboard', 79.99, 6.0)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE prices (id INTEGER, product TEXT, price REAL, tax_rate REAL);",
        "INSERT INTO prices VALUES (1, 'Laptop', 999.99, 0.075), (2, 'Mouse', 24.99, 0.05), (3, 'Keyboard', 79.99, 0.075);",
        "SELECT product, price, ROUND(price * tax_rate, 2) AS tax_rounded FROM prices;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🎲  RANDOM – Generate Number 1‑100\n\n"
        "Write a query that uses RANDOM() and ABS()\n"
        "to generate a random integer between 1 and 100.\n"
        "Use: ABS(RANDOM()) % 100 + 1\n\n"
        "The engine will verify that the result is\n"
        "within the valid range.\n\n"
        "Expected output: [(random number)]"
    ),
    expected_output=None,  # dynamic
    level=Level.HARD,
    hints=[
        "SELECT ABS(RANDOM()) % 100 + 1 AS random_num;"
    ],
    verify_func=lambda conn: (
        (num := conn.execute("SELECT ABS(RANDOM()) % 100 + 1 AS random_num").fetchone()[0]) is not None
        and 1 <= num <= 100
    )
)

hard2 = Task(
    description=(
        "📊  CAST + Aggregates – Score Analysis\n\n"
        "Create a table `grades` with columns:\n"
        "  • student TEXT, score TEXT (stored as text!).\n"
        "Insert 5 rows:\n"
        "  ('Emperor', '95')\n"
        "  ('Rahim', '78')\n"
        "  ('Karim', '82')\n"
        "  ('Ali', '60')\n"
        "  ('Hasan', '91')\n\n"
        "Write a query that:\n"
        "  • CASTs score to INTEGER\n"
        "  • Returns MAX, MIN, and ROUND(AVG) of the scores\n"
        "  • Also counts how many scored > 80 (using CASE inside COUNT)\n"
        "Return a single row with columns:\n"
        "  max_score, min_score, avg_score, above_80\n\n"
        "Expected output: [(95, 60, 81.0, 3)]"
    ),
    expected_output="[(95, 60, 81.0, 3)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE grades (student TEXT, score TEXT);",
        "INSERT INTO grades VALUES ('Emperor', '95'), ('Rahim', '78'), ('Karim', '82'), ('Ali', '60'), ('Hasan', '91');",
        "SELECT MAX(CAST(score AS INTEGER)) AS max_score, MIN(CAST(score AS INTEGER)) AS min_score, ROUND(AVG(CAST(score AS INTEGER)), 1) AS avg_score, COUNT(CASE WHEN CAST(score AS INTEGER) > 80 THEN 1 END) AS above_80 FROM grades;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L19.json",
        module_name="Module_02_Filtering_Conditional_Logic",
        lesson_name="L19_Mathematical_Functions_CAST"
    )
