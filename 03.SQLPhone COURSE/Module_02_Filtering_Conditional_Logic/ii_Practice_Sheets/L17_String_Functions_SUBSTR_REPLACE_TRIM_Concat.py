import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "✂️  SUBSTR – Extract Initials\n\n"
        "Create a table `agents` with columns:\n"
        "  • id INTEGER\n"
        "  • code_name TEXT\n\n"
        "Insert 3 agents:\n"
        "  (1, 'Alpha-007')\n"
        "  (2, 'Beta-009')\n"
        "  (3, 'Gamma-012')\n\n"
        "Use SUBSTR to extract the first 5 characters\n"
        "of each code_name (the Greek letter).\n"
        "Return code_name and the extracted prefix.\n\n"
        "Expected output:\n[('Alpha-007','Alpha'), ('Beta-009','Beta-'), ('Gamma-012','Gamma')]"
    ),
    expected_output="[('Alpha-007', 'Alpha'), ('Beta-009', 'Beta-'), ('Gamma-012', 'Gamma')]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE agents (id INTEGER, code_name TEXT);",
        "INSERT INTO agents VALUES (1,'Alpha-007'), (2,'Beta-009'), (3,'Gamma-012');",
        "SELECT code_name, SUBSTR(code_name, 1, 5) AS prefix FROM agents;"
    ]
)

easy2 = Task(
    description=(
        "➕  Concatenation – Full Address\n\n"
        "Create a table `locations` with columns:\n"
        "  • id INTEGER, city TEXT, country TEXT.\n"
        "Insert 3 rows.\n"
        "Use || to return a single column `address`\n"
        "in the format 'city, country'.\n"
        "Sort by city.\n\n"
        "Expected output:\n[('Chittagong, Bangladesh',), ('Dhaka, Bangladesh',), ('Khulna, Bangladesh',)]"
    ),
    expected_output="[('Chittagong, Bangladesh',), ('Dhaka, Bangladesh',), ('Khulna, Bangladesh',)]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE locations (id INTEGER, city TEXT, country TEXT);",
        "INSERT INTO locations VALUES (1,'Dhaka','Bangladesh'), (2,'Chittagong','Bangladesh'), (3,'Khulna','Bangladesh');",
        "SELECT city || ', ' || country AS address FROM locations ORDER BY city;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🔄  REPLACE – Standardize Phone Numbers\n\n"
        "Create a table `contacts` with columns:\n"
        "  • id INTEGER, name TEXT, phone TEXT.\n"
        "Insert 3 rows with phone numbers containing hyphens.\n"
        "Use REPLACE to remove all hyphens from phone numbers.\n"
        "Return name and the clean phone number.\n\n"
        "Expected output:\n[('Emperor','+8801700000000'), ('Rahim','+8801800000000'), ('Karim','+8801900000000')]"
    ),
    expected_output="[('Emperor', '+8801700000000'), ('Rahim', '+8801800000000'), ('Karim', '+8801900000000')]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE contacts (id INTEGER, name TEXT, phone TEXT);",
        "INSERT INTO contacts VALUES (1,'Emperor','+880-1700-000000'), (2,'Rahim','+880-1800-000000'), (3,'Karim','+880-1900-000000');",
        "SELECT name, REPLACE(phone, '-', '') AS clean_phone FROM contacts;"
    ]
)

medium2 = Task(
    description=(
        "🧹  TRIM – Clean Raw Input\n\n"
        "Create a table `raw_data` with columns:\n"
        "  • id INTEGER, input TEXT.\n"
        "Insert 3 rows with leading/trailing spaces.\n"
        "Use TRIM to return the cleaned input.\n"
        "Also return the length before and after trimming.\n\n"
        "Expected output:\n[('  Emperor  ',10,'Emperor',7), ('  Rahim',7,'Rahim',5), ('Karim  ',7,'Karim',5)]"
    ),
    expected_output="[('  Emperor  ', 10, 'Emperor', 7), ('  Rahim', 7, 'Rahim', 5), ('Karim  ', 7, 'Karim', 5)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE raw_data (id INTEGER, input TEXT);",
        "INSERT INTO raw_data VALUES (1,'  Emperor  '), (2,'  Rahim'), (3,'Karim  ');",
        "SELECT input, LENGTH(input) AS before_len, TRIM(input) AS cleaned, LENGTH(TRIM(input)) AS after_len FROM raw_data;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  Combined Functions – Mask Account\n\n"
        "Create a table `accounts` with columns:\n"
        "  • id INTEGER, holder TEXT, account_number TEXT.\n"
        "Insert 3 rows with 16‑digit account numbers.\n"
        "Return holder and a masked version of the\n"
        "account number showing only the last 4 digits,\n"
        "preceded by '****'.\n"
        "Use SUBSTR and ||.\n\n"
        "Expected output:\n[('Emperor','****3456'), ('Rahim','****7890'), ('Karim','****1234')]"
    ),
    expected_output="[('Emperor', '****3456'), ('Rahim', '****7890'), ('Karim', '****1234')]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE accounts (id INTEGER, holder TEXT, account_number TEXT);",
        "INSERT INTO accounts VALUES (1,'Emperor','1234567890123456'), (2,'Rahim','9876543210987890'), (3,'Karim','5555666677771234');",
        "SELECT holder, '****' || SUBSTR(account_number, -4) AS masked FROM accounts;"
    ]
)

hard2 = Task(
    description=(
        "🔤  SUBSTR + REPLACE – Initials from Name\n\n"
        "Create a table `soldiers` with columns:\n"
        "  • id INTEGER, full_name TEXT.\n"
        "Insert 4 rows with names like 'Emperor PyPhone'.\n"
        "Write a query that returns full_name and\n"
        "initials (e.g., 'E.P.').\n"
        "Steps:\n"
        "  1. Extract first character of full_name (SUBSTR)\n"
        "  2. Find the space position (INSTR)\n"
        "  3. Extract first character after space\n"
        "  4. Concatenate with a dot.\n\n"
        "Expected output:\n[('Emperor PyPhone','E.P.'), ('Rahim Khan','R.K.'), ('Karim Ali','K.A.'), ('Hasan Ahmed','H.A.')]"
    ),
    expected_output="[('Emperor PyPhone', 'E.P.'), ('Rahim Khan', 'R.K.'), ('Karim Ali', 'K.A.'), ('Hasan Ahmed', 'H.A.')]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE soldiers (id INTEGER, full_name TEXT);",
        "INSERT INTO soldiers VALUES (1,'Emperor PyPhone'), (2,'Rahim Khan'), (3,'Karim Ali'), (4,'Hasan Ahmed');",
        "SELECT full_name, SUBSTR(full_name,1,1) || '.' || SUBSTR(full_name, INSTR(full_name,' ')+1, 1) || '.' AS initials FROM soldiers;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L17.json",
        module_name="Module_02_Filtering_Conditional_Logic",
        lesson_name="L17_String_Functions"
    )
