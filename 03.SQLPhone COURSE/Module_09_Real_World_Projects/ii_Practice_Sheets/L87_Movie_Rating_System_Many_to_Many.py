import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🎬  Imperial Movie Club – Build the Schema\n\n"
        "Write Python code that:\n"
        "  1. Connects to ':memory:'\n"
        "  2. Creates the three tables:\n"
        "     users, movies, ratings\n"
        "     (exact schema from the lecture).\n"
        "  3. Inserts seed data:\n"
        "     • Users: Emperor (1), Rahim (2), Karim (3)\n"
        "     • Movies:\n"
        "       (1,'The Matrix','Sci-Fi')\n"
        "       (2,'Titanic','Romance')\n"
        "       (3,'Inception','Sci-Fi')\n"
        "     • Ratings:\n"
        "       (1,1,5), (1,2,3), (2,1,4),\n"
        "       (2,2,5), (3,1,5)\n"
        "  4. Commits, then SELECTs all movie titles\n"
        "     sorted alphabetically and prints them.\n\n"
        "Expected output:\n[('Inception',), ('The Matrix',), ('Titanic',)]"
    ),
    expected_output="[('Inception',), ('The Matrix',), ('Titanic',)]",
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.executescript('''",
        "CREATE TABLE users (user_id INTEGER PRIMARY KEY, name TEXT NOT NULL);",
        "CREATE TABLE movies (movie_id INTEGER PRIMARY KEY, title TEXT NOT NULL, genre TEXT);",
        "CREATE TABLE ratings (user_id INTEGER, movie_id INTEGER, rating INTEGER CHECK(rating BETWEEN 1 AND 5), rated_date TEXT DEFAULT (date('now')), PRIMARY KEY (user_id, movie_id), FOREIGN KEY (user_id) REFERENCES users(user_id), FOREIGN KEY (movie_id) REFERENCES movies(movie_id));",
        "''')",
        "conn.executescript('''",
        "INSERT INTO users VALUES (1,'Emperor'), (2,'Rahim'), (3,'Karim');",
        "INSERT INTO movies VALUES (1,'The Matrix','Sci-Fi'), (2,'Titanic','Romance'), (3,'Inception','Sci-Fi');",
        "INSERT INTO ratings VALUES (1,1,5,'2026-07-01');",
        "INSERT INTO ratings VALUES (1,2,3,'2026-07-02');",
        "INSERT INTO ratings VALUES (2,1,4,'2026-07-02');",
        "INSERT INTO ratings VALUES (2,2,5,'2026-07-03');",
        "INSERT INTO ratings VALUES (3,1,5,'2026-07-03');",
        "''')",
        "conn.commit()",
        "cursor = conn.execute('SELECT title FROM movies ORDER BY title')",
        "print(cursor.fetchall())",
    ]
)

easy2 = Task(
    description=(
        "⭐  Average Rating per Movie – Vote Count\n\n"
        "The movie database is already seeded.\n"
        "Write Python code that shows each movie's title,\n"
        "average rating (rounded to 2 decimals), and the\n"
        "number of votes. Sort by title alphabetically.\n\n"
        "Expected output:\n[('Inception',None,0), ('The Matrix',4.67,3), ('Titanic',4.0,2)]"
    ),
    setup_sql=(
        "CREATE TABLE users (user_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO users VALUES (1,'Emperor'), (2,'Rahim'), (3,'Karim');"
        "CREATE TABLE movies (movie_id INTEGER PRIMARY KEY, title TEXT NOT NULL, genre TEXT);"
        "INSERT INTO movies VALUES (1,'The Matrix','Sci-Fi'), (2,'Titanic','Romance'), (3,'Inception','Sci-Fi');"
        "CREATE TABLE ratings (user_id INTEGER, movie_id INTEGER, rating INTEGER CHECK(rating BETWEEN 1 AND 5), rated_date TEXT DEFAULT (date('now')), PRIMARY KEY (user_id, movie_id), FOREIGN KEY (user_id) REFERENCES users(user_id), FOREIGN KEY (movie_id) REFERENCES movies(movie_id));"
        "INSERT INTO ratings VALUES (1,1,5,'2026-07-01');"
        "INSERT INTO ratings VALUES (1,2,3,'2026-07-02');"
        "INSERT INTO ratings VALUES (2,1,4,'2026-07-02');"
        "INSERT INTO ratings VALUES (2,2,5,'2026-07-03');"
        "INSERT INTO ratings VALUES (3,1,5,'2026-07-03');"
    ),
    expected_output="[('Inception', None, 0), ('The Matrix', 4.66666666666667, 3), ('Titanic', 4.0, 2)]",
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT m.title, AVG(r.rating) AS avg_rating, COUNT(r.rating) AS votes",
        "FROM movies m LEFT JOIN ratings r ON m.movie_id = r.movie_id",
        "GROUP BY m.movie_id ORDER BY m.title",
        "''')",
        "print(cursor.fetchall())",
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🏆  Top‑Rated Movies – Minimum 3 Votes\n\n"
        "The movie database is seeded.\n"
        "Write Python code that finds movies with at least\n"
        "3 ratings. Show title, average rating, and vote count.\n"
        "Sort by average rating descending.\n\n"
        "Expected output:\n[('The Matrix', 4.66666666666667, 3)]"
    ),
    setup_sql=(
        "CREATE TABLE users (user_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO users VALUES (1,'Emperor'), (2,'Rahim'), (3,'Karim');"
        "CREATE TABLE movies (movie_id INTEGER PRIMARY KEY, title TEXT NOT NULL, genre TEXT);"
        "INSERT INTO movies VALUES (1,'The Matrix','Sci-Fi'), (2,'Titanic','Romance'), (3,'Inception','Sci-Fi');"
        "CREATE TABLE ratings (user_id INTEGER, movie_id INTEGER, rating INTEGER CHECK(rating BETWEEN 1 AND 5), rated_date TEXT DEFAULT (date('now')), PRIMARY KEY (user_id, movie_id), FOREIGN KEY (user_id) REFERENCES users(user_id), FOREIGN KEY (movie_id) REFERENCES movies(movie_id));"
        "INSERT INTO ratings VALUES (1,1,5,'2026-07-01');"
        "INSERT INTO ratings VALUES (1,2,3,'2026-07-02');"
        "INSERT INTO ratings VALUES (2,1,4,'2026-07-02');"
        "INSERT INTO ratings VALUES (2,2,5,'2026-07-03');"
        "INSERT INTO ratings VALUES (3,1,5,'2026-07-03');"
    ),
    expected_output="[('The Matrix', 4.66666666666667, 3)]",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT m.title, AVG(r.rating) AS avg_rating, COUNT(*) AS votes",
        "FROM movies m JOIN ratings r ON m.movie_id = r.movie_id",
        "GROUP BY m.movie_id HAVING COUNT(*) >= 3",
        "ORDER BY avg_rating DESC",
        "''')",
        "print(cursor.fetchall())",
    ]
)

medium2 = Task(
    description=(
        "🎭  Genre Popularity – Ratings per Genre\n\n"
        "The movie database is seeded.\n"
        "Write Python code that counts how many ratings\n"
        "each genre received (not movies — ratings).\n"
        "Show genre and the count, sorted by count descending.\n\n"
        "Expected output:\n[('Sci-Fi', 3), ('Romance', 2)]"
    ),
    setup_sql=(
        "CREATE TABLE users (user_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO users VALUES (1,'Emperor'), (2,'Rahim'), (3,'Karim');"
        "CREATE TABLE movies (movie_id INTEGER PRIMARY KEY, title TEXT NOT NULL, genre TEXT);"
        "INSERT INTO movies VALUES (1,'The Matrix','Sci-Fi'), (2,'Titanic','Romance'), (3,'Inception','Sci-Fi');"
        "CREATE TABLE ratings (user_id INTEGER, movie_id INTEGER, rating INTEGER CHECK(rating BETWEEN 1 AND 5), rated_date TEXT DEFAULT (date('now')), PRIMARY KEY (user_id, movie_id), FOREIGN KEY (user_id) REFERENCES users(user_id), FOREIGN KEY (movie_id) REFERENCES movies(movie_id));"
        "INSERT INTO ratings VALUES (1,1,5,'2026-07-01');"
        "INSERT INTO ratings VALUES (1,2,3,'2026-07-02');"
        "INSERT INTO ratings VALUES (2,1,4,'2026-07-02');"
        "INSERT INTO ratings VALUES (2,2,5,'2026-07-03');"
        "INSERT INTO ratings VALUES (3,1,5,'2026-07-03');"
    ),
    expected_output="[('Sci-Fi', 3), ('Romance', 2)]",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT m.genre, COUNT(*) AS ratings_count",
        "FROM ratings r JOIN movies m ON r.movie_id = m.movie_id",
        "GROUP BY m.genre ORDER BY ratings_count DESC",
        "''')",
        "print(cursor.fetchall())",
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🔇  Inactive Members – Haven't Rated\n\n"
        "The movie database includes a 4th member 'Hasan'\n"
        "who has never rated a movie.\n"
        "Write Python code that finds the names of all\n"
        "members who have not submitted any ratings.\n"
        "Sort by name.\n\n"
        "Expected output:\n[('Hasan',)]"
    ),
    setup_sql=(
        "CREATE TABLE users (user_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO users VALUES (1,'Emperor'), (2,'Rahim'), (3,'Karim'), (4,'Hasan');"
        "CREATE TABLE movies (movie_id INTEGER PRIMARY KEY, title TEXT NOT NULL, genre TEXT);"
        "INSERT INTO movies VALUES (1,'The Matrix','Sci-Fi'), (2,'Titanic','Romance'), (3,'Inception','Sci-Fi');"
        "CREATE TABLE ratings (user_id INTEGER, movie_id INTEGER, rating INTEGER CHECK(rating BETWEEN 1 AND 5), rated_date TEXT DEFAULT (date('now')), PRIMARY KEY (user_id, movie_id), FOREIGN KEY (user_id) REFERENCES users(user_id), FOREIGN KEY (movie_id) REFERENCES movies(movie_id));"
        "INSERT INTO ratings VALUES (1,1,5,'2026-07-01');"
        "INSERT INTO ratings VALUES (1,2,3,'2026-07-02');"
        "INSERT INTO ratings VALUES (2,1,4,'2026-07-02');"
        "INSERT INTO ratings VALUES (2,2,5,'2026-07-03');"
        "INSERT INTO ratings VALUES (3,1,5,'2026-07-03');"
    ),
    expected_output="[('Hasan',)]",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''SELECT name FROM users WHERE user_id NOT IN (SELECT DISTINCT user_id FROM ratings) ORDER BY name''')",
        "print(cursor.fetchall())",
    ]
)

hard2 = Task(
    description=(
        "🤝  Similar Tastes – Rated Same Movies as Emperor\n\n"
        "The movie database is seeded.\n"
        "Write Python code that finds users (other than Emperor)\n"
        "who have rated at least one movie that Emperor\n"
        "(user_id=1) also rated. Return distinct names,\n"
        "sorted alphabetically.\n\n"
        "Expected output:\n[('Karim',), ('Rahim',)]"
    ),
    setup_sql=(
        "CREATE TABLE users (user_id INTEGER PRIMARY KEY, name TEXT NOT NULL);"
        "INSERT INTO users VALUES (1,'Emperor'), (2,'Rahim'), (3,'Karim');"
        "CREATE TABLE movies (movie_id INTEGER PRIMARY KEY, title TEXT NOT NULL, genre TEXT);"
        "INSERT INTO movies VALUES (1,'The Matrix','Sci-Fi'), (2,'Titanic','Romance'), (3,'Inception','Sci-Fi');"
        "CREATE TABLE ratings (user_id INTEGER, movie_id INTEGER, rating INTEGER CHECK(rating BETWEEN 1 AND 5), rated_date TEXT DEFAULT (date('now')), PRIMARY KEY (user_id, movie_id), FOREIGN KEY (user_id) REFERENCES users(user_id), FOREIGN KEY (movie_id) REFERENCES movies(movie_id));"
        "INSERT INTO ratings VALUES (1,1,5,'2026-07-01');"
        "INSERT INTO ratings VALUES (1,2,3,'2026-07-02');"
        "INSERT INTO ratings VALUES (2,1,4,'2026-07-02');"
        "INSERT INTO ratings VALUES (2,2,5,'2026-07-03');"
        "INSERT INTO ratings VALUES (3,1,5,'2026-07-03');"
    ),
    expected_output="[('Karim',), ('Rahim',)]",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT DISTINCT u.name FROM ratings r JOIN users u ON r.user_id = u.user_id",
        "WHERE r.movie_id IN (SELECT movie_id FROM ratings WHERE user_id = 1)",
        "AND r.user_id <> 1 ORDER BY u.name",
        "''')",
        "print(cursor.fetchall())",
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L87.json",
        module_name="Module_09_Real_World_Projects",
        lesson_name="L87_Movie_Rating_System_Many_to_Many"
    )