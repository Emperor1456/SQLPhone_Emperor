-- 🐛 BROKEN – Module 06, Lesson 48 (DELETE)
-- DELETE from parent table without CASCADE, leaving orphans.
-- (Assume foreign_key pragma is ON).

DELETE FROM departments WHERE id = 1;  -- ❌ fails if employees exist
