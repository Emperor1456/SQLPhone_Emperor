import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🔁  Recursive CTE – Numbers 1 to 5\n\n"
        "Write a recursive CTE that generates numbers\n"
        "from 1 to 5.\n"
        "Name the CTE `cnt(x)`.\n"
        "The anchor should SELECT 1.\n"
        "The recursive member should SELECT x+1 FROM cnt\n"
        "WHERE x < 5.\n"
        "Then SELECT * FROM cnt.\n\n"
        "Expected output:\n[(1,), (2,), (3,), (4,), (5,)]"
    ),
    expected_output="[(1,), (2,), (3,), (4,), (5,)]",
    level=Level.EASY,
    hints=[
        "WITH RECURSIVE cnt(x) AS (",
        "    SELECT 1",
        "    UNION ALL",
        "    SELECT x + 1 FROM cnt WHERE x < 5",
        ")",
        "SELECT * FROM cnt;"
    ]
)

easy2 = Task(
    description=(
        "📅  Recursive CTE – Dates of a Week\n\n"
        "Write a recursive CTE that generates the dates\n"
        "from '2026-07-01' to '2026-07-07'.\n"
        "Use date() with '+1 day' modifier.\n"
        "Name the CTE `week(d)`.\n"
        "Anchor: SELECT '2026-07-01'.\n"
        "Recursive: SELECT date(d, '+1 day') FROM week\n"
        "WHERE d < '2026-07-07'.\n\n"
        "Expected output:\n[('2026-07-01',), ('2026-07-02',), ('2026-07-03',), ('2026-07-04',), ('2026-07-05',), ('2026-07-06',), ('2026-07-07',)]"
    ),
    expected_output="[('2026-07-01',), ('2026-07-02',), ('2026-07-03',), ('2026-07-04',), ('2026-07-05',), ('2026-07-06',), ('2026-07-07',)]",
    level=Level.EASY,
    hints=[
        "WITH RECURSIVE week(d) AS (",
        "    SELECT '2026-07-01'",
        "    UNION ALL",
        "    SELECT date(d, '+1 day') FROM week WHERE d < '2026-07-07'",
        ")",
        "SELECT * FROM week;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🧬  Org Chart – Recursive CTE\n\n"
        "Create an `employees` table with emp_id, name,\n"
        "and manager_id (self‑referencing).\n"
        "Write a recursive CTE named `org` that returns\n"
        "the full org chart starting from the CEO\n"
        "(WHERE manager_id IS NULL).\n"
        "Include a `level` column starting at 1.\n"
        "Return name and level, sorted by level, then name.\n\n"
        "Expected output:\n[('Emperor',1), ('Ali',2), ('Rahim',2), ('Hasan',3)]"
    ),
    expected_output="[('Emperor', 1), ('Ali', 2), ('Rahim', 2), ('Hasan', 3)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT, manager_id INTEGER REFERENCES employees(emp_id));",
        "INSERT INTO employees VALUES (1,'Emperor',NULL), (2,'Rahim',1), (3,'Ali',1), (4,'Hasan',2);",
        "WITH RECURSIVE org AS (",
        "    SELECT emp_id, name, manager_id, 1 AS level FROM employees WHERE manager_id IS NULL",
        "    UNION ALL",
        "    SELECT e.emp_id, e.name, e.manager_id, o.level + 1 FROM employees e JOIN org o ON e.manager_id = o.emp_id",
        ")",
        "SELECT name, level FROM org ORDER BY level, name;"
    ]
)

medium2 = Task(
    description=(
        "📂  Category Tree – Recursive CTE\n\n"
        "Create a `categories` table with id, name, parent_id.\n"
        "Write a recursive CTE that returns the full tree\n"
        "with a `depth` column.\n"
        "Return name and depth, sorted by depth, then name.\n\n"
        "Expected output:\n[('All',0), ('Electronics',1), ('Furniture',1), ('Laptops',2), ('Mice',2), ('Desks',2)]"
    ),
    expected_output="[('All', 0), ('Electronics', 1), ('Furniture', 1), ('Laptops', 2), ('Mice', 2), ('Desks', 2)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE categories (id INTEGER PRIMARY KEY, name TEXT, parent_id INTEGER REFERENCES categories(id));",
        "INSERT INTO categories VALUES (1,'All',NULL), (2,'Electronics',1), (3,'Furniture',1), (4,'Laptops',2), (5,'Mice',2), (6,'Desks',3);",
        "WITH RECURSIVE cat_tree AS (",
        "    SELECT id, name, parent_id, 0 AS depth FROM categories WHERE parent_id IS NULL",
        "    UNION ALL",
        "    SELECT c.id, c.name, c.parent_id, ct.depth + 1 FROM categories c JOIN cat_tree ct ON c.parent_id = ct.id",
        ")",
        "SELECT name, depth FROM cat_tree ORDER BY depth, name;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🔍  Reporting Chain – Upward Recursive CTE\n\n"
        "Create an `employees` table (same as Medium1).\n"
        "Write a recursive CTE that traces the chain of\n"
        "command FROM a specific employee (Hasan) UP to the CEO.\n"
        "Start with emp_id = 4 (Hasan).\n"
        "Each step joins employees.manager_id = cte.emp_id.\n"
        "Return name, sorted by the natural order (which will\n"
        "be from Hasan up to Emperor).\n\n"
        "Expected output:\n[('Hasan',), ('Rahim',), ('Emperor',)]"
    ),
    setup_sql=(
        "CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT, manager_id INTEGER REFERENCES employees(emp_id));"
        "INSERT INTO employees VALUES (1,'Emperor',NULL), (2,'Rahim',1), (3,'Ali',1), (4,'Hasan',2);"
    ),
    expected_output="[('Hasan',), ('Rahim',), ('Emperor',)]",
    level=Level.HARD,
    hints=[
        "WITH RECURSIVE chain AS (",
        "    SELECT emp_id, name, manager_id FROM employees WHERE emp_id = 4",
        "    UNION ALL",
        "    SELECT e.emp_id, e.name, e.manager_id FROM employees e JOIN chain c ON e.emp_id = c.manager_id",
        ")",
        "SELECT name FROM chain;"
    ]
)

hard2 = Task(
    description=(
        "📊  Subordinates Count – Recursive CTE\n\n"
        "Create an `employees` table (same as above but larger).\n"
        "Write a recursive CTE that, for each manager, counts\n"
        "ALL subordinates (direct + indirect) using recursion.\n"
        "Return manager name and total_team_size.\n"
        "Sort by total_team_size descending.\n\n"
        "Expected output:\n[('Emperor',5), ('Rahim',2), ('Ali',1), ('Hasan',0), ('Fatima',0), ('Karim',0)]"
    ),
    expected_output="[('Emperor', 5), ('Rahim', 2), ('Ali', 1), ('Hasan', 0), ('Fatima', 0), ('Karim', 0)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT, manager_id INTEGER REFERENCES employees(emp_id));",
        "INSERT INTO employees VALUES (1,'Emperor',NULL), (2,'Rahim',1), (3,'Ali',1), (4,'Hasan',2), (5,'Fatima',3), (6,'Karim',4);",
        "WITH RECURSIVE subordinates AS (",
        "    SELECT manager_id AS root, emp_id FROM employees WHERE manager_id IS NOT NULL",
        "    UNION ALL",
        "    SELECT s.root, e.emp_id FROM employees e JOIN subordinates s ON e.manager_id = s.emp_id",
        ")",
        "SELECT e.name, COUNT(DISTINCT s.emp_id) AS team_size FROM employees e LEFT JOIN subordinates s ON e.emp_id = s.root GROUP BY e.emp_id ORDER BY team_size DESC;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L48.json",
        module_name="Module_05_Subqueries_CTEs",
        lesson_name="L48_Recursive_CTEs"
    )
