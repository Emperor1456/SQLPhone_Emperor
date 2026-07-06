-- 🐛 BROKEN – Module 11, Lesson 93 (Movie Ratings)
-- Composite PK missing in Rating table, allowing duplicate votes.

CREATE TABLE Rating (
    user_id INTEGER,
    movie_id INTEGER,
    rating INTEGER
);  -- ❌ should be PRIMARY KEY (user_id, movie_id)
