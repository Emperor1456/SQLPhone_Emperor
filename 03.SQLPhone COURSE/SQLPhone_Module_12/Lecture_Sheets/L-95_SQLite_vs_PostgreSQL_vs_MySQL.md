# 📘 SQLPhone Emperor · SQL Module 12
# 📖 L‑95 – SQLite vs PostgreSQL vs MySQL

## 🎯 OBJECTIVE
Compare the three major relational databases: SQLite,
PostgreSQL, and MySQL. Understand their strengths,
weaknesses, and when to use each.

## 🧱 BRICK 1 – Feature Comparison

| Feature | SQLite | PostgreSQL | MySQL |
|---------|--------|------------|-------|
| Type | Embedded, serverless | Client‑server | Client‑server |
| Setup | Zero‑config | Requires installation | Requires installation |
| Concurrency | Single writer | Excellent (MVCC) | Good (row locking) |
| Data Types | Flexible (5 affinities) | Rich (JSON, arrays, custom) | Standard + some extensions |
| SQL Compliance | Mostly SQL‑92 | Highly compliant (SQL:2011) | Good, but some quirks |
| Extensions | Limited | Powerful (PostGIS, etc.) | Plugins available |
| Use Case | Mobile apps, embedded, prototyping | Complex apps, analytics, GIS | Web applications, LAMP stack |

## 🧱 BRICK 2 – When to Choose Which
- **SQLite** – when you need a simple, portable, single‑file database
  with no server overhead. Perfect for phone‑first development,
  IoT, and small to medium projects.
- **PostgreSQL** – when you need advanced features (JSONB, full‑text
  search, window functions), strict standards compliance, and the
  ability to handle complex queries and high concurrency.
- **MySQL** – often chosen for web apps due to historical popularity,
  good read performance, and wide hosting support.

## 💡 Real‑world Usage
- SQLite powers every smartphone, many browsers, and embedded systems.
- PostgreSQL is used by Instagram, Spotify, and countless startups.
- MySQL runs Wikipedia, Facebook (originally), and many WordPress sites.

## 📌 Key Takeaway
No single database is best for everything.
Choose based on your application’s needs, not hype.
Your SQL skills transfer across all three.

*The database is a tool – pick the right one for the job.*