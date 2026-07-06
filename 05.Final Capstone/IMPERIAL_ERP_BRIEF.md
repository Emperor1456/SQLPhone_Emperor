# 🏛️ Imperial ERP – Final Capstone Project
**SQLPhone Emperor · Portfolio Masterpiece**

## 🎯 Objective
Build a complete, command‑line based Enterprise Resource Planning (ERP) system that integrates **every module** of the SQLPhone Emperor course. This is your proof of mastery.

---

## 🧱 System Modules
The ERP consists of four interconnected business modules:

### 1. Inventory Management
- **Categories** (id, name)
- **Suppliers** (id, name, contact)
- **Products** (id, name, category_id, supplier_id, unit_price, stock_quantity)
- **Inventory Log** (id, product_id, change_amount, reason, timestamp)

### 2. Sales Management
- **Customers** (id, name, email UNIQUE, join_date)
- **Sales Orders** (id, customer_id, order_date, status)
- **Order Items** (order_id, product_id, quantity, unit_price)

### 3. Human Resources
- **Departments** (id, name, location)
- **Employees** (id, name, department_id, hire_date, base_salary)
- **Payroll** (id, employee_id, pay_date, amount, type)

### 4. Reporting & Utilities
- Pre‑built views for: low‑stock products, monthly sales, department payroll cost.
- Backup & restore functionality.
- Export any query result to CSV.

---

## 🧪 Technical Requirements
Your project must demonstrate:

- **All 12 course modules** – DDL, DML, joins, subqueries, CTEs, aggregation, CASE, views, transactions, indexes, Python integration, error handling, backup/restore.
- **Parameterized queries** – no SQL injection.
- **Foreign keys with CASCADE** where appropriate.
- **CHECK and UNIQUE constraints** on business‑critical columns.
- **At least one composite primary key** (e.g., order_items).
- **A CTE** in a reporting query.
- **A correlated subquery** (e.g., employees above department average salary).
- **A transaction** that transfers stock when a sale is made.
- **Indexes** on frequently searched columns (product name, customer email).
- **At least one view** that is queried by the Python application.
- **Export to CSV** of a report.
- **Backup and restore** of the database from within the Python CLI.
- **A clean, modular Python structure** using the `practice_engine` (or your own database helper class).

---

## 🖥️ CLI Menu Structure (example)
```
IMPERIAL ERP MAIN MENU
1. Inventory Management
2. Sales Management
3. Human Resources
4. Reports
5. Utilities (Backup / Restore / Export CSV)
0. Exit
```

Each sub‑menu should offer full CRUD (Create, Read, Update, Delete) for its entities, plus relevant queries.

---

## 📦 Deliverables
1. `imperial_erp.py` – the complete Python application.
2. `imperial_erp.db` – a sample database created by running the app.
3. A short `README.md` inside the capstone folder explaining how to run it.

---

## 🏆 Success Criteria
- The application runs without errors on a fresh Termux install.
- All menu options work and produce correct results.
- Data integrity is enforced at the database level (constraints, foreign keys).
- The code is well‑commented, formatted, and follows professional conventions.
- You can explain every line you wrote.

---

## 💡 Hints & Progression
- Start with the schema: design all tables on paper, then write the DDL script.
- Build one module at a time, testing each menu option before moving on.
- Use the practice engine pattern (`Task`, `verify`, `hints`) if you want to make each sub‑task interactive.
- This is a large project – pace yourself. It’s meant to be your magnum opus.

*When this project runs, you are no longer a student – you are a database engineer.*