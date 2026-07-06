import os, shutil

BASE = "03.SQLPhone COURSE"

# ==================== MODULE-SPECIFIC BROKEN QUERIES ====================
# Format: { module_number: [ (filename, content), ... ] }
# We'll generate three per module.

MODULE_BUGS = {
    "01": [
        ("Broken_01.sql",
         "-- 🐛 BROKEN – Module 01, Lesson 05 (CREATE TABLE)\n"
         "-- This CREATE TABLE is missing a NOT NULL on the name column,\n"
         "-- allowing NULL names. Fix by adding NOT NULL.\n\n"
         "CREATE TABLE employees (\n"
         "    id INTEGER PRIMARY KEY,\n"
         "    name TEXT,          -- ❌ should be TEXT NOT NULL\n"
         "    salary REAL\n"
         ");\n"),
        ("Broken_02.sql",
         "-- 🐛 BROKEN – Module 01, Lesson 06 (INSERT)\n"
         "-- The INSERT forgets the column list and misorders values.\n"
         "-- Fix by adding the column list and matching order.\n\n"
         "INSERT INTO employees VALUES (1, 'Alice');  -- ❌ missing salary\n"),
        ("Broken_03.sql",
         "-- 🐛 BROKEN – Module 01, Lesson 08 (Comments)\n"
         "-- The comment is missing the second dash, causing a syntax error.\n"
         "-- Fix by using '--'.\n\n"
         "- Select all employees\n"
         "SELECT * FROM employees;\n"),
    ],
    "02": [
        ("Broken_01.sql",
         "-- 🐛 BROKEN – Module 02, Lesson 18 (LIKE)\n"
         "-- This query uses '=' with a wildcard. It should use LIKE.\n\n"
         "SELECT * FROM users WHERE email = '%@gmail.com';  -- ❌\n"),
        ("Broken_02.sql",
         "-- 🐛 BROKEN – Module 02, Lesson 16 (BETWEEN)\n"
         "-- BETWEEN is inclusive; this logic misses the upper bound.\n\n"
         "SELECT * FROM orders WHERE amount > 10 AND amount < 50;  -- excludes 50\n"
         "-- Should use BETWEEN 10 AND 50.\n"),
        ("Broken_03.sql",
         "-- 🐛 BROKEN – Module 02, Lesson 14 (ORDER BY)\n"
         "-- ORDER BY column is typed wrong (salry instead of salary).\n\n"
         "SELECT name, salary FROM employees ORDER BY salry DESC;\n"),
    ],
    "03": [
        ("Broken_01.sql",
         "-- 🐛 BROKEN – Module 03, Lesson 26 (HAVING)\n"
         "-- HAVING used without GROUP BY, and aggregate in WHERE.\n\n"
         "SELECT department, COUNT(*) FROM employees\n"
         "WHERE COUNT(*) > 5;  -- ❌ can't use aggregate in WHERE\n"),
        ("Broken_02.sql",
         "-- 🐛 BROKEN – Module 03, Lesson 24 (GROUP BY)\n"
         "-- Missing GROUP BY for non‑aggregate column.\n\n"
         "SELECT department, AVG(salary) FROM employees;  -- ❌ needs GROUP BY department\n"),
        ("Broken_03.sql",
         "-- 🐛 BROKEN – Module 03, Lesson 21 (COUNT)\n"
         "-- COUNT(column) ignores NULLs; this query may miscount.\n"
         "-- If phone is NULL, COUNT(phone) < COUNT(*).\n\n"
         "SELECT COUNT(phone) FROM contacts;  -- ❌ maybe not what you want\n"),
    ],
    "04": [
        ("Broken_01.sql",
         "-- 🐛 BROKEN – Module 04, Lesson 31 (LEFT JOIN)\n"
         "-- INNER JOIN used instead of LEFT JOIN, losing customers without orders.\n\n"
         "SELECT c.name, o.product FROM customers c\n"
         "JOIN orders o ON c.id = o.customer_id;  -- ❌ should be LEFT JOIN\n"),
        ("Broken_02.sql",
         "-- 🐛 BROKEN – Module 04, Lesson 34 (Self‑Join)\n"
         "-- Missing table alias causes ambiguity.\n\n"
         "SELECT name, manager FROM employees e\n"
         "JOIN employees ON e.manager_id = id;  -- ❌ 'id' ambiguous\n"),
        ("Broken_03.sql",
         "-- 🐛 BROKEN – Module 04, Lesson 35 (UNION)\n"
         "-- UNION columns mismatch: first SELECT has 2 cols, second has 3.\n\n"
         "SELECT id, name FROM current_employees\n"
         "UNION\n"
         "SELECT id, name, email FROM former_employees;  -- ❌ column count mismatch\n"),
    ],
    "05": [
        ("Broken_01.sql",
         "-- 🐛 BROKEN – Module 05, Lesson 39 (Scalar Subquery)\n"
         "-- Subquery returns more than one row, causing error.\n\n"
         "SELECT name FROM products\n"
         "WHERE price > (SELECT price FROM products WHERE category='Electronics');\n"
         "-- ❌ if multiple Electronics, scalar subquery fails.\n"),
        ("Broken_02.sql",
         "-- 🐛 BROKEN – Module 05, Lesson 44 (Correlated Subquery)\n"
         "-- Forgot to correlate the inner query; returns same value for all rows.\n\n"
         "SELECT e.name, e.salary FROM employees e\n"
         "WHERE e.salary > (SELECT AVG(salary) FROM employees);  -- ❌ missing e.department\n"),
        ("Broken_03.sql",
         "-- 🐛 BROKEN – Module 05, Lesson 45 (CTE)\n"
         "-- CTE defined but never referenced.\n\n"
         "WITH dept_avg AS (\n"
         "    SELECT department, AVG(salary) AS avg_sal FROM employees GROUP BY department\n"
         ")\n"
         "SELECT * FROM employees;  -- ❌ dept_avg not used\n"),
    ],
    "06": [
        ("Broken_01.sql",
         "-- 🐛 BROKEN – Module 06, Lesson 47 (UPDATE)\n"
         "-- UPDATE without WHERE updates all rows!\n\n"
         "UPDATE products SET price = 9.99;  -- ❌ all rows affected\n"),
        ("Broken_02.sql",
         "-- 🐛 BROKEN – Module 06, Lesson 48 (DELETE)\n"
         "-- DELETE from parent table without CASCADE, leaving orphans.\n"
         "-- (Assume foreign_key pragma is ON).\n\n"
         "DELETE FROM departments WHERE id = 1;  -- ❌ fails if employees exist\n"),
        ("Broken_03.sql",
         "-- 🐛 BROKEN – Module 06, Lesson 55 (CREATE INDEX)\n"
         "-- Index created on column with low cardinality, useless.\n\n"
         "CREATE INDEX idx_gender ON employees(gender);  -- ❌ only 'M'/'F'\n"),
    ],
    "07": [
        ("Broken_01.sql",
         "-- 🐛 BROKEN – Module 07, Lesson 58 (strftime)\n"
         "-- strftime format string wrong: %Y (4-digit year) vs %y (2-digit).\n"
         "-- Also missing a '%' before d.\n\n"
         "SELECT strftime('%Y-%m-%d', 'now');  -- works\n"
         "SELECT strftime('%Y-%m-%d', 'now');  -- ❌ should be %d not d\n"),
        ("Broken_02.sql",
         "-- 🐛 BROKEN – Module 07, Lesson 63 (COALESCE)\n"
         "-- COALESCE with all NULL arguments still returns NULL, not the fallback.\n\n"
         "SELECT COALESCE(NULL, NULL, 'fallback');  -- returns 'fallback'?\n"
         "-- Actually this is correct, but the mistake is expecting it to return 0 when all are NULL.\n"
         "-- The real bug: using COALESCE on a column that is always NULL, and the fallback is also NULL.\n"
         "SELECT COALESCE(middle_name, NULL) FROM contacts;  -- ❌ always NULL\n"),
        ("Broken_03.sql",
         "-- 🐛 BROKEN – Module 07, Lesson 62 (CAST)\n"
         "-- Casting 'abc' to INTEGER yields 0, not an error, causing silent data corruption.\n"
         "INSERT INTO scores VALUES (CAST('abc' AS INTEGER));  -- ❌ inserts 0\n"),
    ],
    "08": [
        ("Broken_01.sql",
         "-- 🐛 BROKEN – Module 08, Lesson 65 (CASE)\n"
         "-- CASE missing END keyword.\n\n"
         "SELECT name,\n"
         "  CASE WHEN score >= 90 THEN 'A'\n"
         "       WHEN score >= 80 THEN 'B'\n"
         "       ELSE 'F'  -- ❌ missing END\n"
         "FROM students;\n"),
        ("Broken_02.sql",
         "-- 🐛 BROKEN – Module 08, Lesson 67 (Views)\n"
         "-- View created with SELECT *, but underlying table adds a column later,\n"
         "-- causing 'too many columns' when querying view.\n\n"
         "CREATE VIEW customer_view AS SELECT * FROM customers;\n"
         "ALTER TABLE customers ADD COLUMN phone TEXT;\n"
         "SELECT * FROM customer_view;  -- ❌ column mismatch\n"),
        ("Broken_03.sql",
         "-- 🐛 BROKEN – Module 08, Lesson 70 (CSV Export)\n"
         "-- Export to CSV without .headers on; missing column names.\n\n"
         ".mode csv\n"
         ".output result.csv\n"
         "SELECT id, name FROM users;\n"
         ".output stdout  -- ❌ headers not included\n"),
    ],
    "09": [
        ("Broken_01.py",  # Python file for this module
         "# 🐛 BROKEN – Module 09, Lesson 73 (Parameterized Insert)\n"
         "# Uses string formatting instead of parameters. Fix with ?.\n\n"
         "name = input('Name: ')\n"
         "cur.execute(f\"INSERT INTO users (name) VALUES ('{name}')\")\n"
         "conn.commit()\n"),
        ("Broken_02.py",
         "# 🐛 BROKEN – Module 09, Lesson 72 (Create Table)\n"
         "# Missing conn.commit() after DDL; table not saved.\n\n"
         "cur.execute('CREATE TABLE test (id INT)')\n"
         "# ❌ need conn.commit()\n"),
        ("Broken_03.py",
         "# 🐛 BROKEN – Module 09, Lesson 74 (fetch methods)\n"
         "# fetchone() called after fetchall() returns empty.\n\n"
         "cur.execute('SELECT * FROM users')\n"
         "all_rows = cur.fetchall()\n"
         "first = cur.fetchone()  # ❌ returns None\n"),
    ],
    "10": [
        ("Broken_01.sql",
         "-- 🐛 BROKEN – Module 10, Lesson 82 (Index Usage)\n"
         "-- Index not used because WHERE uses function on column.\n\n"
         "CREATE INDEX idx_name ON users(name);\n"
         "SELECT * FROM users WHERE UPPER(name) = 'ALICE';  -- ❌ index ignored\n"),
        ("Broken_02.sql",
         "-- 🐛 BROKEN – Module 10, Lesson 84 (Transactions)\n"
         "-- Forgot to commit or rollback after error.\n\n"
         "BEGIN;\n"
         "UPDATE accounts SET balance = balance - 100 WHERE id = 1;\n"
         "-- ❌ no COMMIT or ROLLBACK\n"),
        ("Broken_03.sql",
         "-- 🐛 BROKEN – Module 10, Lesson 85 (Backup)\n"
         "-- .dump creates text SQL, but .backup creates binary copy.\n"
         "-- Using .dump to restore can be slow; but the mistake is not using .backup for speed.\n\n"
         "-- Actually, a common error is to use .dump without redirecting output.\n"
         ".dump\n"
         "-- ❌ no .output specified, just prints to screen\n"),
    ],
    "11": [
        ("Broken_01.sql",
         "-- 🐛 BROKEN – Module 11, Lesson 89 (Library)\n"
         "-- Missing FOREIGN KEY in Loan table, allowing invalid book references.\n\n"
         "CREATE TABLE Loan (\n"
         "    id INTEGER PRIMARY KEY,\n"
         "    book_id INTEGER,\n"
         "    member_id INTEGER,\n"
         "    loan_date TEXT\n"
         ");  -- ❌ no foreign keys\n"),
        ("Broken_02.sql",
         "-- 🐛 BROKEN – Module 11, Lesson 93 (Movie Ratings)\n"
         "-- Composite PK missing in Rating table, allowing duplicate votes.\n\n"
         "CREATE TABLE Rating (\n"
         "    user_id INTEGER,\n"
         "    movie_id INTEGER,\n"
         "    rating INTEGER\n"
         ");  -- ❌ should be PRIMARY KEY (user_id, movie_id)\n"),
        ("Broken_03.sql",
         "-- 🐛 BROKEN – Module 11, Lesson 88 (E‑commerce)\n"
         "-- CHECK constraint missing, allowing negative stock.\n\n"
         "CREATE TABLE Product (\n"
         "    id INTEGER PRIMARY KEY,\n"
         "    name TEXT,\n"
         "    stock_quantity INTEGER  -- ❌ need CHECK (stock_quantity >= 0)\n"
         ");\n"),
    ],
    "12": [
        ("Broken_01.sql",
         "-- 🐛 BROKEN – Module 12, Lesson 95 (DB Comparison)\n"
         "-- Trying to use SQLite syntax on PostgreSQL (LIMIT with OFFSET comma).\n\n"
         "SELECT * FROM users LIMIT 10, 5;  -- ❌ not standard, works in SQLite, fails in others\n"),
        ("Broken_02.sh",  # shell script
         "#!/bin/bash\n"
         "# 🐛 BROKEN – Module 12, Lesson 96 (Installing PostgreSQL)\n"
         "# Forgot to start the service before creating a database.\n\n"
         "apt install postgresql\n"
         "su - postgres -c \"createdb testdb\"  # ❌ service not started\n"),
        ("Broken_03.py",
         "# 🐛 BROKEN – Module 12, Lesson 97 (psycopg2)\n"
         "# Using SQLite placeholder '?' instead of '%s'.\n\n"
         "cur.execute('SELECT * FROM users WHERE id = ?', (1,))  # ❌ should be %s\n"),
    ],
}

# ==================== CLEANUP & CREATE ====================
for mod_num, files in MODULE_BUGS.items():
    debug_dir = os.path.join(BASE, f"SQLPhone_Module_{mod_num}", "iii_Debugging_Sheets")
    # Remove old files (but keep any .gitkeep if exists)
    if os.path.isdir(debug_dir):
        for f in os.listdir(debug_dir):
            if f not in [fn for fn, _ in files] and not f.startswith('.'):
                os.remove(os.path.join(debug_dir, f))
    else:
        os.makedirs(debug_dir, exist_ok=True)
    # Write new files
    for filename, content in files:
        filepath = os.path.join(debug_dir, filename)
        with open(filepath, "w") as f:
            f.write(content)
    print(f"Module {mod_num}: {len(files)} debugging files set.")

print("\n✅ All debugging sheets perfectly tailored to each module.")
