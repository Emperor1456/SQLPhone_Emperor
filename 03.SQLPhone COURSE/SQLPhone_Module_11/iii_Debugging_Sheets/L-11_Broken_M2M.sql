-- 🐛 BROKEN SCHEMA – Module 11
-- This many-to-many relationship is missing a junction table, causing duplication.

-- Broken: putting student courses directly in students table
CREATE TABLE students (id INTEGER, name TEXT, course TEXT);
INSERT INTO students VALUES (1,'Alice','Math'), (1,'Alice','Science');  -- duplicate student info

-- Fix: design a proper schema with students, courses, and enrollments tables.
-- After fixing, ensure no data duplication.
