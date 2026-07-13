import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
WITH RECURSIVE thread AS (
    SELECT comment_id, body, parent_comment_id, 0 AS depth
    FROM comments WHERE post_id = 1 AND parent_comment_id IS NULL
    UNION ALL
    SELECT c.comment_id, c.body, c.parent_comment_id, t.depth + 1
    FROM comments c
    JOIN thread t ON c.parent_comment_id = t.comment_id
)
SELECT * FROM thread ORDER BY depth, comment_id;"""

EXPECTED = "[(1, 'Great post!', None, 0), (2, 'Thanks!', 1, 1), (3, \"You're welcome\", 2, 2)]"

SETUP = """\
CREATE TABLE users (user_id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL, email TEXT UNIQUE NOT NULL);
INSERT INTO users VALUES (1,'emperor','emperor@blog.com'),(2,'rahim','rahim@blog.com');
CREATE TABLE posts (post_id INTEGER PRIMARY KEY, user_id INTEGER, title TEXT NOT NULL, body TEXT, published_date TEXT DEFAULT (datetime('now')), FOREIGN KEY (user_id) REFERENCES users(user_id));
INSERT INTO posts VALUES (1,1,'SQL Mastery','Deep dive...','2026-07-01');
CREATE TABLE comments (comment_id INTEGER PRIMARY KEY, post_id INTEGER, user_id INTEGER, parent_comment_id INTEGER, body TEXT, created_at TEXT DEFAULT (datetime('now')), FOREIGN KEY (post_id) REFERENCES posts(post_id), FOREIGN KEY (user_id) REFERENCES users(user_id), FOREIGN KEY (parent_comment_id) REFERENCES comments(comment_id));
INSERT INTO comments VALUES (1,1,1,NULL,'Great post!','2026-07-02'),(2,1,2,1,'Thanks!','2026-07-02'),(3,1,1,2,\"You're welcome\",'2026-07-03');"""

HINTS = [
    "The recursive CTE is missing the keyword 'RECURSIVE'? No, it's there. But the broken code might have 'WITH RECURSIVE thread AS' – that's correct. However, the bug could be that the CTE references 'comments' but the table is named 'comments' – correct. I'll introduce a typo: 'WITH RECURSIVE thred AS' instead of 'thread' in the CTE name, then used later as 'thread'. That mismatch will cause an error.",
    "Check the CTE name: it's 'thred' in the definition but 'thread' in the JOIN.",
    "Change 'thred' to 'thread'."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L85 – Blog Database (Posts, Comments, Users)",
        setup_sql=SETUP,
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
