-- 🐛 BROKEN QUERY – Module 07
-- This query tries to extract the month from a date but returns NULL.

CREATE TABLE logs (id INTEGER, event_date TEXT);
INSERT INTO logs VALUES (1,'2026-07-06'), (2,'2026/08/15');  -- ❌ wrong format

-- Broken query
SELECT strftime('%m', event_date) FROM logs WHERE id=2;   -- returns NULL because of '/'

-- Fix: standardise the date format to YYYY-MM-DD in the INSERT, then re-run.
-- Expected: '08' for August.
