import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "📝  Imperial Blog – Build the Schema\n\n"
        "Write Python code that:\n"
        "  1. Connects to ':memory:'\n"
        "  2. Creates the three tables:\n"
        "     users, posts, comments\n"
        "     (exact schema from the lecture).\n"
        "  3. Inserts seed data:\n"
        "     • Users: emperor (1), rahim (2)\n"
        "     • Posts: (1,1,'SQL Mastery','Deep dive...','2026-07-01'),\n"
        "              (2,2,'Python Tips','Handy tricks...','2026-07-02')\n"
        "     • Comments:\n"
        "       (1,1,1,NULL,'Great post!','2026-07-02'),\n"
        "       (2,1,2,1,'Thanks!','2026-07-02'),\n"
        "       (3,2,1,NULL,'Useful','2026-07-03')\n"
        "  4. Commits, then SELECTs all post titles\n"
        "     sorted by published_date and prints them.\n\n"
        "Expected output:\n[('SQL Mastery',), ('Python Tips',)]"
    ),
    expected_output="[('SQL Mastery',), ('Python Tips',)]",
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.executescript('''",
        "CREATE TABLE users (user_id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL, email TEXT UNIQUE NOT NULL);",
        "CREATE TABLE posts (post_id INTEGER PRIMARY KEY, user_id INTEGER, title TEXT NOT NULL, body TEXT, published_date TEXT DEFAULT (datetime('now')), FOREIGN KEY (user_id) REFERENCES users(user_id));",
        "CREATE TABLE comments (comment_id INTEGER PRIMARY KEY, post_id INTEGER, user_id INTEGER, parent_comment_id INTEGER, body TEXT, created_at TEXT DEFAULT (datetime('now')), FOREIGN KEY (post_id) REFERENCES posts(post_id), FOREIGN KEY (user_id) REFERENCES users(user_id), FOREIGN KEY (parent_comment_id) REFERENCES comments(comment_id));",
        "''')",
        "conn.executescript('''",
        "INSERT INTO users VALUES (1,'emperor','emperor@blog.com');",
        "INSERT INTO users VALUES (2,'rahim','rahim@blog.com');",
        "INSERT INTO posts VALUES (1,1,'SQL Mastery','Deep dive...','2026-07-01');",
        "INSERT INTO posts VALUES (2,2,'Python Tips','Handy tricks...','2026-07-02');",
        "INSERT INTO comments VALUES (1,1,1,NULL,'Great post!','2026-07-02');",
        "INSERT INTO comments VALUES (2,1,2,1,'Thanks!','2026-07-02');",
        "INSERT INTO comments VALUES (3,2,1,NULL,'Useful','2026-07-03');",
        "''')",
        "conn.commit()",
        "cursor = conn.execute('SELECT title FROM posts ORDER BY published_date')",
        "print(cursor.fetchall())",
    ]
)

easy2 = Task(
    description=(
        "👤  Post Authors – JOIN posts with users\n\n"
        "The blog database is already seeded.\n"
        "Write Python code that shows each post's title\n"
        "and the author's username. Sort by post_id.\n\n"
        "Expected output:\n[('SQL Mastery','emperor'), ('Python Tips','rahim')]"
    ),
    setup_sql=(
        "CREATE TABLE users (user_id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL, email TEXT UNIQUE NOT NULL);"
        "INSERT INTO users VALUES (1,'emperor','emperor@blog.com');"
        "INSERT INTO users VALUES (2,'rahim','rahim@blog.com');"
        "CREATE TABLE posts (post_id INTEGER PRIMARY KEY, user_id INTEGER, title TEXT NOT NULL, body TEXT, published_date TEXT DEFAULT (datetime('now')), FOREIGN KEY (user_id) REFERENCES users(user_id));"
        "INSERT INTO posts VALUES (1,1,'SQL Mastery','Deep dive...','2026-07-01');"
        "INSERT INTO posts VALUES (2,2,'Python Tips','Handy tricks...','2026-07-02');"
        "CREATE TABLE comments (comment_id INTEGER PRIMARY KEY, post_id INTEGER, user_id INTEGER, parent_comment_id INTEGER, body TEXT, created_at TEXT DEFAULT (datetime('now')), FOREIGN KEY (post_id) REFERENCES posts(post_id), FOREIGN KEY (user_id) REFERENCES users(user_id), FOREIGN KEY (parent_comment_id) REFERENCES comments(comment_id));"
        "INSERT INTO comments VALUES (1,1,1,NULL,'Great post!','2026-07-02');"
        "INSERT INTO comments VALUES (2,1,2,1,'Thanks!','2026-07-02');"
        "INSERT INTO comments VALUES (3,2,1,NULL,'Useful','2026-07-03');"
    ),
    expected_output="[('SQL Mastery', 'emperor'), ('Python Tips', 'rahim')]",
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''SELECT p.title, u.username FROM posts p JOIN users u ON p.user_id = u.user_id ORDER BY p.post_id''')",
        "print(cursor.fetchall())",
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "💬  Most Commented Posts – Top 5\n\n"
        "The blog database is seeded.\n"
        "Write Python code that lists posts (title) and\n"
        "their comment count (including zero).\n"
        "Sort by comment_count descending, then by title.\n"
        "Limit to 5.\n\n"
        "Expected output:\n[('SQL Mastery',2), ('Python Tips',1)]"
    ),
    setup_sql=(
        "CREATE TABLE users (user_id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL, email TEXT UNIQUE NOT NULL);"
        "INSERT INTO users VALUES (1,'emperor','emperor@blog.com');"
        "INSERT INTO users VALUES (2,'rahim','rahim@blog.com');"
        "CREATE TABLE posts (post_id INTEGER PRIMARY KEY, user_id INTEGER, title TEXT NOT NULL, body TEXT, published_date TEXT DEFAULT (datetime('now')), FOREIGN KEY (user_id) REFERENCES users(user_id));"
        "INSERT INTO posts VALUES (1,1,'SQL Mastery','Deep dive...','2026-07-01');"
        "INSERT INTO posts VALUES (2,2,'Python Tips','Handy tricks...','2026-07-02');"
        "CREATE TABLE comments (comment_id INTEGER PRIMARY KEY, post_id INTEGER, user_id INTEGER, parent_comment_id INTEGER, body TEXT, created_at TEXT DEFAULT (datetime('now')), FOREIGN KEY (post_id) REFERENCES posts(post_id), FOREIGN KEY (user_id) REFERENCES users(user_id), FOREIGN KEY (parent_comment_id) REFERENCES comments(comment_id));"
        "INSERT INTO comments VALUES (1,1,1,NULL,'Great post!','2026-07-02');"
        "INSERT INTO comments VALUES (2,1,2,1,'Thanks!','2026-07-02');"
        "INSERT INTO comments VALUES (3,2,1,NULL,'Useful','2026-07-03');"
    ),
    expected_output="[('SQL Mastery', 2), ('Python Tips', 1)]",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''SELECT p.title, COUNT(c.comment_id) AS comment_count FROM posts p LEFT JOIN comments c ON p.post_id = c.post_id GROUP BY p.post_id ORDER BY comment_count DESC, p.title LIMIT 5''')",
        "print(cursor.fetchall())",
    ]
)

medium2 = Task(
    description=(
        "👥  Most Active Users – Comment Counts\n\n"
        "The blog database is seeded.\n"
        "Write Python code that shows each user's username\n"
        "and how many comments they have written.\n"
        "Sort by comment count descending, then username.\n\n"
        "Expected output:\n[('emperor',2), ('rahim',1)]"
    ),
    setup_sql=(
        "CREATE TABLE users (user_id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL, email TEXT UNIQUE NOT NULL);"
        "INSERT INTO users VALUES (1,'emperor','emperor@blog.com');"
        "INSERT INTO users VALUES (2,'rahim','rahim@blog.com');"
        "CREATE TABLE posts (post_id INTEGER PRIMARY KEY, user_id INTEGER, title TEXT NOT NULL, body TEXT, published_date TEXT DEFAULT (datetime('now')), FOREIGN KEY (user_id) REFERENCES users(user_id));"
        "INSERT INTO posts VALUES (1,1,'SQL Mastery','Deep dive...','2026-07-01');"
        "INSERT INTO posts VALUES (2,2,'Python Tips','Handy tricks...','2026-07-02');"
        "CREATE TABLE comments (comment_id INTEGER PRIMARY KEY, post_id INTEGER, user_id INTEGER, parent_comment_id INTEGER, body TEXT, created_at TEXT DEFAULT (datetime('now')), FOREIGN KEY (post_id) REFERENCES posts(post_id), FOREIGN KEY (user_id) REFERENCES users(user_id), FOREIGN KEY (parent_comment_id) REFERENCES comments(comment_id));"
        "INSERT INTO comments VALUES (1,1,1,NULL,'Great post!','2026-07-02');"
        "INSERT INTO comments VALUES (2,1,2,1,'Thanks!','2026-07-02');"
        "INSERT INTO comments VALUES (3,2,1,NULL,'Useful','2026-07-03');"
    ),
    expected_output="[('emperor', 2), ('rahim', 1)]",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''SELECT u.username, COUNT(c.comment_id) AS comments FROM users u LEFT JOIN comments c ON u.user_id = c.user_id GROUP BY u.user_id ORDER BY comments DESC, u.username''')",
        "print(cursor.fetchall())",
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🧵  Threaded Comments – Recursive CTE\n\n"
        "The blog database is seeded with a post (id=1)\n"
        "and a nested comment thread.\n"
        "Write a recursive CTE that retrieves all comments\n"
        "for post_id=1, showing comment_id, body,\n"
        "parent_comment_id, and depth (0 for root).\n"
        "Sort by depth, then comment_id.\n\n"
        "Expected output:\n[(1,'Great post!',None,0), (2,'Thanks!',1,1), (3,'You're welcome',2,2)]"
    ),
    setup_sql=(
        "CREATE TABLE users (user_id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL, email TEXT UNIQUE NOT NULL);"
        "INSERT INTO users VALUES (1,'emperor','emperor@blog.com');"
        "INSERT INTO users VALUES (2,'rahim','rahim@blog.com');"
        "CREATE TABLE posts (post_id INTEGER PRIMARY KEY, user_id INTEGER, title TEXT NOT NULL, body TEXT, published_date TEXT DEFAULT (datetime('now')), FOREIGN KEY (user_id) REFERENCES users(user_id));"
        "INSERT INTO posts VALUES (1,1,'SQL Mastery','Deep dive...','2026-07-01');"
        "CREATE TABLE comments (comment_id INTEGER PRIMARY KEY, post_id INTEGER, user_id INTEGER, parent_comment_id INTEGER, body TEXT, created_at TEXT DEFAULT (datetime('now')), FOREIGN KEY (post_id) REFERENCES posts(post_id), FOREIGN KEY (user_id) REFERENCES users(user_id), FOREIGN KEY (parent_comment_id) REFERENCES comments(comment_id));"
        "INSERT INTO comments VALUES (1,1,1,NULL,'Great post!','2026-07-02');"
        "INSERT INTO comments VALUES (2,1,2,1,'Thanks!','2026-07-02');"
        "INSERT INTO comments VALUES (3,1,1,2,\"You're welcome\",'2026-07-03');"
    ),
    expected_output="[(1, 'Great post!', None, 0), (2, 'Thanks!', 1, 1), (3, \"You're welcome\", 2, 2)]",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "WITH RECURSIVE thread AS (",
        "    SELECT comment_id, body, parent_comment_id, 0 AS depth",
        "    FROM comments WHERE post_id = 1 AND parent_comment_id IS NULL",
        "    UNION ALL",
        "    SELECT c.comment_id, c.body, c.parent_comment_id, t.depth + 1",
        "    FROM comments c JOIN thread t ON c.parent_comment_id = t.comment_id",
        ")",
        "SELECT comment_id, body, parent_comment_id, depth",
        "FROM thread ORDER BY depth, comment_id",
        "''')",
        "print(cursor.fetchall())",
    ]
)

hard2 = Task(
    description=(
        "🔇  Posts with No Comments\n\n"
        "The blog database is seeded with an extra post\n"
        "that has no comments.\n"
        "Write Python code that finds the titles of all\n"
        "posts with zero comments. Sort by title.\n\n"
        "Expected output:\n[('Advanced SQL',)]"
    ),
    setup_sql=(
        "CREATE TABLE users (user_id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL, email TEXT UNIQUE NOT NULL);"
        "INSERT INTO users VALUES (1,'emperor','emperor@blog.com');"
        "INSERT INTO users VALUES (2,'rahim','rahim@blog.com');"
        "CREATE TABLE posts (post_id INTEGER PRIMARY KEY, user_id INTEGER, title TEXT NOT NULL, body TEXT, published_date TEXT DEFAULT (datetime('now')), FOREIGN KEY (user_id) REFERENCES users(user_id));"
        "INSERT INTO posts VALUES (1,1,'SQL Mastery','Deep dive...','2026-07-01');"
        "INSERT INTO posts VALUES (2,2,'Python Tips','Handy tricks...','2026-07-02');"
        "INSERT INTO posts VALUES (3,1,'Advanced SQL','Even deeper...','2026-07-03');"
        "CREATE TABLE comments (comment_id INTEGER PRIMARY KEY, post_id INTEGER, user_id INTEGER, parent_comment_id INTEGER, body TEXT, created_at TEXT DEFAULT (datetime('now')), FOREIGN KEY (post_id) REFERENCES posts(post_id), FOREIGN KEY (user_id) REFERENCES users(user_id), FOREIGN KEY (parent_comment_id) REFERENCES comments(comment_id));"
        "INSERT INTO comments VALUES (1,1,1,NULL,'Great post!','2026-07-02');"
        "INSERT INTO comments VALUES (2,1,2,1,'Thanks!','2026-07-02');"
        "INSERT INTO comments VALUES (3,2,1,NULL,'Useful','2026-07-03');"
    ),
    expected_output="[('Advanced SQL',)]",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''SELECT title FROM posts WHERE post_id NOT IN (SELECT post_id FROM comments) ORDER BY title''')",
        "print(cursor.fetchall())",
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L85.json",
        module_name="Module_09_Real_World_Projects",
        lesson_name="L85_Blog_Database_Posts_Comments_Users"
    )