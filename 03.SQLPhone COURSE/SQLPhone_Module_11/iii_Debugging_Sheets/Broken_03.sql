-- 🐛 BROKEN – Module 11, Lesson 88 (E‑commerce)
-- CHECK constraint missing, allowing negative stock.

CREATE TABLE Product (
    id INTEGER PRIMARY KEY,
    name TEXT,
    stock_quantity INTEGER  -- ❌ need CHECK (stock_quantity >= 0)
);
