# 📘 SQLPhone Emperor · SQL Module 11
# 📖 L‑93 – Movie Rating System

## 🎯 OBJECTIVE
Model a many‑to‑many relationship between movies
and users via ratings, with additional metadata.

## 🧱 BRICK 1 – Requirements
Entities:
- **User:** id, username
- **Movie:** id, title, release_year
- **Rating:** user_id, movie_id, rating (1‑5), review_text (nullable)

Constraints:
- Composite PK on (user_id, movie_id) in Rating.
- rating between 1 and 5.

## 🧱 BRICK 2 – Deliverables
1. DDL with constraints and foreign keys.
2. Insert 5 users, 5 movies, and diverse ratings.
3. Queries:
   - Average rating per movie.
   - Movies rated by a specific user.
   - Top‑rated movies (average >= 4).
   - Users who have rated more than 3 movies.

## 💡 Real‑world Usage
Netflix, IMDb, any product with user reviews.

## 📌 Key Takeaway
Ratings are classic many‑to‑many with an additional
attribute (score). The junction table carries the value.

*Opinions become data – ratings shape choices.*