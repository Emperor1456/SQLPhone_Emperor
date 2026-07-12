# 📘 SQLPhone Emperor v3.0 · Module 9
# 📖 L84 – Employee Payroll Database

---

## 🎯 OBJECTIVE — What You Will Master

> Build a payroll system that calculates salaries, taxes, and generates pay slips — the core of every HR department.

- 🧱 **Tables** – employees, departments, salaries, deductions  
- 🧠 **Computed columns** – net pay calculation  
- 🧪 **Reports** – department payroll, tax summary  
- ⚡ **Real‑world** – HRMS software, payroll processing  

---

## 🧱 THE IMPERIAL PAYROLL – BUSINESS REQUIREMENT

The Emperor’s HR department needs to compute monthly net pay for every employee: `base_salary – tax – deductions`. It must also produce a department‑wise payroll summary.

---

## 🧱 SCHEMA

```sql
CREATE TABLE departments (
    dept_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    dept_id INTEGER,
    base_salary REAL CHECK(base_salary > 0),
    tax_rate REAL DEFAULT 0.1,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

CREATE TABLE deductions (
    ded_id INTEGER PRIMARY KEY,
    emp_id INTEGER,
    amount REAL CHECK(amount > 0),
    reason TEXT,
    ded_date TEXT DEFAULT (date('now')),
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
);
```

---

## 🧱 SEED DATA

```sql
INSERT INTO departments VALUES (1, 'Engineering'), (2, 'Sales');
INSERT INTO employees VALUES (1, 'Emperor', 1, 5000, 0.1);
INSERT INTO employees VALUES (2, 'Rahim', 2, 4000, 0.1);
INSERT INTO deductions VALUES (1, 1, 200, 'Health Insurance', '2026-07-01');
```

---

## 🧱 NET PAY REPORT

```sql
SELECT e.name,
       e.base_salary,
       COALESCE(SUM(d.amount), 0) AS total_deductions,
       e.base_salary * (1 - e.tax_rate) - COALESCE(SUM(d.amount), 0) AS net_pay
FROM employees e
LEFT JOIN deductions d ON e.emp_id = d.emp_id
GROUP BY e.emp_id;
```

---

## 🧱 DEPARTMENT PAYROLL SUMMARY

```sql
SELECT d.name,
       COUNT(e.emp_id) AS employees,
       SUM(e.base_salary) AS total_base,
       SUM(e.base_salary * e.tax_rate) AS total_tax,
       SUM(e.base_salary * (1 - e.tax_rate)) AS net_total
FROM departments d
LEFT JOIN employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_id;
```

---

## 💡 Real‑world Usage

- Monthly payroll runs  
- Tax compliance reports  
- Compensation analysis and budgeting  

---

## 🔍 Practice Preview
You will build an employee payroll system.

| Level | Task |
|-------|------|
| Easy | Create tables and seed data. |
| Medium | Compute net pay for all employees. |
| Hard | Generate a department‑wise payroll summary. |

Run the coach:
```bash
python ii_Practice_Sheets/L84_Employee_Payroll_Database.py
```

---

## 📌 Key Takeaway
- `base_salary` and `tax_rate` are stored; net pay is computed.  
- `LEFT JOIN` ensures employees with no deductions still appear.  
- This pattern scales to multi‑currency, multi‑country payroll.

*For Emperor.*