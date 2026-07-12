# 📘 SQLPhone Emperor v3.0 · Module 9
# 📖 L89 – Custom Project – Design & Implement

---

## 🎯 OBJECTIVE — What You Will Master

> Apply every SQL skill you’ve acquired to design, build, and document a complete database from scratch — the ultimate proof of your independence as a database engineer.

- 🧱 **Idea generation** – pick a domain and define clear business requirements
- 🧠 **Schema design** – translate requirements into normalized tables with constraints
- 🧪 **Implementation** – write `schema.sql`, `seed.sql`, and `queries.sql`
- ⚡ **Documentation** – create a professional `README.md` with schema diagram
- 🧰 **Real‑world** – this is exactly how startups build their first database

---

## 🧱 CHOOSING YOUR PROJECT

Pick a domain that excites you — preferably one that aligns with your future Companion modules or a business you’d want to build. The project must include at least **4 tables** with foreign key relationships.

| Domain | Core Tables | Real‑World Example |
|--------|-------------|-------------------|
| **Fitness Tracker** | users, workouts, exercises, sets | Strava, MyFitnessPal |
| **Recipe Manager** | recipes, ingredients, meal_plans, nutrition | Yummly, AllRecipes |
| **Job Board** | companies, listings, applications, users | LinkedIn Jobs, Indeed |
| **Event Scheduler** | events, attendees, venues, reminders | Google Calendar, Eventbrite |
| **Companion Memory** | conversations, facts, embeddings, entities | Your future AI |

---

## 🧱 REQUIREMENTS – FITNESS TRACKER EXAMPLE

> *This example uses a Fitness Tracker. You may substitute your own domain entirely.*

**Business rules:**
- Users log multiple workouts.
- Each workout contains multiple exercises.
- Each exercise has multiple sets (weight, reps).
- Users can follow other users.
- The system must track personal records (max weight per exercise per user).

**Tables:** `users`, `workouts`, `exercises`, `sets`, `follows`, `personal_records`

---

## 🧱 SCHEMA (FITNESS TRACKER)

```sql
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    join_date TEXT DEFAULT (date('now'))
);

CREATE TABLE workouts (
    workout_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    workout_date TEXT DEFAULT (date('now')),
    notes TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE exercises (
    exercise_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    category TEXT  -- e.g., 'chest', 'legs', 'cardio'
);

CREATE TABLE sets (
    set_id INTEGER PRIMARY KEY,
    workout_id INTEGER NOT NULL,
    exercise_id INTEGER NOT NULL,
    weight_kg REAL CHECK(weight_kg >= 0),
    reps INTEGER CHECK(reps > 0),
    FOREIGN KEY (workout_id) REFERENCES workouts(workout_id),
    FOREIGN KEY (exercise_id) REFERENCES exercises(exercise_id)
);

CREATE TABLE follows (
    follower_id INTEGER,
    following_id INTEGER,
    PRIMARY KEY (follower_id, following_id),
    FOREIGN KEY (follower_id) REFERENCES users(user_id),
    FOREIGN KEY (following_id) REFERENCES users(user_id)
);
```

---

## 🧱 SEED DATA (EXCERPT)

```sql
INSERT INTO users VALUES (1, 'emperor', '2026-01-01');
INSERT INTO users VALUES (2, 'rahim', '2026-02-15');
INSERT INTO exercises VALUES (1, 'Bench Press', 'chest');
INSERT INTO exercises VALUES (2, 'Squat', 'legs');
INSERT INTO workouts VALUES (1, 1, '2026-07-01', 'Chest day');
INSERT INTO sets VALUES (1, 1, 1, 80, 10);
INSERT INTO sets VALUES (2, 1, 1, 85, 8);
INSERT INTO sets VALUES (3, 1, 2, 120, 5);
INSERT INTO follows VALUES (1, 2);  -- emperor follows rahim
```

---

## 🧱 BUSINESS QUERIES (MINIMUM 5)

**① Total volume (weight × reps) per user per exercise**
```sql
SELECT u.username, e.name AS exercise, SUM(s.weight_kg * s.reps) AS total_volume
FROM sets s
JOIN workouts w ON s.workout_id = w.workout_id
JOIN users u ON w.user_id = u.user_id
JOIN exercises e ON s.exercise_id = e.exercise_id
GROUP BY u.user_id, e.exercise_id
ORDER BY total_volume DESC;
```

**② Personal record per exercise per user (max weight)**
```sql
SELECT u.username, e.name AS exercise, MAX(s.weight_kg) AS personal_record
FROM sets s
JOIN workouts w ON s.workout_id = w.workout_id
JOIN users u ON w.user_id = u.user_id
JOIN exercises e ON s.exercise_id = e.exercise_id
GROUP BY u.user_id, e.exercise_id;
```

**③ Users followed by 'emperor'**
```sql
SELECT u.username
FROM follows f
JOIN users u ON f.following_id = u.user_id
WHERE f.follower_id = 1;
```

**④ Monthly workout count per user**
```sql
SELECT u.username, strftime('%Y-%m', w.workout_date) AS month, COUNT(*) AS workouts
FROM workouts w
JOIN users u ON w.user_id = u.user_id
GROUP BY u.user_id, month
ORDER BY month;
```

**⑤ Exercises never performed by a user (to suggest new ones)**
```sql
SELECT name FROM exercises
WHERE exercise_id NOT IN (
    SELECT DISTINCT exercise_id FROM sets
    WHERE workout_id IN (SELECT workout_id FROM workouts WHERE user_id = 1)
);
```

---

## 🧱 DELIVERABLES

1. `schema.sql` – all CREATE TABLE statements with constraints
2. `seed.sql` – realistic data (10+ rows per table)
3. `queries.sql` – 5 business reports covering joins, aggregation, subqueries, and a CTE
4. `README.md` explaining the domain, schema (with an ASCII diagram), how to run the files, and what each query does

---

## 💡 Real‑world Usage

- Any startup’s first database begins exactly like this project.
- The pattern of requirements → schema → seed → queries → docs is repeated in every software engineering job.
- You’ll reuse this project workflow when building Companion’s memory module.

---

## 🔍 Practice Preview
You will design and implement your own database project.

| Level | Task |
|-------|------|
| Easy | Choose a domain and write the business requirements in 3‑5 bullet points. |
| Medium | Design the schema and create the `schema.sql` file with at least 4 tables and foreign keys. |
| Hard | Write `seed.sql`, `queries.sql` (5 reports), and a complete `README.md`. |

No automated coach for this lesson — you are the architect now. Run your scripts directly in Termux.

---

## 📌 Key Takeaway
- A self‑designed project proves you can solve real problems with SQL.
- Requirements drive the schema; the schema drives the queries.
- Documentation turns your code into a professional portfolio asset.

*For Emperor.*