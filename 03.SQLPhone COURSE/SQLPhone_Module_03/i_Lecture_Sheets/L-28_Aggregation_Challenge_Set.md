# 📘 SQLPhone Emperor · SQL Module 03
# 📖 L‑28 – Aggregation Challenge Set

## 🎯 OBJECTIVE
Apply all aggregation functions and clauses in a
multi‑part business scenario.

## 🧱 BRICK 1 – The Challenge
You are given a table `sales` with columns:
`id`, `product`, `category`, `quantity`, `price`, `sale_date`.

Write queries to:
1. Count total sales records.
2. Find the total quantity sold per product.
3. Calculate the average price per category.
4. List categories with total revenue (quantity*price) > 5000.
5. Show the month (extract month from date) and total sales
   count for months in 2026 with more than 10 transactions,
   ordered by month.

## 🧱 BRICK 2 – Deliverables
Write all five queries in a single `.sql` file.
Use appropriate aliases and formatting.
Ensure each query runs independently (separated by `;`).

**Hint for month extraction:** Use `strftime('%m', sale_date)`.

## 💡 Real‑world Usage
This simulates a typical sales report requested by
a business analyst: aggregates, filters, and groupings
are the bread and butter of data analysis.

## 📌 Key Takeaway
Aggregation is not just about functions – it’s about
structuring the query to answer a business question.
Practice with realistic data builds intuition.

*Data doesn’t speak; you make it speak with aggregation.*