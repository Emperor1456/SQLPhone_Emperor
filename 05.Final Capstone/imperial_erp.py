#!/usr/bin/env python3
"""
Imperial ERP – SQLPhone Emperor Final Capstone
==============================================
A complete command-line ERP system built on SQLite.
Integrates all 12 course modules.

Usage:
    python imperial_erp.py
"""

import sys
import os
import sqlite3
import csv

# Add parent path to import practice_engine if needed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '03.SQLPhone COURSE'))
from practice_engine import Task, Level, run_task   # optional: you can use the engine for sub-tasks

DB_NAME = "imperial_erp.db"

# ──────────────────────────────────────────────────────────────
# DATABASE SETUP
# ──────────────────────────────────────────────────────────────
def initialize_database():
    """Create all tables and indexes if they don't exist."""
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON")
    cur = conn.cursor()
    
    # ==================== INVENTORY ====================
    cur.executescript("""
        CREATE TABLE IF NOT EXISTS category (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        );
        
        CREATE TABLE IF NOT EXISTS supplier (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            contact TEXT
        );
        
        CREATE TABLE IF NOT EXISTS product (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category_id INTEGER NOT NULL,
            supplier_id INTEGER,
            unit_price REAL NOT NULL CHECK(unit_price > 0),
            stock_quantity INTEGER NOT NULL DEFAULT 0 CHECK(stock_quantity >= 0),
            FOREIGN KEY (category_id) REFERENCES category(id),
            FOREIGN KEY (supplier_id) REFERENCES supplier(id) ON DELETE SET NULL
        );
        
        CREATE TABLE IF NOT EXISTS inventory_log (
            id INTEGER PRIMARY KEY,
            product_id INTEGER NOT NULL,
            change_amount INTEGER NOT NULL,
            reason TEXT,
            timestamp TEXT DEFAULT (datetime('now')),
            FOREIGN KEY (product_id) REFERENCES product(id) ON DELETE CASCADE
        );
    """)
    
    # ==================== SALES ====================
    cur.executescript("""
        CREATE TABLE IF NOT EXISTS customer (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            join_date TEXT DEFAULT (datetime('now'))
        );
        
        CREATE TABLE IF NOT EXISTS sales_order (
            id INTEGER PRIMARY KEY,
            customer_id INTEGER NOT NULL,
            order_date TEXT DEFAULT (datetime('now')),
            status TEXT DEFAULT 'pending' CHECK(status IN ('pending','shipped','cancelled')),
            FOREIGN KEY (customer_id) REFERENCES customer(id) ON DELETE CASCADE
        );
        
        CREATE TABLE IF NOT EXISTS order_item (
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL CHECK(quantity > 0),
            unit_price REAL NOT NULL,
            PRIMARY KEY (order_id, product_id),
            FOREIGN KEY (order_id) REFERENCES sales_order(id) ON DELETE CASCADE,
            FOREIGN KEY (product_id) REFERENCES product(id) ON DELETE CASCADE
        );
    """)
    
    # ==================== HR ====================
    cur.executescript("""
        CREATE TABLE IF NOT EXISTS department (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            location TEXT
        );
        
        CREATE TABLE IF NOT EXISTS employee (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department_id INTEGER NOT NULL,
            hire_date TEXT DEFAULT (datetime('now')),
            base_salary REAL NOT NULL CHECK(base_salary > 0),
            FOREIGN KEY (department_id) REFERENCES department(id) ON DELETE CASCADE
        );
        
        CREATE TABLE IF NOT EXISTS payroll (
            id INTEGER PRIMARY KEY,
            employee_id INTEGER NOT NULL,
            pay_date TEXT NOT NULL,
            amount REAL NOT NULL CHECK(amount > 0),
            type TEXT DEFAULT 'salary' CHECK(type IN ('salary','bonus','deduction')),
            FOREIGN KEY (employee_id) REFERENCES employee(id) ON DELETE CASCADE
        );
    """)
    
    # ==================== INDEXES ====================
    cur.executescript("""
        CREATE INDEX IF NOT EXISTS idx_product_name ON product(name);
        CREATE INDEX IF NOT EXISTS idx_customer_email ON customer(email);
        CREATE INDEX IF NOT EXISTS idx_sales_order_date ON sales_order(order_date);
        CREATE INDEX IF NOT EXISTS idx_payroll_date ON payroll(pay_date);
    """)
    
    # ==================== VIEWS ====================
    cur.executescript("""
        CREATE VIEW IF NOT EXISTS low_stock_products AS
        SELECT p.name, p.stock_quantity, c.name AS category
        FROM product p
        JOIN category c ON p.category_id = c.id
        WHERE p.stock_quantity < 10;
        
        CREATE VIEW IF NOT EXISTS monthly_sales AS
        SELECT strftime('%Y-%m', order_date) AS month,
               SUM(oi.quantity * oi.unit_price) AS revenue
        FROM sales_order so
        JOIN order_item oi ON so.id = oi.order_id
        WHERE so.status != 'cancelled'
        GROUP BY month;
        
        CREATE VIEW IF NOT EXISTS dept_payroll_cost AS
        SELECT d.name, SUM(p.amount) AS total_paid
        FROM department d
        JOIN employee e ON d.id = e.department_id
        JOIN payroll p ON e.id = p.employee_id
        GROUP BY d.id;
    """)
    
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

# ──────────────────────────────────────────────────────────────
# UTILITY FUNCTIONS
# ──────────────────────────────────────────────────────────────
def get_db():
    """Return a connection with foreign keys enabled."""
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def backup_database():
    """Backup the current database to a timestamped file."""
    import shutil
    timestamp = __import__('time').strftime("%Y%m%d_%H%M%S")
    backup_file = f"imperial_erp_backup_{timestamp}.db"
    shutil.copy2(DB_NAME, backup_file)
    print(f"Backup created: {backup_file}")

def restore_database(backup_path):
    """Restore the database from a backup file."""
    if os.path.exists(backup_path):
        import shutil
        shutil.copy2(backup_path, DB_NAME)
        print("Database restored successfully.")
    else:
        print("Backup file not found.")

def export_to_csv(query, filename):
    """Execute a query and save results to CSV."""
    conn = get_db()
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([desc[0] for desc in cur.description])
        writer.writerows(rows)
    conn.close()
    print(f"Exported to {filename}")

# ──────────────────────────────────────────────────────────────
# MENU HANDLERS (stubs – you will implement these)
# ──────────────────────────────────────────────────────────────
def inventory_menu():
    while True:
        print("\n--- INVENTORY ---")
        print("1. Add Category")
        print("2. List Categories")
        print("3. Add Supplier")
        print("4. List Suppliers")
        print("5. Add Product")
        print("6. List Products")
        print("7. Update Stock")
        print("8. Low Stock Report")
        print("0. Back")
        choice = input("> ")
        if choice == '0':
            break
        # TODO: implement each option
        print("Not implemented yet. Use the practice engine to build each task.")

def sales_menu():
    print("Sales menu – to be implemented.")

def hr_menu():
    print("HR menu – to be implemented.")

def reports_menu():
    print("Reports menu – to be implemented.")

def utilities_menu():
    while True:
        print("\n--- UTILITIES ---")
        print("1. Backup Database")
        print("2. Restore Database")
        print("3. Export View to CSV")
        print("0. Back")
        choice = input("> ")
        if choice == '0':
            break
        elif choice == '1':
            backup_database()
        elif choice == '2':
            path = input("Backup file path: ")
            restore_database(path)
        elif choice == '3':
            view = input("View name to export: ")
            filename = input("Output CSV filename: ")
            export_to_csv(f"SELECT * FROM {view}", filename)
        else:
            print("Invalid choice.")

# ──────────────────────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────────────────────
def main():
    initialize_database()
    while True:
        print("\n===== IMPERIAL ERP =====")
        print("1. Inventory Management")
        print("2. Sales Management")
        print("3. Human Resources")
        print("4. Reports")
        print("5. Utilities")
        print("0. Exit")
        choice = input("> ")
        if choice == '0':
            print("Shutting down Imperial ERP. Goodbye, Emperor.")
            break
        elif choice == '1':
            inventory_menu()
        elif choice == '2':
            sales_menu()
        elif choice == '3':
            hr_menu()
        elif choice == '4':
            reports_menu()
        elif choice == '5':
            utilities_menu()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()