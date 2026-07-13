import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "✏️  Update Through a Simple View\n\n"
        "Create a table `officers` with columns:\n"
        "  • id INTEGER PRIMARY KEY\n"
        "  • name TEXT NOT NULL\n"
        "  • rank TEXT\n\n"
        "Insert three officers.\n"
        "Create a view `v_officers` that shows all columns.\n"
        "Then use an UPDATE statement on the VIEW to\n"
        "change the rank of 'Rahim' to 'Colonel'.\n"
        "Finally SELECT all rows from the table (not view)\n"
        "sorted by id to confirm the update worked.\n\n"
        "Expected output:\n[(1,'Emperor','General'), (2,'Rahim','Colonel'), (3,'Ali','Major')]"
    ),
    expected_output="[(1, 'Emperor', 'General'), (2, 'Rahim', 'Colonel'), (3, 'Ali', 'Major')]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE officers (id INTEGER PRIMARY KEY, name TEXT NOT NULL, rank TEXT);",
        "INSERT INTO officers VALUES (1,'Emperor','General'), (2,'Rahim','Major'), (3,'Ali','Major');",
        "CREATE VIEW v_officers AS SELECT * FROM officers;",
        "UPDATE v_officers SET rank = 'Colonel' WHERE name = 'Rahim';",
        "SELECT * FROM officers ORDER BY id;"
    ]
)

easy2 = Task(
    description=(
        "🔍  Read‑Only View – Try to Insert\n\n"
        "Create a view `v_generals` that selects only\n"
        "officers with rank = 'General' from the `officers`\n"
        "table (the same table from Easy1 now has Emperor\n"
        "as the only General).\n"
        "Try to INSERT into this view (it will fail because\n"
        "the view is not updatable – it has a WHERE clause).\n"
        "The engine will catch the error; just show that\n"
        "the underlying table remains unchanged.\n\n"
        "Expected output:\n[(1,'Emperor','General'), (2,'Rahim','Colonel'), (3,'Ali','Major')]"
    ),
    setup_sql=(
        "CREATE TABLE officers (id INTEGER PRIMARY KEY, name TEXT NOT NULL, rank TEXT);"
        "INSERT INTO officers VALUES (1,'Emperor','General'), (2,'Rahim','Colonel'), (3,'Ali','Major');"
        "CREATE VIEW v_generals AS SELECT * FROM officers WHERE rank = 'General';"
    ),
    expected_output="[(1, 'Emperor', 'General'), (2, 'Rahim', 'Colonel'), (3, 'Ali', 'Major')]",
    level=Level.EASY,
    hints=[
        "INSERT INTO v_generals (name, rank) VALUES ('Spy', 'General'); -- fails silently or caught",
        "SELECT * FROM officers ORDER BY id;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🧪  INSTEAD OF Trigger – Make Complex View Updatable\n\n"
        "Create two tables: `regiments` and `soldiers`.\n"
        "Create a view `v_soldier_info` that JOINs them\n"
        "and shows soldier name, regiment name, salary.\n\n"
        "Since the view joins two tables, it is not natively\n"
        "updatable. Create an INSTEAD OF UPDATE trigger\n"
        "that intercepts UPDATEs on the view and updates\n"
        "the underlying soldiers.salary column.\n\n"
        "Then UPDATE the view to raise Emperor's salary to 5500.\n"
        "Finally SELECT the underlying soldiers table.\n\n"
        "Expected output:\n[(1,'Emperor',1,5500.0), (2,'Rahim',2,4000.0)]"
    ),
    expected_output="[(1, 'Emperor', 1, 5500.0), (2, 'Rahim', 2, 4000.0)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE regiments (id INTEGER PRIMARY KEY, regiment_name TEXT);",
        "INSERT INTO regiments VALUES (1,'Imperial Guard'), (2,'Red Guard');",
        "CREATE TABLE soldiers (id INTEGER PRIMARY KEY, name TEXT, regiment_id INTEGER, salary REAL);",
        "INSERT INTO soldiers VALUES (1,'Emperor',1,5000), (2,'Rahim',2,4000);",
        "CREATE VIEW v_soldier_info AS SELECT s.id, s.name, r.regiment_name, s.salary FROM soldiers s JOIN regiments r ON s.regiment_id = r.id;",
        "CREATE TRIGGER trg_update_soldier_info INSTEAD OF UPDATE ON v_soldier_info BEGIN UPDATE soldiers SET salary = NEW.salary WHERE id = OLD.id; END;",
        "UPDATE v_soldier_info SET salary = 5500 WHERE name = 'Emperor';",
        "SELECT * FROM soldiers ORDER BY id;"
    ]
)

medium2 = Task(
    description=(
        "📊  Materialized View Alternative – Summary Table\n\n"
        "Create a table `sales` with columns:\n"
        "  • id INTEGER, product TEXT, amount REAL, sale_date TEXT.\n"
        "Insert 6 sales across two months.\n"
        "Create a summary table `monthly_sales` to hold\n"
        "pre‑computed totals.\n\n"
        "Write a query to populate `monthly_sales` with\n"
        "monthly aggregates (strftime, SUM).\n"
        "Then SELECT from the summary table sorted by month.\n\n"
        "Expected output:\n[('2026-01',800.0,2), ('2026-02',650.0,3)]"
    ),
    expected_output="[('2026-01', 800.0, 2), ('2026-02', 650.0, 3)]",
    level=Level.MEDIUM,
    hints=[
        "CREATE TABLE sales (id INTEGER, product TEXT, amount REAL, sale_date TEXT);",
        "INSERT INTO sales VALUES (1,'Laptop',500,'2026-01-15'), (2,'Mouse',300,'2026-01-25'), (3,'Desk',400,'2026-02-10'), (4,'Chair',150,'2026-02-20'), (5,'Monitor',100,'2026-02-28'), (6,'Keyboard',0,'2026-02-01');",
        "CREATE TABLE monthly_sales (month TEXT, total_amount REAL, order_count INTEGER);",
        "INSERT INTO monthly_sales SELECT strftime('%Y-%m', sale_date), SUM(amount), COUNT(*) FROM sales WHERE amount > 0 GROUP BY strftime('%Y-%m', sale_date);",
        "SELECT * FROM monthly_sales ORDER BY month;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🔄  Refresh Materialized View – Complete Pattern\n\n"
        "Create a `revenue` table with products and prices.\n"
        "Create a materialized summary table `product_revenue`\n"
        "that stores product_name and total_revenue (SUM).\n"
        "Write a refresh procedure:\n"
        "  1. DELETE all rows from product_revenue\n"
        "  2. INSERT aggregated data from revenue.\n"
        "First insert 4 sales, refresh, then show summary.\n"
        "Then insert 2 more sales, refresh again, show summary.\n\n"
        "Expected output (after second refresh):\n[('Laptop',2000.0), ('Mouse',250.0), ('Keyboard',160.0)]"
    ),
    expected_output="[('Laptop', 2000.0), ('Mouse', 250.0), ('Keyboard', 160.0)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE revenue (id INTEGER, product TEXT, amount REAL, sale_date TEXT);",
        "INSERT INTO revenue VALUES (1,'Laptop',1000,'2026-07-01'), (2,'Mouse',50,'2026-07-02'), (3,'Laptop',500,'2026-07-03'), (4,'Keyboard',80,'2026-07-04');",
        "CREATE TABLE product_revenue (product TEXT, total_revenue REAL);",
        "DELETE FROM product_revenue;",
        "INSERT INTO product_revenue SELECT product, SUM(amount) FROM revenue GROUP BY product;",
        "INSERT INTO revenue VALUES (5,'Mouse',200,'2026-07-05'), (6,'Keyboard',80,'2026-07-06');",
        "DELETE FROM product_revenue;",
        "INSERT INTO product_revenue SELECT product, SUM(amount) FROM revenue GROUP BY product;",
        "SELECT * FROM product_revenue ORDER BY product;"
    ]
)

hard2 = Task(
    description=(
        "🧱  Trigger‑Based Materialized View – Auto Refresh\n\n"
        "Create a table `orders` (id, product, qty, price).\n"
        "Create a summary table `order_summary` (product, total_qty, total_value).\n"
        "Write an AFTER INSERT trigger on `orders` that\n"
        "automatically updates the summary table:\n"
        "  • If product already in summary, UPDATE its totals\n"
        "  • If not, INSERT a new row.\n"
        "Insert 3 orders, then SELECT from the summary table,\n"
        "sorted by product.\n\n"
        "Expected output:\n[('Laptop',5,5000.0), ('Mouse',15,750.0)]"
    ),
    expected_output="[('Laptop', 5, 5000.0), ('Mouse', 15, 750.0)]",
    level=Level.HARD,
    hints=[
        "CREATE TABLE orders (id INTEGER PRIMARY KEY, product TEXT, qty INTEGER, price REAL);",
        "CREATE TABLE order_summary (product TEXT PRIMARY KEY, total_qty INTEGER, total_value REAL);",
        "CREATE TRIGGER trg_update_summary AFTER INSERT ON orders BEGIN INSERT INTO order_summary (product, total_qty, total_value) VALUES (NEW.product, NEW.qty, NEW.qty * NEW.price) ON CONFLICT(product) DO UPDATE SET total_qty = total_qty + NEW.qty, total_value = total_value + NEW.qty * NEW.price; END;",
        "INSERT INTO orders (product, qty, price) VALUES ('Laptop', 3, 1000), ('Mouse', 10, 50), ('Laptop', 2, 1000), ('Mouse', 5, 50);",
        "SELECT * FROM order_summary ORDER BY product;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L62.json",
        module_name="Module_07_Views_Optimization_Security",
        lesson_name="L62_Updatable_Views_Materialized"
    )
