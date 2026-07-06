-- 🐛 BROKEN QUERY – Module 10
-- This query is slow because it doesn't use an index.
-- Fix by creating an index on the 'email' column.

CREATE TABLE contacts (id INTEGER, email TEXT, name TEXT);
-- Insert dummy data (many rows) – we'll skip actual inserts for brevity.

-- Query that should be fast after indexing
SELECT name FROM contacts WHERE email = 'test@example.com';

-- Fix: add CREATE INDEX idx_email ON contacts(email); then re-run EXPLAIN QUERY PLAN.
-- Expected: USING INDEX idx_email.
