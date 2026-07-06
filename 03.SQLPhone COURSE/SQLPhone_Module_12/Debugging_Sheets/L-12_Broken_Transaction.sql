-- 🐛 BROKEN TRANSACTION – Module 12
-- This money transfer should be atomic, but a missing ROLLBACK leaves half the work done.

CREATE TABLE accounts (id INTEGER, balance REAL);
INSERT INTO accounts VALUES (1,1000), (2,1000);

-- Broken: if the second UPDATE fails (e.g., constraint violation), the first still persists.
BEGIN;
UPDATE accounts SET balance = balance - 2000 WHERE id = 1;  -- ❌ might go negative
UPDATE accounts SET balance = balance + 2000 WHERE id = 2;
COMMIT;

-- Fix: add a CHECK(balance>=0) constraint to the table, then use a try/except to ROLLBACK on failure.
-- Rewrite this transaction properly.
