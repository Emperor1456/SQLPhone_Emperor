import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks ─────────────────────────────────────────────

easy1 = Task(
    description=(
        "📦  Alembic Installation Command\n\n"
        "Write Python code that prints the exact command\n"
        "to install Alembic as shown in the lecture.\n\n"
        "Expected output:\npip install alembic"
    ),
    expected_output="pip install alembic",
    level=Level.EASY,
    mode="python",
    hints=[
        "The lecture shows: pip install alembic",
        "print('pip install alembic')",
    ]
)

easy2 = Task(
    description=(
        "📁  Initialize Alembic Project\n\n"
        "Print the command that initializes a new Alembic\n"
        "migration environment in a folder named `migrations`.\n\n"
        "Expected output:\nalembic init migrations"
    ),
    expected_output="alembic init migrations",
    level=Level.EASY,
    mode="python",
    hints=[
        "alembic init <directory>",
        "print('alembic init migrations')",
    ]
)

# ── Medium Tasks ──────────────────────────────────────────

medium1 = Task(
    description=(
        "🔧  Alembic Autogenerate Migration\n\n"
        "Write Python code that prints the Alembic command\n"
        "to generate a migration for a new table named\n"
        "'soldiers', exactly as in the lecture.\n\n"
        "Expected output:\nalembic revision --autogenerate -m \"create soldiers table\""
    ),
    expected_output='alembic revision --autogenerate -m "create soldiers table"',
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "Use alembic revision --autogenerate -m",
        "Message is \"create soldiers table\"",
        "print('alembic revision --autogenerate -m \"create soldiers table\"')",
    ]
)

medium2 = Task(
    description=(
        "🔄  Django Migration Commands\n\n"
        "Print the two Django management commands that\n"
        "create and apply migrations after changing models,\n"
        "each on its own line.\n\n"
        "Expected output:\npython manage.py makemigrations\npython manage.py migrate"
    ),
    expected_output="python manage.py makemigrations\npython manage.py migrate",
    level=Level.MEDIUM,
    mode="python",
    hints=[
        "First: python manage.py makemigrations",
        "Second: python manage.py migrate",
        "Print both separated by a newline.",
    ]
)

# ── Hard Tasks ────────────────────────────────────────────

hard1 = Task(
    description=(
        "📈  Full Alembic Workflow – Init to Upgrade\n\n"
        "Print the three‑step Alembic workflow exactly as\n"
        "presented in the lecture:\n"
        "  1. Initialize the environment\n"
        "  2. Generate migration for soldiers table\n"
        "  3. Apply the migration\n\n"
        "Print each command on its own line in order.\n\n"
        "Expected output:\nalembic init migrations\nalembic revision --autogenerate -m \"create soldiers table\"\nalembic upgrade head"
    ),
    expected_output='alembic init migrations\nalembic revision --autogenerate -m "create soldiers table"\nalembic upgrade head',
    level=Level.HARD,
    mode="python",
    hints=[
        "Line 1: alembic init migrations",
        "Line 2: alembic revision --autogenerate -m \"create soldiers table\"",
        "Line 3: alembic upgrade head",
        "Use triple‑quoted string and print.",
    ]
)

hard2 = Task(
    description=(
        "🚀  Django New Model Workflow\n\n"
        "Print the three steps to add a new model in Django:\n"
        "  1. Edit the models file (symbolic placeholder)\n"
        "  2. Make migrations\n"
        "  3. Apply migrations\n\n"
        "Print them exactly as shown below (plain text, no code).\n\n"
        "Expected output:\nedit models.py\npython manage.py makemigrations\npython manage.py migrate"
    ),
    expected_output="edit models.py\npython manage.py makemigrations\npython manage.py migrate",
    level=Level.HARD,
    mode="python",
    hints=[
        "Line 1: edit models.py",
        "Line 2: python manage.py makemigrations",
        "Line 3: python manage.py migrate",
        "Print exactly these three lines.",
    ]
)

if __name__ == "__main__":
    run_sequence(
        [easy1, easy2, medium1, medium2, hard1, hard2],
        save_path=MODULE_DIR,
        progress_name=".progress_L95.json",
        module_name="Module_10_Beyond_SQLite",
        lesson_name="L95_Database_Migrations_Alembic_Django_Migrations"
    )