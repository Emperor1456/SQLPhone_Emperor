-- 🐛 BROKEN – Module 08, Lesson 70 (CSV Export)
-- Export to CSV without .headers on; missing column names.

.mode csv
.output result.csv
SELECT id, name FROM users;
.output stdout  -- ❌ headers not included
