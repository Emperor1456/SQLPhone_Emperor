# 📘 SQLPhone Emperor · SQL Module 11
# 📖 L‑92 – Expense Tracker

## 🎯 OBJECTIVE
Design a personal expense tracking database with
categories and monthly summaries.

## 🧱 BRICK 1 – Requirements
Entities:
- **Category:** id, name (e.g., Food, Rent, Transport)
- **Expense:** id, amount, category_id, expense_date,
  description (optional)

Rules:
- amount > 0
- expense_date is mandatory.

## 🧱 BRICK 2 – Deliverables
1. DDL with constraints.
2. Insert at least 20 expenses across different categories
   and months.
3. Queries:
   - Total expenses per month.
   - Category‑wise spending for a specific month.
   - Average daily spend.
   - Top 3 categories by total spend.

## 💡 Real‑world Usage
Budgeting apps (Mint, YNAB), personal finance tools.

## 📌 Key Takeaway
Time‑based aggregation is critical for financial data.
Grouping by month/category reveals spending patterns.

*Track every penny – data brings financial clarity.*