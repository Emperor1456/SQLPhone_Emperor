-- 🐛 BROKEN – Module 04, Lesson 34 (Self‑Join)
-- Missing table alias causes ambiguity.

SELECT name, manager FROM employees e
JOIN employees ON e.manager_id = id;  -- ❌ 'id' ambiguous
