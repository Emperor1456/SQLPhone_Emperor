# 📘 SQLPhone Emperor v3.0 · Module 9
# 📖 L83 – Library Management with Borrowing Logs

---

## 🎯 OBJECTIVE — What You Will Master

> Build a library database that tracks members, books, borrowing history, and overdue items — the same logic used in public libraries and media rental systems.

- 🧱 **Tables** – members, books, borrowings  
- 🧠 **Constraints** – due dates, unique active borrow  
- 🧪 **Reports** – overdue books, most borrowed titles  
- ⚡ **Real‑world** – library software, video rental, equipment checkout  

---

## 🧱 THE IMPERIAL LIBRARY – BUSINESS REQUIREMENT

The Emperor’s library lends books to registered members. Each borrowing has a due date (14 days after borrow). The librarian needs a daily overdue report and a list of the most popular books.

---

## 🧱 SCHEMA

```sql
CREATE TABLE members (
    member_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    join_date TEXT DEFAULT (date('now'))
);

CREATE TABLE books (
    book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    isbn TEXT UNIQUE
);

CREATE TABLE borrowings (
    borrow_id INTEGER PRIMARY KEY,
    book_id INTEGER,
    member_id INTEGER,
    borrow_date TEXT DEFAULT (date('now')),
    due_date TEXT,
    return_date TEXT,
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);
```

---

## 🧱 SEED DATA

```sql
INSERT INTO members VALUES (1, 'Emperor');
INSERT INTO books VALUES (1, 'SQL Mastery', 'Data King', 'ISBN-001');
INSERT INTO borrowings (book_id, member_id, borrow_date, due_date)
VALUES (1, 1, '2026-07-01', '2026-07-15');
```

---

## 🧱 KEY QUERIES

**① Overdue books (past due date, not returned)**
```sql
SELECT m.name, b.title, bo.due_date
FROM borrowings bo
JOIN members m ON bo.member_id = m.member_id
JOIN books b ON bo.book_id = b.book_id
WHERE bo.return_date IS NULL AND bo.due_date < date('now');
```

**② Most borrowed books (top 3)**
```sql
SELECT b.title, COUNT(bo.borrow_id) AS times_borrowed
FROM books b
JOIN borrowings bo ON b.book_id = bo.book_id
GROUP BY b.book_id
ORDER BY times_borrowed DESC
LIMIT 3;
```

**③ Members with currently borrowed books**
```sql
SELECT m.name, COUNT(bo.borrow_id) AS books_out
FROM members m
JOIN borrowings bo ON m.member_id = bo.member_id
WHERE bo.return_date IS NULL
GROUP BY m.member_id;
```

**④ Books never borrowed**
```sql
SELECT title FROM books
WHERE book_id NOT IN (SELECT book_id FROM borrowings);
```

---

## 💡 Real‑world Usage

- Public library management systems  
- Video rental stores (Redbox, Netflix DVD era)  
- Equipment loan tracking in offices and labs  
- The overdue query is a universal business report  

---

## 🔍 Practice Preview
You will build a library management system.

| Level | Task |
|-------|------|
| Easy | Create tables and seed data with 3 books and 2 members. |
| Medium | Write an overdue books query. |
| Hard | Find the top 3 most borrowed books. |

Run the coach:
```bash
python ii_Practice_Sheets/L83_Library_Management_with_Borrowing_Logs.py
```

---

## 📌 Key Takeaway
- `due_date` and `return_date` model the full lifecycle of a borrowing.  
- Overdue queries use a date comparison — a classic business pattern.  
- `NOT IN` subquery finds books never borrowed.  
- This schema is ready to be the backend of a library app.

*For Emperor.*