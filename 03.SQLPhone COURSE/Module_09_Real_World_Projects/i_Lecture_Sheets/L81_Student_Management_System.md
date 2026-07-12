# 📘 SQLPhone Emperor v3.0 · Module 9
# 📖 L81 – Student Management System

---

## 🎯 OBJECTIVE — What You Will Master

> Build a complete student management database that tracks enrolments, courses, and grades — the exact same type of system used by universities and online learning platforms worldwide.

- 🧱 **Schema design** – students, courses, enrollments, grades  
- 🧠 **Constraints** – foreign keys, CHECK for grades, composite primary keys  
- 🧪 **Queries** – transcripts, GPA calculation, course rosters  
- ⚡ **Real‑world pattern** – academic ERP, LMS, corporate training  

---

## 🧱 THE IMPERIAL ACADEMY – BUSINESS REQUIREMENT

The Emperor’s Academy needs to track every student, every course they take, and every grade they earn. The system must prevent duplicate enrollments and enforce valid grade values.

**Tables:**
- `students` – personal details  
- `courses` – course catalog  
- `enrollments` – links students to courses with a semester  
- `grades` – final result per student per course  

---

## 🧱 SCHEMA

```sql
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    enrollment_date TEXT DEFAULT (date('now'))
);

CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL,
    credits INTEGER CHECK(credits > 0)
);

CREATE TABLE enrollments (
    student_id INTEGER,
    course_id INTEGER,
    semester TEXT NOT NULL,
    PRIMARY KEY (student_id, course_id, semester),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

CREATE TABLE grades (
    student_id INTEGER,
    course_id INTEGER,
    grade TEXT CHECK(grade IN ('A','B','C','D','F')),
    graded_date TEXT DEFAULT (date('now')),
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
```

The composite primary key on `enrollments` allows a student to retake the same course in a different semester. The `grades` table enforces exactly one grade per student per course.

---

## 🧱 SEED DATA

```sql
INSERT INTO students VALUES (1, 'Emperor', 'emperor@academy.edu', '2026-01-10');
INSERT INTO students VALUES (2, 'Rahim', 'rahim@academy.edu', '2026-02-15');

INSERT INTO courses VALUES (1, 'Database Systems', 3);
INSERT INTO courses VALUES (2, 'Calculus', 4);

INSERT INTO enrollments VALUES (1, 1, '2026-Spring');
INSERT INTO enrollments VALUES (1, 2, '2026-Spring');
INSERT INTO enrollments VALUES (2, 1, '2026-Spring');

INSERT INTO grades VALUES (1, 1, 'A', '2026-06-15');
INSERT INTO grades VALUES (1, 2, 'B', '2026-06-16');
INSERT INTO grades VALUES (2, 1, 'C', '2026-06-15');
```

---

## 🧱 KEY QUERIES

**① Student transcript**
```sql
SELECT c.course_name, g.grade
FROM grades g
JOIN courses c ON g.course_id = c.course_id
WHERE g.student_id = 1;
```

**② GPA per student (A=4, B=3, C=2, D=1, F=0)**
```sql
SELECT s.name,
       ROUND(AVG(CASE g.grade
           WHEN 'A' THEN 4 WHEN 'B' THEN 3
           WHEN 'C' THEN 2 WHEN 'D' THEN 1
           ELSE 0 END), 2) AS gpa
FROM students s
JOIN grades g ON s.student_id = g.student_id
GROUP BY s.student_id;
```

**③ Courses with enrollment count**
```sql
SELECT c.course_name, COUNT(e.student_id) AS enrolled
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id;
```

**④ Students not enrolled in any course this semester**
```sql
SELECT s.name
FROM students s
WHERE s.student_id NOT IN (
    SELECT student_id FROM enrollments
    WHERE semester = '2026-Spring'
);
```

---

## 💡 Real‑world Usage

- University registration systems  
- Online learning platforms (Coursera, edX)  
- Corporate training and certification tracking  
- The pattern of linking entities through a join table with a grade extends to any assessment system  

---

## 🔍 Practice Preview
You will build and query the Imperial Academy database.

| Level | Task |
|-------|------|
| Easy | Create the four tables and insert the seed data. |
| Medium | Write a student transcript query. |
| Hard | Compute GPA for all students and list the top performer. |

Run the coach:
```bash
python ii_Practice_Sheets/L81_Student_Management_System.py
```

---

## 📌 Key Takeaway
- Composite primary keys prevent duplicate enrollments and grades.  
- `CHECK` constraints enforce valid data at the database level.  
- GPA calculation with `CASE` is a classic SQL pattern.  
- This is a portfolio‑ready project.

*For Emperor.*