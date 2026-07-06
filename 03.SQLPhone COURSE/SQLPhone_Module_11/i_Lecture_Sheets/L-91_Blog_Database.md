# 📘 SQLPhone Emperor · SQL Module 11
# 📖 L‑91 – Blog Database

## 🎯 OBJECTIVE
Build a simple blogging platform schema with users,
posts, and comments.

## 🧱 BRICK 1 – Requirements
Entities:
- **User:** id, username (UNIQUE), email, created_at
- **Post:** id, title, body, user_id, published_at
- **Comment:** id, post_id, user_id, body, commented_at

Relationships:
- User writes many posts.
- Post has many comments.
- Comment belongs to a user and a post.

## 🧱 BRICK 2 – Deliverables
1. DDL with foreign keys, NOT NULL, and sensible defaults.
2. Insert 5 users, 10 posts, multiple comments.
3. Queries:
   - All posts with author name and comment count.
   - Users who have commented on their own post.
   - Most active commenters.
   - Posts with no comments.

## 💡 Real‑world Usage
Blog engines, social media timelines, forum threads.

## 📌 Key Takeaway
Hierarchical content (post → comments) is a
one‑to‑many relationship. Think in terms of ownership.

*Words connect people – data models connect words.*