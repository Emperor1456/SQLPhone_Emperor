import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "📛  Naming Conventions – Standardize Columns\n\n"
        "The following table was created by a junior engineer:\n"
        "  CREATE TABLE Emp (id INT, Nm TEXT, Dep TEXT, Sal REAL);\n\n"
        "Re-create the table with proper naming conventions:\n"
        "  • Use snake_case\n"
        "  • Use descriptive names (e.g., employee_name, salary)\n"
        "  • Use INTEGER PRIMARY KEY for the ID\n"
        "  • Add a CHECK constraint to ensure salary > 0\n\n"
        "After creating the improved table, insert the same data\n"
        "and SELECT all rows sorted by id.\n\n"
        "Expected output:\n[(1,'Emperor','Engineering',5000.0), (2,'Rahim','Sales',4000.0)]"
    ),
    expected_output="[(1, 'Emperor', 'Engineering', 5000.0), (2, 'Rahim', 'Sales', 4000.0)]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE employees (employee_id INTEGER PRIMARY KEY, employee_name TEXT NOT NULL, department TEXT, salary REAL CHECK(salary > 0));",
        "INSERT INTO employees VALUES (1, 'Emperor', 'Engineering', 5000), (2, 'Rahim', 'Sales', 4000);",
        "SELECT * FROM employees ORDER BY employee_id;"
    ]
)

easy2 = Task(
    description=(
        "📝  Document Your Table – Add Comments\n\n"
        "The `employees` table exists (from Easy1).\n"
        "Write a query that adds a comment block (using SQL\n"
        "comments) describing the table's purpose, and then\n"
        "SELECT all rows.\n"
        "Also include a single‑line comment explaining\n"
        "the SELECT query itself.\n\n"
        "Expected output:\n[(1,'Emperor','Engineering',5000.0), (2,'Rahim','Sales',4000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE employees (employee_id INTEGER PRIMARY KEY, employee_name TEXT NOT NULL, department TEXT, salary REAL CHECK(salary > 0));"
        "INSERT INTO employees VALUES (1, 'Emperor', 'Engineering', 5000), (2, 'Rahim', 'Sales', 4000);"
    ),
    expected_output="[(1, 'Emperor', 'Engineering', 5000.0), (2, 'Rahim', 'Sales', 4000.0)]",
    level=Level.EASY,
    hints=[
        "/*",
        "  Table: employees",
        "  Purpose: Store employee records with department and salary.",
        "  Constraints: salary > 0",
        "*/",
        "-- Retrieve all active employees",
        "SELECT * FROM employees ORDER BY employee_id;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🧹  Normalize a Denormalized Table – Split Columns\n\n"
        "A table `orders_bad` stores repeating product columns:\n"
        "  order_id, product1, product2, product3, customer\n\n"
        "This violates 1NF. Normalize it by creating two tables:\n"
        "  1. `orders` (order_id PRIMARY KEY, customer)\n"
        "  2. `order_items` (order_id, product, PRIMARY KEY(order_id, product))\n\n"
        "Migrate the existing data (2 orders with products).\n"
        "Then SELECT a JOIN showing order_id, customer, product.\n"
        "Sort by order_id, product.\n\n"
        "Expected output:\n[(1,'Emperor','Laptop'), (1,'Emperor','Mouse'), (2,'Rahim','Keyboard'), (2,'Rahim','Monitor')]"
    ),
    expected_output="[(1, 'Emperor', 'Laptop'), (1, 'Emperor', 'Mouse'), (2, 'Rahim', 'Keyboard'), (2, 'Rahim', 'Monitor')]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE orders (order_id INTEGER PRIMARY KEY, customer TEXT);",
        "INSERT INTO orders VALUES (1, 'Emperor'), (2, 'Rahim');",
        "CREATE TABLE order_items (order_id INTEGER, product TEXT, PRIMARY KEY(order_id, product));",
        "INSERT INTO order_items VALUES (1, 'Laptop'), (1, 'Mouse'), (2, 'Keyboard'), (2, 'Monitor');",
        "SELECT o.order_id, o.customer, oi.product FROM orders o JOIN order_items oi ON o.order_id = oi.order_id ORDER BY o.order_id, oi.product;"
    ]
)

medium2 = Task(
    description=(
        "📊  Choose Correct Data Types – Fix a Bad Schema\n\n"
        "The following table was created poorly:\n"
        "  CREATE TABLE products (id TEXT, name TEXT, price TEXT, in_stock TEXT);\n"
        "All columns are TEXT, even numeric ones.\n"
        "Re-create the table with appropriate types:\n"
        "  • id INTEGER PRIMARY KEY\n"
        "  • name TEXT NOT NULL\n"
        "  • price REAL CHECK(price > 0)\n"
        "  • stock INTEGER DEFAULT 0 CHECK(stock >= 0)\n\n"
        "Insert the same data (converted to proper types) and\n"
        "SELECT all rows sorted by id.\n\n"
        "Expected output:\n[(1,'Laptop',999.99,10), (2,'Mouse',24.99,50)]"
    ),
    expected_output="[(1, 'Laptop', 999.99, 10), (2, 'Mouse', 24.99, 50)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, price REAL CHECK(price > 0), stock INTEGER DEFAULT 0 CHECK(stock >= 0));",
        "INSERT INTO products VALUES (1, 'Laptop', 999.99, 10), (2, 'Mouse', 24.99, 50);",
        "SELECT * FROM products ORDER BY id;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  Full 3NF Design – From Requirements to Schema\n\n"
        "Design a normalized schema for an Imperial Academy:\n"
        "  • Teachers have a name, email, and department.\n"
        "  • Courses have a name, credit hours, and are taught by exactly one teacher.\n"
        "  • Students have a name and enrollment date.\n"
        "  • A student can enroll in many courses; each enrollment has a semester.\n"
        "  • Each student gets one grade per course.\n\n"
        "Create all tables (departments, teachers, courses, students,\n"
        "enrollments, grades) with proper foreign keys and constraints.\n"
        "Then list all table names from sqlite_master, sorted alphabetically.\n\n"
        "Expected output:\n[('courses',), ('departments',), ('enrollments',), ('grades',), ('students',), ('teachers',)]"
    ),
    expected_output="[('courses',), ('departments',), ('enrollments',), ('grades',), ('students',), ('teachers',)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE departments (dept_id INTEGER PRIMARY KEY, dept_name TEXT NOT NULL UNIQUE);",
        "CREATE TABLE teachers (teacher_id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, dept_id INTEGER REFERENCES departments(dept_id));",
        "CREATE TABLE courses (course_id INTEGER PRIMARY KEY, course_name TEXT NOT NULL, credits INTEGER CHECK(credits > 0), teacher_id INTEGER REFERENCES teachers(teacher_id));",
        "CREATE TABLE students (student_id INTEGER PRIMARY KEY, name TEXT NOT NULL, enrollment_date TEXT DEFAULT (date('now')));",
        "CREATE TABLE enrollments (student_id INTEGER, course_id INTEGER, semester TEXT, PRIMARY KEY(student_id, course_id, semester), FOREIGN KEY(student_id) REFERENCES students(student_id), FOREIGN KEY(course_id) REFERENCES courses(course_id));",
        "CREATE TABLE grades (student_id INTEGER, course_id INTEGER, grade TEXT CHECK(grade IN ('A','B','C','D','F')), PRIMARY KEY(student_id, course_id), FOREIGN KEY(student_id) REFERENCES students(student_id), FOREIGN KEY(course_id) REFERENCES courses(course_id));",
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
    ]
)

hard2 = Task(
    description=(
        "📊  When to Denormalize – Add a Counter Column\n\n"
        "You have a `customers` table and an `orders` table.\n"
        "The dashboard needs to show each customer's name and\n"
        "their total number of orders frequently.\n"
        "Instead of COUNTing every time, you decide to add an\n"
        "`order_count` column to `customers` and maintain it\n"
        "with a trigger.\n\n"
        "Create the tables, insert sample data, create a trigger\n"
        "that increments `order_count` on each INSERT into orders.\n"
        "Then insert 3 orders and SELECT customers with their\n"
        "order_count, sorted by customer name.\n\n"
        "Expected output:\n[('Ali',1), ('Emperor',2), ('Rahim',0)]"
    ),
    expected_output="[('Ali', 1), ('Emperor', 2), ('Rahim', 0)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT, order_count INTEGER DEFAULT 0);",
        "INSERT INTO customers (name) VALUES ('Emperor'), ('Rahim'), ('Ali');",
        "CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER REFERENCES customers(id), product TEXT);",
        "CREATE TRIGGER trg_increment_order_count AFTER INSERT ON orders BEGIN UPDATE customers SET order_count = order_count + 1 WHERE id = NEW.customer_id; END;",
        "INSERT INTO orders (customer_id, product) VALUES (1,'Laptop'), (1,'Mouse'), (3,'Keyboard');",
        "SELECT name, order_count FROM customers ORDER BY name;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L68.json",
        module_name="Module_07_Views_Optimization_Security",
        lesson_name="L68_Schema_Design_Best_Practices"
    )
