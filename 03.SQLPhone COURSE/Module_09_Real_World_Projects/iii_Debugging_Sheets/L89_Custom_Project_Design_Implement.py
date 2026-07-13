import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
SELECT u.username, e.name, MAX(s.weight_kg) AS max_weight
FROM sets s
JOIN workouts w ON s.workout_id = w.workout_id
JOIN users u ON w.user_id = u.user_id
JOIN exercises e ON s.exercise_id = e.exercise_id
GROUP BY u.user_id, e.exercise_id
ORDER BY u.username, e.name;"""

EXPECTED = "[('emperor', 'Bench Press', 85.0), ('emperor', 'Squat', 120.0), ('rahim', 'Deadlift', 100.0), ('rahim', 'Squat', 130.0)]"

SETUP = """\
CREATE TABLE users (user_id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL, join_date TEXT DEFAULT (date('now')));
INSERT INTO users VALUES (1,'emperor','2026-01-01'), (2,'rahim','2026-02-15');
CREATE TABLE exercises (exercise_id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, category TEXT);
INSERT INTO exercises VALUES (1,'Bench Press','chest'), (2,'Squat','legs'), (3,'Deadlift','back');
CREATE TABLE workouts (workout_id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL, workout_date TEXT DEFAULT (date('now')), notes TEXT, FOREIGN KEY (user_id) REFERENCES users(user_id));
INSERT INTO workouts VALUES (1,1,'2026-07-01','Chest day'), (2,2,'2026-07-02','Leg day');
CREATE TABLE sets (set_id INTEGER PRIMARY KEY, workout_id INTEGER NOT NULL, exercise_id INTEGER NOT NULL, weight_kg REAL CHECK(weight_kg >= 0), reps INTEGER CHECK(reps > 0), FOREIGN KEY (workout_id) REFERENCES workouts(workout_id), FOREIGN KEY (exercise_id) REFERENCES exercises(exercise_id));
INSERT INTO sets VALUES (1,1,1,80,10), (2,1,1,85,8), (3,1,2,120,5), (4,2,2,130,5), (5,2,3,100,8);"""

HINTS = [
    "The query joins four tables and aggregates correctly, but the GROUP BY clause is missing a non‑aggregated column.",
    "You must include all non‑aggregated columns from the SELECT in the GROUP BY clause.",
    "Add 'u.username' and 'e.name' to GROUP BY."
]

if __name__ == "__main__":
    run_debug(
        lesson_title="L89 – Custom Project – Design & Implement",
        setup_sql=SETUP,
        broken_code=BROKEN,
        expected_output=EXPECTED,
        hints=HINTS
    )
