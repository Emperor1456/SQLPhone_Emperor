# 📘 SQLPhone Emperor · SQL Module 05
# 📖 L‑46 – Subquery Practice

## 🎯 OBJECTIVE
Integrate all subquery techniques in a realistic
business scenario.

## 🧱 BRICK 1 – The Scenario
You have a small company database:
- `departments (id, name)`
- `employees (id, name, salary, dept_id)`
- `projects (id, title, budget, dept_id)`
- `assignments (emp_id, proj_id)`

Write queries to:
1. List employees whose salary is above the average
   of their own department (correlated subquery).
2. Find departments that have at least one employee
   earning more than 100,000 (EXISTS).
3. Show employees who are assigned to all projects
   of their own department (use NOT EXISTS with
   a double‑negative pattern).
4. List projects whose budget is greater than ANY
   project budget in a specific department (e.g. 'Engineering').
5. Use a CTE to get the total salary per department,
   then show departments where total exceeds 500,000.

## 🧱 BRICK 2 – Deliverables
Write the DDL, insert sample data, and execute all
five queries in a single `.sql` file.

## 💡 Real‑world Usage
Such queries are daily work for a database developer:
mixing subqueries, CTEs, and joins to answer
non‑trivial business questions.

## 📌 Key Takeaway
Subqueries are not isolated tricks – they are
building blocks for solving layered problems.
Combine them fearlessly.

*Complex questions demand composed solutions.*