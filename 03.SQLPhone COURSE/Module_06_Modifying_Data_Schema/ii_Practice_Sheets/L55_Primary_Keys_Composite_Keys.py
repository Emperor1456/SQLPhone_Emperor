import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🔑  Single Primary Key – Auto‑increment\n\n"
        "Create a table `regiments` with columns:\n"
        "  • regiment_id INTEGER PRIMARY KEY\n"
        "  • regiment_name TEXT NOT NULL\n\n"
        "Insert three rows. Omit regiment_id (or use NULL)\n"
        "so SQLite auto‑assigns values.\n"
        "Then SELECT all rows sorted by regiment_id.\n\n"
        "Expected output:\n[(1,'Imperial Guard'), (2,'Red Guard'), (3,'Blue Shield')]"
    ),
    expected_output="[(1, 'Imperial Guard'), (2, 'Red Guard'), (3, 'Blue Shield')]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE regiments (regiment_id INTEGER PRIMARY KEY, regiment_name TEXT NOT NULL);",
        "INSERT INTO regiments (regiment_name) VALUES ('Imperial Guard'), ('Red Guard'), ('Blue Shield');",
        "SELECT * FROM regiments ORDER BY regiment_id;"
    ]
)

easy2 = Task(
    description=(
        "📋  Single Primary Key – Natural Key\n\n"
        "Create a table `countries` with columns:\n"
        "  • country_code TEXT PRIMARY KEY\n"
        "  • country_name TEXT NOT NULL\n\n"
        "Insert three countries using their real codes.\n"
        "Then SELECT all rows sorted by country_code.\n\n"
        "Expected output:\n[('BD','Bangladesh'), ('IN','India'), ('US','United States')]"
    ),
    expected_output="[('BD', 'Bangladesh'), ('IN', 'India'), ('US', 'United States')]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE countries (country_code TEXT PRIMARY KEY, country_name TEXT NOT NULL);",
        "INSERT INTO countries VALUES ('BD','Bangladesh'), ('IN','India'), ('US','United States');",
        "SELECT * FROM countries ORDER BY country_code;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🧱  Composite Primary Key – Join Table\n\n"
        "Create a table `assignments` with columns:\n"
        "  • soldier_id INTEGER\n"
        "  • mission_id INTEGER\n"
        "  • assigned_date TEXT DEFAULT (date('now'))\n"
        "  • PRIMARY KEY (soldier_id, mission_id)\n\n"
        "Insert four assignments. Try inserting a duplicate\n"
        "(same soldier, same mission), which should fail.\n"
        "Then SELECT the successfully inserted rows,\n"
        "sorted by soldier_id, then mission_id.\n\n"
        "Expected output:\n[(1,1,'2026-07-01'), (1,2,'2026-07-02'), (2,1,'2026-07-03'), (2,3,'2026-07-04')]"
    ),
    expected_output="[(1, 1, '2026-07-01'), (1, 2, '2026-07-02'), (2, 1, '2026-07-03'), (2, 3, '2026-07-04')]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE assignments (soldier_id INTEGER, mission_id INTEGER, assigned_date TEXT DEFAULT (date('now')), PRIMARY KEY(soldier_id, mission_id));",
        "INSERT INTO assignments VALUES (1,1,'2026-07-01'), (1,2,'2026-07-02'), (2,1,'2026-07-03'), (2,3,'2026-07-04');",
        "SELECT * FROM assignments ORDER BY soldier_id, mission_id;"
    ]
)

medium2 = Task(
    description=(
        "📊  Composite PK with Foreign Keys – Order Items\n\n"
        "Create a table `order_items` with columns:\n"
        "  • order_id INTEGER\n"
        "  • product_id INTEGER\n"
        "  • quantity INTEGER CHECK(quantity > 0)\n"
        "  • PRIMARY KEY (order_id, product_id)\n"
        "  • FOREIGN KEY (order_id) REFERENCES orders(id)\n"
        "  • FOREIGN KEY (product_id) REFERENCES products(id)\n\n"
        "Also create `orders` and `products` tables.\n"
        "Insert 2 orders, 3 products, and 4 order_items.\n"
        "Then SELECT a JOIN showing order_id, product name, qty.\n"
        "Sort by order_id, product_id.\n\n"
        "Expected output:\n[(1,'Laptop',2), (1,'Mouse',5), (2,'Keyboard',1), (2,'Monitor',3)]"
    ),
    expected_output="[(1, 'Laptop', 2), (1, 'Mouse', 5), (2, 'Keyboard', 1), (2, 'Monitor', 3)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE orders (id INTEGER PRIMARY KEY, customer TEXT);",
        "INSERT INTO orders VALUES (1,'Emperor'), (2,'Rahim');",
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT);",
        "INSERT INTO products VALUES (1,'Laptop'), (2,'Mouse'), (3,'Keyboard'), (4,'Monitor');",
        "CREATE TABLE order_items (order_id INTEGER, product_id INTEGER, quantity INTEGER CHECK(quantity > 0), PRIMARY KEY(order_id, product_id), FOREIGN KEY(order_id) REFERENCES orders(id), FOREIGN KEY(product_id) REFERENCES products(id));",
        "INSERT INTO order_items VALUES (1,1,2), (1,2,5), (2,3,1), (2,4,3);",
        "SELECT oi.order_id, p.name, oi.quantity FROM order_items oi JOIN products p ON oi.product_id = p.id ORDER BY oi.order_id, oi.product_id;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  Surrogate vs Natural Key – Design Decision\n\n"
        "Create a table `passports` that stores citizen passport\n"
        "information. Decide between a surrogate key (id PK) or\n"
        "a natural key (passport_number PK).\n"
        "Choose the natural key (passport_number TEXT PRIMARY KEY)\n"
        "because passport numbers are unique and immutable.\n"
        "Also add: citizen_name TEXT NOT NULL, expiry_date TEXT.\n"
        "Insert two passports.\n"
        "Then SELECT all rows sorted by passport_number.\n\n"
        "Expected output:\n[('A1234567','Emperor','2031-01-01'), ('B9876543','Rahim','2032-06-15')]"
    ),
    expected_output="[('A1234567', 'Emperor', '2031-01-01'), ('B9876543', 'Rahim', '2032-06-15')]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE passports (passport_number TEXT PRIMARY KEY, citizen_name TEXT NOT NULL, expiry_date TEXT);",
        "INSERT INTO passports VALUES ('A1234567','Emperor','2031-01-01'), ('B9876543','Rahim','2032-06-15');",
        "SELECT * FROM passports ORDER BY passport_number;"
    ]
)

hard2 = Task(
    description=(
        "📊  Composite PK Three Columns – Semester Enrolment\n\n"
        "Create a table `enrollments` with columns:\n"
        "  • student_id INTEGER\n"
        "  • course_id INTEGER\n"
        "  • semester TEXT (e.g., '2026-Spring')\n"
        "  • grade TEXT\n"
        "  • PRIMARY KEY (student_id, course_id, semester)\n\n"
        "This allows a student to take the same course in\n"
        "different semesters.\n"
        "Insert 5 rows, including a retake (same student + course,\n"
        "different semester).\n"
        "Then SELECT all rows sorted by student_id, course_id, semester.\n\n"
        "Expected output:\n[(1,1,'2026-Spring','B'), (1,1,'2026-Summer','A'), (1,2,'2026-Spring','C'), (2,1,'2026-Spring','A'), (2,2,'2026-Spring','D')]"
    ),
    expected_output="[(1, 1, '2026-Spring', 'B'), (1, 1, '2026-Summer', 'A'), (1, 2, '2026-Spring', 'C'), (2, 1, '2026-Spring', 'A'), (2, 2, '2026-Spring', 'D')]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE enrollments (student_id INTEGER, course_id INTEGER, semester TEXT, grade TEXT, PRIMARY KEY(student_id, course_id, semester));",
        "INSERT INTO enrollments VALUES (1,1,'2026-Spring','B'), (1,1,'2026-Summer','A'), (1,2,'2026-Spring','C'), (2,1,'2026-Spring','A'), (2,2,'2026-Spring','D');",
        "SELECT * FROM enrollments ORDER BY student_id, course_id, semester;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L55.json",
        module_name="Module_06_Modifying_Data_Schema",
        lesson_name="L55_Primary_Keys_Composite_Keys"
    )
