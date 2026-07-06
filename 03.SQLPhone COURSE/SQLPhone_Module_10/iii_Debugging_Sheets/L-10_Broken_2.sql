-- 🐛 BROKEN QUERY 2 – Common Mistake
-- This query tries to list all products with a price above average,
-- but the logic is flipped and the alias is misused.

-- Setup (run this first)
-- CREATE TABLE products (name TEXT, price REAL);
-- INSERT INTO products VALUES ('A',10),('B',30),('C',20);

-- Broken query:
SELECT name, price
FROM products
WHERE price < (SELECT AVG(price) FROM products);   -- ❌ uses < instead of >

-- Also, the alias 'avg_price' is defined but not used correctly.
-- Fix the comparison operator and remove the unused alias.
