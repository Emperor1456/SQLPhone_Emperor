-- 🐛 BROKEN QUERY – Module 08
-- This view should show high scorers, but the CASE label is wrong.

CREATE TABLE results (student TEXT, score INT);
INSERT INTO results VALUES ('A',85),('B',72),('C',95);

-- Broken view definition (missing END, wrong logic)
CREATE VIEW grades AS
SELECT student, score,
  CASE
    WHEN score >= 90 THEN 'A'
    WHEN score >= 80 THEN 'B'
    WHEN score >= 70 THEN 'C'   -- ❌ missing END
-- Missing END here

-- Fix: add END and close the CASE. Then query the view.
-- Expected: A (B), B (C), C (A)
