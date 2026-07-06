-- 🐛 BROKEN – Module 08, Lesson 65 (CASE)
-- CASE missing END keyword.

SELECT name,
  CASE WHEN score >= 90 THEN 'A'
       WHEN score >= 80 THEN 'B'
       ELSE 'F'  -- ❌ missing END
FROM students;
