-- 🐛 BROKEN – Module 11, Lesson 89 (Library)
-- Missing FOREIGN KEY in Loan table, allowing invalid book references.

CREATE TABLE Loan (
    id INTEGER PRIMARY KEY,
    book_id INTEGER,
    member_id INTEGER,
    loan_date TEXT
);  -- ❌ no foreign keys
