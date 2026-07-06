-- 🐛 BROKEN – Module 10, Lesson 82 (Index Usage)
-- Index not used because WHERE uses function on column.

CREATE INDEX idx_name ON users(name);
SELECT * FROM users WHERE UPPER(name) = 'ALICE';  -- ❌ index ignored
