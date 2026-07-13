import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🏷️  Column Alias – Rename Output\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Return the name and salary of all soldiers,\n"
        "but rename the columns to `soldier_name`\n"
        "and `monthly_pay`.\n"
        "Sort by monthly_pay descending.\n\n"
        "Expected output:\n[('Emperor',5000.0), ('Ali',4500.0), ('Rahim',4000.0), ('Hasan',3500.0), ('Karim',2000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[('Emperor', 5000.0), ('Ali', 4500.0), ('Rahim', 4000.0), ('Hasan', 3500.0), ('Karim', 2000.0)]",
    level=Level.EASY,
    hints=[
        "SELECT name AS soldier_name, salary AS monthly_pay FROM soldiers ORDER BY monthly_pay DESC;"
    ]
)

easy2 = Task(
    description=(
        "🏗️  Table Alias – Shorter Queries\n\n"
        "The same `soldiers` table.\n"
        "Use a table alias `s` to return the name\n"
        "and rank of all soldiers, sorted by name.\n\n"
        "Expected output:\n[('Ali','General'), ('Emperor','General'), ('Hasan','Colonel'), ('Karim','Private'), ('Rahim','Colonel')]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[('Ali', 'General'), ('Emperor', 'General'), ('Hasan', 'Colonel'), ('Karim', 'Private'), ('Rahim', 'Colonel')]",
    level=Level.EASY,
    hints=[
        "SELECT s.name, s.rank FROM soldiers s ORDER BY s.name;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🧮  Computed Column – Annual Salary\n\n"
        "The `soldiers` table has salary as monthly pay.\n"
        "Return name, salary, and a computed column\n"
        "`annual_salary` (salary * 12) for all soldiers.\n"
        "Sort by annual_salary descending.\n\n"
        "Expected output:\n[('Emperor',5000.0,60000.0), ('Ali',4500.0,54000.0), ('Rahim',4000.0,48000.0), ('Hasan',3500.0,42000.0), ('Karim',2000.0,24000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[('Emperor', 5000.0, 60000.0), ('Ali', 4500.0, 54000.0), ('Rahim', 4000.0, 48000.0), ('Hasan', 3500.0, 42000.0), ('Karim', 2000.0, 24000.0)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT name, salary, salary * 12 AS annual_salary FROM soldiers ORDER BY annual_salary DESC;"
    ]
)

medium2 = Task(
    description=(
        "🔗  Concatenation – Full Name\n\n"
        "Create a table `citizens` with columns\n"
        "  id INTEGER, first_name TEXT, last_name TEXT.\n"
        "Insert 3 rows.\n"
        "Return a single column `full_name` by\n"
        "concatenating first_name and last_name\n"
        "with a space in between.\n"
        "Sort by full_name.\n\n"
        "Expected output:\n[('Emperor PyPhone',), ('Karim Ali',), ('Rahim Khan',)]"
    ),
    expected_output="[('Emperor PyPhone',), ('Karim Ali',), ('Rahim Khan',)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE citizens (id INTEGER, first_name TEXT, last_name TEXT);",
        "INSERT INTO citizens VALUES (1,'Emperor','PyPhone'), (2,'Rahim','Khan'), (3,'Karim','Ali');",
        "SELECT first_name || ' ' || last_name AS full_name FROM citizens ORDER BY full_name;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "📊  Multiple Computed Columns – Tax & Net Pay\n\n"
        "Create a table `payroll` with columns:\n"
        "  id INTEGER, name TEXT, gross REAL, tax_rate REAL.\n"
        "Insert 3 rows with different salaries and tax rates.\n"
        "Return name, gross, tax (gross * tax_rate),\n"
        "and net_pay (gross - tax), all with meaningful aliases.\n"
        "Sort by net_pay descending.\n\n"
        "Expected output:\n[('Emperor',5000.0,500.0,4500.0), ('Ali',4500.0,450.0,4050.0), ('Rahim',4000.0,400.0,3600.0)]"
    ),
    expected_output="[('Emperor', 5000.0, 500.0, 4500.0), ('Ali', 4500.0, 450.0, 4050.0), ('Rahim', 4000.0, 400.0, 3600.0)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE payroll (id INTEGER, name TEXT, gross REAL, tax_rate REAL);",
        "INSERT INTO payroll VALUES (1,'Emperor',5000,0.1), (2,'Rahim',4000,0.1), (3,'Ali',4500,0.1);",
        "SELECT name, gross, gross * tax_rate AS tax, gross - gross * tax_rate AS net_pay FROM payroll ORDER BY net_pay DESC;"
    ]
)

hard2 = Task(
    description=(
        "🧪  Alias in ORDER BY Only\n\n"
        "The `soldiers` table has 5 rows.\n"
        "Return name and salary. Use the alias `pay`\n"
        "for the salary column, and sort by `pay` descending.\n"
        "Remember: you can't use `pay` in WHERE,\n"
        "but you CAN use it in ORDER BY.\n\n"
        "Expected output:\n[('Emperor',5000.0), ('Ali',4500.0), ('Rahim',4000.0), ('Hasan',3500.0), ('Karim',2000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE soldiers (id INTEGER, name TEXT, rank TEXT, salary REAL);"
        "INSERT INTO soldiers VALUES (1,'Emperor','General',5000), (2,'Rahim','Colonel',4000), (3,'Karim','Private',2000), (4,'Ali','General',4500), (5,'Hasan','Colonel',3500);"
    ),
    expected_output="[('Emperor', 5000.0), ('Ali', 4500.0), ('Rahim', 4000.0), ('Hasan', 3500.0), ('Karim', 2000.0)]",
    level=Level.HARD,
    hints=[
        "SELECT name, salary AS pay FROM soldiers ORDER BY pay DESC;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L14.json",
        module_name="Module_02_Filtering_Conditional_Logic",
        lesson_name="L14_Aliases_AS_Computed_Columns"
    )
