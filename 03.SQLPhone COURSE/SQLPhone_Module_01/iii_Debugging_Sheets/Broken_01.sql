-- 🐛 BROKEN – Module 01, Lesson 05 (CREATE TABLE)
-- This CREATE TABLE is missing a NOT NULL on the name column,
-- allowing NULL names. Fix by adding NOT NULL.

CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT,          -- ❌ should be TEXT NOT NULL
    salary REAL
);
