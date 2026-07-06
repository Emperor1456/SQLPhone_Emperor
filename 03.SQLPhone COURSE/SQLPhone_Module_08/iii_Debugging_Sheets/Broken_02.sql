-- 🐛 BROKEN – Module 08, Lesson 67 (Views)
-- View created with SELECT *, but underlying table adds a column later,
-- causing 'too many columns' when querying view.

CREATE VIEW customer_view AS SELECT * FROM customers;
ALTER TABLE customers ADD COLUMN phone TEXT;
SELECT * FROM customer_view;  -- ❌ column mismatch
