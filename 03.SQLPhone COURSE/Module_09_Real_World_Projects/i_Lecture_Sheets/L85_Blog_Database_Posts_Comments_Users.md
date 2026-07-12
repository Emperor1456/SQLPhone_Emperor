# 📘 SQLPhone Emperor v3.0 · Module 9
# 📖 L85 – Blog Database (Posts, Comments, Users)

---

## 🎯 OBJECTIVE — What You Will Master

> Build a blogging platform database with users, posts, and threaded comments — the foundation of every CMS and social media platform.

- 🧱 **Tables** – users, posts, comments  
- 🧠 **Self‑referencing comments** – nested replies  
- 🧪 **Reports** – popular posts, active users  
- ⚡ **Real‑world** – WordPress, Medium, forum software  

---

## 🧱 THE IMPERIAL BLOG – BUSINESS REQUIREMENT

The Emperor’s blog allows users to write posts and leave comments on posts. Comments can be replies to other comments (threaded). The editor needs a dashboard showing the most commented posts and the most active users.

---

## 🧱 SCHEMA

```sql
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL
);

CREATE TABLE posts (
    post_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    title TEXT NOT NULL,
    body TEXT,
    published_date TEXT DEFAULT (datetime('now')),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE comments (
    comment_id INTEGER PRIMARY KEY,
    post_id INTEGER,
    user_id INTEGER,
    parent_comment_id INTEGER,
    body TEXT,
    created_at TEXT DEFAULT (datetime('now')),
    FOREIGN KEY (post_id) REFERENCES posts(post_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (parent_comment_id) REFERENCES comments(comment_id)
);
```

The `parent_comment_id` column references the same table — this is a self‑referencing foreign key, enabling nested replies.

---

## 🧱 SEED DATA

```sql
INSERT INTO users VALUES (1, 'emperor', 'emperor@blog.com');
INSERT INTO posts VALUES (1, 1, 'SQL Mastery', 'Content here...', '2026-07-01');
INSERT INTO comments VALUES (1, 1, 1, NULL, 'Great post!', '2026-07-02');
INSERT INTO comments VALUES (2, 1, 1, 1, 'Thanks!', '2026-07-02');
```

---

## 🧱 KEY QUERIES

**① Most commented posts (top 5)**
```sql
SELECT p.title, COUNT(c.comment_id) AS comment_count
FROM posts p
LEFT JOIN comments c ON p.post_id = c.post_id
GROUP BY p.post_id
ORDER BY comment_count DESC
LIMIT 5;
```

**② Active users (most comments)**
```sql
SELECT u.username, COUNT(c.comment_id) AS comments
FROM users u
JOIN comments c ON u.user_id = c.user_id
GROUP BY u.user_id
ORDER BY comments DESC;
```

**③ Threaded comments for a specific post (recursive CTE preview)**
```sql
WITH RECURSIVE thread AS (
    SELECT comment_id, body, parent_comment_id, 0 AS depth
    FROM comments WHERE post_id = 1 AND parent_comment_id IS NULL
    UNION ALL
    SELECT c.comment_id, c.body, c.parent_comment_id, t.depth + 1
    FROM comments c
    JOIN thread t ON c.parent_comment_id = t.comment_id
)
SELECT * FROM thread ORDER BY depth;
```

---

## 💡 Real‑world Usage

- Blog engines (WordPress, Ghost)  
- Forum software (Reddit, Discourse)  
- Social media comment systems  
- The self‑referencing foreign key pattern is used everywhere for hierarchies  

---

## 🔍 Practice Preview
You will build a blog database.

| Level | Task |
|-------|------|
| Easy | Create tables and seed data. |
| Medium | Write a query to find the most commented posts. |
| Hard | Write a recursive CTE to display threaded comments. |

Run the coach:
```bash
python ii_Practice_Sheets/L85_Blog_Database_Posts_Comments_Users.py
```

---

## 📌 Key Takeaway
- Self‑referencing foreign keys enable nested comments.  
- `LEFT JOIN` counts include posts with zero comments.  
- Recursive CTEs traverse hierarchical data.  
- This schema is the core of any content platform.

*For Emperor.*