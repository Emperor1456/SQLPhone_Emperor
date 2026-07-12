# 📘 SQLPhone Emperor v3.0 · Module 9
# 📖 L87 – Movie Rating System (Many‑to‑Many)

---

## 🎯 OBJECTIVE — What You Will Master

> Model a many‑to‑many relationship — users rate movies — and compute average ratings, top‑ranked lists, and user preference insights. This is the exact pattern behind IMDb, Netflix, and Amazon reviews.

- 🧱 **Tables** – users, movies, ratings (join table)
- 🧠 **Many‑to‑many mechanics** – composite primary key prevents duplicate ratings
- 🧪 **Reports** – average rating, top‑N with minimum votes, genre popularity, user activity
- ⚡ **Real‑world** – any star‑rating system: products, restaurants, services

---

## 🧱 THE IMPERIAL MOVIE DATABASE – BUSINESS REQUIREMENT

Imperial Movie Club lets members rate movies from 1 to 5. No member can rate the same movie twice. The club wants:
- An overall ranking with at least 3 votes to qualify
- Genre popularity (most ratings per genre)
- Members who haven’t rated anything yet (to prompt them)

---

## 🧱 SCHEMA

```sql
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE movies (
    movie_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    genre TEXT
);

CREATE TABLE ratings (
    user_id INTEGER,
    movie_id INTEGER,
    rating INTEGER CHECK(rating BETWEEN 1 AND 5),
    rated_date TEXT DEFAULT (date('now')),
    PRIMARY KEY (user_id, movie_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
);
```

---

## 🧱 SEED DATA

```sql
INSERT INTO users VALUES (1, 'Emperor'), (2, 'Rahim'), (3, 'Karim');
INSERT INTO movies VALUES (1, 'The Matrix', 'Sci-Fi'), (2, 'Titanic', 'Romance'), (3, 'Inception', 'Sci-Fi');
INSERT INTO ratings VALUES (1, 1, 5, '2026-07-01');
INSERT INTO ratings VALUES (1, 2, 3, '2026-07-02');
INSERT INTO ratings VALUES (2, 1, 4, '2026-07-02');
INSERT INTO ratings VALUES (2, 2, 5, '2026-07-03');
INSERT INTO ratings VALUES (3, 1, 5, '2026-07-03');
```

---

## 🧱 KEY QUERIES

**① Average rating per movie with vote count**
```sql
SELECT m.title,
       ROUND(AVG(r.rating), 2) AS avg_rating,
       COUNT(*) AS votes
FROM movies m
JOIN ratings r ON m.movie_id = r.movie_id
GROUP BY m.movie_id
ORDER BY avg_rating DESC;
```

**② Top‑rated movies with at least 3 votes**
```sql
SELECT m.title, AVG(r.rating) AS avg_rating, COUNT(*) AS votes
FROM movies m
JOIN ratings r ON m.movie_id = r.movie_id
GROUP BY m.movie_id
HAVING COUNT(*) >= 3
ORDER BY avg_rating DESC;
```

**③ Users who haven't rated any movie**
```sql
SELECT name FROM users
WHERE user_id NOT IN (SELECT DISTINCT user_id FROM ratings);
```

**④ Genre popularity (number of ratings per genre)**
```sql
SELECT m.genre, COUNT(*) AS ratings_count
FROM ratings r
JOIN movies m ON r.movie_id = m.movie_id
GROUP BY m.genre
ORDER BY ratings_count DESC;
```

**⑤ Users who rated the same movie as Emperor**
```sql
SELECT DISTINCT u.name
FROM ratings r
JOIN users u ON r.user_id = u.user_id
WHERE r.movie_id IN (
    SELECT movie_id FROM ratings WHERE user_id = 1
) AND r.user_id <> 1;
```

> 💡 **INSIGHT:** `HAVING COUNT(*) >= 3` is the classic “minimum votes” filter used by IMDb’s Top 250. Without it, a movie with a single 5‑star rating would outrank classics.

> ⚠️ **WARNING:** The composite primary key `(user_id, movie_id)` prevents duplicate ratings at the database level. If you try to insert the same user/movie pair twice, SQLite throws an error.

---

## 💡 Real‑world Usage

- IMDb, Rotten Tomatoes
- Amazon product reviews
- Yelp restaurant ratings
- App store reviews

---

## 🔍 Practice Preview
You will build a movie rating system.

| Level | Task |
|-------|------|
| Easy | Create tables and seed data with 3 users, 3 movies, and 5 ratings. |
| Medium | Compute average rating per movie with vote count. |
| Hard | Find the top movie(s) with at least 3 votes, and list users who haven’t rated anything. |

Run the coach:
```bash
python ii_Practice_Sheets/L87_Movie_Rating_System_Many_to_Many.py
```

---

## 📌 Key Takeaway
- The join table `ratings` models the many‑to‑many relationship.
- Composite primary key prevents duplicates automatically.
- `HAVING` filters aggregated groups — essential for quality rankings.
- `NOT IN` subquery finds inactive users.

*For Emperor.*