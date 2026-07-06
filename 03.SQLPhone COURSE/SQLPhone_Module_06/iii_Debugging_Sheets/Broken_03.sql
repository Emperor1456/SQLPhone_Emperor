-- 🐛 BROKEN – Module 06, Lesson 55 (CREATE INDEX)
-- Index created on column with low cardinality, useless.

CREATE INDEX idx_gender ON employees(gender);  -- ❌ only 'M'/'F'
