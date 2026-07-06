-- 🐛 BROKEN – Module 04, Lesson 31 (LEFT JOIN)
-- INNER JOIN used instead of LEFT JOIN, losing customers without orders.

SELECT c.name, o.product FROM customers c
JOIN orders o ON c.id = o.customer_id;  -- ❌ should be LEFT JOIN
