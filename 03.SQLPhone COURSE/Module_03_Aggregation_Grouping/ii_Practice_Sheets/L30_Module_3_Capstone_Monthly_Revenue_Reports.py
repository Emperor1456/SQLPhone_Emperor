import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🏗️  Imperial Sales – Create & Seed\n\n"
        "Create three tables with full constraints:\n\n"
        "1. `customers`:\n"
        "  • id INTEGER PRIMARY KEY\n"
        "  • name TEXT NOT NULL\n"
        "  • region TEXT NOT NULL\n\n"
        "2. `products`:\n"
        "  • id INTEGER PRIMARY KEY\n"
        "  • name TEXT NOT NULL\n"
        "  • category TEXT NOT NULL\n"
        "  • price REAL CHECK(price > 0)\n\n"
        "3. `sales`:\n"
        "  • id INTEGER PRIMARY KEY\n"
        "  • customer_id INTEGER REFERENCES customers(id)\n"
        "  • product_id INTEGER REFERENCES products(id)\n"
        "  • quantity INTEGER CHECK(quantity > 0)\n"
        "  • sale_date TEXT DEFAULT (date('now'))\n\n"
        "Seed each table with at least 4 rows.\n"
        "Then SELECT all customers sorted by name.\n\n"
        "Expected output:\n[('Alpha Corp','North'), ('Beta Ltd','South'), ('Gamma Inc','East'), ('Delta LLC','North')]"
    ),
    expected_output="[('Alpha Corp', 'North'), ('Beta Ltd', 'South'), ('Gamma Inc', 'East'), ('Delta LLC', 'North')]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT NOT NULL, region TEXT NOT NULL);",
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, category TEXT NOT NULL, price REAL CHECK(price > 0));",
        "CREATE TABLE sales (id INTEGER PRIMARY KEY, customer_id INTEGER REFERENCES customers(id), product_id INTEGER REFERENCES products(id), quantity INTEGER CHECK(quantity > 0), sale_date TEXT DEFAULT (date('now')));",
        "INSERT INTO customers VALUES (1,'Alpha Corp','North'), (2,'Beta Ltd','South'), (3,'Gamma Inc','East'), (4,'Delta LLC','North');",
        "INSERT INTO products VALUES (1,'Laptop','Electronics',1000), (2,'Desk','Furniture',500), (3,'Mouse','Electronics',50), (4,'Chair','Furniture',250);",
        "INSERT INTO sales (customer_id, product_id, quantity, sale_date) VALUES (1,1,5,'2026-01-15'), (2,2,10,'2026-01-20'), (3,3,20,'2026-02-10'), (4,4,5,'2026-02-15'), (1,2,3,'2026-03-01'), (2,1,2,'2026-03-10');",
        "SELECT name, region FROM customers ORDER BY name;"
    ]
)

easy2 = Task(
    description=(
        "📊  Monthly Revenue – GROUP BY Month\n\n"
        "The three tables are seeded with 6 sales.\n"
        "Write a query that returns the total revenue\n"
        "(SUM(quantity * price)) for each month.\n"
        "Join sales → products to get the price.\n"
        "Group by month (strftime '%Y-%m'),\n"
        "return month and revenue.\n"
        "Sort by month.\n\n"
        "Expected output:\n[('2026-01',10000.0), ('2026-02',2250.0), ('2026-03',3500.0)]"
    ),
    setup_sql=(
        "CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT NOT NULL, region TEXT NOT NULL);"
        "INSERT INTO customers VALUES (1,'Alpha Corp','North'), (2,'Beta Ltd','South'), (3,'Gamma Inc','East'), (4,'Delta LLC','North');"
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, category TEXT NOT NULL, price REAL CHECK(price > 0));"
        "INSERT INTO products VALUES (1,'Laptop','Electronics',1000), (2,'Desk','Furniture',500), (3,'Mouse','Electronics',50), (4,'Chair','Furniture',250);"
        "CREATE TABLE sales (id INTEGER PRIMARY KEY, customer_id INTEGER REFERENCES customers(id), product_id INTEGER REFERENCES products(id), quantity INTEGER CHECK(quantity > 0), sale_date TEXT DEFAULT (date('now')));"
        "INSERT INTO sales (customer_id, product_id, quantity, sale_date) VALUES (1,1,5,'2026-01-15'), (2,2,10,'2026-01-20'), (3,3,20,'2026-02-10'), (4,4,5,'2026-02-15'), (1,2,3,'2026-03-01'), (2,1,2,'2026-03-10');"
    ),
    expected_output="[('2026-01', 10000.0), ('2026-02', 2250.0), ('2026-03', 3500.0)]",
    level=Level.EASY,
    hints=[
        "SELECT strftime('%Y-%m', s.sale_date) AS month, SUM(s.quantity * p.price) AS revenue FROM sales s JOIN products p ON s.product_id = p.id GROUP BY month ORDER BY month;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "📈  Regional Breakdown – GROUP BY Region\n\n"
        "The Imperial database has sales across 3 regions.\n"
        "Write a query that returns the total revenue\n"
        "for each region.\n"
        "Join sales → customers → products.\n"
        "Return region and SUM(quantity * price) as revenue.\n"
        "Sort by revenue descending.\n\n"
        "Expected output:\n[('North',6500.0), ('South',5500.0), ('East',1000.0)]"
    ),
    setup_sql=(
        "CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT NOT NULL, region TEXT NOT NULL);"
        "INSERT INTO customers VALUES (1,'Alpha Corp','North'), (2,'Beta Ltd','South'), (3,'Gamma Inc','East'), (4,'Delta LLC','North');"
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, category TEXT NOT NULL, price REAL CHECK(price > 0));"
        "INSERT INTO products VALUES (1,'Laptop','Electronics',1000), (2,'Desk','Furniture',500), (3,'Mouse','Electronics',50), (4,'Chair','Furniture',250);"
        "CREATE TABLE sales (id INTEGER PRIMARY KEY, customer_id INTEGER REFERENCES customers(id), product_id INTEGER REFERENCES products(id), quantity INTEGER CHECK(quantity > 0), sale_date TEXT DEFAULT (date('now')));"
        "INSERT INTO sales (customer_id, product_id, quantity, sale_date) VALUES (1,1,5,'2026-01-15'), (2,2,10,'2026-01-20'), (3,3,20,'2026-02-10'), (4,4,5,'2026-02-15'), (1,2,3,'2026-03-01'), (2,1,2,'2026-03-10');"
    ),
    expected_output="[('North', 6500.0), ('South', 5500.0), ('East', 1000.0)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT c.region, SUM(s.quantity * p.price) AS revenue FROM sales s JOIN customers c ON s.customer_id = c.id JOIN products p ON s.product_id = p.id GROUP BY c.region ORDER BY revenue DESC;"
    ]
)

medium2 = Task(
    description=(
        "📊  Monthly + Category – Multi‑Column GROUP BY\n\n"
        "The Imperial database has 6 sales.\n"
        "Write a query that groups by month AND category,\n"
        "returning month, category, and SUM(quantity*price) as revenue.\n"
        "Sort by month, then revenue descending.\n\n"
        "Expected output:\n[('2026-01','Electronics',5000.0), ('2026-01','Furniture',5000.0), ('2026-02','Electronics',1000.0), ('2026-02','Furniture',1250.0), ('2026-03','Electronics',2000.0), ('2026-03','Furniture',1500.0)]"
    ),
    setup_sql=(
        "CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT NOT NULL, region TEXT NOT NULL);"
        "INSERT INTO customers VALUES (1,'Alpha Corp','North'), (2,'Beta Ltd','South'), (3,'Gamma Inc','East'), (4,'Delta LLC','North');"
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, category TEXT NOT NULL, price REAL CHECK(price > 0));"
        "INSERT INTO products VALUES (1,'Laptop','Electronics',1000), (2,'Desk','Furniture',500), (3,'Mouse','Electronics',50), (4,'Chair','Furniture',250);"
        "CREATE TABLE sales (id INTEGER PRIMARY KEY, customer_id INTEGER REFERENCES customers(id), product_id INTEGER REFERENCES products(id), quantity INTEGER CHECK(quantity > 0), sale_date TEXT DEFAULT (date('now')));"
        "INSERT INTO sales (customer_id, product_id, quantity, sale_date) VALUES (1,1,5,'2026-01-15'), (2,2,10,'2026-01-20'), (3,3,20,'2026-02-10'), (4,4,5,'2026-02-15'), (1,2,3,'2026-03-01'), (2,1,2,'2026-03-10');"
    ),
    expected_output="[('2026-01', 'Electronics', 5000.0), ('2026-01', 'Furniture', 5000.0), ('2026-02', 'Electronics', 1000.0), ('2026-02', 'Furniture', 1250.0), ('2026-03', 'Electronics', 2000.0), ('2026-03', 'Furniture', 1500.0)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT strftime('%Y-%m', s.sale_date) AS month, p.category, SUM(s.quantity * p.price) AS revenue FROM sales s JOIN products p ON s.product_id = p.id GROUP BY month, p.category ORDER BY month, revenue DESC;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧪  Conditional Breakdown – Pivot by Category\n\n"
        "The Imperial database has 6 sales.\n"
        "Write ONE query that returns, for each month:\n"
        "  • month (YYYY-MM)\n"
        "  • electronics_revenue (SUM where category='Electronics')\n"
        "  • furniture_revenue (SUM where category='Furniture')\n"
        "  • total_revenue (SUM of all)\n"
        "Use SUM(CASE WHEN … THEN amount ELSE 0 END).\n"
        "Sort by month.\n\n"
        "Expected output:\n[('2026-01',5000.0,5000.0,10000.0), ('2026-02',1000.0,1250.0,2250.0), ('2026-03',2000.0,1500.0,3500.0)]"
    ),
    setup_sql=(
        "CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT NOT NULL, region TEXT NOT NULL);"
        "INSERT INTO customers VALUES (1,'Alpha Corp','North'), (2,'Beta Ltd','South'), (3,'Gamma Inc','East'), (4,'Delta LLC','North');"
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, category TEXT NOT NULL, price REAL CHECK(price > 0));"
        "INSERT INTO products VALUES (1,'Laptop','Electronics',1000), (2,'Desk','Furniture',500), (3,'Mouse','Electronics',50), (4,'Chair','Furniture',250);"
        "CREATE TABLE sales (id INTEGER PRIMARY KEY, customer_id INTEGER REFERENCES customers(id), product_id INTEGER REFERENCES products(id), quantity INTEGER CHECK(quantity > 0), sale_date TEXT DEFAULT (date('now')));"
        "INSERT INTO sales (customer_id, product_id, quantity, sale_date) VALUES (1,1,5,'2026-01-15'), (2,2,10,'2026-01-20'), (3,3,20,'2026-02-10'), (4,4,5,'2026-02-15'), (1,2,3,'2026-03-01'), (2,1,2,'2026-03-10');"
    ),
    expected_output="[('2026-01', 5000.0, 5000.0, 10000.0), ('2026-02', 1000.0, 1250.0, 2250.0), ('2026-03', 2000.0, 1500.0, 3500.0)]",
    level=Level.HARD,
    hints=[
        "SELECT strftime('%Y-%m', s.sale_date) AS month, SUM(CASE WHEN p.category='Electronics' THEN s.quantity * p.price ELSE 0 END) AS electronics_revenue, SUM(CASE WHEN p.category='Furniture' THEN s.quantity * p.price ELSE 0 END) AS furniture_revenue, SUM(s.quantity * p.price) AS total_revenue FROM sales s JOIN products p ON s.product_id = p.id GROUP BY month ORDER BY month;"
    ]
)

hard2 = Task(
    description=(
        "📊  Quarter‑over‑Quarter Growth – LAG Window\n\n"
        "Create a table `quarterly` with columns:\n"
        "  • quarter TEXT, revenue REAL.\n"
        "Insert 4 rows (2026-Q1 through 2026-Q4).\n"
        "Use LAG() to compute the previous quarter's\n"
        "revenue and the growth percentage.\n"
        "Return quarter, revenue, prev_quarter,\n"
        "and ROUND((revenue-prev)/prev*100, 1) as growth_pct.\n"
        "Sort by quarter.\n\n"
        "Expected output:\n[('2026-Q1',10000.0,None,None), ('2026-Q2',8000.0,10000.0,-20.0), ('2026-Q3',12000.0,8000.0,50.0), ('2026-Q4',15000.0,12000.0,25.0)]"
    ),
    expected_output="[('2026-Q1', 10000.0, None, None), ('2026-Q2', 8000.0, 10000.0, -20.0), ('2026-Q3', 12000.0, 8000.0, 50.0), ('2026-Q4', 15000.0, 12000.0, 25.0)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE quarterly (quarter TEXT, revenue REAL);",
        "INSERT INTO quarterly VALUES ('2026-Q1',10000), ('2026-Q2',8000), ('2026-Q3',12000), ('2026-Q4',15000);",
        "SELECT quarter, revenue, LAG(revenue) OVER (ORDER BY quarter) AS prev_quarter, ROUND((revenue - LAG(revenue) OVER (ORDER BY quarter)) * 100.0 / LAG(revenue) OVER (ORDER BY quarter), 1) AS growth_pct FROM quarterly ORDER BY quarter;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L30.json",
        module_name="Module_03_Aggregation_Grouping",
        lesson_name="L30_Module_3_Capstone"
    )
