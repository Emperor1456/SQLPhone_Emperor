# 📘 SQLPhone Emperor · SQL Module 11
# 📖 L‑90 – Employee Payroll Database

## 🎯 OBJECTIVE
Manage employee data, departments, salaries, and
payroll history for a company.

## 🧱 BRICK 1 – Requirements
Entities:
- **Department:** id, name, location
- **Employee:** id, name, dept_id, hire_date, base_salary
- **Payroll:** id, employee_id, pay_date, amount (could be
  different from base due to deductions/bonuses)

Relationships:
- Department has many employees.
- Employee has many payroll records.

## 🧱 BRICK 2 – Deliverables
1. DDL with constraints (salary > 0).
2. Seed data (3 departments, at least 8 employees,
   multiple payroll entries).
3. Queries:
   - Total payroll cost per department per month.
   - Employees who received a bonus (payroll amount > base_salary).
   - Average salary by department.
   - List employees hired in the last year.

## 💡 Real‑world Usage
HR systems, accounting software, enterprise ERP.

## 📌 Key Takeaway
Payroll requires historical records, not just current state.
Design for auditability and aggregation.

*Every paycheck is a data point.*