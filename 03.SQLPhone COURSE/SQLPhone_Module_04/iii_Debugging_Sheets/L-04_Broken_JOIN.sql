-- 🐛 BROKEN QUERY – Module 04
-- This LEFT JOIN should list all customers and their orders,
-- but it behaves like an INNER JOIN due to a misplaced condition.

CREATE TABLE cust (id INTEGER, name TEXT);
CREATE TABLE ord (id INTEGER, cust_id INTEGER, product TEXT);
INSERT INTO cust VALUES (1,'Alice'),(2,'Bob');
INSERT INTO ord VALUES (1,1,'Pen'),(2,1,'Book');

-- Broken query
SELECT c.name, o.product
FROM cust c
LEFT JOIN ord o ON c.id = o.cust_id
WHERE o.product IS NOT NULL;   -- ❌ filters out the customer with no orders

-- Fix: move the condition to the ON clause or use a subquery.
-- Expected: Alice (Pen), Alice (Book), Bob (NULL).
