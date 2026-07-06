-- 🐛 BROKEN – Module 12, Lesson 95 (DB Comparison)
-- Trying to use SQLite syntax on PostgreSQL (LIMIT with OFFSET comma).

SELECT * FROM users LIMIT 10, 5;  -- ❌ not standard, works in SQLite, fails in others
