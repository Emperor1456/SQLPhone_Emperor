-- 🐛 BROKEN – Module 01, Lesson 06 (INSERT)
-- The INSERT forgets the column list and misorders values.
-- Fix by adding the column list and matching order.

INSERT INTO employees VALUES (1, 'Alice');  -- ❌ missing salary
