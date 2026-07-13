import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "🔗  Supabase Connection String\n\n"
        "Write Python code that prints the exact Supabase\n"
        "connection string format shown in the lecture\n"
        "(with placeholders for password and host).\n\n"
        "Expected output:\n"
        "postgresql://postgres:password@db.xyz.supabase.co:5432/postgres"
    ),
    expected_output="postgresql://postgres:password@db.xyz.supabase.co:5432/postgres",
    level=Level.EASY,
    mode="python",
    hints=[
        "The string starts with postgresql://",
        "User is postgres, then :password",
        "Host: db.xyz.supabase.co, port 5432",
        "print('postgresql://postgres:password@db.xyz.supabase.co:5432/postgres')",
    ]
)

easy2 = Task(
    description=(
        "☁️  AWS RDS Connection String\n\n"
        "Print the AWS RDS connection string format\n"
        "exactly as it appears in the lecture.\n\n"
        "Expected output:\n"
        "postgresql://user:password@my-instance.xyz.us-east-1.rds.amazonaws.com:5432/empire"
    ),
    expected_output="postgresql://user:password@my-instance.xyz.us-east-1.rds.amazonaws.com:5432/empire",
    level=Level.EASY,
    mode="python",
    hints=[
        "Format: postgresql://user:password@host:port/database",
        "Host is my-instance.xyz.us-east-1.rds.amazonaws.com",
        "Database name: empire",
        "print the exact string.",
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🐍  Connecting Python to Supabase\n\n"
        "Print the two lines of Python code from the lecture\n"
        "that connect to a Supabase database using psycopg2\n"
        "and the connection string. Use the exact variable\n"
        "names and quotes.\n\n"
        "Expected output:\n"
        "import psycopg2\n"
        "conn = psycopg2.connect(\"postgresql://postgres:password@db.xyz.supabase.co:5432/postgres\")"
    ),
    expected_output='import psycopg2\nconn = psycopg2.connect("postgresql://postgres:password@db.xyz.supabase.co:5432/postgres")',
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "First import psycopg2.",
        "Then psycopg2.connect with the connection string as argument.",
        "Print both lines separated by \\n.",
    ]
)

medium2 = Task(
    description=(
        "🌐  PlanetScale Connection String\n\n"
        "Print the PlanetScale connection string from the\n"
        "lecture, including the ssl parameter.\n\n"
        "Expected output:\n"
        'mysql://user:password@aws.connect.psdb.cloud/empire?ssl={"rejectUnauthorized":true}'
    ),
    expected_output='mysql://user:password@aws.connect.psdb.cloud/empire?ssl={"rejectUnauthorized":true}',
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "It starts with mysql://",
        "Host: aws.connect.psdb.cloud",
        "Database: empire",
        'Query parameter ssl={\"rejectUnauthorized\":true}',
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "🚀  Companion Launch – Database Choice\n\n"
        "According to the lecture, which cloud database is\n"
        "recommended for the initial launch of Companion\n"
        "(small user base, side project)? Print the name\n"
        "and its key advantage in one line, exactly as below.\n\n"
        "Expected output:\n"
        "Supabase – generous free tier, auto‑generated API, ideal for launching Companion."
    ),
    expected_output="Supabase – generous free tier, auto‑generated API, ideal for launching Companion.",
    level=Level.HARD,
    mode="python",
    hints=[
        "The lecture says: Companion – start on Supabase (free).",
        "Key advantage: generous free tier, auto‑generated API.",
        "Print exactly: Supabase – generous free tier, auto‑generated API, ideal for launching Companion.",
    ]
)

hard2 = Task(
    description=(
        "📈  Companion at Scale – Migration Target\n\n"
        "When Companion reaches 10,000+ users, the lecture\n"
        "recommends migrating to a different database.\n"
        "Print its name and the main reasons, exactly as below.\n\n"
        "Expected output:\n"
        "AWS RDS – enterprise‑grade, multi‑AZ high availability, automated backups, read replicas."
    ),
    expected_output="AWS RDS – enterprise‑grade, multi‑AZ high availability, automated backups, read replicas.",
    level=Level.HARD,
    mode="python",
    hints=[
        "The lecture: migrate to AWS RDS when you have 10,000+ users.",
        "Reasons: enterprise‑grade, multi‑AZ, backups, read replicas.",
        "Print exactly: AWS RDS – enterprise‑grade, multi‑AZ high availability, automated backups, read replicas.",
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L96.json",
        module_name="Module_10_Beyond_SQLite",
        lesson_name="L96_Cloud_Databases_AWS_RDS_Supabase_PlanetScale"
    )