import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🏗️  Imperial Supply Chain – Create Tables & Seed\n\n"
        "Create five tables with full constraints:\n\n"
        "1. `suppliers` (supplier_id PK, name TEXT NOT NULL)\n"
        "2. `products` (product_id PK, name TEXT NOT NULL,\n"
        "   supplier_id INTEGER REFERENCES suppliers)\n"
        "3. `warehouses` (warehouse_id PK, name TEXT NOT NULL)\n"
        "4. `shipments` (shipment_id PK, supplier_id INTEGER\n"
        "   REFERENCES suppliers, warehouse_id INTEGER\n"
        "   REFERENCES warehouses, ship_date TEXT DEFAULT (date('now')))\n"
        "5. `shipment_items` (shipment_id INTEGER, product_id INTEGER,\n"
        "   quantity INTEGER CHECK(quantity > 0),\n"
        "   PRIMARY KEY(shipment_id, product_id),\n"
        "   FK(shipment_id) REFERENCES shipments ON DELETE CASCADE,\n"
        "   FK(product_id) REFERENCES products)\n\n"
        "Insert 2 suppliers, 3 products, 2 warehouses, 3 shipments,\n"
        "and 4 shipment items.\n"
        "Then SELECT all supplier names sorted alphabetically.\n\n"
        "Expected output: [('OfficeDepot',), ('TechCorp',)]"
    ),
    expected_output="[('OfficeDepot',), ('TechCorp',)]",
    level=Level.EASY,
    hints=[
        "CREATE TABLE suppliers (supplier_id INTEGER PRIMARY KEY, name TEXT NOT NULL);",
        "INSERT INTO suppliers VALUES (1,'TechCorp'), (2,'OfficeDepot');",
        "CREATE TABLE products (product_id INTEGER PRIMARY KEY, name TEXT NOT NULL, supplier_id INTEGER REFERENCES suppliers(supplier_id));",
        "INSERT INTO products VALUES (1,'Laptop',1), (2,'Mouse',1), (3,'Desk',2);",
        "CREATE TABLE warehouses (warehouse_id INTEGER PRIMARY KEY, name TEXT NOT NULL);",
        "INSERT INTO warehouses VALUES (1,'Dhaka'), (2,'Chittagong');",
        "CREATE TABLE shipments (shipment_id INTEGER PRIMARY KEY, supplier_id INTEGER REFERENCES suppliers(supplier_id), warehouse_id INTEGER REFERENCES warehouses(warehouse_id), ship_date TEXT DEFAULT (date('now')));",
        "INSERT INTO shipments VALUES (1,1,1,'2026-07-01'), (2,2,1,'2026-07-02'), (3,1,2,'2026-07-03');",
        "CREATE TABLE shipment_items (shipment_id INTEGER, product_id INTEGER, quantity INTEGER CHECK(quantity > 0), PRIMARY KEY(shipment_id, product_id), FOREIGN KEY(shipment_id) REFERENCES shipments(shipment_id) ON DELETE CASCADE, FOREIGN KEY(product_id) REFERENCES products(product_id));",
        "INSERT INTO shipment_items VALUES (1,1,10), (1,2,50), (2,3,20), (3,2,30);",
        "SELECT name FROM suppliers ORDER BY name;"
    ]
)

easy2 = Task(
    description=(
        "📊  Quantity per Product per Warehouse – Multi‑table JOIN\n\n"
        "The supply chain tables are seeded.\n"
        "Write a query that returns, for each product and warehouse,\n"
        "the total quantity shipped. Show product_name, warehouse_name,\n"
        "and SUM(quantity) as total_shipped.\n"
        "Join shipment_items → products, shipments, warehouses.\n"
        "Group by product and warehouse.\n"
        "Sort by product_name, then warehouse_name.\n\n"
        "Expected output:\n[('Desk','Dhaka',20), ('Laptop','Dhaka',10), ('Mouse','Chittagong',30), ('Mouse','Dhaka',50)]"
    ),
    setup_sql=(
        "CREATE TABLE suppliers (supplier_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO suppliers VALUES (1,'TechCorp'), (2,'OfficeDepot');"
        "CREATE TABLE products (product_id INTEGER PRIMARY KEY, name TEXT NOT NULL, supplier_id INTEGER REFERENCES suppliers(supplier_id));"
        "INSERT INTO products VALUES (1,'Laptop',1), (2,'Mouse',1), (3,'Desk',2);"
        "CREATE TABLE warehouses (warehouse_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO warehouses VALUES (1,'Dhaka'), (2,'Chittagong');"
        "CREATE TABLE shipments (shipment_id INTEGER PRIMARY KEY, supplier_id INTEGER REFERENCES suppliers(supplier_id), warehouse_id INTEGER REFERENCES warehouses(warehouse_id), ship_date TEXT DEFAULT (date('now')));"
        "INSERT INTO shipments VALUES (1,1,1,'2026-07-01'), (2,2,1,'2026-07-02'), (3,1,2,'2026-07-03');"
        "CREATE TABLE shipment_items (shipment_id INTEGER, product_id INTEGER, quantity INTEGER CHECK(quantity > 0), PRIMARY KEY(shipment_id, product_id), FOREIGN KEY(shipment_id) REFERENCES shipments(shipment_id) ON DELETE CASCADE, FOREIGN KEY(product_id) REFERENCES products(product_id));"
        "INSERT INTO shipment_items VALUES (1,1,10), (1,2,50), (2,3,20), (3,2,30);"
    ),
    expected_output="[('Desk', 'Dhaka', 20), ('Laptop', 'Dhaka', 10), ('Mouse', 'Chittagong', 30), ('Mouse', 'Dhaka', 50)]",
    level=Level.EASY,
    hints=[
        "SELECT p.name, w.name, SUM(si.quantity) AS total_shipped FROM shipment_items si JOIN products p ON si.product_id = p.product_id JOIN shipments s ON si.shipment_id = s.shipment_id JOIN warehouses w ON s.warehouse_id = w.warehouse_id GROUP BY p.product_id, w.warehouse_id ORDER BY p.name, w.name;"
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "📈  Supplier Performance – Total Units Shipped\n\n"
        "The supply chain tables are seeded.\n"
        "Write a query that shows each supplier name and the\n"
        "total units they have shipped (SUM of shipment_items.quantity).\n"
        "Include suppliers with zero shipments (LEFT JOIN, COALESCE).\n"
        "Sort by total_units descending.\n\n"
        "Expected output:\n[('TechCorp',90), ('OfficeDepot',20)]"
    ),
    setup_sql=(
        "CREATE TABLE suppliers (supplier_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO suppliers VALUES (1,'TechCorp'), (2,'OfficeDepot');"
        "CREATE TABLE products (product_id INTEGER PRIMARY KEY, name TEXT NOT NULL, supplier_id INTEGER REFERENCES suppliers(supplier_id));"
        "INSERT INTO products VALUES (1,'Laptop',1), (2,'Mouse',1), (3,'Desk',2);"
        "CREATE TABLE warehouses (warehouse_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO warehouses VALUES (1,'Dhaka'), (2,'Chittagong');"
        "CREATE TABLE shipments (shipment_id INTEGER PRIMARY KEY, supplier_id INTEGER REFERENCES suppliers(supplier_id), warehouse_id INTEGER REFERENCES warehouses(warehouse_id), ship_date TEXT DEFAULT (date('now')));"
        "INSERT INTO shipments VALUES (1,1,1,'2026-07-01'), (2,2,1,'2026-07-02'), (3,1,2,'2026-07-03');"
        "CREATE TABLE shipment_items (shipment_id INTEGER, product_id INTEGER, quantity INTEGER CHECK(quantity > 0), PRIMARY KEY(shipment_id, product_id), FOREIGN KEY(shipment_id) REFERENCES shipments(shipment_id) ON DELETE CASCADE, FOREIGN KEY(product_id) REFERENCES products(product_id));"
        "INSERT INTO shipment_items VALUES (1,1,10), (1,2,50), (2,3,20), (3,2,30);"
    ),
    expected_output="[('TechCorp', 90), ('OfficeDepot', 20)]",
    level=Level.MEDIUM,
    hints=[
        "SELECT sup.name, COALESCE(SUM(si.quantity), 0) AS total_units FROM suppliers sup LEFT JOIN shipments s ON sup.supplier_id = s.supplier_id LEFT JOIN shipment_items si ON s.shipment_id = si.shipment_id GROUP BY sup.supplier_id ORDER BY total_units DESC;"
    ]
)

medium2 = Task(
    description=(
        "📅  Most Recent Shipment per Warehouse\n\n"
        "The supply chain tables are seeded.\n"
        "Write a query that shows each warehouse name and the\n"
        "date of the most recent shipment received.\n"
        "Include warehouses that have never received a shipment\n"
        "(LEFT JOIN), showing NULL for the date.\n"
        "Sort by warehouse name.\n\n"
        "Expected output:\n[('Chittagong','2026-07-03'), ('Dhaka','2026-07-02')]"
    ),
    setup_sql=(
        "CREATE TABLE suppliers (supplier_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO suppliers VALUES (1,'TechCorp'), (2,'OfficeDepot');"
        "CREATE TABLE products (product_id INTEGER PRIMARY KEY, name TEXT NOT NULL, supplier_id INTEGER REFERENCES suppliers(supplier_id));"
        "INSERT INTO products VALUES (1,'Laptop',1), (2,'Mouse',1), (3,'Desk',2);"
        "CREATE TABLE warehouses (warehouse_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO warehouses VALUES (1,'Dhaka'), (2,'Chittagong');"
        "CREATE TABLE shipments (shipment_id INTEGER PRIMARY KEY, supplier_id INTEGER REFERENCES suppliers(supplier_id), warehouse_id INTEGER REFERENCES warehouses(warehouse_id), ship_date TEXT DEFAULT (date('now')));"
        "INSERT INTO shipments VALUES (1,1,1,'2026-07-01'), (2,2,1,'2026-07-02'), (3,1,2,'2026-07-03');"
        "CREATE TABLE shipment_items (shipment_id INTEGER, product_id INTEGER, quantity INTEGER CHECK(quantity > 0), PRIMARY KEY(shipment_id, product_id), FOREIGN KEY(shipment_id) REFERENCES shipments(shipment_id) ON DELETE CASCADE, FOREIGN KEY(product_id) REFERENCES products(product_id));"
        "INSERT INTO shipment_items VALUES (1,1,10), (1,2,50), (2,3,20), (3,2,30);"
    ),
    expected_output="[('Chittagong', '2026-07-03'), ('Dhaka', '2026-07-02')]",
    level=Level.MEDIUM,
    hints=[
        "SELECT w.name, MAX(s.ship_date) AS last_shipment FROM warehouses w LEFT JOIN shipments s ON w.warehouse_id = s.warehouse_id GROUP BY w.warehouse_id ORDER BY w.name;"
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🔍  Products Never Shipped – LEFT JOIN + IS NULL\n\n"
        "The supply chain tables are seeded.\n"
        "Write a query that finds all products that have NEVER\n"
        "been included in any shipment.\n"
        "Return product name and supplier name.\n"
        "Sort by product name.\n\n"
        "Expected output: [('Desk','OfficeDepot'), ('Mouse','TechCorp')]"
    ),
    setup_sql=(
        "CREATE TABLE suppliers (supplier_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO suppliers VALUES (1,'TechCorp'), (2,'OfficeDepot');"
        "CREATE TABLE products (product_id INTEGER PRIMARY KEY, name TEXT NOT NULL, supplier_id INTEGER REFERENCES suppliers(supplier_id));"
        "INSERT INTO products VALUES (1,'Laptop',1), (2,'Mouse',1), (3,'Desk',2);"
        "CREATE TABLE warehouses (warehouse_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO warehouses VALUES (1,'Dhaka'), (2,'Chittagong');"
        "CREATE TABLE shipments (shipment_id INTEGER PRIMARY KEY, supplier_id INTEGER REFERENCES suppliers(supplier_id), warehouse_id INTEGER REFERENCES warehouses(warehouse_id), ship_date TEXT DEFAULT (date('now')));"
        "INSERT INTO shipments VALUES (1,1,1,'2026-07-01'), (2,2,1,'2026-07-02'), (3,1,2,'2026-07-03');"
        "CREATE TABLE shipment_items (shipment_id INTEGER, product_id INTEGER, quantity INTEGER CHECK(quantity > 0), PRIMARY KEY(shipment_id, product_id), FOREIGN KEY(shipment_id) REFERENCES shipments(shipment_id) ON DELETE CASCADE, FOREIGN KEY(product_id) REFERENCES products(product_id));"
        "INSERT INTO shipment_items VALUES (1,1,10), (1,2,50), (2,3,20), (3,2,30);"
    ),
    expected_output="[('Desk', 'OfficeDepot'), ('Mouse', 'TechCorp')]",
    level=Level.HARD,
    hints=[
        "SELECT p.name, sup.name FROM products p JOIN suppliers sup ON p.supplier_id = sup.supplier_id LEFT JOIN shipment_items si ON p.product_id = si.product_id WHERE si.shipment_id IS NULL ORDER BY p.name;"
    ]
)

hard2 = Task(
    description=(
        "📊  Full Shipment Manifest – 5‑Table Join\n\n"
        "The supply chain tables are seeded.\n"
        "Write a query that returns a complete shipment manifest:\n"
        "  • shipment_id\n"
        "  • supplier name\n"
        "  • product name\n"
        "  • quantity\n"
        "  • warehouse name\n"
        "  • ship_date\n"
        "Join all five tables.\n"
        "Sort by ship_date DESC, then shipment_id.\n\n"
        "Expected output:\n[(3,'TechCorp','Mouse',30,'Chittagong','2026-07-03'), (2,'OfficeDepot','Desk',20,'Dhaka','2026-07-02'), (1,'TechCorp','Laptop',10,'Dhaka','2026-07-01'), (1,'TechCorp','Mouse',50,'Dhaka','2026-07-01')]"
    ),
    setup_sql=(
        "CREATE TABLE suppliers (supplier_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO suppliers VALUES (1,'TechCorp'), (2,'OfficeDepot');"
        "CREATE TABLE products (product_id INTEGER PRIMARY KEY, name TEXT NOT NULL, supplier_id INTEGER REFERENCES suppliers(supplier_id));"
        "INSERT INTO products VALUES (1,'Laptop',1), (2,'Mouse',1), (3,'Desk',2);"
        "CREATE TABLE warehouses (warehouse_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO warehouses VALUES (1,'Dhaka'), (2,'Chittagong');"
        "CREATE TABLE shipments (shipment_id INTEGER PRIMARY KEY, supplier_id INTEGER REFERENCES suppliers(supplier_id), warehouse_id INTEGER REFERENCES warehouses(warehouse_id), ship_date TEXT DEFAULT (date('now')));"
        "INSERT INTO shipments VALUES (1,1,1,'2026-07-01'), (2,2,1,'2026-07-02'), (3,1,2,'2026-07-03');"
        "CREATE TABLE shipment_items (shipment_id INTEGER, product_id INTEGER, quantity INTEGER CHECK(quantity > 0), PRIMARY KEY(shipment_id, product_id), FOREIGN KEY(shipment_id) REFERENCES shipments(shipment_id) ON DELETE CASCADE, FOREIGN KEY(product_id) REFERENCES products(product_id));"
        "INSERT INTO shipment_items VALUES (1,1,10), (1,2,50), (2,3,20), (3,2,30);"
    ),
    expected_output="[(3, 'TechCorp', 'Mouse', 30, 'Chittagong', '2026-07-03'), (2, 'OfficeDepot', 'Desk', 20, 'Dhaka', '2026-07-02'), (1, 'TechCorp', 'Laptop', 10, 'Dhaka', '2026-07-01'), (1, 'TechCorp', 'Mouse', 50, 'Dhaka', '2026-07-01')]",
    level=Level.HARD,
    hints=[
        "SELECT sh.shipment_id, sup.name, p.name, si.quantity, w.name, sh.ship_date FROM shipments sh JOIN suppliers sup ON sh.supplier_id = sup.supplier_id JOIN shipment_items si ON sh.shipment_id = si.shipment_id JOIN products p ON si.product_id = p.product_id JOIN warehouses w ON sh.warehouse_id = w.warehouse_id ORDER BY sh.ship_date DESC, sh.shipment_id;"
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L40.json",
        module_name="Module_04_Joins_Relationships",
        lesson_name="L40_Module_4_Capstone"
    )
