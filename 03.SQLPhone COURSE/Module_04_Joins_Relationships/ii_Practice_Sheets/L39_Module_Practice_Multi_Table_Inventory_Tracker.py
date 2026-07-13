import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🏗️  Imperial Inventory – Create Tables\n\n"
        "Create four tables with full foreign key relationships:\n\n"
        "1. `suppliers` (id INTEGER PK, name TEXT NOT NULL)\n"
        "2. `products` (id INTEGER PK, name TEXT NOT NULL,\n"
        "   supplier_id INTEGER REFERENCES suppliers(id))\n"
        "3. `warehouses` (id INTEGER PK, name TEXT NOT NULL)\n"
        "4. `stock` (product_id INTEGER, warehouse_id INTEGER,\n"
        "   quantity INTEGER CHECK(quantity >= 0),\n"
        "   PRIMARY KEY(product_id, warehouse_id),\n"
        "   FK(product_id) REFERENCES products(id),\n"
        "   FK(warehouse_id) REFERENCES warehouses(id))\n\n"
        "Insert 2 suppliers, 3 products, 2 warehouses, and\n"
        "5 stock records.\n"
        "Then SELECT all products with their supplier name.\n\n"
        "Expected output:\n[('Laptop','TechCorp'), ('Mouse','TechCorp'), ('Desk','OfficeDepot')]"
    ),
    expected_output="[('Laptop', 'TechCorp'), ('Mouse', 'TechCorp'), ('Desk', 'OfficeDepot')]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE suppliers (id INTEGER PRIMARY KEY, name TEXT NOT NULL);",
        "INSERT INTO suppliers VALUES (1,'TechCorp'), (2,'OfficeDepot');",
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, supplier_id INTEGER REFERENCES suppliers(id));",
        "INSERT INTO products VALUES (1,'Laptop',1), (2,'Mouse',1), (3,'Desk',2);",
        "CREATE TABLE warehouses (id INTEGER PRIMARY KEY, name TEXT NOT NULL);",
        "INSERT INTO warehouses VALUES (1,'Dhaka'), (2,'Chittagong');",
        "CREATE TABLE stock (product_id INTEGER, warehouse_id INTEGER, quantity INTEGER CHECK(quantity >= 0), PRIMARY KEY(product_id, warehouse_id), FOREIGN KEY(product_id) REFERENCES products(id), FOREIGN KEY(warehouse_id) REFERENCES warehouses(id));",
        "INSERT INTO stock VALUES (1,1,50), (1,2,30), (2,1,100), (2,2,75), (3,1,20);",
        "SELECT p.name, s.name FROM products p JOIN suppliers s ON p.supplier_id = s.id ORDER BY p.name;"
    ]
)

easy2 = Task(
    description=(
        "📊  Stock per Warehouse – Basic JOIN\n\n"
        "The four inventory tables are seeded.\n"
        "Write a query that shows the warehouse name,\n"
        "product name, and quantity for all stock records.\n"
        "Join stock → products → warehouses.\n"
        "Sort by warehouse name, then product name.\n\n"
        "Expected output:\n[('Chittagong','Laptop',30), ('Chittagong','Mouse',75), ('Dhaka','Desk',20), ('Dhaka','Laptop',50), ('Dhaka','Mouse',100)]"
    ),
    setup_sql=(
        "CREATE TABLE suppliers (id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO suppliers VALUES (1,'TechCorp'), (2,'OfficeDepot');"
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, supplier_id INTEGER REFERENCES suppliers(id));"
        "INSERT INTO products VALUES (1,'Laptop',1), (2,'Mouse',1), (3,'Desk',2);"
        "CREATE TABLE warehouses (id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO warehouses VALUES (1,'Dhaka'), (2,'Chittagong');"
        "CREATE TABLE stock (product_id INTEGER, warehouse_id INTEGER, quantity INTEGER CHECK(quantity >= 0), PRIMARY KEY(product_id, warehouse_id), FOREIGN KEY(product_id) REFERENCES products(id), FOREIGN KEY(warehouse_id) REFERENCES warehouses(id));"
        "INSERT INTO stock VALUES (1,1,50), (1,2,30), (2,1,100), (2,2,75), (3,1,20);"
    ),
    expected_output="[('Chittagong', 'Laptop', 30), ('Chittagong', 'Mouse', 75), ('Dhaka', 'Desk', 20), ('Dhaka', 'Laptop', 50), ('Dhaka', 'Mouse', 100)]",
    level=Level.EASY,
    hints=[
        "SELECT w.name, p.name, s.quantity FROM stock s JOIN products p ON s.product_id = p.id JOIN warehouses w ON s.warehouse_id = w.id ORDER BY w.name, p.name;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "📈  Total Stock per Product – GROUP BY + JOIN\n\n"
        "The four inventory tables are seeded.\n"
        "Write a query that shows the product name and\n"
        "the total quantity across all warehouses.\n"
        "Include products that have NO stock (LEFT JOIN),\n"
        "showing 0 for their total.\n"
        "Sort by total_quantity descending.\n\n"
        "Expected output:\n[('Mouse',175), ('Laptop',80), ('Desk',20)]"
    ),
    setup_sql=(
        "CREATE TABLE suppliers (id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO suppliers VALUES (1,'TechCorp'), (2,'OfficeDepot');"
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, supplier_id INTEGER REFERENCES suppliers(id));"
        "INSERT INTO products VALUES (1,'Laptop',1), (2,'Mouse',1), (3,'Desk',2);"
        "CREATE TABLE warehouses (id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO warehouses VALUES (1,'Dhaka'), (2,'Chittagong');"
        "CREATE TABLE stock (product_id INTEGER, warehouse_id INTEGER, quantity INTEGER CHECK(quantity >= 0), PRIMARY KEY(product_id, warehouse_id), FOREIGN KEY(product_id) REFERENCES products(id), FOREIGN KEY(warehouse_id) REFERENCES warehouses(id));"
        "INSERT INTO stock VALUES (1,1,50), (1,2,30), (2,1,100), (2,2,75), (3,1,20);"
    ),
    expected_output="[('Mouse', 175), ('Laptop', 80), ('Desk', 20)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT p.name, COALESCE(SUM(s.quantity), 0) AS total_quantity FROM products p LEFT JOIN stock s ON p.id = s.product_id GROUP BY p.id ORDER BY total_quantity DESC;"
    ]
)

medium2 = Task(
    description=(
        "🔍  Supplier Performance – Units Shipped\n\n"
        "The four inventory tables are seeded.\n"
        "Write a query that shows each supplier name,\n"
        "the number of distinct products they supply,\n"
        "and the total quantity of all their products in stock.\n"
        "Include suppliers with zero stock (LEFT JOIN, COALESCE).\n"
        "Sort by total_quantity descending.\n\n"
        "Expected output:\n[('TechCorp',2,255), ('OfficeDepot',1,20)]"
    ),
    setup_sql=(
        "CREATE TABLE suppliers (id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO suppliers VALUES (1,'TechCorp'), (2,'OfficeDepot');"
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, supplier_id INTEGER REFERENCES suppliers(id));"
        "INSERT INTO products VALUES (1,'Laptop',1), (2,'Mouse',1), (3,'Desk',2);"
        "CREATE TABLE warehouses (id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO warehouses VALUES (1,'Dhaka'), (2,'Chittagong');"
        "CREATE TABLE stock (product_id INTEGER, warehouse_id INTEGER, quantity INTEGER CHECK(quantity >= 0), PRIMARY KEY(product_id, warehouse_id), FOREIGN KEY(product_id) REFERENCES products(id), FOREIGN KEY(warehouse_id) REFERENCES warehouses(id));"
        "INSERT INTO stock VALUES (1,1,50), (1,2,30), (2,1,100), (2,2,75), (3,1,20);"
    ),
    expected_output="[('TechCorp', 2, 255), ('OfficeDepot', 1, 20)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT s.name, COUNT(DISTINCT p.id) AS product_count, COALESCE(SUM(st.quantity), 0) AS total_quantity FROM suppliers s LEFT JOIN products p ON s.id = p.supplier_id LEFT JOIN stock st ON p.id = st.product_id GROUP BY s.id ORDER BY total_quantity DESC;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "⚠️  Low‑Stock Alert – Multi‑Table HAVING\n\n"
        "The four inventory tables are seeded.\n"
        "Write a query that shows the product name and\n"
        "total quantity across all warehouses for products\n"
        "whose TOTAL stock is less than 50.\n"
        "Use JOIN, GROUP BY, and HAVING.\n"
        "Also include the supplier name.\n"
        "Sort by total_quantity ascending.\n\n"
        "Expected output:\n[('Desk','OfficeDepot',20)]"
    ),
    setup_sql=(
        "CREATE TABLE suppliers (id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO suppliers VALUES (1,'TechCorp'), (2,'OfficeDepot');"
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, supplier_id INTEGER REFERENCES suppliers(id));"
        "INSERT INTO products VALUES (1,'Laptop',1), (2,'Mouse',1), (3,'Desk',2);"
        "CREATE TABLE warehouses (id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO warehouses VALUES (1,'Dhaka'), (2,'Chittagong');"
        "CREATE TABLE stock (product_id INTEGER, warehouse_id INTEGER, quantity INTEGER CHECK(quantity >= 0), PRIMARY KEY(product_id, warehouse_id), FOREIGN KEY(product_id) REFERENCES products(id), FOREIGN KEY(warehouse_id) REFERENCES warehouses(id));"
        "INSERT INTO stock VALUES (1,1,50), (1,2,30), (2,1,100), (2,2,75), (3,1,20);"
    ),
    expected_output="[('Desk', 'OfficeDepot', 20)]",
    level=Level.HARD,
    hints=[
        "SELECT p.name, sup.name, SUM(s.quantity) AS total_qty FROM products p JOIN suppliers sup ON p.supplier_id = sup.id JOIN stock s ON p.id = s.product_id GROUP BY p.id HAVING SUM(s.quantity) < 50 ORDER BY total_qty ASC;"
    ]
)

hard2 = Task(
    description=(
        "📊  Full Inventory Dashboard – Multi‑KPI\n\n"
        "The four inventory tables are seeded.\n"
        "Write ONE query that returns, for each warehouse:\n"
        "  • warehouse name\n"
        "  • total_units (SUM of all quantities)\n"
        "  • unique_products (COUNT DISTINCT of product_id)\n"
        "  • most_stocked_product (the product with MAX quantity)\n"
        "Use JOIN, GROUP BY, and a subquery for the max product.\n"
        "Sort by total_units descending.\n\n"
        "Expected output:\n[('Dhaka',170,3,'Mouse'), ('Chittagong',105,2,'Mouse')]"
    ),
    setup_sql=(
        "CREATE TABLE suppliers (id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO suppliers VALUES (1,'TechCorp'), (2,'OfficeDepot');"
        "CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, supplier_id INTEGER REFERENCES suppliers(id));"
        "INSERT INTO products VALUES (1,'Laptop',1), (2,'Mouse',1), (3,'Desk',2);"
        "CREATE TABLE warehouses (id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO warehouses VALUES (1,'Dhaka'), (2,'Chittagong');"
        "CREATE TABLE stock (product_id INTEGER, warehouse_id INTEGER, quantity INTEGER CHECK(quantity >= 0), PRIMARY KEY(product_id, warehouse_id), FOREIGN KEY(product_id) REFERENCES products(id), FOREIGN KEY(warehouse_id) REFERENCES warehouses(id));"
        "INSERT INTO stock VALUES (1,1,50), (1,2,30), (2,1,100), (2,2,75), (3,1,20);"
    ),
    expected_output="[('Dhaka', 170, 3, 'Mouse'), ('Chittagong', 105, 2, 'Mouse')]",
    level=Level.HARD,
    hints=[
        "SELECT w.name, SUM(s.quantity) AS total_units, COUNT(DISTINCT s.product_id) AS unique_products, (SELECT p2.name FROM stock s2 JOIN products p2 ON s2.product_id = p2.id WHERE s2.warehouse_id = w.id ORDER BY s2.quantity DESC LIMIT 1) AS most_stocked FROM warehouses w JOIN stock s ON w.id = s.warehouse_id GROUP BY w.id ORDER BY total_units DESC;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L39.json",
        module_name="Module_04_Joins_Relationships",
        lesson_name="L39_Module_Practice_Inventory_Tracker"
    )
