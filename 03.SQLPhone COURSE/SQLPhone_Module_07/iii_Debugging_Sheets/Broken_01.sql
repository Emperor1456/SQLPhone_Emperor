-- 🐛 BROKEN – Module 07, Lesson 58 (strftime)
-- strftime format string wrong: %Y (4-digit year) vs %y (2-digit).
-- Also missing a '%' before d.

SELECT strftime('%Y-%m-%d', 'now');  -- works
SELECT strftime('%Y-%m-%d', 'now');  -- ❌ should be %d not d
