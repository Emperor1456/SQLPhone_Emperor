# 📘 SQLPhone Emperor · SQL Module 11
# 📖 L‑87 – Student Management System

## 🎯 OBJECTIVE
Build a database to manage students, courses, and
enrollments – a classic academic system.

## 🧱 BRICK 1 – Requirements
Entities:
- **Student:** id, name, email, enrollment_year
- **Course:** id, title, credits
- **Enrollment:** student_id, course_id, grade (nullable)

Relationships:
- Many‑to‑many between Student and Course via Enrollment.
- Ensure unique enrollment per student per course.

## 🧱 BRICK 2 – Deliverables
1. DDL with proper constraints (PK, FK, UNIQUE, CHECK).
2. Insert sample data (at least 5 students, 3 courses,
   varied enrollments).
3. Write queries to:
   - List students with their enrolled courses.
   - Find students not enrolled in any course.
   - Calculate average grade per course (ignore NULL grades).
   - Find courses with more than 3 students.

## 💡 Real‑world Usage
Academic institutions, online learning platforms,
training management systems all use this pattern.

## 📌 Key Takeaway
Many‑to‑many relationships are everywhere.
A junction table (Enrollment) is the key.
Practice until building such schemas is instinctive.

*Students, courses, grades – the blueprint for learning.*