import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
SELECT m.title, ROUND(AVG(r.rating), 2) AS avg_rating, COUNT(*) AS votes
FROM movies m
JOIN ratings r ON m.movie_id = r.movie_id
GROUP BY m.movie_id
HAVING COUNT(*) >= 3
ORDER BY avg_rating DESC;"""

EXPECTED = "[('The Matrix', 4.67, 3)]"

SETUP = """\
CREATE TABLE users (user_id INTEGER PRIMARY KEY, name TEXT NOT NULL);
INSERT INTO users VALUES (1,'Emperor'), (2,'Rahim'), (3,'Karim');
CREATE TABLE movies (movie_id INTEGER PRIMARY KEY, title TEXT NOT NULL, genre TEXT);
INSERT INTO movies VALUES (1,'The Matrix','Sci-Fi'), (2,'Titanic','Romance'), (3,'Inception','Sci-Fi');
CREATE TABLE ratings (user_id INTEGER, movie_id INTEGER, rating INTEGER CHECK(rating BETWEEN 1 AND 5), rated_date TEXT DEFAULT (date('now')), PRIMARY KEY (user_id, movie_id), FOREIGN KEY (user_id) REFERENCES users(user_id), FOREIGN KEY (movie_id) REFERENCES movies(movie_id));
INSERT INTO ratings VALUES (1,1,5,'2026-07-01'),(1,2,3,'2026-07-02'),(2,1,4,'2026-07-02'),(2,2,5,'2026-07-03'),(3,1,5,'2026-07-03');"""

HINTS = [
    "The query is correct, but the broken code may have a typo in the HAVING clause.",
    "Check the spelling: 'HAVING' might be written as 'HAVINGG'.",
    "Change 'HAVINGG' to 'HAVING'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L87 – Movie Rating System (Many‑to‑Many)",
        setup_sql=SETUP,
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
