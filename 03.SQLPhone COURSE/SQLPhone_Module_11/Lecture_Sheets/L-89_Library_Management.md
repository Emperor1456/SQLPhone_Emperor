# 📘 SQLPhone Emperor · SQL Module 11
# 📖 L‑89 – Library Management

## 🎯 OBJECTIVE
Create a database for a library to track books,
members, and borrowing transactions.

## 🧱 BRICK 1 – Requirements
Entities:
- **Book:** id, title, author, isbn (UNIQUE), published_year
- **Member:** id, name, email, join_date
- **Loan:** id, book_id, member_id, loan_date, return_date (nullable)

Rules:
- A book can have only one active loan (return_date IS NULL).
- Member can borrow multiple books.

## 🧱 BRICK 2 – Deliverables
1. DDL with foreign keys, UNIQUE on isbn, CHECK for
   loan_date < return_date.
2. Insert sample data (10 books, 5 members, active loans).
3. Queries:
   - Books currently borrowed (return_date IS NULL).
   - Members with overdue books (loan_date > 30 days ago,
     return_date IS NULL).
   - Most borrowed book.
   - Members who never borrowed.

## 💡 Real‑world Usage
Public libraries, school libraries, DVD rental stores
(remember those?) all use this model.

## 📌 Key Takeaway
Tracking state (active vs returned) is crucial.
Use NULL to represent ongoing events.

*Knowledge is borrowed – track its journey.*