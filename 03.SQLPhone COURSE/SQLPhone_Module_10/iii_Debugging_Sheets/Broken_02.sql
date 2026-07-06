-- 🐛 BROKEN – Module 10, Lesson 84 (Transactions)
-- Forgot to commit or rollback after error.

BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
-- ❌ no COMMIT or ROLLBACK
