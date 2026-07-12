# 📘 SQLPhone Emperor v3.0 · Module 6
# 📖 L60 – Module 6 Capstone: School Management Schema

---

## 🎯 OBJECTIVE — What You Will Master

> Design, build, and evolve a complete school management database — integrating every Module‑6 skill into a real‑world system.

- 🧱 **Full schema design** – students, teachers, courses, enrollments, grades
- 🧠 **Constraints** – foreign keys, CHECK, UNIQUE, NOT NULL, DEFAULT
- 🧪 **Indexing** – speed up common queries
- ⚡ **Migration scenario** – evolve the schema with a transactional migration
- 🛡️ **Production readiness** – constraints, indexes, and documentation

---

## 🧱 THE IMPERIAL ACADEMY SCHEMA

```sql
CREATE TABLE teachers (
    teacher_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    hire_date TEXT DEFAULT (date('now'))
);

CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL,
    teacher_id INTEGER,
    credits INTEGER CHECK(credits > 0),
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
);

CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    enrollment_date TEXT DEFAULT (date('now'))
);

CREATE TABLE enrollments (
    student_id INTEGER,
    course_id INTEGER,
    enrolled_date TEXT DEFAULT (date('now')),
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

CREATE TABLE grades (
    grade_id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    grade TEXT CHECK(grade IN ('A','B','C','D','F')),
    graded_date TEXT DEFAULT (date('now')),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    UNIQUE(student_id, course_id)  -- one grade per course per student
);
```

---

## 🧱 SEED DATA

```sql
INSERT INTO teachers VALUES (1, 'Dr. Karim', 'karim@academy.edu', '2025-01-15');
INSERT INTO teachers VALUES (2, 'Prof. Begum', 'begum@academy.edu', '2025-02-01');

INSERT INTO courses VALUES (1, 'Database Systems', 1, 3);
INSERT INTO courses VALUES (2, 'Calculus', 2, 4);

INSERT INTO students VALUES (1, 'Emperor', '2026-01-10');
INSERT INTO students VALUES (2, 'Rahim', '2026-02-15');

INSERT INTO enrollments VALUES (1, 1, '2026-06-01');
INSERT INTO enrollments VALUES (1, 2, '2026-06-01');
INSERT INTO enrollments VALUES (2, 1, '2026-06-01');

INSERT INTO grades VALUES (1, 1, 1, 'A', '2026-06-20');
INSERT INTO grades VALUES (2, 1, 2, 'B', '2026-06-21');
INSERT INTO grades VALUES (3, 2, 1, 'C', '2026-06-20');
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

**② Courses with enrollment count**
```sql
SELECT c.course_name, COUNT(e.student_id) AS enrolled
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id;
```

**③ Teacher workload (courses taught)**
```sql
SELECT t.name, COUNT(c.course_id) AS courses
FROM teachers t
LEFT JOIN courses c ON t.teacher_id = c.teacher_id
GROUP BY t.teacher_id;
```

**④ Students with GPA (A=4, B=3, C=2, D=1, F=0)**
```sql
SELECT s.name, ROUND(AVG(
    CASE g.grade
        WHEN 'A' THEN 4 WHEN 'B' THEN 3
        WHEN 'C' THEN 2 WHEN 'D' THEN 1
        ELSE 0
    END), 2) AS gpa
FROM students s
JOIN grades g ON s.student_id = g.student_id
GROUP BY s.student_id;
```

**⑤ Courses with no enrollments**
```sql
SELECT course_name FROM courses
WHERE course_id NOT IN (SELECT DISTINCT course_id FROM enrollments);
```

---

## 🧱 MIGRATION CHALLENGE

Add a `department` column to `teachers` and create a `departments` table, then migrate existing teacher data.

```sql
BEGIN;
CREATE TABLE departments (
    dept_id INTEGER PRIMARY KEY,
    dept_name TEXT UNIQUE
);
INSERT INTO departments (dept_name) VALUES ('Science'), ('Arts'), ('Commerce');
ALTER TABLE teachers ADD COLUMN dept_id INTEGER DEFAULT 1 REFERENCES departments(dept_id);
COMMIT;
```

---

## 💡 Real‑world Usage

This schema is a direct template for:
- University student information systems
- Online course platforms (like Coursera, Udemy)
- Training management systems for corporations

---

## 🔍 Practice Preview
You will build the Imperial Academy database and run reports.

| Level | Task |
|-------|------|
| Easy | Create all five tables with constraints and seed data. |
| Medium | Write a student transcript query showing course name and grade. |
| Hard | Perform the department migration (add `departments` table, add `dept_id` column, migrate data). |

Run the coach:
```bash
python ii_Practice_Sheets/L60_Module_6_Capstone_School_Management_Schema.py
```

---

## 📌 Key Takeaway
- A school management system models students, teachers, courses, and grades with strict constraints.
- Composite keys ensure each student can be enrolled once per course and graded once.
- Migrations allow schema evolution without data loss.

*For Emperor.*