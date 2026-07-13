import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🏋️  Fitness Tracker – Core Tables\n\n"
        "Write Python code that:\n"
        "  1. Connects to ':memory:'\n"
        "  2. Creates tables `users` and `exercises`:\n"
        "     • users(user_id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL, join_date TEXT DEFAULT (date('now')))\n"
        "     • exercises(exercise_id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, category TEXT)\n"
        "  3. Inserts:\n"
        "     • users: (1,'emperor','2026-01-01'), (2,'rahim','2026-02-15')\n"
        "     • exercises: (1,'Bench Press','chest'), (2,'Squat','legs'), (3,'Deadlift','back')\n"
        "  4. Commits, then SELECTs all exercise names sorted alphabetically and prints them.\n\n"
        "Expected output:\n[('Bench Press',), ('Deadlift',), ('Squat',)]"
    ),
    expected_output="[('Bench Press',), ('Deadlift',), ('Squat',)]",
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "conn.executescript('''",
        "CREATE TABLE users (user_id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL, join_date TEXT DEFAULT (date('now')));",
        "CREATE TABLE exercises (exercise_id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, category TEXT);",
        "''')",
        "conn.executescript('''",
        "INSERT INTO users VALUES (1,'emperor','2026-01-01'), (2,'rahim','2026-02-15');",
        "INSERT INTO exercises VALUES (1,'Bench Press','chest'), (2,'Squat','legs'), (3,'Deadlift','back');",
        "''')",
        "conn.commit()",
        "cursor = conn.execute('SELECT name FROM exercises ORDER BY name')",
        "print(cursor.fetchall())",
    ]
)

easy2 = Task(
    description=(
        "📊  Total Volume per Exercise – Emperor\n\n"
        "The database already has users and exercises.\n"
        "Also, tables `workouts` and `sets` are pre‑seeded:\n"
        "  • workouts: (1,1,'2026-07-01','Chest day'),\n"
        "    (2,2,'2026-07-02','Leg day')\n"
        "  • sets:\n"
        "    (1,1,1,80,10), (2,1,1,85,8),\n"
        "    (3,1,2,120,5), (4,2,2,130,5),\n"
        "    (5,2,3,100,8)\n"
        "Write Python code that computes total volume\n"
        "(weight × reps) for user_id=1 (Emperor) per\n"
        "exercise. Show exercise name and total_volume.\n"
        "Sort by total_volume descending.\n\n"
        "Expected output:\n[('Squat',600.0), ('Bench Press',1480.0)]"
    ),
    setup_sql=(
        "CREATE TABLE users (user_id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL, join_date TEXT DEFAULT (date('now')));"
        "INSERT INTO users VALUES (1,'emperor','2026-01-01'), (2,'rahim','2026-02-15');"
        "CREATE TABLE exercises (exercise_id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, category TEXT);"
        "INSERT INTO exercises VALUES (1,'Bench Press','chest'), (2,'Squat','legs'), (3,'Deadlift','back');"
        "CREATE TABLE workouts (workout_id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL, workout_date TEXT DEFAULT (date('now')), notes TEXT, FOREIGN KEY (user_id) REFERENCES users(user_id));"
        "INSERT INTO workouts VALUES (1,1,'2026-07-01','Chest day'), (2,2,'2026-07-02','Leg day');"
        "CREATE TABLE sets (set_id INTEGER PRIMARY KEY, workout_id INTEGER NOT NULL, exercise_id INTEGER NOT NULL, weight_kg REAL CHECK(weight_kg >= 0), reps INTEGER CHECK(reps > 0), FOREIGN KEY (workout_id) REFERENCES workouts(workout_id), FOREIGN KEY (exercise_id) REFERENCES exercises(exercise_id));"
        "INSERT INTO sets VALUES (1,1,1,80,10), (2,1,1,85,8), (3,1,2,120,5), (4,2,2,130,5), (5,2,3,100,8);"
    ),
    expected_output="[('Squat', 600.0), ('Bench Press', 1480.0)]",
    level=Level.EASY,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT e.name, SUM(s.weight_kg * s.reps) AS total_volume",
        "FROM sets s JOIN workouts w ON s.workout_id = w.workout_id",
        "JOIN exercises e ON s.exercise_id = e.exercise_id",
        "WHERE w.user_id = 1 GROUP BY e.exercise_id ORDER BY total_volume DESC",
        "''')",
        "print(cursor.fetchall())",
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🏆  Personal Record – Max Weight per Exercise\n\n"
        "The full fitness schema is seeded.\n"
        "Write Python code that returns each user's\n"
        "personal record (the maximum weight they ever\n"
        "lifted) for each exercise.\n"
        "Show username, exercise name, and max_weight.\n"
        "Sort by username, then exercise name.\n\n"
        "Expected output:\n[('emperor','Bench Press',85.0), ('emperor','Squat',120.0), ('rahim','Deadlift',100.0), ('rahim','Squat',130.0)]"
    ),
    setup_sql=(
        "CREATE TABLE users (user_id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL, join_date TEXT DEFAULT (date('now')));"
        "INSERT INTO users VALUES (1,'emperor','2026-01-01'), (2,'rahim','2026-02-15');"
        "CREATE TABLE exercises (exercise_id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, category TEXT);"
        "INSERT INTO exercises VALUES (1,'Bench Press','chest'), (2,'Squat','legs'), (3,'Deadlift','back');"
        "CREATE TABLE workouts (workout_id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL, workout_date TEXT DEFAULT (date('now')), notes TEXT, FOREIGN KEY (user_id) REFERENCES users(user_id));"
        "INSERT INTO workouts VALUES (1,1,'2026-07-01','Chest day'), (2,2,'2026-07-02','Leg day');"
        "CREATE TABLE sets (set_id INTEGER PRIMARY KEY, workout_id INTEGER NOT NULL, exercise_id INTEGER NOT NULL, weight_kg REAL CHECK(weight_kg >= 0), reps INTEGER CHECK(reps > 0), FOREIGN KEY (workout_id) REFERENCES workouts(workout_id), FOREIGN KEY (exercise_id) REFERENCES exercises(exercise_id));"
        "INSERT INTO sets VALUES (1,1,1,80,10), (2,1,1,85,8), (3,1,2,120,5), (4,2,2,130,5), (5,2,3,100,8);"
    ),
    expected_output="[('emperor', 'Bench Press', 85.0), ('emperor', 'Squat', 120.0), ('rahim', 'Deadlift', 100.0), ('rahim', 'Squat', 130.0)]",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT u.username, e.name, MAX(s.weight_kg) AS max_weight",
        "FROM sets s JOIN workouts w ON s.workout_id = w.workout_id",
        "JOIN users u ON w.user_id = u.user_id",
        "JOIN exercises e ON s.exercise_id = e.exercise_id",
        "GROUP BY u.user_id, e.exercise_id ORDER BY u.username, e.name",
        "''')",
        "print(cursor.fetchall())",
    ]
)

medium2 = Task(
    description=(
        "👥  Following – Who Emperor Follows\n\n"
        "A `follows` table is added and seeded:\n"
        "  (follower_id, following_id) -> (1,2), (2,1)\n"
        "Write Python code that finds the usernames of\n"
        "all users that user_id=1 (emperor) follows.\n"
        "Sort by username.\n\n"
        "Expected output:\n[('rahim',)]"
    ),
    setup_sql=(
        "CREATE TABLE users (user_id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL, join_date TEXT DEFAULT (date('now')));"
        "INSERT INTO users VALUES (1,'emperor','2026-01-01'), (2,'rahim','2026-02-15');"
        "CREATE TABLE follows (follower_id INTEGER, following_id INTEGER, PRIMARY KEY (follower_id, following_id), FOREIGN KEY (follower_id) REFERENCES users(user_id), FOREIGN KEY (following_id) REFERENCES users(user_id));"
        "INSERT INTO follows VALUES (1,2), (2,1);"
    ),
    expected_output="[('rahim',)]",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT u.username FROM follows f JOIN users u ON f.following_id = u.user_id",
        "WHERE f.follower_id = 1 ORDER BY u.username",
        "''')",
        "print(cursor.fetchall())",
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "📅  Monthly Workout Count – All Users\n\n"
        "The full fitness schema (without follows) is seeded.\n"
        "Write Python code that counts the number of\n"
        "workouts each user logged per month.\n"
        "Show username, month (YYYY‑MM), and count.\n"
        "Sort by month, then username.\n\n"
        "Expected output:\n[('emperor','2026-07',1), ('rahim','2026-07',1)]"
    ),
    setup_sql=(
        "CREATE TABLE users (user_id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL, join_date TEXT DEFAULT (date('now')));"
        "INSERT INTO users VALUES (1,'emperor','2026-01-01'), (2,'rahim','2026-02-15');"
        "CREATE TABLE exercises (exercise_id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, category TEXT);"
        "INSERT INTO exercises VALUES (1,'Bench Press','chest'), (2,'Squat','legs'), (3,'Deadlift','back');"
        "CREATE TABLE workouts (workout_id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL, workout_date TEXT DEFAULT (date('now')), notes TEXT, FOREIGN KEY (user_id) REFERENCES users(user_id));"
        "INSERT INTO workouts VALUES (1,1,'2026-07-01','Chest day'), (2,2,'2026-07-02','Leg day');"
        "CREATE TABLE sets (set_id INTEGER PRIMARY KEY, workout_id INTEGER NOT NULL, exercise_id INTEGER NOT NULL, weight_kg REAL CHECK(weight_kg >= 0), reps INTEGER CHECK(reps > 0), FOREIGN KEY (workout_id) REFERENCES workouts(workout_id), FOREIGN KEY (exercise_id) REFERENCES exercises(exercise_id));"
        "INSERT INTO sets VALUES (1,1,1,80,10), (2,1,1,85,8), (3,1,2,120,5), (4,2,2,130,5), (5,2,3,100,8);"
    ),
    expected_output="[('emperor', '2026-07', 1), ('rahim', '2026-07', 1)]",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT u.username, strftime('%Y-%m', w.workout_date) AS month, COUNT(*) AS workouts",
        "FROM workouts w JOIN users u ON w.user_id = u.user_id",
        "GROUP BY u.user_id, month ORDER BY month, u.username",
        "''')",
        "print(cursor.fetchall())",
    ]
)

hard2 = Task(
    description=(
        "🆕  Suggest New Exercises – Not Done by Emperor\n\n"
        "The full fitness schema is seeded.\n"
        "Write Python code that finds all exercises Emperor\n"
        "(user_id=1) has NEVER performed (i.e., not in any\n"
        "of his sets). Show the exercise name sorted.\n\n"
        "Expected output:\n[('Deadlift',)]"
    ),
    setup_sql=(
        "CREATE TABLE users (user_id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL, join_date TEXT DEFAULT (date('now')));"
        "INSERT INTO users VALUES (1,'emperor','2026-01-01'), (2,'rahim','2026-02-15');"
        "CREATE TABLE exercises (exercise_id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, category TEXT);"
        "INSERT INTO exercises VALUES (1,'Bench Press','chest'), (2,'Squat','legs'), (3,'Deadlift','back');"
        "CREATE TABLE workouts (workout_id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL, workout_date TEXT DEFAULT (date('now')), notes TEXT, FOREIGN KEY (user_id) REFERENCES users(user_id));"
        "INSERT INTO workouts VALUES (1,1,'2026-07-01','Chest day'), (2,2,'2026-07-02','Leg day');"
        "CREATE TABLE sets (set_id INTEGER PRIMARY KEY, workout_id INTEGER NOT NULL, exercise_id INTEGER NOT NULL, weight_kg REAL CHECK(weight_kg >= 0), reps INTEGER CHECK(reps > 0), FOREIGN KEY (workout_id) REFERENCES workouts(workout_id), FOREIGN KEY (exercise_id) REFERENCES exercises(exercise_id));"
        "INSERT INTO sets VALUES (1,1,1,80,10), (2,1,1,85,8), (3,1,2,120,5), (4,2,2,130,5), (5,2,3,100,8);"
    ),
    expected_output="[('Deadlift',)]",
    level=Level.HARD,
    mode="python",
    hints=[
        "import sqlite3",
        "conn = sqlite3.connect(':memory:')",
        "cursor = conn.execute('''",
        "SELECT name FROM exercises WHERE exercise_id NOT IN (",
        "    SELECT DISTINCT s.exercise_id FROM sets s",
        "    JOIN workouts w ON s.workout_id = w.workout_id",
        "    WHERE w.user_id = 1",
        ") ORDER BY name",
        "''')",
        "print(cursor.fetchall())",
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L89.json",
        module_name="Module_09_Real_World_Projects",
        lesson_name="L89_Custom_Project_Design_Implement"
    )